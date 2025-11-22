# ES6+ Modules Cheat Sheet
## import/export syntax, live bindings (JavaScript)

### ES6 Modules Overview
ES6 modules introduce a native module system in JavaScript. They allow code splitting into reusable files with explicit imports and exports. Modules are always executed in strict mode. Each module has its own scope and is loaded once; subsequent imports use the same module instance.

### Exporting
You can export bindings for others to import.

**Named exports**
```js
export const pi = 3.14;
export function add(a, b) { return a + b; }
export class Logger { log(x) { console.log(x); } }
```

**Export list**
```js
const x = 10;
const y = 20;
export { x, y };
```

**Renaming exports**
```js
function greet() {}
export { greet as sayHello };
```

**Default exports**
```js
export default function () { return 'hi'; }
export default class Person {}
export default 42;
```

### Importing
**Named imports**
```js
import { add, pi } from './math.js';
```

**Renaming imports**
```js
import { add as sum } from './math.js';
```

**Default import**
```js
import foo from './module.js';
```

**Mixing default + named**
```js
import foo, { x, y } from './module.js';
```

**Import all**
```js
import * as utils from './utils.js';
utils.doSomething();
```

### Live Bindings
ES6 modules use *live bindings*. This means imports reflect updates to the exported variables.

```js
// counter.js
export let count = 0;
export function inc() { count++; }

// main.js
import { count, inc } from './counter.js';
console.log(count); // 0
inc();
console.log(count); // 1   live binding!
```

The imported binding is not a copy; it's a reference to the exported variable.

### Module Execution Model
- Each module is evaluated once and cached.
- Imports always refer to the same module instance.
- Circular imports are supported but evaluated carefully: dependent modules get partially initialized bindings.

### Interview Q&A (Theory)
**What are ES6 modules?**  
A built‑in module system supporting imports and exports with static structure.

**Difference between default and named exports?**  
A module can have one default export; named exports can be many. Import syntax differs.

**What are live bindings?**  
Imports are references, not copies. Changes in the exporting module reflect in the importing module.

**Why are ES6 imports statically analyzable?**  
Import/export syntax must appear at top level and cannot be dynamic, allowing bundlers and engines to optimize.

**How do modules handle circular dependencies?**  
They expose partially initialized bindings; evaluation order is determined by the dependency graph.

### Coding Questions
**1. Implement a module that maintains private state using exports.**
```js
// store.js
let value = 0;
export const get = () => value;
export const set = v => { value = v; };
```

**2. Create a module that exports a function and a default configuration.**
```js
// config.js
export default { env: 'prod' };
export function setEnv(e) { console.log(e); }
```

**3. Demonstrate live binding with two modules.**
```js
// a.js
export let n = 1;
export function inc() { n++; }

// b.js
import { n, inc } from './a.js';
inc();
console.log(n); // 2
```

# ES6+ Promises Cheat Sheet  
### Topic: Promises  
### Sub Topic: Chaining, async/await Conversion  

---

## 🔹 What Are Promises?
A Promise is an object representing the eventual completion or failure of an asynchronous operation.  
It has three states: **pending**, **fulfilled**, and **rejected**.

---

## 🔹 Promise Chaining
Promise chaining allows asynchronous tasks to run in sequence, where the output of one `.then()` is fed into the next.

### Example
```js
fetchData()
  .then(response => processData(response))
  .then(result => saveResult(result))
  .then(() => console.log("Completed"))
  .catch(err => console.error(err));
```

### Key Points
- Each `.then()` returns a new Promise.
- Errors propagate down the chain until caught by `.catch()`.
- Returning values from `.then()` passes them forward.

---

## 🔹 Converting Chained Promises to async/await

### Promise Chain
```js
getUser()
  .then(user => getPosts(user.id))
  .then(posts => getComments(posts))
  .catch(err => handleError(err));
```

### Equivalent async/await
```js
async function loadUserData() {
  try {
    const user = await getUser();
    const posts = await getPosts(user.id);
    const comments = await getComments(posts);
    return comments;
  } catch (err) {
    handleError(err);
  }
}
```

### Why async/await is nicer
- Looks synchronous (but is still async)
- Easier error handling with `try/catch`
- No deeply nested `.then()` chains

---

## 🔹 Theory-Based Interview Questions (With Concise Answers)

**1. What is a Promise?**  
A Promise is an object representing an async task that will complete in the future with a success value or an error.

**2. What does “Promise chaining” mean?**  
It means using `.then()` sequentially so the result of one promise is passed into the next.

**3. How does error handling work in Promise chains?**  
Any rejection propagates down until it hits a `.catch()`.

**4. Difference between `async/await` and `.then()`?**  
`async/await` is syntactic sugar over Promises, making asynchronous code appear synchronous.

**5. What happens if you forget `await` inside async function?**  
You get a pending promise instead of its resolved value.

**6. Are async functions still using Promises internally?**  
Yes, async functions always return a Promise.

---

## 🔹 Coding Interview-Style Problems

### Problem 1: Implement a delay using Promises
```js
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Usage:
await delay(1000);
console.log("Executed after 1s");
```

### Problem 2: Convert a callback to a Promise
```js
function fetchData(cb) {
  setTimeout(() => cb(null, "done"), 1000);
}

function fetchDataPromise() {
  return new Promise((resolve, reject) => {
    fetchData((err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}
```

### Problem 3: Run async tasks in sequence
```js
async function runTasks(tasks) {
  const results = [];
  for (const task of tasks) {
    results.push(await task());
  }
  return results;
}
```

### Problem 4: Run async tasks in parallel
```js
async function runParallel(tasks) {
  return Promise.all(tasks.map(t => t()));
}
```

---

## 🚀 Quick Reference Summary

- `.then()` chains async operations.
- `.catch()` handles any rejection in the chain.
- `.finally()` always runs regardless of success or failure.
- `async/await` simplifies promise usage.
- Always wrap async operations in `try/catch`.

---

# ES6+ Map & Set Cheat Sheet  
### Topic: Map & Set  
### Sub Topic: Unique Elements, Iteration  

---

## 🔹 Set: Unique Collections

A **Set** stores unique values.  
No duplicates, no index-based access—just pure uniqueness in a tidy little bag.

### Creating a Set
```js
const s = new Set([1, 2, 3, 3]);
console.log(s); // Set {1, 2, 3}
```

### Core Operations
```js
s.add(4);
s.has(2);   // true
s.delete(1);
s.size;     // number of elements
```

### Iteration
```js
for (const value of s) {
  console.log(value);
}
```

### Convert Set → Array
```js
const arr = [...s]; 
```

### When to Use a Set
- Deduplicating arrays  
- Checking existence fast (`O(1)` average)  
- Iterating unique elements in insertion order  

---

## 🔹 Map: Key–Value Store With Superpowers

A **Map** allows keys of any type—objects, functions, primitives.  
More predictable than plain objects for dictionary-style operations.

### Creating a Map
```js
const map = new Map();
map.set("name", "Harshith");
map.set(42, "answer");
map.set({ x: 1 }, "object-key");
```

### Core Operations
```js
map.get("name");
map.has(42);
map.delete(42);
map.size;
```

### Iteration Patterns
```js
for (const [k, v] of map) console.log(k, v);     // entries
for (const k of map.keys()) console.log(k);      // keys
for (const v of map.values()) console.log(v);    // values
```

### Convert Map → Object (if keys are strings)
```js
Object.fromEntries(map);
```

### When to Use a Map
- When you need keys that aren’t strings  
- When key insertion order matters  
- When performance on frequent inserts/lookups matters  

---

## 🔹 Theory-Based Interview Questions (Concise Answers)

**1. Difference between Map and Object?**  
Map allows any key type, preserves insertion order, and provides predictable iteration. Objects force string keys and have prototypal baggage.

**2. Difference between Set and Array?**  
Set ensures uniqueness, provides fast lookup, and has no index access.

