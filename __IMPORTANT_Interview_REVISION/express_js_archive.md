- Serving static files in Express

```js
app.use(express.static('public'))

// http://localhost:3000/images/kitten.jpg
// http://localhost:3000/css/style.css
// http://localhost:3000/js/app.js
// http://localhost:3000/images/bg.png
// http://localhost:3000/hello.html


```

- serving multiple static files

```js
app.use(express.static('public'))
app.use(express.static('files'))

```

- to create a virtual path as prefix add

```js
app.use("/static", express.static("public"))

// every api should be prefixed with static thing now
```


- dynamic routes


```js
app.get('/users/:userId/books/:bookId', (req, res) => {
  res.send(req.params)
})

```


⚙️ 4. Middleware Basics (req, res, next)


```js
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next(); // move to the next middleware
});

```

🧱 Types of Middleware:

Application-level – Runs on every request (app.use()).

Router-level – Attached to specific routes using express.Router().

Built-in middleware – Like express.json() or express.static().

Third-party middleware – Like cors, helmet, or morgan.

```js
const express = require('express');
const app = express();

const userRoutes = require('./routes/userRoutes');

app.use(express.json());
app.use('/api/users', userRoutes);

module.exports = app;


const app = require('./src/app');

app.listen(3000, () => console.log('Server running on port 3000'));

```

- working with cookies

```js
// app.js
const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();

// Use cookie-parser middleware
app.use(cookieParser());

// Simple route to set a cookie
app.get('/set-cookie', (req, res) => {
  res.cookie('username', 'harshith', { maxAge: 60000 }); // expires in 1 minute
  res.send('Cookie has been set!');
});

// Route to read cookies
app.get('/get-cookie', (req, res) => {
  console.log(req.cookies); // logs: { username: 'harshith' }
  res.send(`Hello ${req.cookies.username}`);
});

// Route to clear cookie
app.get('/clear-cookie', (req, res) => {
  res.clearCookie('username');
  res.send('Cookie cleared!');
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));

```

- creating a signed cookie

```js
app.use(cookieParser('mySecretKey')); // pass a secret key

app.get('/set-signed', (req, res) => {
  res.cookie('token', 'abc123', { signed: true });
  res.send('Signed cookie set!');
});

app.get('/get-signed', (req, res) => {
  console.log(req.signedCookies); // { token: 'abc123' }
  res.send(`Signed cookie value: ${req.signedCookies.token}`);
});

```

# 🚀 Express.js Roadmap — From Basics to Advanced (10 Days)

### 🎯 Goal
Learn Express.js from scratch, build one full project, and prepare for interviews — all in 10 days.

Your project: **DevConnect** — a mini developer community API (like mini Reddit + Auth + Posts + Comments).

---

## 🗓️ Day 1 – Fundamentals + Setup
**Goal:** Understand what Express is and how Node.js + Express work together.

**Topics:**
- What is Express.js and why use it
- Installing Node & Express
- Creating your first server (`app.get('/', ...)`)
- Middleware basics (`req`, `res`, `next`)
- Handling routes and parameters (`req.params`, `req.query`)
- Folder structure for scalable Express apps

**Project Task:**
- Initialize your project with `npm init`
- Setup basic Express server
- Add `/health` route returning `{ status: 'ok' }`

---

## 🗓️ Day 2 – Routing & Middleware Deep Dive
**Goal:** Master routing and middleware chaining.

**Topics:**
- Express Router (`express.Router()`)
- Route parameters and grouping
- Built-in middleware (`express.json()`, `express.urlencoded()`)
- Custom middleware (logging, validation)
- Error-handling middleware

**Project Task:**
- Create routers: `/api/users`, `/api/posts`
- Add logging middleware
- Implement centralized error handler

---

## 🗓️ Day 3 – RESTful APIs + CRUD
**Goal:** Build real REST APIs and learn CRUD patterns.

**Topics:**
- HTTP methods: GET, POST, PUT, DELETE
- REST principles
- Sending JSON responses
- Handling invalid routes
- Proper status codes and response structure

