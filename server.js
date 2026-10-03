const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

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
        const loginPath = path.join(fullPath, 'login.html');
        if (fs.existsSync(loginPath) && fs.statSync(loginPath).isFile()) {
            return loginPath;
        }
    }

    // 3. Clean URL matching (e.g. /services -> services.html)
    const htmlPath = fullPath + '.html';
    if (fs.existsSync(htmlPath) && fs.statSync(htmlPath).isFile()) {
        return htmlPath;
    }

    return null;
}

const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url);

    // 301 Redirect for duplicate PCMC page to canonical /solar-panel-pimpri-chinchwad
    if (parsedUrl.pathname === '/pimpri-chinchwad' || parsedUrl.pathname === '/pimpri-chinchwad.html') {
        res.writeHead(301, { 'Location': '/solar-panel-pimpri-chinchwad' });
        res.end();
        return;
    }

    // 301 Redirect for legacy /areas/* paths to /areas hub
    if (parsedUrl.pathname.startsWith('/areas/')) {
        res.writeHead(301, { 'Location': '/areas' });
        res.end();
        return;
    }

    const resolvedPath = resolveFile(parsedUrl.pathname);

    if (!resolvedPath) {
        res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(`
            <!DOCTYPE html>
            <html lang="en">
            <head><title>404 Not Found</title><style>body{font-family:sans-serif;text-align:center;padding:50px;background:#0d1117;color:#fff;}a{color:#fbc02d;}</style></head>
            <body>
                <h1>404 - Page Not Found</h1>
                <p>The requested URL <code>${parsedUrl.pathname}</code> was not found on this server.</p>
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
            'Content-Type': contentType,
            'Access-Control-Allow-Origin': '*'
        });
        res.end(data);
    });
});

server.listen(PORT, '0.0.0.0', () => {
    console.log(`====================================================`);
    console.log(`🚀 E Green Solution Local Server is Running!`);
    console.log(`👉 Local:   http://localhost:${PORT}`);
    console.log(`👉 Network: http://127.0.0.1:${PORT}`);
    console.log(`📁 Root:    ${ROOT}`);
    console.log(`====================================================`);
});
