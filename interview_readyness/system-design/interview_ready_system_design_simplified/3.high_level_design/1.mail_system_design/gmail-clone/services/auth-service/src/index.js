// index.js
const express = require('express');
const authRoutes = require('./routes/auth');
require('dotenv').config();

// import your pool
const pool = require('./db');

const app = express();
app.use(express.json());
app.use('/auth', authRoutes);

// simple health endpoint (we’ll enhance it below)
app.get('/health', async (req, res) => {
	try {
	 await pool.query('SELECT 1');
    	 res.json({ status: 'UP' });
  	} catch (err) {
    		console.error('Health check DB error:', err.message);
   		 res.status(503).json({ status: 'DOWN', error: err.message });
  	}
});

const PORT = process.env.PORT || 3000;

// wrap startup in an async init function
async function startServer() {
  try {
    // try a minimal query
    await pool.query('SELECT 1');
    console.log('✅ Database connection OK');

    // now start listening
    app.listen(PORT, () => {
      console.log(`Auth service running on port ${PORT}`);
    });
  } catch (err) {
    console.error('❌ Database connection failed:', err.message);
    process.exit(1);                            // abort startup
  }
}

startServer();

