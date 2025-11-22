
# Deep Copy vs Shallow Copy — JavaScript Interview Cheat Sheet

**Topic:** Deep Copy vs Shallow Copy  
**Sub Topic:** `Object.assign`, Spread (`...`), Recursion, `structuredClone`, `JSON.parse(JSON.stringify())`, `_.cloneDeep`

---

## 1) Key concepts — short and precise

- **Shallow copy**: copies only top-level properties. Nested objects/arrays remain *shared references* between source and copy. Common shallow-copy mechanisms: `Object.assign()`, spread syntax `{ ...obj }`, `Array.prototype.slice`, `Array.from()`.  
- **Deep copy (deep clone)**: recursively duplicates all nested objects/arrays so the copy is fully independent from the original.

---

## 2) Native JavaScript behaviors & examples

### Shallow copy examples
```js
const original = { a: 1, b: { c: 2 } };

const assigned = Object.assign({}, original);
const spread = { ...original };

assigned.b.c = 99;
console.log(original.b.c); // 99  (because `b` is still the same object)
```

`Object.assign()` and spread copy *property values*; if a property value is a reference (object/array), the reference is copied — not the underlying object. citeturn0search4turn0search16

### Deep copy (modern native)
```js
const original = { a: 1, b: { c: 2 } };
const clone = structuredClone(original);

clone.b.c = 99;
console.log(original.b.c); // 2
```
`structuredClone()` implements the structured clone algorithm and performs a deep copy of many value types (and handles cycles). It's the recommended native API for deep copying in modern runtimes. citeturn0search1turn0search5

### JSON approach — quick but limited
```js
const clone = JSON.parse(JSON.stringify(original));
```
This works for simple data (plain objects/arrays of JSON-compatible types) but **loses** functions, `undefined`, `Symbol`, `Date` becomes string, `RegExp` becomes `{}`, and fails for circular references. Use only when you know data is JSON-safe. citeturn0search3turn0search7

---

## 3) When to use each approach (practical guidance)

- **Performance-sensitive, shallow-only needs**: use spread or `Object.assign()` (fast, low memory).  
- **Trusted simple JSON data**: `JSON.parse(JSON.stringify())` for quick one-off copies (beware the type losses).  
- **Robust, general-purpose deep copy**: `structuredClone()` if available in your environment (Node >=17 / modern browsers). Check compatibility for your target platforms. citeturn0search1turn0search12  
- **Cross-environment or advanced needs**: `_.cloneDeep()` (Lodash) or a tested recursive clone utility — good when you need predictable cross-platform support or custom cloning rules.

---

## 4) Interview-style theory questions (concise answers)

**Q1 — What is the difference between shallow and deep copy?**  
A: Shallow copies duplicate top-level properties only; nested objects remain shared. Deep copies recursively duplicate all nested values so source and copy are independent.

**Q2 — Does `Object.assign()` perform a deep copy?**  
A: No. It performs a shallow copy of enumerable own properties; nested references remain shared. citeturn0search4

**Q3 — Is `JSON.parse(JSON.stringify(obj))` a full deep clone?**  
A: Not fully. It only preserves JSON-compatible types, loses functions/`undefined`/`Symbol`, converts `Date` to ISO strings, and fails on circular references. Use only for JSON-safe objects. citeturn0search3turn0search7

**Q4 — What is `structuredClone()` and when should I use it?**  
A: `structuredClone()` is a Web API that performs deep cloning using the structured clone algorithm. Use it for a robust native deep clone (it supports many built-in types and cycles). Verify runtime support for your target environment. citeturn0search1turn0search5

**Q5 — How do you deep-clone objects with circular references?**  
A: Use `structuredClone()` or an implementation that keeps a `WeakMap`/Map to track visited nodes during recursion (to avoid infinite loops).

---

## 5) Practical coding interview tasks (with hints / short solutions)

### Task 1 — Implement a safe deepClone that handles cycles (ES6)
**Hint**: Use recursion and a `Map` to remember visited references.

```js
function deepClone(value, map = new Map()) {
  if (value === null || typeof value !== 'object') return value;
  if (map.has(value)) return map.get(value);

  let cloned;
  if (Array.isArray(value)) {
    cloned = [];
    map.set(value, cloned);
    for (let i = 0; i < value.length; i++) cloned[i] = deepClone(value[i], map);
    return cloned;
  }

  // For plain objects
  cloned = {};
  map.set(value, cloned);
  for (const key of Object.keys(value)) {
    cloned[key] = deepClone(value[key], map);
  }
  return cloned;
}
```

This handles arrays, plain objects and circular references. For production use, consider edge cases and types (Date, RegExp, Map, Set, classes).

### Task 2 — Convert nested object mutation bug into immutable update
Given `state = { user: { name: 'A' } }`, produce a new state with `user.name = 'B'` without mutating original.

```js
const newState = {
  ...state,
  user: {
    ...state.user,
    name: 'B'
  }
};
```

### Task 3 — Detect whether a copy is deep or shallow
**Approach**: Change nested property on copy and check original.

```js
function isShallowCopy(original, copy) {
  for (const k of Object.keys(original)) {
    if (
      original[k] && typeof original[k] === 'object' &&
      original[k] === copy[k]
    ) return true; // top-level nested reference still shared => shallow
  }
  return false;
}
```

---

## 6) Short cheat-sheet table

| Use case | Fast | Preserves functions | Supports cycles | Recommended |
|---|---:|:---:|:---:|---|
| `Object.assign` / spread | ✅ | ❌ | ❌ | Top-level shallow copies |
| `JSON.parse(JSON.stringify)` | ✅ | ❌ | ❌ | Quick JSON-safe deep copy |
| `structuredClone()` | ✅ | ✅ (some types) | ✅ | Modern, preferred native deep clone |
| `_.cloneDeep()` | ⚠️ (slower) | ✅ (depends) | ✅ | Cross-platform, well-tested |

(References: MDN structuredClone, Object.assign, structured clone algorithm, compatibility tables.) citeturn0search1turn0search4turn0search5turn0search12

---

## 7) Further reading / references
- MDN — structuredClone() and Structured clone algorithm. citeturn0search1turn0search5  
- MDN — Object.assign() docs. citeturn0search4  
- CanIUse — structuredClone support. citeturn0search12

---

## 8) Save & reuse
This document is formatted for interview prep. Copy, paste, or print the sections labeled **Theory** and **Practical coding tasks** into your revision notes.

---


# Event Loop Tracing — async/await, Promises, setTimeout (JavaScript)

## Topic
Event Loop Tracing

## Sub Topic
async/await + promises + setTimeout sequence

---

## 1) Core explanation (concise)
JavaScript runs code on a single thread using an **event loop**. Asynchronous callbacks are scheduled into queues:
- **Microtask queue** (also called "jobs"): includes `Promise` callbacks (`.then`, `catch`, `finally`) and the resumptions created by `await`.
- **Macrotask queue** (also called "task" or "callback queue"): includes `setTimeout`, `setInterval`, I/O callbacks, UI events.

When the synchronous code (call stack) finishes, the runtime runs **all** microtasks (in FIFO order) before dequeuing the next macrotask. This ordering makes microtasks higher priority than macrotasks.

---

## 2) Practical trace example

```js
console.log('1');

setTimeout(() => console.log('2'), 0);

Promise.resolve().then(() => console.log('3'));

(async () => {
  console.log('4');
  await null;         // causes the rest of the async function to run as a microtask
  console.log('5');
})();

console.log('6');
```

