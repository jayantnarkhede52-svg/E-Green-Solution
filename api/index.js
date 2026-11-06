// Vercel Serverless Function Handler for E Green Solution
const { requestHandler, connectDB } = require('../server.js');

module.exports = async (req, res) => {
    try {
        await connectDB();
    } catch (err) {
        console.error('MongoDB serverless connection error:', err.message);
    }

    // Reconstruct intended API route when rewritten by Vercel
    if (req.query && req.query.match) {
        const match = Array.isArray(req.query.match) ? req.query.match.join('/') : req.query.match;
        req.url = '/api/' + match;
    } else if (req.query && req.query.path) {
        const p = Array.isArray(req.query.path) ? req.query.path.join('/') : req.query.path;
        req.url = '/api/' + p;
    } else if (req.headers['x-matched-path']) {
        const mp = req.headers['x-matched-path'];
        if (mp.startsWith('/api/')) req.url = mp;
    }

    return requestHandler(req, res);
};