**3. How does Map ensure key uniqueness?**  
Keys are compared using SameValueZero (like `===` but treats `NaN` equal to `NaN`).

**4. Can a Set contain objects?**  
Yes. Uniqueness is based on reference identity, not structure.

**5. How is iteration order preserved?**  
Both Map and Set preserve insertion order and iterate using that order.

**6. Complexity of Map/Set operations?**  
`O(1)` average for insert, lookup, delete.

---

## 🔹 Coding Interview–Style Problems

### Problem 1: Remove duplicates using Set
```js
const dedupe = arr => [...new Set(arr)];
```

### Problem 2: Count frequency using Map
```js
function freqCount(arr) {
  const map = new Map();
  for (const item of arr) {
    map.set(item, (map.get(item) || 0) + 1);
  }
  return map;
}
```

### Problem 3: Find first unique element
```js
function firstUnique(arr) {
  const map = freqCount(arr);
  for (const item of arr) {
    if (map.get(item) === 1) return item;
  }
  return null;
}
```

### Problem 4: Use Set for fast membership checks
```js
function intersection(a, b) {
  const s = new Set(b);
  return a.filter(x => s.has(x));
}
```

---

## 🚀 Quick Reference Summary

- **Set** → unique values, fast lookup, simple iteration.  
- **Map** → flexible keys, ordered, optimized for key/value operations.  
- Both preserve insertion order.  
- Both ideal for performance-heavy tasks.  

---

# ES6+ Classes Cheat Sheet  
### Topic: Classes  
### Sub Topic: Inheritance, Static Methods, Private Fields  

---

## 🔹 What Are ES6 Classes?
Classes provide a cleaner, more structured syntax for creating constructor functions and prototypes.  
They are still prototype-based under the hood, just presented with a modern, readable face.

---

## 🔹 Basic Class Syntax
```js
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello, ${this.name}`;
  }
}
```

---

## 🔹 Inheritance (extends + super)

### Example
```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);          // call parent constructor
    this.breed = breed;
  }

  speak() {
    return `${this.name} barks`;
  }
}
```

### Key Points
- `extends` establishes prototype inheritance.
- `super()` must be called before `this` in child constructors.
- Overriding methods works via prototype resolution.

---

## 🔹 Static Methods

Static methods belong to the class itself—not its instances.

```js
class MathOps {
  static add(a, b) {
    return a + b;
  }
}

MathOps.add(2, 3); // 5
```

### When to use static methods
- Utility functions  
- Factory methods  
- Operations that don’t depend on instance data  

---

## 🔹 Private Fields (#field)

Private fields are accessible only inside the class.

```js
class Counter {
  #count = 0;

  increment() {
    this.#count++;
  }

  get value() {
    return this.#count;
  }
}
```

### Characteristics
- Cannot be accessed outside (`obj.#count` → SyntaxError)  
- Cannot be dynamically added  
- Enforced at language level  

---

## 🔹 Theory-Based Interview Questions (Concise Answers)

**1. Are classes in JS syntactic sugar?**  
Yes. Under the hood they use prototypes.

**2. What does `super` do?**  
Calls the parent constructor or parent methods.

**3. Difference between `super()` and `super.method()`?**  
`super()` invokes parent constructor; `super.method()` calls a parent method.

**4. Are static methods inherited?**  
Yes, child classes inherit static methods unless overridden.

**5. Why private fields?**  
They ensure true encapsulation without naming conventions.

**6. Can you access private fields via bracket notation?**  
No. They are not real property keys.

**7. What happens if child constructor doesn't call `super()`?**  
Using `this` before calling `super()` throws a ReferenceError.

---

## 🔹 Coding Interview–Style Problems

### Problem 1: Implement a simple class with private fields
```js
class BankAccount {
  #balance = 0;

  deposit(amount) { this.#balance += amount; }
  withdraw(amount) { this.#balance -= amount; }
  getBalance() { return this.#balance; }
}
```

### Problem 2: Inheritance with method override
```js
class Vehicle {
  move() { return "Moving"; }
}

class Car extends Vehicle {
  move() { return "Car driving"; }
}
```

### Problem 3: Static factory method
```js
class User {
  constructor(name) { this.name = name; }

  static fromJSON(json) {
    return new User(json.name);
  }
}
```

### Problem 4: Use private fields for encapsulation
```js
class Temperature {
  #celsius;

  constructor(c) { this.#celsius = c; }
  toF() { return this.#celsius * 9/5 + 32; }
}
```

---

## 🚀 Quick Reference Summary

- Classes are modern syntax over prototypes.  
- Inheritance uses `extends` and `super`.  
- Static methods belong to the class, not instances.  
- Private fields (`#field`) provide true encapsulation.  
- Overriding methods follows prototype chaining.  

---

# ES6+ Default Parameters — Cheat Sheet

## Topic: ES6+ Features  
## Sub Topic: Default Parameters (Default values in functions)

Default parameters allow functions to initialize values when no argument or `undefined` is passed.

---

## Detailed Explanation

Default parameters were introduced in ES6. They remove the need for manual checks like:

```js
param = param || "default";
```

Example:

```js
function greet(name = "Guest") {
  return `Hello, ${name}!`;
}
```

`greet();` → `"Hello, Guest!"`

Defaults apply only if the argument is missing or `undefined`.  
Passing `null` does **not** trigger the default.

```js
greet(null); // "Hello, null!"
```

Default values can be expressions:

```js
function add(a, b = a) {
  return a + b;
}
```

They work with destructuring too:

```js
function config({ theme = "light", debug = false } = {}) {
  console.log(theme, debug);
}

config(); // light false
```

# Practice & Interview Questions — ES6 Default Parameters

## Theory / Interview Questions (With Short Answers)

1. **When is a default parameter used?**  
   When the argument is `undefined` or not provided.

2. **Difference between `null` and `undefined` for defaults?**  
   `undefined` triggers default; `null` is a valid value.

3. **Can default parameters depend on earlier parameters?**  
   Yes — evaluated left to right.

4. **Do default parameters have their own scope?**  
   Yes, parameter initialization happens in a separate scope.

5. **Can default parameters be combined with destructuring?**  
   Yes, very commonly for config objects.

## Coding Practice Problems

1. **Implement `multiply(a, b = 1)`**  
   ```js
   function multiply(a, b = 1) {
     return a * b;
   }
   // multiply(5) -> 5
   // multiply(5, 3) -> 15
   ```

2. **Write `makeUser(name = "Anonymous", role = "viewer")` returning an object.**  
   ```js
   function makeUser(name = "Anonymous", role = "viewer") {
     return { name, role };
   }
   ```

3. **Implement `connect({ host = "localhost", port = 3306 } = {})`.**  
   ```js
   function connect({ host = "localhost", port = 3306 } = {}) {
     return `Connecting to ${host}:${port}`;
   }
   ```

4. **Arrow function with defaults:**  
   ```js
   const sum = (a = 0, b = 0) => a + b;
   ```

---

## Notes on splitting content into multiple files

If the content becomes large, I will split the material into multiple `.md` files by logical sections (e.g., theory, examples, exercises, advanced topics). Each file will be provided as a separate downloadable `.md` file.

# Browser & Web APIs – Fetch & Axios  
## fetch API, interceptors, cancellation (JavaScript)

---

## 1. Fetch API – Detailed Explanation

### What Fetch Is  
Fetch is the modern, promise‑based API for making HTTP requests in browsers. It returns a Promise that resolves to a `Response` object. The surface is minimal: you get streaming bodies, async reading, and no magic defaults.

### Core Features  
- Promise-based request handling  
- Supports streaming responses  
- Supports **AbortController** for cancellation  
- Automatically rejects only on **network errors** (not HTTP errors)

### Basic Syntax  
```js
fetch("https://api.example.com/data")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

### POST Request  
```js
await fetch("/login", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ username, password })
});
```

### Handling HTTP Errors Manually  
```js
const res = await fetch("/api");

