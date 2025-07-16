const express = require('express');
const authRoutes = require('./routes/auth');
require('dotenv').config();

const app = express();
app.use(express.json());

app.use('/auth', authRoutes);

app.get('/health', (req, res) => res.send('Auth service healthy'));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Auth service running on port ${PORT}`));