**Predicted output:**  
```
1
4
6
3
5
2
```

**Why:** `1,4,6` are synchronous. `Promise.then` and the `await` continuation are microtasks → run next (3 then 5). Finally the macrotask from `setTimeout` runs (2).

---

## 3) Key rules to remember
1. `Promise` callbacks and `await` continuations are **microtasks**. They run after the current synchronous code but before timers and rendering. (See: MDN, javascript.info). citeturn0search17turn0search8  
2. `setTimeout(..., 0)` schedules a **macrotask** (timer). It will run after microtasks and after the event loop moves to the next macrotask. citeturn0search1turn0search4  
3. `async` functions pause at `await` and resume later — the resume is scheduled as a microtask. This means `await` is effectively sugar over `Promise` behavior. citeturn0search8turn0search14

---

## 4) Interview-style theory questions (short + crisp answers)

**Q1 — What's the difference between microtask and macrotask?**  
A: Microtasks (jobs) run immediately after the current call stack clears and before the next macrotask; macrotasks are scheduled tasks (timers, I/O) processed from the task queue. Microtasks have higher priority. citeturn0search8turn0search10

**Q2 — Does `await` yield to `setTimeout(..., 0)`?**  
A: Yes. `await` resumes in a microtask; microtasks run before macrotasks like `setTimeout(..., 0)`.

**Q3 — If a promise resolves during a macrotask, when will its `.then` run?**  
A: Its `.then` callback is queued as a microtask and will run at the microtask checkpoint after the current macrotask finishes (before the next macrotask). citeturn0search3

**Q4 — How can a long-running synchronous loop affect microtasks/timers?**  
A: It blocks the event loop — no microtasks or macrotasks run while the loop runs. Timers that expire during the blocking will only run after the loop ends and microtasks are drained. citeturn0search11

**Q5 — Which runs first: `Promise.resolve().then(...)` or multiple `setTimeout(..., 0)`?**  
A: The promise `.then` (microtask) will run before any of the `setTimeout` callbacks (macrotasks).

---

## 5) Short debugging checklist (how to trace issues)
- Convert suspicious `await` into explicit `Promise` chains to see microtask placements.  
- Replace `setTimeout(..., 0)` with `setTimeout(..., 0)` or `queueMicrotask(...)` to test priority differences.  
- Insert `console.log` markers before/after awaits and then check ordering.  
- Use DevTools' async stack traces and Performance profiling to spot long sync blocks. citeturn0search14

---

## 6) Coding-based interview problems (with answers)

### Problem 1 — Predict the output
Predict output for the example in section 2.  
**Answer:** `1 4 6 3 5 2` (explained above).

### Problem 2 — Fix the ordering
You want `5` to print before `3` in the example. Minimal change?  
**Solution:** Make the `await` continuation run earlier by resolving a promise synchronously before `.then` is queued — e.g. move `Promise.resolve().then` after the async's await by forcing ordering is tricky; simpler: use `queueMicrotask` to schedule intentionally:
```js
(async () => {
  console.log('4');
  await null;        // continuation is a microtask
  console.log('5');
})();

Promise.resolve().then(() => console.log('3'));
// To force 5 before 3 you'd have to schedule 3 differently — e.g. setTimeout(..., 0) for 3
```
**Note:** Microtasks are FIFO; to reorder you'd switch callback types (microtask → macrotask) or re-sequence registration.

### Problem 3 — Implement `sleep(ms)` that `await` can use
```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// usage:
(async () => {
  console.log('A');
  await sleep(0);
  console.log('B'); // runs in later macrotask
})();
```

### Problem 4 — Explain why this logs "A C B" and not "A B C"
```js
console.log('A');

setTimeout(() => console.log('B'), 0);

Promise.resolve().then(() => console.log('C'));
```
**Answer:** Sync `A`, then microtask `C`, then macrotask `B` → `A C B`. (Promises before timers). citeturn0search8

### Problem 5 — Implement a `nextTick` polyfill using microtasks
```js
function nextTick(cb) {
  if (typeof queueMicrotask === 'function') {
    queueMicrotask(cb);
  } else {
    Promise.resolve().then(cb);
  }
}
```

---

## 7) Tips for interviews (how to talk about it)
- Start by describing the call stack, web APIs, and event loop.  
- Distinguish microtask vs macrotask with concrete examples (`Promise.then` vs `setTimeout`).  
- Walk through a short trace (3–6 lines) and explain ordering step-by-step.  
- Mention real-world implications: UI updates, preventing jank, ordering race conditions.

---

## Appendix — Further reading
- MDN: JavaScript execution model.  
- javascript.info: Event loop, microtasks and macrotasks.  
(These are excellent for deeper reading and interview prep.)

---

# End of cheat-sheet


# Event Loop Tracing — async/await, Promises, setTimeout (JavaScript)

## Topic
Event Loop Tracing

## Sub Topic
async/await + promises + setTimeout sequence

---

## 1) Core explanation (concise)
JavaScript runs code on a single thread using an **event loop**. Asynchronous callbacks are scheduled into queues:
- **Microtask queue** (also called "jobs"): includes `Promise` callbacks (`.then`, `catch`, `finally`) and the resumptions created by `await`.
- **Macrotask queue** (also called "task" or "callback queue"): includes `setTimeout`, `setInterval`, I/O callbacks, UI events.

When the synchronous code (call stack) finishes, the runtime runs **all** microtasks (in FIFO order) before dequeuing the next macrotask. This ordering makes microtasks higher priority than macrotasks.

---

## 2) Practical trace example

```js
console.log('1');

setTimeout(() => console.log('2'), 0);

Promise.resolve().then(() => console.log('3'));

(async () => {
  console.log('4');
  await null;         // causes the rest of the async function to run as a microtask
  console.log('5');
})();

console.log('6');
```

**Predicted output:**  
```
1
4
6
3
5
2
```

**Why:** `1,4,6` are synchronous. `Promise.then` and the `await` continuation are microtasks → run next (3 then 5). Finally the macrotask from `setTimeout` runs (2).

---

## 3) Key rules to remember
1. `Promise` callbacks and `await` continuations are **microtasks**. They run after the current synchronous code but before timers and rendering. (See: MDN, javascript.info). citeturn0search17turn0search8  
2. `setTimeout(..., 0)` schedules a **macrotask** (timer). It will run after microtasks and after the event loop moves to the next macrotask. citeturn0search1turn0search4  
3. `async` functions pause at `await` and resume later — the resume is scheduled as a microtask. This means `await` is effectively sugar over `Promise` behavior. citeturn0search8turn0search14

---

## 4) Interview-style theory questions (short + crisp answers)

**Q1 — What's the difference between microtask and macrotask?**  
A: Microtasks (jobs) run immediately after the current call stack clears and before the next macrotask; macrotasks are scheduled tasks (timers, I/O) processed from the task queue. Microtasks have higher priority. citeturn0search8turn0search10

**Q2 — Does `await` yield to `setTimeout(..., 0)`?**  
A: Yes. `await` resumes in a microtask; microtasks run before macrotasks like `setTimeout(..., 0)`.

**Q3 — If a promise resolves during a macrotask, when will its `.then` run?**  
A: Its `.then` callback is queued as a microtask and will run at the microtask checkpoint after the current macrotask finishes (before the next macrotask). citeturn0search3

**Q4 — How can a long-running synchronous loop affect microtasks/timers?**  
A: It blocks the event loop — no microtasks or macrotasks run while the loop runs. Timers that expire during the blocking will only run after the loop ends and microtasks are drained. citeturn0search11

