// Vercel Serverless Function Handler for E Green Solution
const { requestHandler, connectDB } = require('../server.js');

module.exports = async (req, res) => {
    try {
        await connectDB();
    } catch (err) {
        console.error('MongoDB serverless connection error:', err.message);
    }
    return requestHandler(req, res);
};