if (!res.ok) {
  throw new Error(`HTTP ${res.status} – ${res.statusText}`);
}
```

---

## 2. Fetch Cancellation with AbortController  
Cancellation is *built in* with Fetch.

```js
const controller = new AbortController();

fetch("/long-task", { signal: controller.signal })
  .catch(err => {
    if (err.name === "AbortError") {
      console.log("Request cancelled");
    }
  });

// cancel
controller.abort();
```

Useful for:
- Search‑as‑you‑type  
- Avoiding race conditions  
- Cancelling slow requests on route change  

---

## 3. Axios – Detailed Explanation

Axios is a promise-based HTTP client with more conveniences than fetch.

### Why Axios?  
- Automatically rejects on **HTTP 4xx/5xx**  
- JSON parsing done automatically  
- Request/response interceptors  
- Request cancellation (AbortController or legacy cancel tokens)  
- Timeout built‑in  

### Basic Axios Request  
```js
import axios from "axios";

const res = await axios.get("/api");
console.log(res.data);
```

### POST Example  
```js
await axios.post("/login", { username, password });
```

---

## 4. Axios Interceptors  
Interceptors allow modifying requests/responses globally.

### Request Interceptor  
```js
axios.interceptors.request.use(config => {
  config.headers["Authorization"] = "Bearer token123";
  return config;
});
```

### Response Interceptor  
```js
axios.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401) {
      console.log("Unauthorized, redirect to login");
    }
    return Promise.reject(err);
  }
);
```

Uses:
- Attach tokens  
- Global error handling  
- Logging  
- Response transformation  

---

## 5. Axios Request Cancellation  
Axios supports AbortController (recommended):

```js
const controller = new AbortController();

axios.get("/slow", { signal: controller.signal })
  .catch(err => {
    if (axios.isCancel(err)) console.log("Cancelled");
  });

controller.abort();
```

---

## 6. Interview Theory Questions (Concise Answers)

**Q1: Difference between Fetch and Axios?**  
Fetch is built‑in, minimal, and manual with error handling; Axios is feature-rich with interceptors, JSON handling, and automatic HTTP error rejection.

**Q2: Why does fetch not reject on HTTP errors?**  
By design—it only rejects on network failures. HTTP error codes still produce valid responses.

**Q3: How do you cancel fetch requests?**  
Using `AbortController` and passing `signal` to fetch.

**Q4: How do Axios interceptors work?**  
They allow hooking into requests/responses, modifying config or handling errors globally.

**Q5: How do you set timeouts in fetch?**  
No native timeout—must use `AbortController` and set a manual timer.

**Q6: Does Axios support streaming?**  
Axios in the browser doesn’t support streaming responses like Fetch does.

---

## 7. Coding-Based Questions + Solutions

### 1. Implement Fetch with Timeout  
```js
function fetchWithTimeout(url, ms) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), ms);

  return fetch(url, { signal: controller.signal })
    .finally(() => clearTimeout(timeout));
}
```

### 2. Create a Custom Axios Instance with Interceptors  
```js
const api = axios.create({
  baseURL: "https://api.example.com"
});

api.interceptors.request.use(cfg => {
  cfg.headers["X-App"] = "InterviewApp";
  return cfg;
});
```

### 3. Retry Fetch Request (Simple Retry Logic)  
```js
async function retryFetch(url, options, retries = 3) {
  try {
    return await fetch(url, options);
  } catch (err) {
    if (retries === 0) throw err;
    return retryFetch(url, options, retries - 1);
  }
}
```

---

Downloadable `.md` file prepared below.

# Browser & Web APIs – LocalStorage & SessionStorage  
## differences, size limits, serialization (JavaScript)

---

## 1. LocalStorage & SessionStorage – Detailed Explanation

LocalStorage and SessionStorage are part of the Web Storage API — tiny key‑value databases inside the browser.  
They look harmless, like a desk drawer, but behave more like a desk drawer with a strict librarian guarding exactly 5MB of space.

Both stores only **string data**, persist synchronously, and are scoped per-origin.

### LocalStorage  
LocalStorage persists **until explicitly cleared** by:
- Code (`localStorage.clear()`)
- Browser manually cleared
- User clearing site data

It survives:
- Page reloads  
- Browser restarts  
- System restarts  

### SessionStorage  
SessionStorage persists **only for the current tab session**.  
It is cleared when:
- The tab is closed  
- `sessionStorage.clear()` is called  
- The browser crashes (sometimes)  

A duplicated tab gets a **fresh** SessionStorage.

---

## 2. API Methods (Same for Both)

```js
localStorage.setItem("key", "value");
localStorage.getItem("key");
localStorage.removeItem("key");
localStorage.clear();
```

Keys & values **must be strings**.

### Checking if key exists
```js
if (localStorage.getItem("token") !== null) {}
```

---

## 3. Serialization  
Because only strings are allowed, objects need formatting.

### Storing Objects  
```js
localStorage.setItem("user", JSON.stringify({ name: "Harshith", role: "dev" }));
```

### Retrieving Objects  
```js
const user = JSON.parse(localStorage.getItem("user"));
```

### Handling JSON safely  
```js
function getJSON(key) {
  try {
    return JSON.parse(localStorage.getItem(key));
  } catch {
    return null;
  }
}
```

---

## 4. Differences Between LocalStorage & SessionStorage

| Feature | LocalStorage | SessionStorage |
|--------|--------------|----------------|
| Lifespan | Until cleared | Until tab closes |
| Tab Isolation | Shared across tabs | Unique per tab |
| Browser Restart | Persists | Erased |
| Storage Limit | ~5–10MB | ~5MB |
| Use Case | Tokens, theme, preferences | Form state, temporary data |

---

## 5. Storage Size Limits  
The limits vary by browser but commonly:
- Chrome: 10MB per origin  
- Firefox: 10MB  
- Safari: ~5MB  
- Mobile: Often 2.5–5MB  

Both are **synchronous** → can block main thread for very large writes.

---

## 6. Interview Theory Questions (Concise Answers)

**Q1: Why can LocalStorage only store strings?**  
Because the spec defines it as a simple string-based key-value store — not structured storage.

**Q2: How do you store objects in LocalStorage?**  
Serialize with `JSON.stringify` and parse with `JSON.parse`.

**Q3: Why avoid storing JWT tokens in LocalStorage?**  
They are vulnerable to XSS attacks; better to use httpOnly cookies.

**Q4: Key difference between LocalStorage and SessionStorage?**  
Persistence: LocalStorage is permanent until cleared, SessionStorage resets per tab session.

**Q5: Why is LocalStorage synchronous?**  
The Web Storage API was designed before async patterns were common; small size makes synchronous acceptable.

**Q6: Maximum storage of LocalStorage?**  
Usually 5–10MB depending on browser.

---

## 7. Coding-Based Questions + Solutions

### 1. Implement a wrapper that auto-serializes data  
```js
const store = {
  set(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
  },
  get(key) {
    return JSON.parse(localStorage.getItem(key));
  },
  remove(key) {
    localStorage.removeItem(key);
  }
};
```

### 2. Check available space in LocalStorage  
```js
function storageRemaining() {
  let used = 0;
  for (let key in localStorage) {
    const val = localStorage.getItem(key);
    if (val) used += key.length + val.length;
  }
  return used;
}
```

### 3. Migrate data from SessionStorage → LocalStorage  
```js
Object.keys(sessionStorage).forEach(key => {
  localStorage.setItem(key, sessionStorage.getItem(key));
});
```

---

The Markdown file is ready below.

# Browser & Web APIs — Cookies & JWT  
## httpOnly, SameSite, Secure Flags (JavaScript)

---

## 1. Cookies & JWT Explained in Detail

### Cookies  
Cookies are tiny pieces of data stored by the browser and sent automatically with every request to the same domain.  
They are used for sessions, auth tokens, preferences, tracking, etc.

### JWT (JSON Web Token)  
A JWT is a signed token (header + payload + signature) used for stateless authentication.  
It is usually stored in:
- **httpOnly cookies** (more secure)
- or **LocalStorage** (less secure, vulnerable to XSS)

JWTs are *not cookies themselves*, but cookies can *store* JWTs.

---

## Important Cookie Flags

### httpOnly  
Prevents JavaScript access via `document.cookie`.  
Protects against XSS token theft.

**Use case:** Storing JWT securely.

```
Set-Cookie: token=abc123; HttpOnly
```

### Secure  
Cookie will only be sent on HTTPS.  
Protects against MITM attacks.

```
Set-Cookie: token=abc123; Secure
```

### SameSite  
Controls cross-site request behavior. Prevents CSRF.

Values:
- **Strict** → Only sent for same-site requests.
- **Lax** → Sent for top-level navigations (safe default).
- **None** → Cookie sent for cross-site… but MUST include `Secure`.

```
Set-Cookie: token=abc123; SameSite=Lax
```

---

## Cookie Example (JWT Storage)

### Server-side (Node.js / Express)

```js
res.cookie("token", jwtToken, {
  httpOnly: true,
  secure: true,
  sameSite: "lax",
  maxAge: 24 * 60 * 60 * 1000
});
```

### Browser cannot access:
```js
console.log(document.cookie); // JWT not visible due to httpOnly
```

---

## When to Use What

- **httpOnly** → Always ON for auth cookies.
- **Secure** → Always ON in production.
- **SameSite=Lax** → Best default, protects CSRF.
- **SameSite=None + Secure** → Needed for cross-domain setups (e.g., frontend on different domain).

---

## 2. Interview Questions with Crisp Answers

### 1. Why store JWT in httpOnly cookies instead of localStorage?  
Because `httpOnly` prevents token theft via XSS, while localStorage is readable by JavaScript.

### 2. Does httpOnly protect against CSRF?  
No. CSRF uses cookies automatically; httpOnly doesn't block requests. SameSite + CSRF tokens help.

### 3. What does SameSite None require?  
It requires `Secure=true` and HTTPS.

### 4. Can JavaScript read secure cookies?  
Yes, unless httpOnly is set. `Secure` only restricts transmission to HTTPS.

### 5. Why is SameSite=Lax preferred?  
It blocks most CSRF attacks but allows normal navigation-based flows.

---

## 3. Coding Questions (Applied)

### Q1: Set a cookie with JWT securely (Node.js)

```js
app.post("/login", (req, res) => {
  const token = createJWT(req.body);
  res.cookie("jwt", token, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    maxAge: 86400000
  });
  res.send("Logged in");
});
```

### Q2: Read a non-httpOnly cookie in JavaScript

```js
const theme = document.cookie
  .split("; ")
  .find((c) => c.startsWith("theme="))
  ?.split("=")[1];