**Q5 — Which runs first: `Promise.resolve().then(...)` or multiple `setTimeout(..., 0)`?**  
A: The promise `.then` (microtask) will run before any of the `setTimeout` callbacks (macrotasks).

---

## 5) Short debugging checklist (how to trace issues)
- Convert suspicious `await` into explicit `Promise` chains to see microtask placements.  
- Replace `setTimeout(..., 0)` with `setTimeout(..., 0)` or `queueMicrotask(...)` to test priority differences.  
- Insert `console.log` markers before/after awaits and then check ordering.  
- Use DevTools' async stack traces and Performance profiling to spot long sync blocks. citeturn0search14

---

## 6) Coding-based interview problems (with answers)

### Problem 1 — Predict the output
Predict output for the example in section 2.  
**Answer:** `1 4 6 3 5 2` (explained above).

### Problem 2 — Fix the ordering
You want `5` to print before `3` in the example. Minimal change?  
**Solution:** Make the `await` continuation run earlier by resolving a promise synchronously before `.then` is queued — e.g. move `Promise.resolve().then` after the async's await by forcing ordering is tricky; simpler: use `queueMicrotask` to schedule intentionally:
```js
(async () => {
  console.log('4');
  await null;        // continuation is a microtask
  console.log('5');
})();

Promise.resolve().then(() => console.log('3'));
// To force 5 before 3 you'd have to schedule 3 differently — e.g. setTimeout(..., 0) for 3
```
**Note:** Microtasks are FIFO; to reorder you'd switch callback types (microtask → macrotask) or re-sequence registration.

### Problem 3 — Implement `sleep(ms)` that `await` can use
```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// usage:
(async () => {
  console.log('A');
  await sleep(0);
  console.log('B'); // runs in later macrotask
})();
```

### Problem 4 — Explain why this logs "A C B" and not "A B C"
```js
console.log('A');

setTimeout(() => console.log('B'), 0);

Promise.resolve().then(() => console.log('C'));
```
**Answer:** Sync `A`, then microtask `C`, then macrotask `B` → `A C B`. (Promises before timers). citeturn0search8

### Problem 5 — Implement a `nextTick` polyfill using microtasks
```js
function nextTick(cb) {
  if (typeof queueMicrotask === 'function') {
    queueMicrotask(cb);
  } else {
    Promise.resolve().then(cb);
  }
}
```

---

## 7) Tips for interviews (how to talk about it)
- Start by describing the call stack, web APIs, and event loop.  
- Distinguish microtask vs macrotask with concrete examples (`Promise.then` vs `setTimeout`).  
- Walk through a short trace (3–6 lines) and explain ordering step-by-step.  
- Mention real-world implications: UI updates, preventing jank, ordering race conditions.

---

## Appendix — Further reading
- MDN: JavaScript execution model.  
- javascript.info: Event loop, microtasks and macrotasks.  
(These are excellent for deeper reading and interview prep.)

---

# End of cheat-sheet


# Topic : Memoization, Data Privacy, Function Factories

## Sub Topic : Practical Use, Interview Prep, JavaScript

---

## 1) Overview — what we'll cover

This cheat-sheet explains **memoization**, **data privacy (in JS)**, and **function factories** with practical examples, interview-style theory Q&A, and coding problems you can practice. Each section contains: a concise conceptual summary, common pitfalls, performance / security notes, and code examples you can paste into Node or the browser console.

---

# Memoization

## Concept
Memoization is a caching optimization: store a function's computed outputs keyed by its inputs so repeated calls with the same inputs return the cached result instead of recomputing. Best for expensive pure functions (no side effects, deterministic results).

## When to use
- CPU-heavy computations (e.g., recursive Fibonacci, combinatorics).
- Pure functions where inputs are small/serializable.
- Avoid when inputs are large objects that are expensive to stringify or when memory is limited.

## Implementation patterns
### Simple single-argument memoize (using Map)
```js
function memoize(fn) {
  const cache = new Map();
  return function(arg) {
    if (cache.has(arg)) return cache.get(arg);
    const res = fn.call(this, arg);
    cache.set(arg, res);
    return res;
  };
}

const slowSquare = n => { /* pretend heavy work */ for (let i=0;i<1e7;i++); return n*n; };
const fast = memoize(slowSquare);
```

### Variadic-safe memoize (serialize args)
```js
function memoizeArgs(fn, serializer = JSON.stringify) {
  const cache = new Map();
  return function(...args) {
    const key = serializer(args);
    if (cache.has(key)) return cache.get(key);
    const res = fn.apply(this, args);
    cache.set(key, res);
    return res;
  };
}
```

### LRU cache variant (bounded cache)
- Use when caching unbounded results would leak memory.
- Implement with a `Map` and maintain insertion order or use an LRU library.

## Pitfalls & performance notes
- **Serialization cost:** JSON.stringify can be expensive and loses function/non-JSON types; prefer specialized keying for primitive-heavy arguments.
- **Memory leaks:** caches hold references — use weak references (WeakMap) only when keys are objects and you don't want to prevent GC.
- **Non-deterministic functions:** do not memoize functions that depend on external state, time, or randomness.
- **Equality semantics:** decide conceptually what counts as "same input" (deep equality vs. reference equality).

---

# Data Privacy in JavaScript

## Concept
Data privacy refers to limiting access to sensitive data (user tokens, credentials, secrets) in code so only intended code paths can read or modify them. In JS this is mainly about *encapsulation* and *least privilege*.

## Patterns & mechanisms
- **Module scope / closure-based privacy:** variables declared inside a factory/module function are not exported — closures expose only allowed APIs.
- **ES private fields:** `class X { #secret; }` gives syntax-level private fields (not accessible from outside).
- **Symbols and WeakMaps:** use `WeakMap`-backed private state keyed by instance for truly hidden per-instance state.
- **Server vs client:** never store secrets in client-side storage (localStorage/sessionStorage). Use cookies with `HttpOnly` for session tokens or keep secrets server-side.

## Best practices
- **Minimize surface area:** expose only functions needed for external code; prefer read-only getters where possible.
- **Avoid storing sensitive tokens in browser storage** — prefer secure, short-lived HTTP-only cookies or handle auth on the server.
- **Input validation & output redaction**: sanitize inputs and redact sensitive fields in logs.
- **Use HTTPS/TLS** always to protect data in transit.
- **Follow OWASP and secure-coding checklists** for production systems.

## Examples
### Closure-based private state (module/factory)
```js
function makeCounter(initial = 0) {
  let count = initial; // private
  return {
    increment() { count++; return count; },
    get() { return count; }
  };
}

const c = makeCounter(2);
// c.count is undefined; can only interact through methods
```

### ES private fields
```js
class SecretHolder {
  #secret;
  constructor(secret) { this.#secret = secret; }
  revealIfAllowed(key) { /* policy check */ return this.#secret; }
}
```

---

# Function Factories

## Concept
A function factory is a function that returns other functions. It uses closures to 'bake in' parameters or state and produce specialized functions — a lightweight alternative to classes for many use-cases.

## Use-cases
- Creating configured handlers (e.g., `createLogger(level)` returns a logger function bound to that level).
- Partial application / currying.
- Building private-instance behavior without classes.

## Example: multiplier factory
```js
function multiplier(factor) {
  return function(x) { return x * factor; };
}
const double = multiplier(2);
console.log(double(5)); // 10
```

