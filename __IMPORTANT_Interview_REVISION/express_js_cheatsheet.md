# Express.js — Introduction Cheatsheet

**Previewable + Downloadable Link:** Use the canvas preview in the top‑right to download/export.

---

## I. 💡 Basic Details of Express.js
Express.js is a minimalist and flexible web framework for Node.js designed to simplify building HTTP APIs and web applications. It provides a thin abstraction over Node’s built-in `http` module, letting developers define routes, plug in middleware, and manage request/response flows without boilerplate.

**Purpose**
- Make route handling simpler and more structured.
- Provide a powerful middleware system for cross-cutting concerns (auth, logging, validation).
- Enable quick prototyping and production-ready API development.

**History & relevance**
Launched in 2010, Express became the de‑facto standard framework in the Node ecosystem, powering countless APIs, services, and applications. Even newer frameworks (Fastify, NestJS) build on patterns popularized by Express.

**Minimal app structure**
A basic Express app exposes an `app` instance, registers middleware, registers routes, and starts an HTTP server.

---

## II. 🧠 Important Concepts to Remember
**1. Middleware stack** — Functions that run in order for every request unless short‑circuited. They modify `req`, `res`, or pass control using `next()`. Think of it like a conveyor belt where each station can inspect or transform the request.

**2. Routing** — Mapping URL paths + HTTP verbs (GET, POST, PUT, DELETE) to handlers. Express routes match in the order defined.

**3. Request/Response objects** — `req` holds incoming data (params, query, headers, body). `res` sends the final output (`json()`, `send()`, `status()`).

**4. Error handling middleware** — A special middleware with 4 arguments `(err, req, res, next)` used to catch errors globally.

**5. Application-level vs Router-level middleware** — You can group routes into `express.Router()` instances for clean modular design.

**6. Built-in vs third-party middleware** — Built-ins like `express.json()` parse bodies; third-party ones handle tasks like rate-limiting or CORS.

**7. Request lifecycle** — Request enters → passes through middleware chain → reaches route handler → generates response → optional error handler.

---

## III. 📝 Theory — Most Asked Interview Questions (with concise answers)

**Q1: What is Express used for?**
**A:** Express is used to build HTTP APIs and web applications in Node.js. It simplifies routing, middleware composition, and request handling.

**Q2: Explain middleware in Express.**
**A:** Middleware are functions that execute sequentially for each request. They can read/modify `req` and `res`, perform validation, logging, authentication, or stop the chain by sending a response.

**Q3: What is the request/response lifecycle in Express?**
**A:** A request enters the app, flows through ordered middleware, reaches a route handler, and the handler sends a response. If an error occurs, the error-handling middleware processes it.

**Q4: How does Express handle routing?**
**A:** Routes are defined per HTTP method and matched in the order they are registered. You can group routes using routers.

**Q5: Why is Express called “unopinionated”?**
**A:** Express does not enforce folder structure, patterns, or architecture. Developers decide how to organize code.

---

## IV. 💻 Coding / Practical — Most Asked Questions (with approaches)

**Q1: Create a minimal Express server.**
**Approach:** Initialize `express()`, register `express.json()`, define a route (`app.get('/'...)`), and call `app.listen()`.

**Q2: Build custom middleware for logging.**
**Approach:** Define a function `(req, res, next)` that logs details, then call `next()`.

**Q3: Create modular routing with `express.Router()`.**
**Approach:** Instantiate a router, define routes on it, export it, and mount it with `app.use('/api', router)`.

**Q4: Implement error handling middleware.**
**Approach:** Write a function `(err, req, res, next)` that returns a structured error JSON.

**Q5: Add validation using third‑party middleware.**
**Approach:** Use a library like `joi`/`celebrate` or `zod` to validate incoming request bodies inside a route or middleware.

---

## V. 🚀 Follow-Up Topics to Learn
**1. Fastify** — A faster alternative to Express with built‑in schema validation and improved performance.

**2. NestJS** — A structured framework built around Express (or Fastify), offering modules, DI, decorators.