```

### Q3: Delete cookie

```js
res.clearCookie("jwt", {
  httpOnly: true,
  secure: true,
  sameSite: "lax"
});
```

---

## 4. Summary for Quick Revision

- Cookies automatically sent ↔ JWT must be manually attached unless in cookies.  
- httpOnly protects against XSS.  
- Secure protects against non-HTTPS leaks.  
- SameSite protects against CSRF.  
- JWT + Cookies = secure, stateless authentication.

---

# Browser & Web APIs — Web Workers & Service Workers  
### background tasks, caching — JavaScript

---

## 1. Detailed Explanation

### Web Workers  
Web Workers allow JavaScript to run **in background threads** separate from the main UI thread.  
They do not block rendering or UI events. They cannot access the DOM or `window` directly.

**Use cases:**  
- Heavy computations  
- Image processing  
- Data parsing  
- Encryption / compression  

**Key points:**  
- Created using: `new Worker("worker.js")`  
- Communicate via `postMessage()` / `onmessage`  
- Terminate via `worker.terminate()`  
- Lifetime = tied to the page/tab that created them

---

### Service Workers  
Service Workers run as **network proxies** in the background, controlling how the browser handles requests.  
They enable offline caching, background sync, push notifications, and reliable loading.

**Use cases:**  
- Offline-first PWAs  
- Custom caching strategies  
- Background sync  
- Intercepting fetch calls  
- Push notifications

**Key points:**  
- Registered with:  
  ```js
  navigator.serviceWorker.register('/sw.js')
  ```
- Listens for: `install`, `activate`, `fetch`, `sync`, `push`  
- Requires HTTPS  
- Controls all pages under its scope  
- Independent of page lifecycle

---

### Key Differences

| Feature | Web Worker | Service Worker |
|--------|------------|----------------|
| Primary Purpose | CPU-heavy background tasks | Network proxy, offline, caching |
| DOM Access | ❌ No | ❌ No |
| Intercept Network | ❌ No | ✔️ Yes |
| Lifetime | Tied to page | Persistent, event‑driven |
| Events | `onmessage` | `install`, `activate`, `fetch`, `sync`, `push` |
| Use Case | Compute tasks | Caching, offline, PWA |

---

## 2. Interview Questions (Concise Answers)

**1. What is a Web Worker?**  
A background JavaScript thread to offload heavy computations without blocking UI.

**2. What is a Service Worker?**  
A programmable network proxy enabling offline caching, background sync, and push notifications.

**3. Why can't Workers access the DOM?**  
They run in separate threads for safety and concurrency control.

**4. Difference between Web Worker & Service Worker?**  
Web Worker handles CPU tasks; Service Worker handles network/caching and persists across sessions.

**5. Why does a Service Worker require HTTPS?**  
To prevent man‑in‑the‑middle attacks since it intercepts all network traffic.

**6. What is a fetch event?**  
Service Worker intercepts network requests via `self.addEventListener("fetch", ...)`.

**7. What is Stale-While-Revalidate?**  
Load cached data instantly while refreshing cache in background.

**8. How do Workers communicate?**  
With message passing (`postMessage` + `onmessage`).

---

## 3. Coding Examples

### Web Worker Example  
**worker.js**
```js
self.onmessage = (e) => {
  const n = e.data;
  let sum = 0;
  for (let i = 0; i < n; i++) sum += i;
  self.postMessage(sum);
};
```

**main.js**
```js
const worker = new Worker("worker.js");
worker.postMessage(1000000000);
worker.onmessage = (e) => {
  console.log("Result:", e.data);
  worker.terminate();
};
```

---

### Service Worker Caching Example

**sw.js**
```js
const CACHE = "v1";

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => {
      return cache.addAll(["/", "/index.html", "/app.js"]);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      return (
        cached ||
        fetch(event.request).then((res) => {
          return caches.open(CACHE).then((cache) => {
            cache.put(event.request, res.clone());
            return res;
          });
        })
      );
    })
  );
});
```

**main.js**
```js
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("/sw.js");
}
```

---

## 4. Summary

- Web Workers = CPU work off main thread  
- Service Workers = Background service for caching + offline + network control  
- Both cannot access DOM  
- Service Workers require HTTPS  
- Key to building responsive apps & PWAs  

---

# Browser & Web APIs — Intersection Observer  
### Lazy Loading, Infinite Scroll — JavaScript

---

## 1. Detailed Explanation

### What is the Intersection Observer API?  
Intersection Observer is a browser API that lets you **asynchronously detect when an element enters or leaves the viewport**.  
It removes the need for scroll event listeners and provides efficient lazy loading and infinite scrolling.

Core idea:  
The browser notifies you when a target element intersects with a root (viewport or container).

---

### Why it's better than scroll handlers  
- Scroll events fire continuously → heavy, causes jank.  
- Intersection Observer is **event-driven**, handled by browser internals.  
- More performant and battery-friendly.

---

### How to Create an Observer

```js
const observer = new IntersectionObserver((entries, obs) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      console.log("Visible!");
    }
  });
}, {
  root: null,      // viewport
  threshold: 0.1   // 10% visible
});
```

Attach to element:
```js
observer.observe(document.querySelector("#box"));
```

---

## 2. Lazy Loading Images with Intersection Observer

### HTML
```html
<img data-src="big-image.jpg" class="lazy" />
```

### JavaScript
```js
const imgs = document.querySelectorAll(".lazy");