## Combining with memoization
Factories can produce memoized functions with private caches:
```js
function makeFibMemo() {
  const cache = new Map();
  function fib(n) {
    if (n < 2) return n;
    if (cache.has(n)) return cache.get(n);
    const v = fib(n-1)+fib(n-2);
    cache.set(n, v);
    return v;
  }
  return fib;
}
const fib = makeFibMemo();
```

---

# Interview-style Theory Questions (concise answers)

1. **What is memoization and when is it appropriate?**
- Memoization caches function outputs to avoid recomputation. Appropriate for pure, CPU-heavy functions with repeated calls.

2. **Why might JSON.stringify be a bad choice for cache keys?**
- It can be slow, order-dependent for object keys, and fails on non-JSON types (functions, symbols, cyclic refs).

3. **How do closures enable data privacy?**
- Closures capture lexical variables that are not accessible from outside the function, so you can expose only controlled APIs.

4. **When would you prefer an ES private field over closure-based privacy?**
- Use ES private fields for class-based APIs when you want per-instance private state with clearer syntax; use closures for module-level or factory-based privacy.

5. **How can memoization lead to memory leaks? How to mitigate?**
- Unbounded caches keep references and prevent garbage collection. Mitigate with bounded caches (LRU), WeakMaps (for object keys), or explicit cache invalidation.

6. **Explain function factory vs class constructor — pros/cons.**
- Factories are simple, encourage composition, and avoid `this` complexity; classes provide clearer prototypes, inheritance, and shared methods on `prototype` (memory-efficient for many instances).

---

# Coding Interview Questions (practice)

1. **Implement a memoize(fn) that supports multiple arguments and preserves `this`.**
- Expectation: use `Map`, serialize args carefully, handle `this` with `fn.apply`.

2. **Write an LRU cache class with `get` and `put` methods.**
- Expectation: O(1) operations using a doubly-linked list + Map, or using `Map` insertion order tricks.

3. **Create a function factory `createRateLimiter(limit, windowMs)` that returns a function which returns `true` if a call is allowed.**
- Expectation: use closure to keep timestamps and sliding window logic.

4. **Given a class with private data, convert it to a closure-based factory and explain trade-offs.**
- Expectation: show both implementations, discuss introspection/testing and performance trade-offs.

---

# Sample Solutions (concise)

### 1) memoize supporting `this` and multiple args
```js
function memoize(fn, serializer = JSON.stringify) {
  const cache = new Map();
  return function(...args) {
    const key = serializer(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  }
}
```

### 2) Simple LRU using Map (limited-size cache)
```js
class LRUCache {
  constructor(limit = 100) { this.limit = limit; this.map = new Map(); }
  get(key) {
    if (!this.map.has(key)) return undefined;
    const val = this.map.get(key);
    this.map.delete(key);
    this.map.set(key, val);
    return val;
  }
  put(key, val) {
    if (this.map.has(key)) this.map.delete(key);
    this.map.set(key, val);
    if (this.map.size > this.limit) {
      const firstKey = this.map.keys().next().value;
      this.map.delete(firstKey);
    }
  }
}
```

---

# Quick checklist for production-readiness
- Avoid storing secrets client-side; use HttpOnly cookies or server storage.
- Limit cache size; use LRU or TTL invalidation.
- Use WeakMap for object-keyed private data to avoid preventing GC.
- Avoid memoizing functions with side-effects.
- Add telemetry: hit/miss counters for caches to validate benefit.

---

# How to use this file
- Paste examples into Node REPL or browser console.
- For interviews: explain trade-offs, mention complexity (time/space), and state assumptions.

---

**End of cheat-sheet.**

# Call, Apply, Bind — Implementation & Interview Prep (JavaScript)

## Topic: Call, Apply, Bind  
## Sub Topic: Hand‑Written Polyfills (Implementation)

---

## 1. Detailed Explanation

In JavaScript, `call`, `apply`, and `bind` are methods available on every function via `Function.prototype`. They allow you to manually set the value of `this` when invoking a function.

### `call`
Invokes a function immediately with a specified `this` context and individual arguments.

```js
func.call(context, arg1, arg2);
```

### `apply`
Invokes a function immediately with a specified `this` but takes **arguments as an array**.

```js
func.apply(context, [arg1, arg2]);
```

### `bind`
Returns a **new function** with `this` permanently set to the provided context.  
It does **not** call the function immediately.

```js
const newFn = func.bind(context, arg1);
newFn(arg2);
```

---

## 2. Polyfills (Hand-Written Implementations)

### Polyfill for `call`
```js
Function.prototype.myCall = function(context, ...args) {
  context = context || globalThis;
  const fn = Symbol("fn");
  context[fn] = this;
  const result = context[fn](...args);
  delete context[fn];
  return result;
};
```

### Polyfill for `apply`
```js
Function.prototype.myApply = function(context, args) {
  context = context || globalThis;
  const fn = Symbol("fn");
  context[fn] = this;
  const result = args ? context[fn](...args) : context[fn]();
  delete context[fn];
  return result;
};
```

### Polyfill for `bind`
```js
Function.prototype.myBind = function(context, ...args1) {
  const self = this;
  return function (...args2) {
    return self.apply(context, [...args1, ...args2]);
  };
};
```

---

## 3. Theory-Based Interview Questions and Answers

### 1. What is the difference between `call`, `apply`, and `bind`?
`call` and `apply` execute the function immediately; `bind` returns a new function. `call` takes arguments individually, `apply` takes them as an array.

### 2. Why do we use `call`/`apply`?
To manually control the value of `this`, especially in borrowing methods or function reusability.

### 3. What problem does `bind` solve?
Binding ensures that the method always uses the intended `this` context regardless of how it’s called (used in event handlers, callbacks).

### 4. Why does `bind` create a new function?
Because its semantics specify that binding is persistent and should not mutate the original function.

### 5. What happens if `this` is set to `null` or `undefined`?
Non‑strict mode defaults to `globalThis`. Strict mode leaves `this` as `null`/`undefined`.

### 6. Why do polyfills use a unique key like `Symbol()`?
To prevent clashing with existing properties on the object.

---

## 4. Coding Interview Questions (Application Level)

### Implement `myCall`
```js
Function.prototype.myCall = function(context, ...args) {
  context = context || globalThis;
  const fn = Symbol();
  context[fn] = this;
  const res = context[fn](...args);
  delete context[fn];
  return res;
};
```

### Implement `myApply`
```js
Function.prototype.myApply = function(context, args) {
  context = context || globalThis;
  const fn = Symbol();
  context[fn] = this;
  const res = Array.isArray(args) ? context[fn](...args) : context[fn]();
  delete context[fn];
  return res;
};
```

### Implement `myBind`
```js
Function.prototype.myBind = function(context, ...boundArgs) {
  const self = this;
  return function (...args) {
    return self.apply(context, [...boundArgs, ...args]);
  };
};
```

### Extra Challenge: Support constructor behavior in `bind`
```js
Function.prototype.myBind = function(context, ...boundArgs) {
  const self = this;

  function boundFunction(...args) {
    if (this instanceof boundFunction) {
      return new self(...boundArgs, ...args);
    }
    return self.apply(context, [...boundArgs, ...args]);
  }

  boundFunction.prototype = Object.create(self.prototype);
  return boundFunction;
};
```

---

Enjoy mastering this—it's a core JS superpower and an interview favorite!


# Topic : Promise.all Polyfill

## Sub Topic : implementation and concurrency handling

---

### 1. Quick summary

