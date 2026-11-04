require('dotenv').config();
const { MongoClient, ObjectId } = require('mongodb');
const bcrypt = require('bcryptjs');

const MONGODB_URI = process.env.MONGODB_URI || "mongodb+srv://purchaseegreensolution1_db_user:rDlEXHRIgFNsuDyA@egreen.ycgdvn5.mongodb.net/egreen?retryWrites=true&w=majority&appName=egreen";
const DB_NAME = "egreen";

let client = null;
let db = null;

async function connectDB() {
    if (db) return db;

    try {
        client = new MongoClient(MONGODB_URI, {
            maxPoolSize: 10,
            serverSelectionTimeoutMS: 8000
        });
        await client.connect();
        db = client.db(DB_NAME);
        console.log(`✅ Connected to MongoDB Atlas [Database: ${DB_NAME}]`);

        // Create indexes
        await db.collection('leads').createIndex({ createdAt: -1 });
        await db.collection('leads').createIndex({ phone: 1 });
        await db.collection('admins').createIndex({ username: 1 }, { unique: true });
        await db.collection('sessions').createIndex({ token: 1 }, { unique: true });
        await db.collection('sessions').createIndex({ expiresAt: 1 }, { expireAfterSeconds: 0 }); // TTL index

        // Initialize default admin if none exists
        const defaultUser = process.env.ADMIN_DEFAULT_USER || 'egreen_admin';
        const defaultPass = process.env.ADMIN_DEFAULT_PASS || 'EGreen@Pune2026!';
        
        const existingAdmin = await db.collection('admins').findOne({ username: defaultUser });
        if (!existingAdmin) {
            const passwordHash = await bcrypt.hash(defaultPass, 10);
            await db.collection('admins').insertOne({
                username: defaultUser,
                passwordHash: passwordHash,
                role: 'superadmin',
                createdAt: new Date(),
                updatedAt: new Date()
            });
            console.log(`🔐 Default admin user '${defaultUser}' initialized.`);
        }

        return db;
    } catch (err) {
        console.error("❌ MongoDB connection error:", err.message);
        throw err;
    }
}

function getDB() {
    if (!db) {
        throw new Error("Database not connected. Call connectDB() first.");
    }
    return db;
}

module.exports = {
    connectDB,
    getDB,
    ObjectId
};
