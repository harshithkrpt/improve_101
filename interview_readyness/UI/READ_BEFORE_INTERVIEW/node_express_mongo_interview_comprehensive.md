# Node.js, Express.js & MongoDB Interview Questions and Answers

Each entry includes a concise theory summary and a practical code snippet.

---

## 1. Explain the event loop in Node.js
**Theory:** Node’s event loop, powered by libuv, processes callbacks in phases: timers, I/O callbacks, idle, poll, check, and close, with separate microtask (process.nextTick, Promises) handling.
```js
console.log('start');
setTimeout(() => console.log('timeout'), 0);
process.nextTick(() => console.log('nextTick'));
Promise.resolve().then(() => console.log('promise'));
console.log('end');
// Output: start, end, nextTick, promise, timeout
```

---

## 2. Explain the internal architecture of Node.js
**Theory:** Node uses a single-threaded JS engine, a libuv thread pool for I/O, and an event loop to delegate non-blocking operations.
```js
// 'fs' operations use the thread pool
const fs = require('fs');
fs.readFile('data.txt', 'utf8', (err, data) => {
  console.log(data);
});
console.log('Reading file...');
```

---

## 3. What is npm and list out its uses
**Theory:** npm is Node’s package manager for installing, versioning, and publishing packages, managing dependencies via package.json.
```bash
npm init -y
npm install express mongoose dotenv
npm run start
```

---

## 4. What are the different phases of the event loop
**Theory:** Phases: timers (setTimeout), pending callbacks, idle, poll (I/O), check (setImmediate), close; microtasks run after each phase.
```js
setImmediate(() => console.log('check phase'));
setTimeout(() => console.log('timer phase'), 0);
```

---

## 5. Execution flow of Promise, async/await, setTimeout, setImmediate, process.nextTick()
**Theory:** nextTick → Promises → I/O callbacks → timers → check; async/await is syntax over Promises.
```js
async function fn() {
  await Promise.resolve();
  console.log('after await');
}
fn();
process.nextTick(() => console.log('nextTick'));
Promise.resolve().then(() => console.log('promise'));
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));
```

---

## 6. Purpose of package.json in Node.js
**Theory:** Describes project metadata, scripts, dependencies, and configuration.
```json
{
  "name": "app",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.18.0"
  }
}
```

---

## 7. http module and creating a server
**Theory:** Built-in http module handles HTTP requests/responses.
```js
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type':'text/plain'});
  res.end('Hello, Node.js!');
});
server.listen(3000);
```

---

## 8. Secure server setup with Express and HTTPS
**Theory:** Use HTTPS module with SSL certificates.
```js
const fs = require('fs');
const https = require('https');
const express = require('express');
const app = express();
const options = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};
https.createServer(options, app).listen(443, () => console.log('HTTPS running'));
```

---

## 9. Updating existing npm packages
**Theory:** Use `npm update [pkg]`, or `npm install pkg@latest`.
```bash
npm outdated
npm update express
```

---

## 10. Global objects in Node.js
**Theory:** Objects like `global`, `process`, `__dirname`, `module.exports`.
```js
console.log(global);
console.log(process.env.NODE_ENV);
```

---

## 11. Stream vs Buffer
**Theory:** Buffer holds raw binary data; streams process data in chunks.
```js
const fs = require('fs');
const readStream = fs.createReadStream('file.txt');
readStream.on('data', chunk => console.log(chunk.toString()));
```

---

## 12. Microtask and macrotask in Node.js
**Theory:** Microtasks (process.nextTick, Promises) run before next phase; macrotasks are timers, I/O, setImmediate.
```js
setImmediate(() => console.log('macrotask'));
process.nextTick(() => console.log('microtask'));
```

---

## 13. Piping between streams
**Theory:** Connects readable to writable streams for efficient data transfer.
```js
const fs = require('fs');
fs.createReadStream('in.txt').pipe(fs.createWriteStream('out.txt'));
```

---

