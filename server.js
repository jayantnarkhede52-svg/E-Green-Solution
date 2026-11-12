require('dotenv').config();
const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const url = require('url');
const crypto = require('crypto');
const bcrypt = require('bcryptjs');
const { connectDB, getDB, ObjectId } = require('./lib/db');

const PORT = process.env.PORT || 3000;
const ROOT = path.resolve(__dirname);

const MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.webp': 'image/webp',
    '.pdf': 'application/pdf',
    '.mp4': 'video/mp4',
    '.txt': 'text/plain; charset=utf-8',
    '.xml': 'application/xml; charset=utf-8',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
    '.ttf': 'font/ttf',
    '.eot': 'application/vnd.ms-fontobject'
};


function forwardToFormSubmit(lead) {
    return new Promise((resolve) => {
        const postData = JSON.stringify({
            name: lead.name || 'Anonymous Lead',
            phone: lead.phone || '',
            email: lead.email || 'N/A',
            location: lead.location || 'Pune / PCMC',
            service: lead.service || 'Turnkey Rooftop Solar',
            monthlyBill: lead.bill || 'N/A',
            message: lead.message || 'Website Lead',
            sourcePage: lead.source || 'Website Form',
            _subject: `New Solar Lead: ${lead.name} (${lead.service})`,
            _template: 'table'
        });

        const req = https.request('https://formsubmit.co/ajax/egreensolution1@gmail.com', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Content-Length': Buffer.byteLength(postData),
                'Origin': 'https://www.egreensolution.in',
                'Referer': 'https://www.egreensolution.in/'
            },
            timeout: 8000
        }, (res) => {
            let body = '';
            res.on('data', chunk => body += chunk);
            res.on('end', () => resolve({ status: res.statusCode, body }));
        });

        req.on('error', (e) => resolve({ error: e.message }));
        req.on('timeout', () => { req.destroy(); resolve({ error: 'Timeout' }); });
        req.write(postData);
        req.end();
    });
}

function parseCookies(cookieHeader) {
    const cookies = {};
    if (!cookieHeader) return cookies;
    cookieHeader.split(';').forEach(c => {
        const parts = c.split('=');
        if (parts.length >= 2) {
            cookies[parts[0].trim()] = decodeURIComponent(parts.slice(1).join('=').trim());
        }
    });
    return cookies;
}

function parseBody(req) {
    // 1. If running under Vercel Serverless / body-parser, req.body is already pre-parsed
    if (req.body && typeof req.body === 'object') {
        return Promise.resolve(req.body);
    }
    if (typeof req.body === 'string' && req.body.trim()) {
        try {
            return Promise.resolve(JSON.parse(req.body));
        } catch (e) {
            return Promise.resolve({ raw: req.body });
        }
    }

    // 2. Fallback to stream consumption for native Node.js HTTP server
    return new Promise((resolve, reject) => {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
            if (body.length > 1e6) { // 1MB limit
                req.destroy();
                reject(new Error('Payload too large'));
            }
        });
        req.on('end', () => {
            if (!body) return resolve({});
            try {
                if (req.headers['content-type'] && req.headers['content-type'].includes('application/json')) {
                    resolve(JSON.parse(body));
                } else if (req.headers['content-type'] && req.headers['content-type'].includes('application/x-www-form-urlencoded')) {
                    const params = new URLSearchParams(body);
                    const obj = {};
                    for (const [k, v] of params.entries()) obj[k] = v;
                    resolve(obj);
                } else {
                    resolve({ raw: body });
                }
            } catch (err) {
                resolve({});
            }
        });
        req.on('error', reject);
    });
}

async function getAuthUser(req) {
    const cookies = req.cookies || parseCookies(req.headers.cookie);
    const token = cookies['egreen_auth_token'];
    if (!token) return null;

    try {
        const db = getDB();
        const session = await db.collection('sessions').findOne({
            token: token,
            expiresAt: { $gt: new Date() }
        });
        return session ? session.username : null;
    } catch (err) {
        return null;
    }
}

function resolveFile(pathname) {
    let decoded = decodeURIComponent(pathname);
    let safePath = path.normalize(decoded).replace(/^(\.\.[\/\\])+/, '');
    let fullPath = path.join(ROOT, safePath);

    // 1. Direct file match
    if (fs.existsSync(fullPath) && fs.statSync(fullPath).isFile()) {
        return fullPath;
    }

    // 2. Directory checks
    if (fs.existsSync(fullPath) && fs.statSync(fullPath).isDirectory()) {
        const indexPath = path.join(fullPath, 'index.html');
        if (fs.existsSync(indexPath) && fs.statSync(indexPath).isFile()) {
            return indexPath;
        }
        const dashboardPath = path.join(fullPath, 'dashboard.html');
        if (fs.existsSync(dashboardPath) && fs.statSync(dashboardPath).isFile()) {
            return dashboardPath;
        }
    }

    // 3. Clean URL matching (e.g. /services -> services.html)
    const htmlPath = fullPath + '.html';
    if (fs.existsSync(htmlPath) && fs.statSync(htmlPath).isFile()) {
        return htmlPath;
    }

    return null;
}

