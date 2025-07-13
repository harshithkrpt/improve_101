
# 🧠 Node.js Mastery Guide (Concepts + 10 Projects)

---

## 🧱 1. Foundations of Node.js

**Topics:**
- What is Node.js?
- Event Loop
- V8 Engine
- Core Modules (`fs`, `http`, `path`, etc.)

### 🧱 Core Node.js Modules

Node.js provides several core (built-in) modules that are compiled into the binary distribution and can be used without installing them via npm.

---

#### 🗂️ File System & Paths

| Module        | Description                                  |
|---------------|----------------------------------------------|
| `fs`          | File system operations (read/write, watch)   |
| `fs/promises` | Promise-based file system API                |
| `path`        | File and directory path utilities            |

---

#### 🌐 Networking & Communication

| Module        | Description                                      |
|---------------|--------------------------------------------------|
| `http`        | Create HTTP servers and clients                  |
| `https`       | Secure HTTP communication                        |
| `net`         | TCP servers and clients                          |
| `tls`         | TLS/SSL secured socket communication             |
| `dgram`       | UDP datagram sockets                             |
| `dns`         | DNS resolution and lookups                       |

---

#### 🔄 Streams, Buffers, and Compression

| Module        | Description                           |
|---------------|---------------------------------------|
| `stream`      | Stream-based data handling            |
| `buffer`      | Working with binary data              |
| `zlib`        | Compression (gzip, deflate) utilities |

---

#### 🧠 Utilities & Helpers

| Module                | Description                           |
|------------------------|----------------------------------------|
| `util`                | Utility functions like `promisify()`   |
| `events`              | EventEmitter class                     |
| `assert`              | Assertion testing utilities            |
| `perf_hooks`          | Performance measuring tools            |
| `diagnostics_channel` | Publish/subscribe diagnostic channel   |

---

#### ⏱️ Timers

| Module            | Description                              |
|------------------|------------------------------------------|
| `timers`         | `setTimeout`, `setInterval`, etc.        |
| `timers/promises`| Promise-based timers                     |

---

#### 🧰 System & Process Management

| Module            | Description                                  |
|------------------|----------------------------------------------|
| `os`             | Information about the operating system        |
| `process`        | Provides process information & control        |
| `child_process`  | Spawn and communicate with child processes    |
| `cluster`        | Run multiple Node instances (multi-core)      |
| `worker_threads` | Spawn threads for parallel execution          |

---

#### 📦 Modules and Execution

| Module    | Description                                |
|-----------|--------------------------------------------|
| `module`  | Internal module loader                     |
| `vm`      | Run code in a virtual machine context      |
| `repl`    | Read-Eval-Print-Loop interface             |

---

#### 🔐 Security & Encryption

| Module    | Description                                |
|-----------|--------------------------------------------|
| `crypto`  | Cryptographic functionality (hashing, HMAC)|
| `https`   | Secure HTTP via TLS/SSL                    |

---

#### 🐞 Debugging & Inspection

| Module           | Description                                |
|------------------|--------------------------------------------|
| `inspector`      | DevTools inspection protocol               |
| `trace_events`   | Trace event diagnostics                    |
| `v8`             | Access to V8 engine internals              |

---

#### 🧪 Testing

| Module    | Description                                  |
|-----------|----------------------------------------------|
| `test`    | Built-in test runner (since Node v18+)       |

---

#### ✅ Usage

Core modules are used without installing them:

```js
const fs = require('fs');
const path = require('path');
```

**🛠️ Project 1: CLI File Organizer**  
Build a command-line tool that organizes files in a directory by extension.  
Learn `fs`, `path`, and CLI args (`process.argv`).