`Promise.all(iterable)` takes an iterable of promises (or values) and returns a new promise that:

- resolves to an array of resolved values **in the same order** as the input iterable, once *all* input promises have resolved; or
- rejects immediately with the first rejection reason if any input promise rejects.

Important behaviors to remember:
- Non-promise values are treated as `Promise.resolve(value)`.
- Order of results matches the iteration order, not the order of resolution.
- If the iterable is empty, `Promise.all([])` resolves to `[]`.

---

### 2. Minimal, correct polyfill (ECMAScript-compatible behavior)

```javascript
// Promise.all polyfill (ES6 behaviour)
if (typeof Promise !== 'undefined' && !Promise.all) {
  Promise.all = function(iterable) {
    return new Promise(function(resolve, reject) {
      if (iterable == null) {
        return reject(new TypeError('Promise.all accepts an iterable'));
      }

      var results = [];
      var remaining = 0;
      var index = 0;
      var called = false;

      // Convert iterable to an array of entries to preserve iteration order and allow multiple passes
      try {
        var items = Array.from(iterable);
      } catch (e) {
        return reject(e);
      }

      if (items.length === 0) return resolve([]);

      remaining = items.length;

      items.forEach(function(item, i) {
        // Ensure non-promise values become promises
        Promise.resolve(item)
          .then(function(value) {
            results[i] = value; // preserve order
            remaining -= 1;
            if (remaining === 0 && !called) {
              called = true;
              resolve(results);
            }
          })
          .catch(function(err) {
            if (!called) {
              called = true; // ensure only first rejection wins
              reject(err);
            }
          });
      });
    });
  };
}
```

Notes on correctness:
- Uses `Array.from(iterable)` to support any iterable and preserve iteration order.
- Wraps each item with `Promise.resolve` to normalize values and then attaches `then`/`catch`.
- Keeps `results` array keyed by original index so results order is stable.
- The `called` guard prevents multiple resolve/reject calls.

---

### 3. Concurrency handling: what `Promise.all` actually does

`Promise.all` does **not** limit concurrency. It starts the conversion of every input to a promise immediately (by calling `Promise.resolve(item)`), which means asynchronous operations embedded in those promises begin right away. It simply aggregates results but does not control how many tasks run in parallel.

If you need to restrict concurrency (e.g., when making many network requests), you must implement a *pool* or *throttling* layer that runs a limited number of promises at a time.

---

### 4. Concurrency-limited variant (promise pool)

This is **not** `Promise.all` polyfill; rather a utility to run N tasks in parallel and resolve when all complete (useful for large batches).

```javascript
// Run tasks with concurrency limit
function promisePool(tasks, concurrency) {
  return new Promise((resolve, reject) => {
    const results = new Array(tasks.length);
    let index = 0; // next task index
    let active = 0;
    let finished = 0;
    let errored = false;

    function runNext() {
      if (errored) return;
      if (finished === tasks.length) return resolve(results);
      while (active < concurrency && index < tasks.length) {
        const currentIndex = index++;
        active++;
        Promise.resolve()
          .then(() => tasks[currentIndex]()) // tasks are functions returning promises
          .then((value) => {
            results[currentIndex] = value;
            active--;
            finished++;
            runNext();
          })
          .catch((err) => {
            errored = true;
            reject(err); // fail-fast behavior (mirrors Promise.all semantics)
          });
      }
    }

    if (tasks.length === 0) return resolve([]);
    runNext();
  });
}

// Example usage:
// const tasks = urls.map(url => () => fetch(url).then(r => r.json()));
// promisePool(tasks, 5).then(results => ...).catch(err => ...);
```

Key points:
- `tasks` is an array of *functions* that return promises when invoked. This defers starting tasks until the pool runs them.
- The pool keeps `concurrency` tasks active and starts new ones as others finish.
- This implementation uses fail-fast semantics like `Promise.all` (first rejection rejects the pool promise).

---

### 5. Variants & related APIs

- `Promise.allSettled(iterable)` — waits for all to settle and returns an array of `{status, value/reason}`. Useful when you want results regardless of failures.
- `Promise.race(iterable)` — resolves/rejects as soon as any input resolves/rejects.
- `Promise.any(iterable)` — resolves with the first fulfilled promise, rejects only if all reject.

If building a pool you may want all-settled semantics (collecting both successes and failures) rather than fail-fast.

---

### 6. Edge cases & micro-behaviors interviewers like

- `Promise.all` is eager about starting conversions: `Promise.resolve(item)` is called immediately for each item.
- The order of *resolution* can differ from order of *iteration*; results are still returned in iteration order.
- Passing a non-iterable throws a `TypeError` (polyfill should mimic this behavior).
- Passing a single promise (not in an array) is not valid; it must be an iterable.

---

### 7. Tests / quick checks (unit-test friendly)

```javascript
// Basic
Promise.all([1, Promise.resolve(2), 3]).then(res => {
  // res -> [1, 2, 3]
});

// Rejection
Promise.all([Promise.resolve(1), Promise.reject(new Error('boom'))])
  .then(() => console.log('should not happen'))
  .catch(err => console.assert(err.message === 'boom'));

// Empty
Promise.all([]).then(res => console.assert(Array.isArray(res) && res.length === 0));
```

---

## Interview-style theory questions (concise answers)

1. **Q:** What does `Promise.all` do when one of the input promises rejects?  
   **A:** It rejects immediately with that reason; the returned promise rejects and further resolved values are ignored.

2. **Q:** Does `Promise.all` preserve the order of results?  
   **A:** Yes — results are returned in the same order as the iterable's order, regardless of resolution order.

3. **Q:** Is `Promise.all` concurrency-limited?  
   **A:** No — it starts all provided promises (via `Promise.resolve`) immediately. Use a pool to limit concurrency.

4. **Q:** How does `Promise.all` handle non-promise values in the iterable?  
   **A:** Non-promises are treated like `Promise.resolve(value)`.

5. **Q:** What's the difference between `Promise.all` and `Promise.allSettled`?  
   **A:** `Promise.all` rejects on first rejection; `allSettled` waits for all inputs to settle and returns their statuses.

6. **Q:** Why do we need to keep an index when implementing `Promise.all`?  
   **A:** To store results in iteration order, since promises may resolve in any order.

7. **Q:** What does `Promise.all` do with an empty iterable?  
   **A:** Resolves to an empty array immediately.

8. **Q:** Can `Promise.all` be used with generators?  
   **A:** Yes — as long as the generator is an iterable (e.g., `Array.from(generator)` will work), but be mindful that converting the generator will iterate it immediately.

---

## Coding interview prompts (with hints / short answers)

1. **Prompt:** Implement `Promise.any` polyfill.  
   **Hint:** Keep track of number of rejections; resolve when first fulfillment occurs; reject with an `AggregateError` if all reject.

2. **Prompt:** Implement a cancellation-aware `promisePool` where tasks can be cancelled if one fails.  
   **Hint:** Return `AbortController` or cancellation tokens to tasks; when a failure occurs, signal cancellation and reject.

3. **Prompt:** Implement `promiseAllSettled` polyfill.  
   **Answer (short):** Map each item to `Promise.resolve(item).then(v => ({status:'fulfilled', value:v}), r => ({status:'rejected', reason:r}))` and `Promise.all` that mapped list.

4. **Prompt:** Given 1000 URLs, design an approach to fetch them with a max concurrency of 10 and return only successful JSON bodies.  
   **Hint:** Use `promisePool` with task factories `() => fetch(url).then(r => r.json()).catch(()=>null)` and filter out `null`.