const imgObserver = new IntersectionObserver((entries, obs) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      obs.unobserve(img);
    }
  });
}, { threshold: 0.1 });

imgs.forEach(img => imgObserver.observe(img));
```

How it works:  
- Images load only when coming into view.  
- Observer disconnects after loading once.

---

## 3. Infinite Scroll using Intersection Observer

### HTML
```html
<div id="list"></div>
<div id="sentinel"></div>
```

### JavaScript
```js
const sentinel = document.querySelector("#sentinel");

const loadMore = () => {
  for (let i = 0; i < 10; i++) {
    const item = document.createElement("div");
    item.textContent = "Item " + Math.random().toString(36).slice(2);
    document.querySelector("#list").appendChild(item);
  }
};

loadMore(); // initial

const observer = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting) {
    loadMore();
  }
}, {
  root: null,
  threshold: 1.0
});

observer.observe(sentinel);
```

How it works:  
- As sentinel becomes visible, new content loads.  
- Sentinel moves down as items append.

---

## 4. Options You Can Pass

```js
{
  root: null,          // null => viewport
  rootMargin: "0px",   // like CSS margin around root
  threshold: 0.25      // callback fires when 25% visible
}
```

Examples:  
- `threshold: 0` → enters viewport  
- `threshold: 1.0` → fully visible  
- `rootMargin: "200px"` → trigger earlier (good for preloading)

---

## 5. Interview Questions (Concise Answers)

**1. What is the Intersection Observer API?**  
An async browser API that tracks element visibility relative to viewport or container.

**2. Why is it preferred over scroll events?**  
Because it is event-driven, more efficient, and avoids running code on every scroll.

**3. What are key components of an observer?**  
Callback + options (`root`, `rootMargin`, `threshold`).

**4. How does lazy loading work with observers?**  
Observe images with `data-src`, load actual src when they intersect, unobserve afterwards.

**5. How to use it for infinite scrolling?**  
Attach observer to a sentinel element at bottom; when visible, load more items.

**6. Can an Intersection Observer track multiple elements?**  
Yes. Call `observe()` for each target.

**7. What is rootMargin used for?**  
To expand or shrink the observable viewport—useful for preloading slightly before visible.

**8. When should threshold be 1.0?**  
When the callback should run only when the element is fully visible.

---

## 6. Summary

- Detects visibility efficiently without scroll events  
- Perfect for lazy loading, infinite scroll, analytics, animations  
- Uses browser-optimized intersection logic  
- Supports root, rootMargin, threshold for fine control  
- Works across multiple targets with one observer  

---

# Browser & Web APIs: Clipboard & Notifications (JavaScript)

## Topic: Clipboard & Notifications  
## Sub Topic: copy/paste APIs, permissions

[Content already provided above in chat]

# Browser & Web APIs  
## Clipboard & Notifications (copy/paste APIs, permissions)

### Clipboard API  
**What it is**  
The Clipboard API lets web apps read-from and write-to the system clipboard (text, images, other formats), provided security/permission requirements are met.

**Key interfaces & methods**  
- `navigator.clipboard` → `Clipboard` object  
- `Clipboard.writeText(text)` → Promise that writes text to clipboard  
- `Clipboard.readText()` → Promise reading plain text from clipboard  
- `Clipboard.read()` → Promise reading data (images/other formats)  
- Events: `copy`, `cut`, `paste` via `ClipboardEvent` / `clipboardData`

**Usage conditions & security/permissions**  
- Secure context (HTTPS or localhost)  
- User gesture / focus / user interaction required often  
- Browser support must be checked  
- Permissions may be required (especially for `read`)  
- Data may be sanitized (for safety)  
- In iframes may need allow attributes (`allow="clipboard-read; clipboard-write"`)

**Example code**  
_**Copy text**_  
```js
async function copyTextToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    console.log('Copied to clipboard: ' + text);
  } catch (err) {
    console.error('Failed to copy: ', err);
  }
}
```
_**Read text**_  
```js
async function readClipboardText() {
  try {
    const text = await navigator.clipboard.readText();
    console.log('Read from clipboard: ', text);
  } catch (err) {
    console.error('Failed to read: ', err);
  }
}
```
_**Override copy event**_  
```js
document.addEventListener('copy', e => {
  e.clipboardData.setData('text/plain', 'My custom text');
  e.clipboardData.setData('text/html', '<b>My custom text</b>');
  e.preventDefault();
});
```

**Browser compatibility / fallback**  
- Check `'clipboard' in navigator` or `navigator.clipboard` before using.  
- Fallback: use `document.execCommand('copy')` technique (temporary textarea, select, copy).  
- Note: older browsers or iOS may have limited support.

**Summary**  
Use the async Clipboard API when available, but always check support and provide fallback. Be aware of security/permission constraints.

---

### Notifications API  
**What it is**  
The Notifications API allows a web page/app to send system-level notifications to the user (even when the page is in background) using the browser’s notification system.

**Key features & methods**  
- `Notification.requestPermission()` → Promise returning `'granted'`, `'denied'`, or `'default'`  
- `Notification.permission` → current permission state  
- `new Notification(title, options)` → show a notification (if permission granted)  
- Events: `onclick`, `onshow`, `onerror`, `onclose` on the notification object

**Permissions & security**  
- Requires secure context (HTTPS) in most browsers  
- Must ask user permission — cannot send blindly  
- Browser may remember user’s decision and not prompt repeatedly  
- Check support: `if ('Notification' in window)`

**Example code**  
```js
if ('Notification' in window) {
  Notification.requestPermission().then(permission => {
    if (permission === 'granted') {
      const notif = new Notification('Hello!', {
        body: 'This is your notification body.',
        icon: '/path/to/icon.png'
      });
      notif.onclick = () => {
        console.log('Notification clicked');
      };
    } else {
      console.log('Notification permission is ' + permission);
    }
  });
}
```

**Integration with Push & Service Workers**  
For more advanced use (e.g., notifications when the page is closed), integrate with Push API + service worker + browser push service.

**Summary**  
Ask permission, check support, then show notifications. Ensure you use HTTPS. For advanced apps, consider push notifications for background handling.

---

## Theory Questions & Concise Answers  
1. **What is the difference between `navigator.clipboard.writeText()` and `document.execCommand('copy')`?**  
   → `writeText()` is modern, asynchronous, promise-based, secure context required; `execCommand('copy')` is legacy, synchronous, less reliable.  
2. **What conditions must be met for Clipboard API to successfully read from the clipboard?**  
   → Secure context (HTTPS), user gesture/focus, permissions may be needed, browser support.  
3. **What are the possible return values of `Notification.requestPermission()` and what do they mean?**  
   → `'granted'` (allowed), `'denied'` (blocked), `'default'` (no decision/dismissed).  
4. **Why must web apps use a secure context for Clipboard and Notification APIs?**  
   → Because these APIs involve sensitive user data or OS-level features; secure context ensures integrity and prevents man-in-the-middle or malicious misuse.  
5. **Can you always read the clipboard anytime? If not, why?**  
   → No. Browsers restrict arbitrary clipboard reading for privacy and security. Usually need user gesture, permissions, focus, secure context.  
6. **How would you detect if the Notification API is supported in the browser?**  
   → By checking `if ('Notification' in window) { … }`.  
7. **What is a good fallback for copying text if the Clipboard API is not supported?**  
   → Use `document.execCommand('copy')`: create hidden `textarea`, set value, select, `execCommand('copy')`, remove element.

---

## Coding / Application Questions  
1. **Write a React component (using your stack) that displays a “Copy Link” button, and when clicked, copies a given URL to clipboard and shows a “Copied!” message.**  
   *(Implementation left to candidate; key is use of clipboard API, state for feedback, error handling.)*  
2. **For a web chat application: implement “Paste Image” from clipboard: when user pastes an image (e.g., screenshot), capture and display it.**  
   *(Key: use `navigator.clipboard.read()` if supported, iterate `ClipboardItem`s, convert `blob` to image, display; else fallback.)*  
3. **Create a function `showNotification(title, body)` that asks for permission if needed and displays a notification with the given title/body.**  
   *(Implementation: check `Notification.permission`, if 'default' call `requestPermission()`, if granted then `new Notification(...)`.)*  
4. **High-level: In a service-worker enabled PWA, integrate push notifications and handle click on notification to open a URL.**  
   *(Key: service worker registration, `push` event => `showNotification`, `notificationclick` event => `clients.openWindow(url)`.)*  
5. **Write error-resilient code for copying text that checks for clipboard API support, uses fallback if necessary, logs error if all fail.**  
   *(Already provided snippet above in “safeCopy” function.)*

---

---

# Topic : Browser & Web APIs

## Sub Topic : File & Blob APIs — file uploads, drag/drop (JavaScript)

---

## 1. Quick overview (what these APIs are)

- **Blob**: a file-like immutable object of raw binary data. Useful for creating binary payloads in-memory (e.g., images generated on the client). (MDN: Blob).
- **File**: a specialized `Blob` with metadata (`name`, `lastModified`) that represents a file from the user's system (from `<input type="file">` or drag/drop). (MDN: File).
- **FileList**: collection returned from `<input type="file">` or `DataTransfer.files`.
- **FileReader**: legacy high-level API to read blobs/files as text, ArrayBuffer, or data URL (works on main thread and in Web Workers).
- **ReadableStream / Streams API**: modern streaming APIs to process blob data without buffering whole file in memory.
- **FormData**: convenient key/value builder for `multipart/form-data` requests (works with `fetch` and `XMLHttpRequest`).
- **Drag & Drop (DataTransfer)**: `dragenter`, `dragover`, `drop` events with `event.dataTransfer.files` to access dropped files.
- **File System Access API (FileSystemHandle)**: (origin-trial / permissioned) lets sites read/write files and directories with user permission; useful for advanced editors and local file saves.
- **tus / resumable protocols**: open protocols/libs for resumable uploads (tus-js-client, server implementations).

Key references: MDN Web Docs — Blob & File & File API & FormData.

---

## 2. Common tasks & patterns (how to use them)

### Selecting files
```html
<input id="file" type="file" multiple accept="image/*,application/pdf" />
```
```js
const input = document.getElementById('file');
input.addEventListener('change', e => {
  const files = e.target.files; // FileList
  for (const f of files) console.log(f.name, f.size, f.type);
});
```

### Drag & drop
```html
<div id="dropzone">Drop files here</div>
```
```js
const dz = document.getElementById('dropzone');
['dragenter','dragover','dragleave','drop'].forEach(ev => dz.addEventListener(ev, e => e.preventDefault()));

