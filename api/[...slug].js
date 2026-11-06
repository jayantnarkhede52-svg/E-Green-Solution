// Vercel Serverless Catch-All for /api/*
const { requestHandler, connectDB } = require('../server.js');

module.exports = async (req, res) => {
    try {
        await connectDB();
    } catch (err) {
        console.error('MongoDB serverless connection error:', err.message);
    }

    // Dynamic slug routing: req.query.slug is array of path segments
    if (req.query && req.query.slug) {
        const slug = Array.isArray(req.query.slug) ? req.query.slug.join('/') : req.query.slug;
        req.url = '/api/' + slug;
    }

    return requestHandler(req, res);
};