5. **Prompt:** Explain how you'd test your `Promise.all` polyfill for correctness.  
   **Answer:** Unit tests covering: empty iterable, non-iterable error, order preservation, immediate rejection, non-promise values, large input arrays, generator input, and interleaved sync/async resolutions.

---

## Example: `Promise.all` polyfill + concurrency pool example in one file

(see code earlier for `Promise.all` polyfill and `promisePool` implementation)

---

## Further reading & references

- MDN: `Promise.all` and `Promise.allSettled` (read the spec notes on ordering and eager resolution).
- ECMAScript specification (Promise combinators section) for detailed semantics.


---

*Generated for interview preparation — concise, testable, and focused on practical implementation details.*



# Interview-Focused Topics: Custom Map / Reduce / Filter in JavaScript

## Topic: Custom Map/Reduce/Filter  
## Sub Topic: Manual Implementation Questions

### Detailed Coverage

#### Custom `map`
`map` creates a new array by applying a callback to each element.

```javascript
function myMap(arr, callback) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(callback(arr[i], i, arr));
  }
  return result;
}
```

#### Custom `filter`
```javascript
function myFilter(arr, callback) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    if (callback(arr[i], i, arr)) {
      result.push(arr[i]);
    }
  }
  return result;
}
```

#### Custom `reduce`
```javascript
function myReduce(arr, callback, initialValue) {
  let acc = initialValue !== undefined ? initialValue : arr[0];
  let start = initialValue !== undefined ? 0 : 1;
  for (let i = start; i < arr.length; i++) {
    acc = callback(acc, arr[i], i, arr);
  }
  return acc;
}
```

---

## Interview Theory Questions

1. Difference between map, filter, reduce.  
2. Why reduce needs an initial value.  
3. Whether these functions mutate the original array.  
4. How reduce can emulate map and filter.

---

## Coding Questions

### Map using reduce
```javascript
const mapWithReduce = (arr, cb) =>
  arr.reduce((acc, val, idx, array) => {
    acc.push(cb(val, idx, array));
    return acc;
  }, []);
```

### Filter using reduce
```javascript
const filterWithReduce = (arr, cb) =>
  arr.reduce((acc, val, idx, array) => {
    if (cb(val, idx, array)) acc.push(val);
    return acc;
  }, []);
```

### Flatten using reduce
```javascript
const flatten = arr =>
  arr.reduce((acc, val) => {
    return Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val);
  }, []);
```

# Throttling & Debouncing – Interview Cheat Sheet (JavaScript)

## Topic: Throttling & Debouncing  
## Sub Topic: Manual Implementations for Interviews

---

## 🔍 Deep Dive into Throttling & Debouncing

Throttling and debouncing are tiny time‑shaping spells you cast on functions to tame noisy, rapid‑fire events like scrolling, resizing, or typing.

Debouncing groups rapid calls and executes **only once** after silence.  
Throttling caps execution frequency, ensuring the function fires **at most once every X ms**.

These patterns matter because browsers fire some events at speeds that would make a hummingbird dizzy — dozens to hundreds of times per second.

---

## 📘 Debouncing (Theory + Detail)

Debouncing delays execution until a *pause* occurs.  
If calls keep coming in before the timer expires, the timer resets.  
Useful for: search autocomplete, resize handlers, saving drafts, validating form inputs.

### Manual Debounce Implementation

```js
function debounce(fn, delay) {
  let timer = null;

  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}
```

### Leading + Trailing Debounce (Advanced)

```js
function debounce(fn, delay, immediate = false) {
  let timer = null;
  return function (...args) {
    const callNow = immediate && !timer;

    clearTimeout(timer);
    timer = setTimeout(() => {
      timer = null;
      if (!immediate) fn.apply(this, args);
    }, delay);

    if (callNow) fn.apply(this, args);
  };
}
```

---

## 🚀 Throttling (Theory + Detail)

Throttling ensures the function fires at controlled intervals even if triggered repeatedly.

Useful for: scroll listeners, drag events, window resize, infinite scroll loading.

### Timestamp-based Throttle

```js
function throttle(fn, delay) {
  let last = 0;

  return function (...args) {
    const now = Date.now();
    if (now - last >= delay) {
      last = now;
      fn.apply(this, args);
    }
  };
}
```

### Timer-based Throttle

```js
function throttle(fn, delay) {
  let timer = null;

  return function (...args) {
    if (!timer) {
      timer = setTimeout(() => {
        fn.apply(this, args);
        timer = null;
      }, delay);
    }
  };
}
```

### Combined Throttle (timestamp + timer)

This ensures smooth leading + trailing behavior.

```js
function throttle(fn, delay) {
  let last = 0;
  let timer = null;

  return function (...args) {
    const now = Date.now();
    const remaining = delay - (now - last);

    if (remaining <= 0) {
      clearTimeout(timer);
      timer = null;
      last = now;
      fn.apply(this, args);
    } else if (!timer) {
      timer = setTimeout(() => {
        last = Date.now();
        timer = null;
        fn.apply(this, args);
      }, remaining);
    }
  };
}
```

---

## 🧠 Interview Theory Questions (Concise Answers)

**1. What is debouncing?**  
A technique that delays execution until there’s a pause in event firing.

**2. What is throttling?**  
A technique that ensures the function executes at most once every specific interval.

**3. Real-world example of debouncing?**  
Live search input: avoid sending API requests on every keystroke.

**4. Real-world example of throttling?**  
Handling scroll events during page scroll animations.

**5. Difference between trailing and leading debouncing?**  
Leading: execute first call immediately.  
Trailing: execute after silence.

**6. Which is better for scroll events?**  
Throttling — ensures regular updates.

**7. Why not always throttle everything?**  
Some interactions need final-state accuracy (like validating field input), which debouncing provides.

**8. Can debounce cause missed calls?**  
Yes — if frequent calls never allow the timer to finish.

---

## 💻 Coding Questions You Might Get

**1. Implement debounce from scratch.**  
Covered above.

**2. Implement throttle with both leading & trailing.**  
Covered (combined version).

**3. Convert throttled function to return a Promise.**

```js
function throttlePromise(fn, delay) {
  let last = 0;
  let timer = null;

  return (...args) =>
    new Promise((resolve) => {
      const now = Date.now();
      const remaining = delay - (now - last);

      if (remaining <= 0) {
        clearTimeout(timer);
        timer = null;
        last = now;
        resolve(fn(...args));
      } else if (!timer) {
        timer = setTimeout(() => {
          last = Date.now();
          timer = null;
          resolve(fn(...args));
        }, remaining);
      }
    });
}
```

**4. Create a debounced fetch wrapper.**

```js
const debouncedFetch = debounce((url) => fetch(url), 300);
```

**5. Implement debounce that can be cancelled.**

```js
function debounce(fn, delay) {
  let timer = null;

  function wrapper(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  }

  wrapper.cancel = () => clearTimeout(timer);

  return wrapper;
}
```

---

## 🎯 Summary

Debouncing silences the noise.  
Throttling disciplines the chaos.  
Together they give you control over high-frequency browser events.

This cheat sheet gives the interview-ready fundamentals, the practical implementations, and the coding puzzles that appear again and again.

---

# Currying – Interview Cheat Sheet (JavaScript)

## Topic: Curry Function  
## Sub Topic: Implementation and Theory

---