dz.addEventListener('drop', e => {
  const files = e.dataTransfer.files; // FileList
  handleFiles(files);
});
```
Notes: call `event.preventDefault()` in `dragover` and `drop` to allow dropping. Use visual focus/hover styles for accessibility.

### Reading files in the browser
- Small reads: `FileReader.readAsArrayBuffer` / `readAsText` / `readAsDataURL`.
- Large files / streaming: `file.stream()` returns a `ReadableStream` you can `getReader()` from and pipe to processing code or to `fetch` body.

Example: streaming read (modern)
```js
async function streamFile(file) {
  const reader = file.stream().getReader();
  let received = 0;
  while (true) {
    const {done, value} = await reader.read();
    if (done) break;
    received += value.length;
    // process chunk (Uint8Array)
  }
}
```

### Uploading files
- **Simple**: `FormData` + `fetch` or `XHR`.
- **Large / resumable**: chunking + resume, or use tus protocol.

`fetch` + `FormData` example:
```js
const fd = new FormData();
fd.append('file', file, file.name);
fd.append('userId', '123');

fetch('/upload', { method: 'POST', body: fd })
  .then(r => r.ok ? r.json() : Promise.reject(r))
  .then(console.log)
  .catch(console.error);
```

Important: do NOT set `Content-Type` header manually when sending `FormData`; the browser sets the multipart boundary.

### Chunked upload (slice)
```js
const CHUNK = 5 * 1024 * 1024; // 5MB
async function uploadInChunks(file) {
  const total = file.size;
  let start = 0, index = 0;
  while (start < total) {
    const end = Math.min(start + CHUNK, total);
    const chunk = file.slice(start, end);
    const fd = new FormData();
    fd.append('chunk', chunk, file.name);
    fd.append('index', index);
    fd.append('start', start);
    await fetch('/upload/chunk', { method: 'POST', body: fd });
    start = end; index++;
  }
}
```
Then the server is responsible for reassembling chunks.

---

## 3. Server-side: Node + Express example (multer)
```js
// server.js
const express = require('express');
const multer = require('multer');
const fs = require('fs');
const upload = multer({ dest: 'uploads/' });
const app = express();

app.post('/upload', upload.single('file'), (req, res) => {
  // req.file has info: path, originalname, mimetype
  res.json({ok: true, file: req.file});
});

app.listen(3000);
```
For chunked uploads you can accept chunk requests, store them to a temp directory, and once all parts are present, use `fs.createWriteStream` to concatenate.

---

## 4. Security, privacy & permissions
- Browsers protect the local filesystem — you cannot read files without explicit user action (file input, drag/drop, or File System Access permission).
- Validate file type and size on both client and server.
- Avoid trusting `file.type` alone — MIME sniffing can be fooled; verify server-side (magic bytes / file signature) for critical systems.
- Rate-limit uploads and scan for malware on server.
- Use HTTPS for uploads.

---

## 5. Performance & UX best practices
- Show progress: use `XMLHttpRequest` `upload.onprogress` or the `fetch` + `ReadableStream` approach with custom progress events.
- For many small files, batch in a FormData or parallelize with limited concurrency (e.g., 3 simultaneous uploads).
- For large files, chunk and retry failed chunks; keep the checksum or ETag of each chunk.
- Use client-side resizing/compression for images before upload (Canvas, `createImageBitmap`, `blob.slice`, or `imageBitmapToBlob` workflow).
- Provide clear error messages and allow pause/resume.

---

## 6. Advanced topics & libraries
- **tus** (resumable): tus-js-client + compatible servers for resumable uploads.
- **File System Access API**: read/write files and directories after permission (good for editors, heavy local workflows).
- **Service Workers**: can cache upload metadata or perform background sync (note: Background Uploads API is still limited across browsers).
- **Direct-to-cloud**: presigned S3 uploads (client uploads directly to object store) to reduce server bandwidth.

References: MDN, tus.io, Cloudflare docs on resumable uploads.

---

## 7. Interview theory questions (concise answers)

1. **Q:** What is the difference between `Blob` and `File`?
   **A:** `File` inherits from `Blob` and adds file-specific metadata like `name` and `lastModified`. Use `File` for user-selected files.

2. **Q:** How does `FormData` work with `fetch`? Any gotchas?
   **A:** `FormData` serializes fields as `multipart/form-data`; do not set `Content-Type` manually — the browser will set the boundary. `fetch` will stream the body where supported.

3. **Q:** How can you implement resumable uploads?
   **A:** Chunk the file (e.g., slice), send each chunk with an identifier and index, track uploaded chunks on server and client, retry failed chunks. Alternatively use a protocol/library like `tus`.

4. **Q:** How to show upload progress?
   **A:** Use `XMLHttpRequest.upload.onprogress` for `XMLHttpRequest`. With `fetch` you need to use `ReadableStream` or track bytes sent in chunked uploads (native fetch doesn't expose upload progress easily in all browsers).

5. **Q:** Why should you verify file content on server even if you check on client?
   **A:** Client checks are easily bypassed. Server must validate MIME, size, and ideally sniff file signature or scan for malware.

---

## 8. Common interview coding questions (practical)

1. **Implement a drag-and-drop zone and upload selected files to `/upload` using `fetch` and `FormData`.**
   - Expected: Prevent default on drag events, extract `dataTransfer.files`, send via `FormData` using `fetch`, show progress, handle errors.

2. **Implement chunked upload client-side and server-side reassembly in Node/Express.**
   - Expected: Use `file.slice()`, send chunks with metadata, server writes chunks to temporary files and then concatenates them in order.

3. **Implement client-side image resizing before upload.**
   - Expected: Use `createImageBitmap` or `Image` + `canvas` to resize, then `canvas.toBlob()` to get a smaller `Blob` and upload.

---

## 9. Minimal working example (client)
```html
<input id="file" type="file" />
<div id="dz">Drop files here</div>
<script>
async function uploadFile(file){
  const fd = new FormData();
  fd.append('file', file, file.name);
  const res = await fetch('/upload', { method: 'POST', body: fd });
  return res.json();
}