async function requestHandler(req, res) {
    const parsedUrl = url.parse(req.url, true);
    const pathname = parsedUrl.pathname;
    const method = req.method.toUpperCase();

    // CORS & Security Headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    res.setHeader('X-Content-Type-Options', 'nosniff');

    if (method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }

    // ============================================================
    // 1. API ROUTES
    // ============================================================

    // Public Lead Submission: POST /api/leads
    if (pathname === '/api/leads' && method === 'POST') {
        try {
            const body = await parseBody(req);
            if (!body.name && !body.phone) {
                res.writeHead(400, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Name and phone are required' }));
                return;
            }

            const db = getDB();
            const leadDoc = {
                name: body.name || 'Anonymous Inquiry',
                phone: body.phone || '',
                email: body.email || '',
                location: body.location || body.city || 'Pune / PCMC',
                service: body.service || 'Turnkey Rooftop Solar',
                bill: body.bill || '',
                capacity: body.capacity || '',
                message: body.message || body.comments || '',
                status: 'New',
                notes: '',
                source: body.source || 'Website Form',
                ip: req.socket.remoteAddress || '',
                createdAt: new Date(),
                updatedAt: new Date()
            };

            const result = await db.collection('leads').insertOne(leadDoc);

            // Forward asynchronously to FormSubmit (egreensolution1@gmail.com)
            forwardToFormSubmit(leadDoc).then(res => {
                if (res.error) console.log('FormSubmit forward note:', res.error);
                else console.log('FormSubmit forwarded, status:', res.status);
            }).catch(() => {});

            res.writeHead(201, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
                success: true,
                message: 'Your inquiry has been submitted successfully to E Green Solution.',
                id: result.insertedId
            }));
            return;
        } catch (err) {
            console.error('Lead submission error:', err);
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Internal server error saving lead' }));
            return;
        }
    }

    // Admin Login: POST /api/admin/login
    if (pathname === '/api/admin/login' && method === 'POST') {
        try {
            const body = await parseBody(req);
            const { username, password } = body;

            if (!username || !password) {
                res.writeHead(400, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Username and password are required' }));
                return;
            }

            const db = getDB();
            const admin = await db.collection('admins').findOne({ username: username.trim() });
            if (!admin) {
                res.writeHead(401, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Invalid username or password' }));
                return;
            }

            const isValid = await bcrypt.compare(password, admin.passwordHash);
            if (!isValid) {
                res.writeHead(401, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Invalid username or password' }));
                return;
            }

            // Create cryptographically secure session
            const token = crypto.randomBytes(32).toString('hex');
            const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000); // 7 days

            await db.collection('sessions').insertOne({
                token,
                username: admin.username,
                role: admin.role,
                createdAt: new Date(),
                expiresAt
            });

            res.writeHead(200, {
                'Content-Type': 'application/json',
                'Set-Cookie': `egreen_auth_token=${token}; Path=/; HttpOnly; SameSite=Strict; Max-Age=604800`
            });
            res.end(JSON.stringify({ success: true, redirect: '/admin/dashboard' }));
            return;
        } catch (err) {
            console.error('Login error:', err);
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Authentication service error' }));
            return;
        }
    }

    // Admin Logout: POST /api/admin/logout
    if (pathname === '/api/admin/logout' && method === 'POST') {
        const cookies = parseCookies(req.headers.cookie);
        const token = cookies['egreen_auth_token'];
        if (token) {
            try {
                const db = getDB();
                await db.collection('sessions').deleteOne({ token });
            } catch (err) {}
        }

        res.writeHead(200, {
            'Content-Type': 'application/json',
            'Set-Cookie': 'egreen_auth_token=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT'
        });
        res.end(JSON.stringify({ success: true }));
        return;
    }

    // Check Auth Status: GET /api/admin/check-auth
    if (pathname === '/api/admin/check-auth' && method === 'GET') {
        const authUser = await getAuthUser(req);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ authenticated: !!authUser, username: authUser || null }));
        return;
    }

    // Change Password: POST /api/admin/change-password
    if (pathname === '/api/admin/change-password' && method === 'POST') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(401, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Unauthorized' }));
            return;
        }

        try {
            const body = await parseBody(req);
            const { currentPassword, newPassword } = body;
            if (!currentPassword || !newPassword || newPassword.length < 8) {
                res.writeHead(400, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'New password must be at least 8 characters' }));
                return;
            }

            const db = getDB();
            const admin = await db.collection('admins').findOne({ username: authUser });
            if (!admin) {
                res.writeHead(404, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Admin not found' }));
                return;
            }

            const isValid = await bcrypt.compare(currentPassword, admin.passwordHash);
            if (!isValid) {
                res.writeHead(400, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Current password is incorrect' }));
                return;
            }

            const newHash = await bcrypt.hash(newPassword, 10);
            await db.collection('admins').updateOne(
                { username: authUser },
                { $set: { passwordHash: newHash, updatedAt: new Date() } }
            );

            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true, message: 'Password updated successfully' }));
            return;
        } catch (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to update password' }));
            return;
        }
    }

    
    // Admin Analytics Stats: GET /api/admin/stats
    if (pathname === '/api/admin/stats' && method === 'GET') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(401, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Unauthorized' }));
            return;
        }

        try {
            const db = getDB();
            const now = new Date();

            const startOfToday = new Date(now.getFullYear(), now.getMonth(), now.getDate());
            const startOfWeek = new Date(startOfToday.getTime() - ((startOfToday.getDay() + 6) % 7) * 86400000);
            const startOfMonth = new Date(now.getFullYear(), now.getMonth(), 1);
            const startOfLastMonth = new Date(now.getFullYear(), now.getMonth() - 1, 1);

            const [totalLeads, newLeads, thisMonthLeads, lastMonthLeads, thisWeekLeads, todayLeads] = await Promise.all([
                db.collection('leads').countDocuments({}),
                db.collection('leads').countDocuments({ status: 'New' }),
                db.collection('leads').countDocuments({ createdAt: { $gte: startOfMonth } }),
                db.collection('leads').countDocuments({ createdAt: { $gte: startOfLastMonth, $lt: startOfMonth } }),
                db.collection('leads').countDocuments({ createdAt: { $gte: startOfWeek } }),
                db.collection('leads').countDocuments({ createdAt: { $gte: startOfToday } })
            ]);

            // Growth percentage vs last month
            let monthGrowthPct = 0;
            if (lastMonthLeads > 0) {
                monthGrowthPct = Math.round(((thisMonthLeads - lastMonthLeads) / lastMonthLeads) * 100);
            } else if (thisMonthLeads > 0) {
                monthGrowthPct = 100;
            }

            // Weekly Trend: Past 7 days
            const weeklyDays = [];
            for (let i = 6; i >= 0; i--) {
                const dayStart = new Date(startOfToday.getTime() - i * 86400000);
                const dayEnd = new Date(dayStart.getTime() + 86400000);
                const count = await db.collection('leads').countDocuments({
                    createdAt: { $gte: dayStart, $lt: dayEnd }
                });
                const dayName = dayStart.toLocaleDateString('en-US', { weekday: 'short' });
                const dateNum = dayStart.getDate();
                weeklyDays.push({ label: `${dayName} ${dateNum}`, count });
            }

            // Monthly Trend: Last 6 months
            const monthlyTrend = [];
            for (let i = 5; i >= 0; i--) {
                const mStart = new Date(now.getFullYear(), now.getMonth() - i, 1);
                const mEnd = new Date(now.getFullYear(), now.getMonth() - i + 1, 1);
                const count = await db.collection('leads').countDocuments({
                    createdAt: { $gte: mStart, $lt: mEnd }
                });
                const mLabel = mStart.toLocaleDateString('en-US', { month: 'short', year: '2-digit' });
                monthlyTrend.push({ label: mLabel, count });
            }

            // Service Breakdown
            const serviceAggregation = await db.collection('leads').aggregate([
                { $group: { _id: { $ifNull: ['$service', 'General Inquiry'] }, count: { $sum: 1 } } },
                { $sort: { count: -1 } }
            ]).toArray();

            // Status Breakdown
            const statusAggregation = await db.collection('leads').aggregate([
                { $group: { _id: { $ifNull: ['$status', 'New'] }, count: { $sum: 1 } } },
                { $sort: { count: -1 } }
            ]).toArray();

            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
                totalLeads,
                newLeads,
                thisMonthLeads,
                lastMonthLeads,
                thisWeekLeads,
                todayLeads,
                monthGrowthPct,
                weeklyDays,
                monthlyTrend,
                serviceAggregation,
                statusAggregation
            }));
            return;
        } catch (err) {
            console.error('Error computing stats:', err);
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to compute stats' }));
            return;
        }
    }

    // Admin Trigger FormSubmit Test & Activation: POST /api/admin/test-formsubmit
    if (pathname === '/api/admin/test-formsubmit' && method === 'POST') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(401, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Unauthorized' }));
            return;
        }

        try {
            const db = getDB();
            const testDoc = {
                name: 'E Green Solution Test Lead',
                phone: '+91 72491 87969',
                email: 'egreensolution1@gmail.com',
                location: 'Pune Headquarters',
                service: 'System Verification & FormSubmit Activation',
                bill: '₹ 15,000 / month',
                message: 'Test dispatch triggered from Admin Dashboard to verify FormSubmit email delivery to egreensolution1@gmail.com',
                status: 'New',
                notes: 'Automated test lead from admin dashboard',
                source: 'Admin Test Dispatch',
                createdAt: new Date(),
                updatedAt: new Date()
            };

            await db.collection('leads').insertOne(testDoc);
            const fsResult = await forwardToFormSubmit(testDoc);

            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
                success: true,
                message: 'Test lead saved to MongoDB Atlas & forwarded to FormSubmit (egreensolution1@gmail.com).',
                formSubmitResult: fsResult
            }));
            return;
        } catch (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to dispatch test lead' }));
            return;
        }
    }

    // Get All Leads: GET /api/admin/leads
    if (pathname === '/api/admin/leads' && method === 'GET') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(401, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Unauthorized' }));
            return;
        }

        try {
            const db = getDB();
            const leads = await db.collection('leads')
                .find({})
                .sort({ createdAt: -1 })
                .limit(500)
                .toArray();

            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(leads));
            return;
        } catch (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to fetch leads' }));
            return;
        }
    }

    // Add Manual Lead: POST /api/admin/leads
    if (pathname === '/api/admin/leads' && method === 'POST') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(401, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Unauthorized' }));
            return;
        }

        try {
            const body = await parseBody(req);
            const db = getDB();
            const leadDoc = {
                name: body.name || 'Offline Inquiry',
                phone: body.phone || '',
                email: body.email || '',
                location: body.location || 'Pune / PCMC',
                service: body.service || 'Turnkey Rooftop Solar',
                bill: body.bill || '',
                capacity: body.capacity || '',
                message: body.message || '',
                status: body.status || 'New',
                notes: body.notes || '',
                source: 'Manual Admin Entry',
                createdBy: authUser,
                createdAt: new Date(),
                updatedAt: new Date()
            };

            const result = await db.collection('leads').insertOne(leadDoc);
            res.writeHead(201, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true, id: result.insertedId }));
            return;
        } catch (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to create manual lead' }));
            return;
        }
    }

    // Update Lead: PATCH /api/admin/leads/:id
    if (pathname.startsWith('/api/admin/leads/') && method === 'PATCH') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(401, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Unauthorized' }));
            return;
        }

        const id = pathname.replace('/api/admin/leads/', '').trim();
        try {
            const body = await parseBody(req);
            const db = getDB();
            const updateFields = { updatedAt: new Date() };

            if (body.status !== undefined) updateFields.status = body.status;
            if (body.notes !== undefined) updateFields.notes = body.notes;
            if (body.priority !== undefined) updateFields.priority = body.priority;

            await db.collection('leads').updateOne(
                { _id: new ObjectId(id) },
                { $set: updateFields }
            );

            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true }));
            return;
        } catch (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to update lead' }));
            return;
        }
    }

    // Delete Lead: DELETE /api/admin/leads/:id
    if (pathname.startsWith('/api/admin/leads/') && method === 'DELETE') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(401, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Unauthorized' }));
            return;
        }

        const id = pathname.replace('/api/admin/leads/', '').trim();
        try {
            const db = getDB();
            await db.collection('leads').deleteOne({ _id: new ObjectId(id) });
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true }));
            return;
        } catch (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to delete lead' }));
            return;
        }
    }

    // Export CSV: GET /api/admin/leads/export-csv
    if (pathname === '/api/admin/leads/export-csv' && method === 'GET') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(401, { 'Content-Type': 'text/plain' });
            res.end('Unauthorized');
            return;
        }

        try {
            const db = getDB();
            const leads = await db.collection('leads').find({}).sort({ createdAt: -1 }).toArray();

            let csv = 'ID,Date,Customer Name,Phone,Email,Location,Service,Monthly Bill,Status,Notes\r\n';
            leads.forEach(l => {
                const date = l.createdAt ? new Date(l.createdAt).toISOString().split('T')[0] : '';
                const clean = (val) => `"${String(val || '').replace(/"/g, '""')}"`;
                csv += `${l._id},${date},${clean(l.name)},${clean(l.phone)},${clean(l.email)},${clean(l.location)},${clean(l.service)},${clean(l.bill)},${clean(l.status || 'New')},${clean(l.notes)}\r\n`;
            });

            res.writeHead(200, {
                'Content-Type': 'text/csv; charset=utf-8',
                'Content-Disposition': 'attachment; filename="egreen-solar-leads.csv"'
            });
            res.end(csv);
            return;
        } catch (err) {
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end('Error exporting CSV');
            return;
        }
    }

    // ============================================================
    // 2. ADMIN AUTH ROUTE GUARDS
    // ============================================================

    // Check if accessing admin dashboard
    if (pathname === '/admin/dashboard' || pathname === '/admin/dashboard.html') {
        const authUser = await getAuthUser(req);
        if (!authUser) {
            res.writeHead(302, { 'Location': '/admin' });
            res.end();
            return;
        }
        res.setHeader('X-Robots-Tag', 'noindex, nofollow, noarchive');
    }

    // Check if already logged in and visiting login page
    if (pathname === '/admin' || pathname === '/admin/' || pathname === '/admin/index.html') {
        const authUser = await getAuthUser(req);
        if (authUser) {
            res.writeHead(302, { 'Location': '/admin/dashboard' });
            res.end();
            return;
        }
        res.setHeader('X-Robots-Tag', 'noindex, nofollow, noarchive');
    }

    // ============================================================
    // 3. LEGACY 301 REDIRECTS
    // ============================================================

    
    if (pathname === '/solar-subsidy' || pathname === '/solar-subsidy.html') {
        res.writeHead(301, { 'Location': '/residential-solar' + (parsedUrl.search || '') });
        res.end();
        return;
    }

    if (pathname === '/sitemp.xml') {
        res.writeHead(301, { 'Location': '/sitemap.xml' + (parsedUrl.search || '') });
        res.end();
        return;
    }

    if (pathname === '/pimpri-chinchwad' || pathname === '/pimpri-chinchwad.html') {
        res.writeHead(301, { 'Location': '/solar-panel-pimpri-chinchwad' });
        res.end();
        return;
    }

    if (pathname.startsWith('/areas/')) {
        res.writeHead(301, { 'Location': '/areas' });
        res.end();
        return;
    }

    // ============================================================
    // 4. STATIC FILE SERVING
    // ============================================================

    const resolvedPath = resolveFile(pathname);

    if (!resolvedPath) {
        res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(`
            <!DOCTYPE html>
            <html lang="en">
            <head><title>404 Not Found</title><style>body{font-family:sans-serif;text-align:center;padding:50px;background:#0d1117;color:#fff;}a{color:#7BD894;}</style></head>
            <body>
                <h1>404 - Page Not Found</h1>
                <p>The requested URL <code>${pathname}</code> was not found on this server.</p>
                <p><a href="/">Return to Homepage</a></p>
            </body>
            </html>
        `);
        return;
    }

    const ext = path.extname(resolvedPath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    fs.readFile(resolvedPath, (err, data) => {
        if (err) {
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end('500 Internal Server Error');
            return;
        }

        res.writeHead(200, {
            'Content-Type': contentType
        });
        res.end(data);
    });
}

const server = http.createServer(requestHandler);
let currentPort = Number(PORT);

server.on('error', (err) => {
    if (err.code === 'EADDRINUSE') {
        console.log(`⚠️  Port ${currentPort} is already in use. Trying port ${currentPort + 1}...`);
        currentPort++;
        server.listen(currentPort);
    } else {
        console.error('Server error:', err);
    }
});

server.on('listening', () => {
    const address = server.address();
    const port = typeof address === 'object' && address ? address.port : currentPort;
    console.log(`====================================================`);
    console.log(`🚀 E Green Solution Local Server is Running!`);
    console.log(`👉 Local:   http://localhost:${port}`);
    console.log(`👉 Portal:  http://localhost:${port}/admin`);
    console.log(`📁 Root:    ${ROOT}`);
    console.log(`====================================================`);
});

if (require.main === module) {
    connectDB()
        .then(() => {
            server.listen(currentPort, '0.0.0.0');
        })
        .catch((err) => {
            console.error('❌ Failed to connect to MongoDB on startup. Starting offline mode...', err.message);
            server.listen(currentPort, '0.0.0.0');
        });
}

module.exports = { requestHandler, connectDB, getDB, forwardToFormSubmit };