## 14. Features of Express.js
**Theory:** Minimalist, middleware-based routing, plugins for templating, error handling.
```js
const express = require('express');
const app = express();
app.use(express.json());
app.get('/', (req, res) => res.send('Hello'));
```

---

## 15. Passing parameter to next() in middleware
**Theory:** `next(err)` signals error-handling middleware.
```js
app.use((req, res, next) => {
  if (!req.user) return next(new Error('Unauthorized'));
  next();
});
```

---

## 16. Skipping middleware
**Theory:** Call `next('route')` to skip remaining middleware for that route.
```js
app.get('/user/:id', mw1, (req, res, next) => {
  if (req.params.id === '0') return next('route');
  next();
}, mw2);
```

---

## 17. Difference between PATCH and PUT
**Theory:** PUT replaces entire resource; PATCH applies partial updates.
```js
app.put('/item/:id', /* full update */);
app.patch('/item/:id', /* partial update */);
```

---

## 18. Middleware concept in Node.js
**Theory:** Functions with access to req, res, next, used for logging, auth, parsing.
```js
function logger(req, res, next) { console.log(req.url); next(); }
app.use(logger);
```

---

## 19. Optional path parameters in Express
**Theory:** Use `?` in route definitions.
```js
app.get('/user/:id?', (req, res) => res.send(req.params.id || 'none'));
```

---

## 20. Error handling in Express.js
**Theory:** Error middleware signature `err, req, res, next`.
```js
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});
```

---

## 21. JWT and token structure
**Theory:** JSON Web Token: header.payload.signature, signed with secret.
```js
const jwt = require('jsonwebtoken');
const token = jwt.sign({ userId: 1 }, 'secret', { expiresIn: '1h' });
```

---

## 22. Modifying JWT signature
**Theory:** Tampering invalidates signature; cannot modify without secret.
```js
// Attempting jwt.decode without verify will show payload but invalid signature
```

---

## 23. Authentication vs Authorization
**Theory:** AuthN verifies identity; AuthZ checks permissions.
```js
// AuthN: passport.authenticate()
// AuthZ: role-based middleware
```

---

## 24. Role-based & permission-based access control
**Theory:** Check roles/permissions in middleware.
```js
function permit(...allowed) {
  return (req, res, next) => {
    if (allowed.includes(req.user.role)) return next();
    res.status(403).send('Forbidden');
  };
}
```

---

## 25. API best practices
**Theory:** Use REST conventions, versioning, validation, pagination.
```js
// Example: GET /api/v1/items?page=2&limit=10
```

---

## 26. Input validation & sanitization
**Theory:** Use libraries like express-validator to prevent injection.
```js
const { body, validationResult } = require('express-validator');
app.post('/user', [
  body('email').isEmail(),
], (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) return res.status(400).json({ errors: errors.array() });
});
```

---

## 27. Rate limiting
**Theory:** Throttle requests using middleware (express-rate-limit).
```js
const rateLimit = require('express-rate-limit');
app.use(rateLimit({ windowMs: 60000, max: 10 }));
```

---

## 28. Logging & monitoring
**Theory:** Use Winston, Morgan, or external APM (New Relic).
```js
const morgan = require('morgan');
app.use(morgan('combined'));
```

---

## 29. Stateless vs Stateful API
**Theory:** Stateless APIs do not store client context between requests; stateful do.
```js
// JWT-based auth is stateless.
```

---

## 30. State management in Node.js
**Theory:** Use external stores (Redis) or in-memory caches with caution.
```js
const redis = require('redis');
const client = redis.createClient();
```

---

## 31. Scaling with cluster module
**Theory:** Spawn multiple worker processes sharing server port.
```js
const cluster = require('cluster');
if (cluster.isMaster) {
  for (let i = 0; i < 4; i++) cluster.fork();
} else {
  require('./server.js');
}
```

---

## 32. Worker threads for CPU tasks
**Theory:** Offload CPU-bound work to worker_threads.
```js
const { Worker } = require('worker_threads');
new Worker('./worker.js');
```

---

## 33. Concurrency vs parallelism
**Theory:** Concurrency via async callbacks; parallelism via threads or processes.

