const pool = require('../db');
const redis = require('redis');
const { generateToken } = require('../utils/token');
const { sendOTP } = require('../utils/mailer');
const bcrypt = require('bcrypt');
const speakeasy = require('speakeasy');
require('dotenv').config();

// Setup Redis client
const redisClient = redis.createClient({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT,
});
redisClient.on('error', console.error);

async function signup(req, res) {
  const { email, password } = req.body;
  console.log(`${email} `);
  const hashed = await bcrypt.hash(password, 10);
  const [result] = await pool.query(
    'INSERT INTO users (email, password) VALUES (?, ?)',
    [email, hashed]
  );
  res.json({ userId: result.insertId });
}

async function login(req, res) {
  const { email, password } = req.body;
  const [rows] = await pool.query(
    'SELECT id, password FROM users WHERE email = ?',
    [email]
  );
  if (!rows.length) return res.status(401).json({ error: 'Invalid credentials' });
  const user = rows[0];
  const match = await bcrypt.compare(password, user.password);
  if (!match) return res.status(401).json({ error: 'Invalid credentials' });

  // Generate TOTP
  const otp = speakeasy.totp({ secret: process.env.JWT_SECRET, digits: 6 });
  // Store OTP in Redis with 5 min expiry
  redisClient.setex(`otp_${user.id}`, 300, otp);
  await sendOTP(email, otp);
  res.json({ message: 'OTP sent' });
}

async function verifyOTP(req, res) {
  const { email, otp } = req.body;
  const [rows] = await pool.query(
    'SELECT id FROM users WHERE email = ?',
    [email]
  );
  if (!rows.length) return res.status(401).json({ error: 'Invalid user' });
  const userId = rows[0].id;

  redisClient.get(`otp_${userId}`, (err, stored) => {
    if (err || stored !== otp) return res.status(401).json({ error: 'Invalid OTP' });
    const token = generateToken({ userId });
    res.json({ token });
  });
}

module.exports = { signup, login, verifyOTP };