**Project Task:**
- Implement `/api/posts` CRUD:
  - `GET /api/posts` → list posts
  - `POST /api/posts` → create post
  - `GET /api/posts/:id` → get single post
  - `PUT /api/posts/:id` → update post
  - `DELETE /api/posts/:id` → delete post

---

## 🗓️ Day 4 – Connecting Express with MySQL
**Goal:** Persist your data.

**Topics:**
- Intro to databases in Node.js
- Using MySQL (or PostgreSQL/MongoDB)
- Using `mysql2`, `sequelize`, or `prisma`
- Async/await with DB queries
- Environment variables (`dotenv`)

**Project Task:**
- Setup MySQL DB connection
- Store posts in DB
- Implement CRUD using SQL or ORM
- Add `.env` for DB credentials

---

## 🗓️ Day 5 – Authentication & Authorization
**Goal:** Implement secure login and access control.

**Topics:**
- JWT (JSON Web Token)
- Password hashing (`bcryptjs`)
- Auth middleware (protect routes)
- Role-based access (RBAC basics)

**Project Task:**
- Create `/api/auth/register` and `/api/auth/login`
- Generate and verify JWT tokens
- Protect post routes (only logged-in users can create/update/delete)
- Store user info in DB

---

## 🗓️ Day 6 – Validation, Security & Rate Limiting
**Goal:** Make your API robust and secure.

**Topics:**
- Input validation (`express-validator` or `joi`)
- Sanitization
- Rate limiting (`express-rate-limit`)
- CORS setup
- Helmet (security headers)

**Project Task:**
- Add validation for register/login/post APIs
- Add rate limiter for `/auth/login`
- Enable CORS for frontend
- Use Helmet for security

---

## 🗓️ Day 7 – File Uploads + Static Files
**Goal:** Handle user uploads and serve assets.

**Topics:**
- Static file serving (`express.static()`)
- File upload using `multer`
- File structure and storage (local vs cloud)
- Handling images in APIs

**Project Task:**
- Allow users to upload profile pictures
- Serve uploaded files via `/uploads`
- Validate file size and type

---

## 🗓️ Day 8 – API Versioning, Pagination & Optimization
**Goal:** Scale and optimize APIs.

**Topics:**
- Pagination (`limit`, `offset`, `page`)
- Sorting & filtering data
- API versioning (`/api/v1/...`)
- Query optimization (indexes, caching basics)

**Project Task:**
- Add pagination to `/api/posts`
- Implement `/api/v1` prefix for versioning
- Optimize queries for performance

---

## 🗓️ Day 9 – Testing + Error Handling
**Goal:** Write reliable and testable Express code.

**Topics:**
- Unit testing with Jest or Mocha
- Supertest for endpoint testing
- Centralized error handling patterns
- Logging with Winston or Morgan
- Handling async errors cleanly

**Project Task:**
- Write tests for Auth and Posts routes
- Add global error handler with stack trace logging
- Log all errors to a file

---

## 🗓️ Day 10 – Deployment + Interview Prep
**Goal:** Make your app production-ready and prepare for interviews.

**Topics:**
- Production environment setup
- Using PM2 or Docker
- Deploy on Render / Railway / AWS
- Express performance optimization (compression, caching)
- Common interview questions

**Project Task:**
- Deploy your API
- Write a README with setup steps
- Review interview concepts:
  - Middleware flow
  - Error handling
  - JWT flow
  - `app.use` vs `app.get`
  - How Express handles a request internally

---

## 💡 Bonus Topics (if you have time)
- WebSockets with Express + Socket.io (real-time notifications)
- Redis caching
- Rate limiter with Redis store
- Integrate a React frontend
- Dockerize your app

---

## 🧠 Interview Focus
Interviewers look for:
- Middleware and routing clarity
- Security awareness (auth, validation)
- Performance reasoning (pagination, caching)
- System design and scalability thinking

Document your learning as you go — it helps you stand out.

---

## ⚡ Next Step
Would you like a **daily time plan (hours + resource links)** to make this roadmap actionable?
I can give you a 10-day schedule with docs, videos, and code tasks aligned to each day.


- add more about domain specific things
  - scheduling cron jobs
  - triggeting email notifications
  - sending whats app message , sms.
  - building + storing dashboards type of data.