**3. OpenAPI / Swagger** — Document and validate Express APIs with auto‑generated client SDKs.

**4. Authentication & Authorization** — Strategies using JWT, OAuth2, sessions, and Passport.js.

**5. Performance & Security** — Learn rate limiting, helmet, morgan, clustering, caching, and load-testing.

---

Let me know if you'd like runnable code samples (minimal app, routers, error-handling), or if you want this exported as Markdown/PDF.

[Previewable + Downloadable Link](#)

# Express.js — Routing Cheatsheet

### I. 💡 Basic Details of Express.js Routing

**Definition & purpose**
Express routing is the mechanism by which an Express application maps HTTP requests (method + path) to JavaScript functions (route handlers). Routing makes your server respond to different endpoints and HTTP verbs (GET, POST, PUT, DELETE, etc.), enabling REST APIs, web pages, and microservices.

**Short history & relevance**
Express is a minimalist Node.js web framework created in 2010 that became the de facto standard for building server-side apps in Node. Routing is one of its central features — understanding it is essential for building well-structured, maintainable backends.


### II. 🧠 Important Concepts to Remember

1. **Route definition (path + method)**
   * `app.get('/users', handler)` — routes are defined by an HTTP verb and a path. Think of routes like numbered post boxes: each combination of verb+path points to a different handler.

2. **Route parameters (`:id`)**
   * URL segments prefixed with `:` become `req.params`. Use for resource identifiers: `/users/:userId/orders/:orderId`.
   * Analogy: params are variable slots in a template URL.

3. **Query parsing (`?page=2`)**
   * Query string parameters appear in `req.query`. Use for filters, pagination, sorting.
   * Analogy: query string is the options menu for how you want the data presented.

4. **Route ordering & precedence**
   * Express matches routes top-to-bottom. Specific routes should come before catch-alls or param-heavy routes. Wildcards and `app.use()` can shadow later routes.
   * Think of routes like firewall rules — first match wins.

5. **Modular routers (`express.Router`)**
   * Routers let you split endpoints into modules (e.g., `usersRouter`, `ordersRouter`). Mount with `app.use('/users', usersRouter)`.
   * Analogy: routers are neighbourhoods in a city map — each handles its own streets.

6. **Middleware in routing**
   * Middleware can be global (`app.use`), router-level, or route-level. Middleware runs before handlers and can modify `req`/`res` or terminate the request.

7. **Error handling & async handlers**
   * Use `next(err)` or centralized error middleware (`(err, req, res, next)` signature). Wrap async handlers or use helper wrappers to catch rejections.


### III. 📝 Theory — Most Asked Questions (Interview Prep)

**Q1: How does Express decide which route handler to run for a request?**
**Model answer:** Express checks defined routes in the order they were added. For each route it tests both the HTTP method and the path pattern; the first matching route's middleware/handler chain runs. Middlewares added with `app.use()` can also run if their path matches or if they are global.

**Q2: What's the difference between route params and query params?**
**Model answer:** Route params (`req.params`) are part of the URL path used to identify resources (e.g., `/users/:id`). Query params (`req.query`) are key/value pairs in the query string used for filtering, pagination or options and are not part of the resource identity.

**Q3: How do you mount and organize routes in a large Express app?**
**Model answer:** Use `express.Router()` to group related routes (users, auth, posts). Export routers from modules and mount them with `app.use('/prefix', router)`. Apply router-level middleware for authentication or validation to avoid duplication.

**Q4: How should you handle async route handlers and errors?**
**Model answer:** Wrap async handlers to catch promise rejections (e.g., a small helper `const wrap = fn => (req,res,next)=>fn(req,res,next).catch(next)`) and provide centralized error-handling middleware with the four-argument signature to produce consistent error responses.

**Q5: Explain route ordering pitfalls and how to avoid them.**
**Model answer:** A generic route (e.g., `app.get('/:slug')` or `app.use('*', ...)`) placed earlier can intercept requests intended for more specific routes. Put concrete routes first, then param routes, then wildcards/404 handlers. Keep `app.use()` with path prefixes carefully ordered.


### IV. 💻 Coding / Practical — Most Asked Questions (Interview Prep)

**P1: Define a router for `users` with CRUD endpoints.**
**Approach:** Use `express.Router()`, define `GET /` (list), `POST /` (create), `GET /:id` (read), `PUT /:id` (update), `DELETE /:id` (delete). Mount with `app.use('/users', usersRouter)`.

**P2: Parse pagination and validation for a list endpoint.**
**Approach:** Read `req.query.page` and `req.query.limit`, coerce with `parseInt`, clamp defaults, and validate. Use middleware or a validation library (Joi, Zod) at route-level to keep handler code focused.

**P3: Route parameter middleware (e.g., preload user by `:userId`).**
**Approach:** Use `router.param('userId', async (req, res, next, id) => { req.user = await User.findById(id); if(!req.user) return next(new Error('Not found')); next(); })` then handlers can use `req.user` directly.

**P4: Avoiding route conflicts and shadowing.**
**Approach:** Order routes: static/specific routes first. Prefer explicit prefixes (`/users/new` before `/users/:id`). Use stricter parameter patterns if necessary (e.g., regex `/:id(\d+)`).

**P5: Implementing auth middleware on selected routes.**
**Approach:** Write `function requireAuth(req,res,next){ if(!req.user) return res.status(401).json({...}); next(); }` and attach it like `router.post('/', requireAuth, createHandler)` or apply to router `router.use(requireAuth)` for all routes.

**P6: Example — create a paginated `GET /users` handler (pseudo):**
```
// inside usersRouter
router.get('/', async (req,res,next)=>{
  const page = Math.max(1, parseInt(req.query.page)||1);
  const limit = Math.min(100, parseInt(req.query.limit)||20);
  const skip = (page-1)*limit;
  const items = await User.find().skip(skip).limit(limit);
  res.json({page, limit, items});
});
```


### V. 🚀 Follow-Up Topics to Learn

1. **Middleware patterns & composition** — to write reusable middleware and transaction-safe request flows.
2. **Authentication & Authorization (JWT, sessions, OAuth)** — necessary to secure route access correctly.
3. **Testing Express apps (supertest, jest/mocha)** — unit and integration tests for route behavior and error handling.
4. **TypeScript + Express** — for better type safety in route parameters, `req`/`res` augmentation and larger codebases.
5. **Performance & scaling (clustering, reverse proxies, rate-limiting)** — avoid bottlenecks in routing under heavy load.

---

*Quick tweak ideas:* add example projects, ESLint & routing conventions, or a small cheatsheet file with command snippets and common regex route patterns.

# Express.js — Middleware Cheatsheet

> **Previewable + Downloadable link in the top-right corner**

---

## I. 💡 Basic Details of Express.js Middleware

**Definition:** Middleware in Express.js is a function with signature `(req, res, next)` (or `(err, req, res, next)` for error middleware) that sits in the request-response pipeline and can read/modify the `req` and `res` objects, end the response, or pass control to the next middleware by calling `next()`.

**Purpose & relevance:** Middleware composes application behavior — routing, parsing, auth, logging, error handling, and more — into small reusable units. It’s the backbone of Express’s extensibility and a core pattern for building web servers in Node.js.

**History:** Influenced by Connect (the precursor to Express). Express formalized middleware ordering and handler conventions that remain standard across many Node frameworks.

---

## II. 🧠 Important Concepts to Remember

1. **Middleware types (application, router, error-handling):**
   - *Application middleware* is attached to the `app` (e.g., `app.use(...)`) and runs for every matching route.
   - *Router middleware* lives on `express.Router()` instances and runs only for routes handled by that router.
   - *Error-handling middleware* has four arguments `(err, req, res, next)` and is called when `next(err)` is used or an exception bubbles.
   *Analogy:* Think of middleware as conveyor-belt workers — app-level workers see all packages, router workers only see boxes routed to their line, error workers handle broken packages.

2. **`next()` and control flow:** Calling `next()` passes control to the next matching middleware. Calling `next('route')` skips remaining middleware for the current route and jumps to the next route. Omitting `next()` or not ending the response causes the request to hang.

3. **Synchronous vs asynchronous middleware:** If middleware is async (returns a promise or uses `async`), errors thrown must be passed to Express via `next(err)` or will be caught automatically in recent Express versions if `async` functions are used correctly. Always `return` or `await` asynchronous work to avoid leaking control.

4. **Composing middleware:** Multiple middleware can be composed in an array or chained inline. Order is significant — earlier middleware can modify `req`/`res` for later middleware.

5. **Built-in vs third-party vs custom middleware:** Express exposes a few utilities (like `express.static`), but most functionality comes from third-party packages (e.g., `body-parser` — now built into Express as `express.json()`/`express.urlencoded()`, `compression`, `cors`, `helmet`, `morgan`) or project-specific middleware.

6. **Short-circuiting and response lifecycle:** Middleware can end the response (`res.send`, `res.json`, `res.end`). Once the response is sent, other middleware will not run for that request unless you intentionally stream or pipe.

7. **Mount paths and middleware specificity:** `app.use('/api', middleware)` mounts middleware only for paths starting with `/api`. Router instances can be mounted similarly (`app.use('/users', usersRouter)`).

---

## III. 📝 Theory — Most Asked Questions (Interview Prep)

**Q1: What is middleware in Express and how does it work?**
**A:** Middleware are functions that receive `req`, `res`, and `next`. They can inspect/modify the request and response objects, end the response, or call `next()` to continue. Middleware are invoked in registration order for matching routes.

**Q2: How do you write error-handling middleware?**
**A:** Define a function with four parameters: `function errorHandler(err, req, res, next) { /* handle, log, respond */ }`. Register it after routes: `app.use(errorHandler)`. Call `next(err)` upstream or throw in async handlers to route control to it.

**Q3: How does `next('route')` differ from `next()`?**
**A:** `next()` passes control to the next middleware/handler; `next('route')` skips remaining middleware for the current route and jumps to the next route handler.

**Q4: When should you place authentication middleware — before or after route handlers?**
**A:** Before the route handlers it should protect. Mount it at the app/router level or on specific routes. Use selective mounting to avoid authenticating public assets.

**Q5: Why does order matter in middleware?**
**A:** Because middleware can modify `req`/`res` and can short-circuit responses. The registration order defines pipeline behavior.

---

## IV. 💻 Coding/Practical — Most Asked Questions (Interview Prep)

**Problem 1 — Implement a request logger middleware**
- *Question:* Write middleware that logs method and URL and continues.
- *Optimal approach:* Simple sync middleware using `console.log` and `next()`.

```js
function logger(req, res, next) {
  console.log(`${req.method} ${req.originalUrl}`);
  next();
}
app.use(logger);
```

**Problem 2 — Error capture for async route handlers**
- *Question:* Ensure async route errors are passed to Express error handler.
- *Optimal approach:* Use a helper wrapper or `express-async-handler`, or an `async` wrapper:

```js
const wrap = (fn) => (req, res, next) => Promise.resolve(fn(req, res, next)).catch(next);
app.get('/items', wrap(async (req, res) => {
  const items = await db.get();
  res.json(items);
}));
```

**Problem 3 — Compose middleware for a route**
- *Question:* Apply validation, auth, and handler in order.
- *Optimal approach:* Chain middleware array on the route.

```js
app.post('/orders', [validateOrder, requireAuth, createOrderHandler]);
```

**Problem 4 — Create an error-handling middleware that hides stack traces in production**
- *Question:* Return error message but avoid leaking stack.
- *Optimal approach:* Check `process.env.NODE_ENV`.

```js
function errorHandler(err, req, res, next) {
  const status = err.status || 500;
  const body = { message: err.message };
  if (process.env.NODE_ENV !== 'production') body.stack = err.stack;
  res.status(status).json(body);
}
app.use(errorHandler);
```

**Problem 5 — Mount middleware for a route prefix**
- *Question:* Serve JSON parsing only on `/api` endpoints.
- *Optimal approach:* `app.use('/api', express.json(), apiRouter)` — keeps other routes unaffected.

---

## V. 🚀 Follow-Up Topics to Learn

1. **Express internals & Connect pipeline** — learn how Express matches routes and how middleware stack is implemented (good for debugging and advanced middleware).
2. **Security middleware (Helmet, rate-limiters)** — important for production hardening.
3. **Streaming & middleware (file uploads, proxies)** — handling large payloads and backpressure properly.
4. **Testing middleware (supertest + sinon/jest)** — how to unit-test middleware in isolation.
5. **Alternative frameworks (Koa, Fastify)** — compare middleware design (Koa uses async functions and `ctx`, Fastify emphasizes performance and plugin encapsulation).

---

*Quick tips:* Keep middleware small and single-responsibility. Prefer composition (small middleware combined) over monolith middleware. Always handle errors and timeouts explicitly.

---

*Generated: Express.js — Middleware Cheatsheet*


# Express.js — Request Handling Cheatsheet

---

### I. 💡 Basic Details of Request Handling

**Definition & purpose**
Request handling in Express.js is the set of primitives and patterns for receiving HTTP requests, extracting data from them, and sending responses. It covers the `req` (request) and `res` (response) objects, streaming behavior, body parsing, and best practices for robust, secure handlers.

**Brief history & relevance**
Express, created in 2010, standardized a minimal, middleware-driven approach to handling HTTP in Node.js. Request handling is central to building web APIs and server-side apps — it shapes performance, security, and developer ergonomics.

---

### II. 🧠 Important Concepts to Remember (5–7 key ideas)

1. **`req` and `res` core shape**
   - `req` contains incoming data: headers (`req.headers`), method (`req.method`), URL (`req.url`), params (`req.params`), query (`req.query`), body (`req.body`), and a readable stream (`req` itself).
   - `res` is the writable side: methods like `res.status()`, `res.set()`, `res.send()`, `res.json()`, `res.end()`; it is also a writable stream.
   - Analogy: `req` is an incoming letter with attachments; `res` is your reply envelope and stamp.

2. **Middleware pattern & `next()`**
   - Handlers are chained functions `(req, res, next)`; call `next()` to pass control. Error middleware has signature `(err, req, res, next)`.
   - Use middleware for parsing, auth, logging, validation — keep handlers single-responsibility.

3. **Streams in req/res: memory vs streaming**
   - `req` and `res` are Node streams; large payloads should be streamed (e.g., file uploads/downloads) to avoid high memory use.
   - Use `pipeline()` or `stream.pipe()` for efficient transfers. If you `await` `req` into memory (e.g., body-parsers), you trade memory for convenience.

4. **Body parsing strategies**
   - Built-in `express.json()` and `express.urlencoded()` for common JSON and form-encoded bodies. `body-parser` used to be external; now largely wrapped by Express.
   - For raw, text, or custom parsing, use `express.raw()` / `express.text()` or custom middleware.
   - For multipart/form-data (files) use `multer`, `busboy`, or `formidable` (do not use `express.json()` for file streams).

5. **Security & validation at the boundary**
   - Set size limits (e.g., `{ limit: '10kb' }`) to mitigate DoS. Always validate/sanitize `req.body`, `req.params`, and `req.query`.
   - Check `Content-Type` before parsing. Use helmet, rate-limiting, and CORS policies where appropriate.

6. **Idempotency & status codes**
   - Choose correct HTTP verbs and idempotent behavior. Return clear status codes and use `res.location()`/`res.set()` for headers.

7. **Error handling & async handlers**
   - Wrap async route handlers to forward errors to Express (or use a helper to catch rejected promises). Unhandled rejections can crash the app if not forwarded to error middleware.

---

### III. 📝 Theory — Most Asked Questions (Interview Prep)

**Q1: What’s the difference between `req.params`, `req.query`, and `req.body`?**
**A:** `req.params` are URL route parameters (e.g., `/users/:id`), `req.query` are URL query strings (`?page=2`), and `req.body` contains the parsed request payload (POST/PUT PATCH) provided by body-parsing middleware.

**Q2: How does Express handle middleware ordering?**
**A:** Express executes middleware and routes in the order they are `app.use()`/`app.METHOD()` registered. First-match wins for route handlers; ensure parsing and auth middleware are registered before routes that rely on them.

**Q3: How do streams affect request handling?**
**A:** `req` is a readable stream and `res` a writable stream. Streams let you process data incrementally (important for large uploads/downloads). Using streams avoids buffering entire payloads in memory and reduces latency.

**Q4: How would you safely parse JSON bodies?**
**A:** Use `express.json({ limit: 'Xkb' })` to parse JSON with a size limit, validate types and required fields, handle `SyntaxError` from parser via error middleware, and check `Content-Type: application/json` when necessary.

**Q5: What is the proper way to handle errors in async route handlers?**
**A:** Wrap async handlers with a try/catch and call `next(err)` on error, or use a helper wrapper like `const wrap = fn => (req,res,next)=>fn(req,res,next).catch(next)`. Provide centralized error middleware `(err, req, res, next)`.

---

### IV. 💻 Coding / Practical — Most Asked Questions

**P1: Implement streaming a large file download**
- *Question:* How to stream a file from disk to the response and set correct headers?
- *Approach:* Use `fs.createReadStream(filePath).pipe(res)` or `pipeline()` to stream and handle errors; set `res.setHeader('Content-Type', mime)` and `res.setHeader('Content-Length', size)` if known; use `res.status(200)`.

**P2: Parse JSON body with size limit and handle parse errors**
- *Question:* Add JSON body parsing with 10kb limit and provide friendly error response on invalid JSON.
- *Approach:* `app.use(express.json({ limit: '10kb' }))` and an error handler:

```js
app.use((err, req, res, next) => {
  if (err.type === 'entity.parse.failed' || err instanceof SyntaxError) {
    return res.status(400).json({ error: 'Invalid JSON' });
  }
  next(err);
});
```

**P3: Accept file upload without buffering entire file**
- *Question:* Receive multipart upload and stream file to disk or S3.
- *Approach:* Use `busboy` or `multer` with streaming mode; with `busboy` you can pipe the file stream directly to storage (avoid memory buffers).

**P4: Build an endpoint that supports both JSON and raw text**
- *Question:* Single route should accept either `application/json` or `text/plain`.
- *Approach:* Mount both parsers before route: `app.use(express.json({ limit }))`, `app.use(express.text({ type: 'text/*', limit }))`, then inspect `req.get('Content-Type')` or check `typeof req.body` in handler.

**P5: Protect against large payload DoS**
- *Question:* How to limit request body sizes and overall request rate?
- *Approach:* Use the parser `limit` option, `express-rate-limit`, reverse-proxy/body-size enforcement at nginx/cluster level, and timeouts for slow requests.

---

### V. 🚀 Follow-Up Topics to Learn

1. **Streaming & Backpressure (Node streams & `stream.pipeline`)** — deep dive to efficiently handle large data flows and correctly manage backpressure.
   - *Why:* Critical for file transfers, proxied requests, and memory-safe servers.

2. **Multipart form handling & file storage patterns** — `busboy`, `multer`, direct-to-S3 streaming.
   - *Why:* Real-world apps often accept files; doing it right improves performance and security.

3. **API Security at the edge** — rate limiting, content-type validation, request throttling, helmet, CORS patterns.
   - *Why:* Prevents common attack vectors and hardens production endpoints.

4. **Testing request handlers** — `supertest`, integration testing patterns, mocking streams.
   - *Why:* Ensures correctness and prevents regressions in complex request flows.

5. **Performance profiling (Node/Express)** — using flamegraphs, monitoring request latency, Node event-loop insights.
   - *Why:* Optimizes throughput and reduces p99 latency for production services.

---

*Cheatsheet created for quick interview prep and reference. Concise examples are included; adapt limits and libs to your project's needs.*