📘 Resources:
- [Node.js Handbook](https://flaviocopes.com/node-handbook/)
- [Node.js Official Docs](https://nodejs.org/en/docs)

---

## ⚙️ 2. Core Concepts

**Topics:**
- Asynchronous programming (`callback`, `promise`, `async/await`)
- Event Emitters
- Streams & Buffers
- Worker Threads & Child Processes

**🛠️ Project 2: Log File Reader (Streaming)**  
Stream and parse a large log file for search keywords using streams to avoid memory overhead.

📘 Resources:
- [Node.js Streams](https://nodejs.org/api/stream.html)
- [Understanding Worker Threads](https://nodejs.org/api/worker_threads.html)

---

## 🧰 3. Tooling & Package Management

**Topics:**
- `npm`, `yarn`, `npx`
- Package.json scripts
- Semantic versioning
- Monorepos (Lerna/Nx)

**🛠️ Project 3: Custom NPM Package**  
Create and publish a small utility package (like slugify or date formatter).

📘 Resources:
- [npm CLI Docs](https://docs.npmjs.com/)
- [Lerna](https://lerna.js.org/)
- [Nx](https://nx.dev/)

---

## 🏗️ 4. Server Development with Express.js

**Topics:**
- Express.js Routing
- Middleware
- Request/Response cycle
- Error handling
- REST API

**🛠️ Project 4: Blog API**  
Build a CRUD API with Express and file-based storage (no DB yet).  
Add validations, status codes, and modular structure.

📘 Resources:
- [Express.js Docs](https://expressjs.com/)

---

## 🔐 5. Security Best Practices

**Topics:**
- Helmet.js
- CORS
- Input validation
- Rate limiting
- JWT & session management

**🛠️ Project 5: Auth System**  
Add login/signup/logout to your blog API using JWT + password hashing (bcrypt).

📘 Resources:
- [OWASP Cheat Sheet for Node.js](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)

---

## 🧬 6. Database Integration

**Topics:**
- MongoDB with Mongoose
- PostgreSQL with Knex or Sequelize
- Redis for caching

**🛠️ Project 6: Todo App (DB-Powered)**  
Convert your Blog API to use MongoDB or PostgreSQL.  
Add basic filtering, pagination, and sorting.

📘 Resources:
- [Mongoose Docs](https://mongoosejs.com/)
- [Sequelize Docs](https://sequelize.org/)

---

## 🧪 7. Testing

**Topics:**
- Mocha, Chai, Jest
- Supertest
- Unit vs Integration Testing
- Test coverage

**🛠️ Project 7: Tested REST API**  
Add unit + integration tests to Blog or Todo app.  
Use `jest` + `supertest` + `mongodb-memory-server`.

📘 Resources:
- [Jest Docs](https://jestjs.io/)

---

## 🚀 8. Real-time & Microservices

**Topics:**
- WebSockets with `socket.io`
- Event-driven design
- Kafka/RabbitMQ
- Message queues

**🛠️ Project 8: Real-time Chat App**  
Build a socket-based multi-user chat app with rooms and private messaging.

📘 Resources:
- [Socket.io Docs](https://socket.io/docs/v4/)
- [Kafka with Node.js](https://www.npmjs.com/package/kafkajs)

---

## 🚚 9. Deployment & DevOps

**Topics:**
- `pm2`, Docker, Nodemon
- Logging (`winston`, `morgan`)
- `.env` handling
- GitHub Actions CI/CD

**🛠️ Project 9: Dockerized Production API**  
Dockerize Blog API with MongoDB.  
Setup `pm2`, `.env`, logging, and GitHub CI workflow.

📘 Resources:
- [PM2 Docs](https://pm2.keymetrics.io/)
- [Dockerizing Node.js App](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)

---

## ⚙️ 10. Architecture, Design Patterns, and System Design

**Topics:**
- Clean Code Architecture
- Layered, Modular Design
- Dependency Injection
- Microservices and Queues
- Load balancing and caching

**🛠️ Project 10: Push Notification System**  
A microservice with:  
- Kafka (event bus)  
- Elasticsearch for message history  
- Redis caching  
- React frontend  
- Real-time updates

📘 Resources:
- [Node.js Design Patterns Book](https://www.oreilly.com/library/view/nodejs-design-patterns/9781839214110/)
- [System Design Primer GitHub](https://github.com/donnemartin/system-design-primer)

---

## ✅ Bonus: Interview & Practice

- System Design: Rate Limiting, Retry, Throttling
- DSA: Practice NeetCode 150 in JS
- Build: URL Shortener, Instagram clone (backend), Job Queue, etc.