---

## 34. Optimizing database queries
**Theory:** Use indexes, projections, and query optimization.
```js
db.collection('users').find({}, { projection: { password: 0 } });
```

---

## 35. Redis and its uses
**Theory:** In-memory store for caching, sessions, pub/sub.
```js
client.set('key', 'value', 'EX', 60);
```

---

## 36. Improving Node.js performance
**Theory:** Avoid blocking code, use clustering, caching.
```js
// Avoid synchronous fs
fs.readFileSync('data.txt');
```

---

## 37. Profiling in Node.js
**Theory:** Use --inspect and Chrome DevTools or clinic.js.

---

## 38. Connection pooling
**Theory:** Reuse DB connections to reduce overhead.
```js
const mongoose = require('mongoose');
mongoose.connect(uri, { poolSize: 10 });
```

---

## 39. RBAC middleware example
**Theory & Code:**
```js
function rbac(roles) {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) return res.status(403).end();
    next();
  };
}
```

---

## 40. OAuth2.0 integration
**Theory:** Use Passport strategies (e.g., passport-google-oauth).
```js
passport.use(new GoogleStrategy({...}, (token, refresh, profile, done) => { ... }));
```

---

## 41. Refresh token mechanism
**Theory:** Issue long-lived refresh tokens and rotate on use.
```js
// On refresh: verify refreshToken, issue new accessToken & refreshToken
```

---

## 42. Role of indexes in performance
**Theory:** Indexes speed up lookups but slow writes and use memory.
```js
db.users.createIndex({ email: 1 }, { unique: true });
```

---

## 43. MongoDB aggregation pipeline
**Theory:** Process data through staged transformations (`$match`, `$group`, `$sort`).
```js
db.orders.aggregate([
  { $match: { status: 'A' } },
  { $group: { _id: '$custId', total: { $sum: '$amount' } } }
]);
```

---

## 44. Transactions in MongoDB
**Theory:** Multi-document ACID transactions in replica set or sharded clusters.
```js
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Order.create([{ /*...*/ }], { session });
  await session.commitTransaction();
} catch (e) {
  await session.abortTransaction();
}
```

---

## 45. Transactions and rollback
**Theory:** On error, abortTransaction reverts changes within the session.

---

## 46. Hashing vs Encryption vs Encoding
**Theory:** Hashing is one-way; encryption is reversible; encoding is for data transport.
```js
const bcrypt = require('bcrypt');
bcrypt.hash('password', 10).then(hash => console.log(hash));
```

---

## 47. Identifying slow queries
**Theory:** Use MongoDB profiler or `.explain()`.
```js
db.collection('users').find({}).explain('executionStats');
```

---

## 48. Replica sets and sharding
**Theory:** Replica sets for high availability; sharding for horizontal scaling.

---

## 49. Failover and DR in MongoDB
**Theory:** Configure replica sets with appropriate priorities and backup strategies.

---

## 50. Load balancer in Node.js
**Theory:** Use Nginx or AWS ELB, or Node’s cluster with sticky sessions.

---

## 51. Avoiding schema pitfalls
**Theory:** Use schema validation with Mongoose or MongoDB validator.

---

## 52. Efficient queries
**Theory:** Lean projections, limit and skip, and cursor optimization.

---

## 53. Health checks in MongoDB
**Theory:** Use ping command or implement HTTP /health endpoint checking DB connection.

```js
app.get('/health', async (req, res) => {
  try {
    await mongoose.connection.db.admin().ping();
    res.sendStatus(200);
  } catch {
    res.sendStatus(500);
  }
});
```

---

## 54. SOLID principles
**Theory:** Single Responsibility, Open-Closed, Liskov, Interface Segregation, Dependency Inversion applied in JS modules and services.

---

## 55. Kafka and use cases
**Theory:** Distributed streaming for event sourcing, log aggregation, real-time pipelines.

---

## 56. Minimizing middleware overhead
**Theory:** Mount middleware only on needed routes and keep functions lightweight.