const dz = document.getElementById('dz');
['dragenter','dragover'].forEach(e=>dz.addEventListener(e,ev=>ev.preventDefault()));

dz.addEventListener('drop', async ev => {
  ev.preventDefault();
  const files = ev.dataTransfer.files;
  for(const f of files) await uploadFile(f);
});
</script>
```

---

## 10. Quick checklist before production deploy
- Validate on server (MIME/type/size/signature).
- HTTPS and authentication.
- Rate limiting and quotas.
- Virus/malware scanning if user files are stored.
- Backups and lifecycle policies for stored files.
- Use presigned URLs when possible to avoid proxying large file data.

---

## 11. Further reading & links
- MDN: Blob, File, File API, FormData. citeturn0search0turn0search4turn0search5
- Resumable uploads (tus). citeturn0search6turn0search14
- Chunking & large uploads guidance (Cloudflare). citeturn0search3
- Practical drag & drop guides and examples. citeturn0search13turn0search1


---

*This cheat-sheet is optimized for interviews and quick implementation. If you want, I can produce a focused version for React (hooks + Dropzone integration), or a detailed Node/Express chunk-reassembly server sample with tests.*

# Browser & Web APIs – Performance API (Navigation Timing & Resource Timing)

## 1. Overview
The Performance API provides high‑resolution, browser‑native performance metrics.  
Two key subsets:
- **Navigation Timing API** – Measures the document navigation + full load lifecycle.
- **Resource Timing API** – Measures performance of resources such as images, CSS, JS, fetch/XHR, fonts, etc.

## 2. Navigation Timing API
The modern interface is `PerformanceNavigationTiming`, retrievable via:
```js
performance.getEntriesByType("navigation")
```

### Key timestamps  
- `startTime` – Always `0`  
- `fetchStart`, `domainLookupStart/End`, `connectStart/End`  
- `secureConnectionStart`  
- `requestStart`, `responseStart`, `responseEnd`  
- `domInteractive`, `domContentLoadedEventStart/End`  
- `domComplete`, `loadEventStart`, `loadEventEnd`  
- `type`, `redirectCount`

## 3. Resource Timing API
Retrieve via:
```js
performance.getEntriesByType("resource")
```

### Key properties
- `startTime`, `responseEnd`  
- `domainLookupStart/End`, `connectStart/End`, `requestStart`, `responseStart`  
- `transferSize`, `encodedBodySize`, `decodedBodySize`  
- `initiatorType`  
Cross‑origin requires:
```
Timing-Allow-Origin: *
```

## 4. Code Snippets

### Page Load
```js
const [nav] = performance.getEntriesByType("navigation");
console.log("Page Load:", nav.loadEventEnd - nav.startTime);
```

### Resource Durations
```js
performance.getEntriesByType("resource").forEach(r => {
  console.log(r.name, r.responseEnd - r.startTime);
});
```

### Resource Breakdown
```js
const dns = r.domainLookupEnd - r.domainLookupStart;
const tcp = r.connectEnd - r.connectStart;
const req = r.responseStart - r.requestStart;
const download = r.responseEnd - r.responseStart;
```

### Observer
```js
new PerformanceObserver(list => {
  list.getEntries().forEach(e => console.log("New:", e.name));
}).observe({ entryTypes: ["resource"] });
```

## 5. Interview Questions

**What is Navigation Timing?**  
Measures full navigation lifecycle.

**What is Resource Timing?**  
Measures each resource’s network timings.

**How to get page load time?**  
`navigation[0].loadEventEnd`.

**Why might values be zero?**  
Missing `Timing-Allow-Origin` header.

**Difference from `performance.now()`?**  
`performance.now()` measures manual durations; timing APIs measure network lifecycle.

## 6. Practice Tasks
- Log slowest 5 resources  
- Calculate TTFB  
- Send navigation metrics to backend  
- Detect cross‑origin missing timing data  
- Make performance dashboard with `PerformanceObserver`

# Topic : Browser & Web APIs
## Sub Topic : RequestAnimationFrame (smooth animations, repaint sync)

---

## Overview
`requestAnimationFrame` (rAF) is a browser API that tells the user agent you wish to perform an animation and requests that the browser call a specified callback **before the next repaint**. It synchronizes JavaScript animation updates with the browser's refresh rate for smoother, more efficient animations.

---

## Syntax
```js
// schedule a single callback
const id = window.requestAnimationFrame(callback);

// cancel a scheduled callback
window.cancelAnimationFrame(id);

// typical loop
function loop(timestamp) {
  // update animation state
  window.requestAnimationFrame(loop);
}
window.requestAnimationFrame(loop);
```

`callback` receives a `DOMHighResTimeStamp` (often named `timestamp`) indicating the current time in milliseconds with sub-millisecond precision.

---

## Why use requestAnimationFrame (key points)
- Runs callbacks **right before a repaint**, producing smoother visual updates compared to `setInterval`/`setTimeout`.  
- Automatically throttles in background tabs (pauses), saving CPU and battery.  
- Typically integrates with the display refresh (commonly 60fps), so your updates align with painting and reduce visual tearing.

---

## Best practices
1. **Do minimal work inside the rAF callback.** Compute heavy logic outside or split work across frames.  
2. **Use transforms & opacity** for DOM animations (GPU-accelerated) rather than animating layout properties like `top/left`.  
3. **Throttle to a lower FPS** if you don't need 60fps (measure elapsed time between frames).  
4. **Cancel when invisible/unmounted** (e.g., component unmount) to avoid leaks.  
5. **Profile and budget ~16.67ms per frame at 60Hz** — keep total work per frame below this.

---

## Examples

### Basic canvas animation
```js
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');
let x = 0;

function draw(timestamp) {
  ctx.clearRect(0,0,canvas.width,canvas.height);
  x = (x + 2) % canvas.width;
  ctx.fillStyle = 'tomato';
  ctx.fillRect(x, 50, 50, 50);
  requestAnimationFrame(draw);
}

requestAnimationFrame(draw);
```

### Throttling to target FPS (e.g., 30 FPS)
```js
const targetFPS = 30;
const interval = 1000 / targetFPS;
let last = 0;