## 🔍 What is Currying? (Short Answer)
Currying is a functional programming technique that transforms a function with multiple arguments `f(a, b, c)` into a sequence of functions each taking a single argument: `f(a)(b)(c)`. Currying **returns new functions** until all arguments are supplied.  
(See: JavaScript info; Wikipedia.)

---

## 📘 Theory & Why It Matters
- Currying helps with **partial application** (pre-filling some arguments) and **composition**, making functions more reusable and composable in pipelines. citeturn0search5turn0search6
- Currying is *not identical* to partial application: currying transforms the function shape into unary functions, while partial application produces a function with fewer parameters by fixing some arguments. citeturn0search7turn0search1
- Practical uses: event handlers, configuration factories, building small utility functions, and composing transformations. citeturn0search10turn0search12

---

## 🛠️ Basic Manual Implementations

### 1) Simple curried function (manual)
```js
// direct curried function
const add = x => y => x + y;

console.log(add(2)(3)); // 5
```

### 2) Generic curry (fixed arity)
```js
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return function (...next) {
      return curried.apply(this, args.concat(next));
    }
  }
}
```

Usage:
```js
function multiply(a, b, c) { return a * b * c; }
const curriedMultiply = curry(multiply);

curriedMultiply(2)(3)(4); // 24
curriedMultiply(2, 3)(4); // 24
curriedMultiply(2)(3, 4); // 24
```

### 3) Flexible arity curry (accepts any number until invoked)
```js
function curryFlex(fn, arity = fn.length) {
  return function next(...args) {
    if (args.length >= arity) {
      return fn(...args);
    }
    return (...more) => next(...args, ...more);
  }
}
```

### 4) Lodash-style curry (accepts explicit arity and placeholders)
A production-ready `curry` handles placeholders, explicit arity, and argument positions (lodash, Ramda). For reference implementations and design decisions see articles and the lodash docs. citeturn0search2turn0search8

---

## 🧪 Advanced Patterns & Pitfalls
- `fn.length` returns declared arity (number of parameters) — beware of rest parameters and default values which change `length`. citeturn0search0  
- Currying doesn't automatically improve performance — it improves **composability** and **readability**. citeturn0search10
- Decide whether your `curry` should accept multiple args per call (common in JS) or strictly one-by-one (classic definition). JavaScript libraries often favor flexibility. citeturn0search5

---

## 🧠 Interview Theory Questions (Concise Answers)

**Q1 — What is currying?**  
A: Transforming a multi-arg function into a chain of unary functions; call as `f(a)(b)(c)`. citeturn0search5

**Q2 — How does currying differ from partial application?**  
A: Currying restructures a function into unary functions; partial application fixes some arguments and returns a function of the remaining ones. citeturn0search7turn0search1

**Q3 — When would you use currying?**  
A: When you want reusable, pre-configured functions (factories), or to compose small utilities (e.g., `map`, `filter` pipelines). citeturn0search10

**Q4 — How do you handle variable arity or placeholders in curry?**  
A: Use an explicit `arity` argument and implement placeholder logic (e.g., lodash's implementation). citeturn0search8turn0search2

**Q5 — What are common mistakes?**  
A: Relying on `fn.length` blindly, expecting one-arg-only behaviour in JS, and over-currying leading to less-readable code. citeturn0search0turn0search5

---

## 💻 Coding Questions (Practice)

1. **Implement `curry` from scratch** — support calling with any grouping of arguments (example provided).  
2. **Implement `curryRight`** — arguments are applied from right to left.  
3. **Implement `autoCurry(fn)`** — auto-curry a function so it keeps collecting args until full arity is reached; allow multiple args per call.  
4. **Write tests** verifying functions work for `fn.length`, default params, and rest params.  
5. **Implement `curry` with placeholder support** (e.g., `_` placeholder similar to lodash).  

---

## ✅ Quick Reference Snippets

**Basic curry**
```js
const curry = fn => (...a) =>
  a.length >= fn.length ? fn(...a) : (...b) => curry(fn)(...a.concat(b));
```

**curryRight**
```js
const curryRight = fn => (...a) =>
  a.length >= fn.length ? fn(...a.reverse()) : (...b) => curryRight(fn)(...a.concat(b));
```

---

## 🎯 Summary
Currying transforms function shape to enable partial application and composition. In JavaScript, practical implementations often trade the pure unary definition for flexibility (accepting multiple args per call, explicit arity, placeholders). Use currying when it simplifies configuration and composition — not merely for style.

---

# Flatten Nested Array – Interview Cheat Sheet (JavaScript)

## Topic: Flatten Nested Array  
## Sub Topic: Recursion or Stack-Based Solution

---

## Theory Overview

Flattening converts a deeply nested array into a one‑dimensional array.  
Two classic interview‑friendly implementations: **recursion** and **iterative stack**.

Time complexity is **O(n)** where n is total elements.  
Space complexity depends on output + recursion depth or stack size.

---

## Recursion-Based Implementation

```js
function flatten(arr) {
  const result = [];
  for (let el of arr) {
    if (Array.isArray(el)) {
      result.push(...flatten(el));
    } else {
      result.push(el);
    }
  }
  return result;
}
```

### Functional Reduce Version
```js
function flatten(arr) {
  return arr.reduce((acc, el) => {
    if (Array.isArray(el)) {
      return acc.concat(flatten(el));
    } else {
      return acc.concat(el);
    }
  }, []);
}
```

---

## Stack-Based (Iterative) Implementation

```js
function flattenIterative(arr) {
  const result = [];
  const stack = [...arr];

  while (stack.length) {
    const el = stack.pop();
    if (Array.isArray(el)) {
      for (let i = el.length - 1; i >= 0; i--) {
        stack.push(el[i]);
      }
    } else {
      result.push(el);
    }
  }
  return result.reverse();
}
```

---

## Depth-Limited Flatten (Optional Interview Question)

```js
function flattenDepth(arr, depth = 1) {
  if (depth === 0) return arr.slice();

  const result = [];
  for (let el of arr) {
    if (Array.isArray(el)) {
      result.push(...flattenDepth(el, depth - 1));
    } else {
      result.push(el);
    }
  }
  return result;
}
```

---

## Interview Theory Questions (Concise)

**1. What is flattening?**  
Converting nested arrays into a single-level array.

**2. Why recursion works well here?**  
Nested arrays map naturally to recursive structure: base case (non‑array), recursive case (array).

**3. Why might you avoid recursion?**  
Deeply nested arrays can exceed call stack limits; iterative stack avoids this.

**4. Complexity?**  
O(n) time. Space: O(n) output + O(depth) recursion or O(depth) stack.

**5. Does JS provide a built-in method?**  
`arr.flat(Infinity)` flattens fully, but interviews usually require manual implementation.

---

## Coding Practice Questions

1. Implement recursive `flatten`.  
2. Implement iterative stack‑based `flattenIterative`.  
3. Implement `flattenDepth(arr, depth)`.  
4. Modify flatten to handle Sets or Maps.  
5. Implement a performance‑optimized flatten avoiding repeated `concat`.  
6. Handle edge cases: empty arrays, very deep nesting, mixed types.

---

## Summary

Flattening a nested array tests recursion fundamentals, stack simulation skills, and complexity reasoning.  
Master both recursion and iterative solutions, and be ready to discuss depth‑limited behavior and edge cases.

---


# Async Retry Mechanism – Interview Cheat Sheet (JavaScript)

## Topic: Async Retry Mechanism  
## Sub Topic: Exponential Backoff Logic (with Jitter)

---

## Why retries + backoff matter
Retries smooth over transient failures (temporary network glitches, throttling, service hiccups) so clients can succeed without human intervention. However, naive retries can worsen overload (thundering herds). Exponential backoff — increasing wait time after each failed attempt — plus *jitter* (randomization) is the recommended defensive pattern. See AWS and Google Cloud best practices for guidance. citeturn0search4turn0search2

Key guidelines:
- Retry **only** for transient, idempotent errors and where the operation is safe to repeat. citeturn0search8  
- Cap the maximum number of retries and the maximum delay to avoid indefinite looping and very long waits. citeturn0search4  
- Add **jitter** to avoid synchronized retries across many clients (thundering herd). AWS documents several jitter strategies (full, equal, decorrelated). citeturn0search0  
- Honor server signals like `Retry-After` when present. RFCs define `Retry-After` semantics for 503 responses. citeturn0search17

---

## Backoff strategies (short digest)

- **Fixed delay**: simple sleep between attempts (not ideal under load).  
- **Exponential backoff**: delay = base * (2 ** attempt) (often capped).  
- **Exponential + jitter**: add randomness to delay to avoid synchronized retries. Common variants:
  - *Full jitter*: pick random between 0 and `cap` where `cap = min(maxDelay, base * 2**attempt)`. Recommended by many. citeturn0search0
  - *Equal jitter*: `delay = cap/2 + random(0, cap/2)`.
  - *Decorrelated jitter*: avoids correlation across retries; AWS Builders Library describes this approach. citeturn0search4

---

## Simple JS implementations

### Utility: sleep
```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

### 1) Basic exponential backoff (no jitter)
```js
async function retryExponential(fn, {
  retries = 5,
  baseDelay = 100, // ms
  maxDelay = 10000,
  shouldRetry = () => true
} = {}) {
  let attempt = 0;
  while (true) {
    try {
      return await fn();
    } catch (err) {
      attempt++;
      if (attempt > retries || !shouldRetry(err)) throw err;
      const delay = Math.min(maxDelay, baseDelay * (2 ** (attempt - 1)));
      await sleep(delay);
    }
  }
}
```

### 2) Exponential backoff with *full jitter* (recommended)
```js
function randomInt(max) {
  return Math.floor(Math.random() * max);
}

async function retryWithFullJitter(fn, {
  retries = 5,
  baseDelay = 100,
  maxDelay = 10000,
  shouldRetry = () => true
} = {}) {
  let attempt = 0;
  while (true) {
    try {
      return await fn();
    } catch (err) {
      attempt++;
      if (attempt > retries || !shouldRetry(err)) throw err;
      const cap = Math.min(maxDelay, baseDelay * (2 ** (attempt - 1)));
      const delay = randomInt(cap); // full jitter: uniform [0, cap)
      await sleep(delay);
    }
  }
}
```

### 3) Decorrelated jitter (AWS Builders Library pattern)
```js
async function retryDecorrelatedJitter(fn, {
  retries = 5,
  baseDelay = 100,
  maxDelay = 10000,
  shouldRetry = () => true
} = {}) {
  let attempt = 0;
  let sleepTime = baseDelay;
  while (true) {
    try {
      return await fn();
    } catch (err) {
      attempt++;
      if (attempt > retries || !shouldRetry(err)) throw err;
      // decorrelated: sleep = min(maxDelay, random(base, sleep * 3))
      const rnd = baseDelay + Math.random() * (sleepTime * 3 - baseDelay);
      sleepTime = Math.min(maxDelay, Math.floor(rnd));
      await sleep(sleepTime);
    }
  }
}
```

### 4) Respect `Retry-After` header (when available)
If the server responds with `Retry-After` (HTTP header), prefer it over client-side backoff calculation when it indicates a retry delay.
```js
function parseRetryAfter(header) {
  if (!header) return null;
  const secs = parseInt(header, 10);
  if (!Number.isNaN(secs)) return secs * 1000;
  const date = Date.parse(header);
  return Number.isNaN(date) ? null : date - Date.now();
}

// Example: when using fetch
async function fetchWithRetry(url, opts = {}, retryOpts = {}) {
  const shouldRetry = (err, res) => {
    if (err) return true; // network error
    if (!res) return false;
    // retry on 429, 503, 502, 504 (common transient/throttling errors)
    return [429, 502, 503, 504].includes(res.status);
  };

  return retryWithFullJitter(async () => {
    const res = await fetch(url, opts);
    if (!res.ok && shouldRetry(null, res)) {
      const ra = parseRetryAfter(res.headers.get('Retry-After'));
      const err = new Error('HTTP ' + res.status);
      err.retryAfter = ra;
      throw err;
    }
    return res;
  }, retryOpts);
}
```
See RFCs and server docs for `Retry-After` semantics. citeturn0search17

---

## Retry knobs & safety checks (what to expose)

- `maxRetries` — upper bound for retries.  
- `baseDelay` — initial backoff base (ms).  
- `maxDelay` — cap on wait interval.  
- `shouldRetry(error, response)` — predicate to decide retriable problems (status codes, network errors, idempotency).  
- `signal` or `abortController` — allow cancellation of waiting/retries.  
- `onRetry(attempt, delay, error)` — hook for logging/metrics.  
- Metric logging: count retries and final failure reason for debugging. citeturn0search11

---

## Interview Theory Questions (Concise Answers)

**Q1. What is exponential backoff?**  
A: A retry strategy where wait times increase exponentially between attempts (e.g., base × 2^attempt), often with caps to avoid unbounded delays. citeturn0search21

**Q2. Why add jitter?**  
A: To randomize retry timings across clients so they don't all retry simultaneously, preventing thundering‑herd and improving overall system stability. AWS strongly recommends jitter. citeturn0search0

**Q3. When should you NOT retry?**  
A: For non‑idempotent operations (unsafe to repeat), client errors that indicate a bad request (4xx other than 429), or when server explicitly says not to via headers or error payloads. citeturn0search8turn0search14

**Q4. What is `Retry-After`?**  
A: An HTTP header servers can send (e.g., with 503 or 429) telling clients how long to wait before retrying. Clients should prefer server guidance when available. citeturn0search17

**Q5. How do you avoid infinite retries?**  
A: Use `maxRetries`, exponential caps, and circuit‑breaker patterns. Log and surface retry metadata for observability. citeturn0search4turn0search8

---

## Coding/Design Interview Questions

1. Implement a generic `retry(fn, options)` in JavaScript that supports exponential backoff with jitter, an abort signal, hooks for logging, and a `shouldRetry` predicate.  
2. Demonstrate how to integrate `Retry-After` header into client backoff logic.  
3. Compare and implement *full jitter* vs *decorrelated jitter*; run a simple simulation showing distribution of retry timestamps for many clients.  
4. Build a rate-limited parallel loader that retries failed chunks with exponential backoff — ensure retries don’t starve new work.  
5. Design a retry + circuit‑breaker combo for a high‑traffic API client.

---

## Quick Reference: Example `retry` usage
```js
const res = await retryWithFullJitter(() => fetch('/api'), {
  retries: 4,
  baseDelay: 200,
  maxDelay: 5000,
  shouldRetry: (err, res) => err || [429,502,503,504].includes(res?.status)
});
```

---

## Summary
Implement exponential backoff with capped retries and prefer adding jitter to avoid synchronized retries — AWS and Google Cloud call this best practice. Respect server signals (`Retry-After`), retry only when safe, and expose configuration + observability hooks for production readiness. citeturn0search0turn0search4turn0search2

---