function loop(timestamp) {
  if (!last) last = timestamp;
  const delta = timestamp - last;
  if (delta >= interval) {
    // update and render here
    last = timestamp - (delta % interval);
  }
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

### Using rAF safely in React (hook)
```js
import { useEffect, useRef } from 'react';

export function useRaf(callback, running = true) {
  const cbRef = useRef(callback);
  const frameRef = useRef(null);

  useEffect(() => {
    cbRef.current = callback;
  }, [callback]);

  useEffect(() => {
    let mounted = true;
    function loop(ts) {
      if (!mounted) return;
      cbRef.current(ts);
      frameRef.current = requestAnimationFrame(loop);
    }
    if (running) frameRef.current = requestAnimationFrame(loop);
    return () => {
      mounted = false;
      if (frameRef.current != null) cancelAnimationFrame(frameRef.current);
    };
  }, [running]);
}
```

### Using in workers
Modern browsers expose `requestAnimationFrame` on `DedicatedWorkerGlobalScope` in some implementations for scheduling visuals-related work from workers. (If not available, fallback strategies are required.)

---

## Interview-style theory questions (concise answers)

1. **Q: What does `requestAnimationFrame` do?**  
   A: Schedules a callback to run before the browser's next repaint; callback receives a high-resolution timestamp.

2. **Q: Why is rAF preferred over `setInterval` for animations?**  
   A: rAF synchronizes with repaint, reduces tearing, and is throttled in background tabs, improving smoothness and efficiency.

3. **Q: How to limit animation to 30 FPS using rAF?**  
   A: Compare the `timestamp` passed to the callback against the last-render time and only render when the elapsed time ≥ 1000/30 ms.

4. **Q: When should you cancel rAF?**  
   A: Cancel when animation is paused, component unmounts, or the element is removed to prevent wasted cycles and memory leaks.

5. **Q: What should you avoid inside an rAF callback?**  
   A: Heavy synchronous work and layout-triggering DOM reads/writes (e.g., reading offsetHeight and then writing style), which cause layout thrash.

---

## Related coding questions (with short solutions)

1. **Implement a smooth sprite animation loop (canvas)** — see *Basic canvas animation* example above.

2. **Detect and pause animation when tab is hidden**  
   rAF already throttles in background; for additional control use the Page Visibility API (`document.visibilityState`) to pause logic when `hidden`.

3. **Measure frame time and log dropped frames**  
```js
let last = performance.now();
function loop(ts) {
  const dt = ts - last;
  const expected = 1000/60;
  if (dt > expected * 1.5) console.warn('dropped frame', Math.round(dt/expected));
  last = ts;
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

4. **Fallback for environments without requestAnimationFrame**
```js
const raf = window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame ||
            function(cb) { return setTimeout(() => cb(performance.now()), 1000/60); };

const caf = window.cancelAnimationFrame ||
            window.webkitCancelAnimationFrame ||
            window.mozCancelAnimationFrame ||
            function(id) { clearTimeout(id); };
```

---

## Debugging & Performance tips
- Use browser devtools FPS meter and performance profiling to find long frames.  
- Avoid forced synchronous layouts; batch reads and writes (read all then write all).  
- Consider `will-change: transform` only on elements you plan to animate, and unset it after animation to avoid rendering cost.

---

## References
- MDN: `window.requestAnimationFrame()`  
- MDN Performance guide (CSS & JS animations)  
- Can I Use: `requestAnimationFrame` browser support  
- Examples and community articles (StackOverflow, CSS-Tricks)

---

*Cheat-sheet created for interview preparation and quick reference.*

# WebSockets & Server-Sent Events (SSE) — Real‑Time Browser APIs (JavaScript)

## Topic: Browser & Web APIs  
## Sub Topic: WebSocket & SSE  
Realtime connections, difference from HTTP polling

---

## 1. Detailed Explanation

### Why Real‑Time?
Traditional HTTP is strictly request→response. The server can’t speak unless the client asks first. Real‑time needs the opposite: persistent, event‑driven communication.

Browsers offer three major approaches:

1. **HTTP Polling** – Client keeps asking “Anything new?”  
2. **Server‑Sent Events (SSE)** – Server pushes events to the client (one‑way).  
3. **WebSockets** – Full duplex (two‑way) persistent connection.

---

## 2. HTTP Polling (Baseline Reference)

### How it works
The client sends repeated requests at intervals:
```js
setInterval(async () => {
  const res = await fetch("/updates");
  const data = await res.json();
  console.log(data);
}, 2000);
```

### Limitations
- Wastes bandwidth.  
- Slow updates (interval‑based).  
- Not truly real‑time.

---

## 3. Server‑Sent Events (SSE)

### What is SSE?
A **unidirectional**, server→client streaming mechanism built over HTTP.  
Client subscribes to a stream; server pushes events.

### Benefits
- Lightweight and simple.  
- Auto‑reconnect built‑in.  
- Ideal for notifications, dashboards, logs.

### Limitations
- Only server→client.  
- Not binary‑friendly (text only).  
- Not suitable for high‑frequency interactions.

### Example: SSE Client
```js
const events = new EventSource("/stream");

events.onmessage = (event) => {
  console.log("Message:", event.data);
};

events.onerror = () => {
  console.log("SSE error");
};
```

### Example: SSE Server (Node.js Express)
```js
app.get("/stream", (req, res) => {
  res.set({
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive"
  });

  setInterval(() => {
    res.write(`data: ${JSON.stringify({ time: Date.now() })}

`);
  }, 2000);
});
```

---

## 4. WebSockets

### What is WebSocket?
A **full‑duplex** communication channel over a single TCP connection.  
Both client and server can send data anytime.

### Benefits
- Bi‑directional.  
- Low latency.  
- Supports text and binary.  
- Perfect for chat, gaming, collaborative apps.

### Limitations
- More complex to scale.  
- Load balancer & proxy issues (sticky sessions).  
- Not ideal for simple event streams.

### WebSocket Client
```js
const socket = new WebSocket("ws://localhost:8080");

socket.onopen = () => {
  console.log("Connected");
  socket.send("Hello server");
};

socket.onmessage = (msg) => {
  console.log("Received:", msg.data);
};
```

### WebSocket Server (Node.js: ws library)
```js
import { WebSocketServer } from "ws";

const wss = new WebSocketServer({ port: 8080 });

wss.on("connection", (ws) => {
  ws.send("Welcome!");

  ws.on("message", (msg) => {
    console.log("Client:", msg.toString());
    ws.send("Echo: " + msg);
  });
});
```

---

## 5. WebSocket vs SSE vs Polling — Quick Comparison

| Feature | WebSocket | SSE | Polling |
|--------|-----------|-----|---------|
| Direction | Two‑way | Server → Client | Client → Server |
| Realtime | Yes | Yes | Limited |
| Binary Support | Yes | No | Yes |
| Auto Reconnect | No (manual) | Yes | No |
| Complexity | Medium | Low | Low |
| Ideal For | Chats, games | Notifications, dashboards | Simple updates |

---

## 6. Theory-based Interview Questions (With Concise Answers)

**1. Why do we need WebSockets?**  
To support full‑duplex real‑time communication where both client and server push data without waiting for requests.

**2. How is SSE different from WebSockets?**  
SSE is one‑way (server→client) and simpler; WebSockets are two‑way.

**3. When to choose SSE over WebSockets?**  
When only server→client events are needed, such as stock tickers or alerts.

**4. Does SSE support binary data?**  
No. SSE only supports UTF‑8 text.

**5. Do WebSockets use HTTP?**  
WebSockets start with an HTTP handshake, then upgrade to a WebSocket protocol.

**6. What happens if a WebSocket connection breaks?**  
Reconnect must be implemented manually.

**7. Are SSE connections scalable?**  
They are lightweight, but long‑lived HTTP connections require proper server tuning.

---

## 7. Coding Interview Tasks

### 1. Implement a SSE notification system
- API endpoint emitting stream  
- Client listening with EventSource  

### 2. Build a WebSocket chat server  
- Broadcast messages to all clients  
- Handle join/leave events

### 3. Convert HTTP polling to WebSockets  
- Replace periodic fetch with persistent socket  
- Improve latency and bandwidth usage

---

## 8. Summary
WebSockets are the heavy machinery for fully interactive real‑time apps. SSE is the elegant fountain pen for server‑only updates. Polling is the slow, polite tap on the shoulder. Understanding when to use each is the real superpower.

