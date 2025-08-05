
# Node.js Promises Guide

## 📝 Promise States

Promises have three states:

- **Pending**: Initial state, neither fulfilled nor rejected.
- **Fulfilled**: Operation completed successfully.
- **Rejected**: Operation failed.

**Example Scenario**:
Fetching data from an API.

## 📌 Basic Syntax of a Promise

```javascript
const promise = new Promise((resolve, reject) => {
  if (true) {
    resolve("Success!");
  } else {
    reject("Failed!");
  }
});
```

**What it Does**:
Creates a new Promise that resolves or rejects based on a condition.

## ✅ Handling Promises

### Using `.then()`, `.catch()`, and `.finally()`

```javascript
promise
  .then(result => console.log(result))
  .catch(error => console.error(error))
  .finally(() => console.log("Done"));
```

**What it Does**:
Handles successful and error cases and executes cleanup logic.

## 🔗 Chaining Promises

```javascript
fetchData()
  .then(parseData)
  .then(processData)
  .catch(handleError);
```

**What it Does**:
Sequentially performs asynchronous operations.

## 🚀 Async/Await with Promises

```javascript
async function fetchData() {
  try {
    const data = await apiCall();
    return data;
  } catch (error) {
    console.error(error);
  }
}
```

**What it Does**:
Simplifies asynchronous code to look synchronous.

## 🌐 Top-Level Await

```javascript
const data = await fetchData();
console.log(data);
```

**What it Does**:
Allows use of `await` at the module's top-level scope.

## 📡 Promise-based Node.js APIs

```javascript
const fs = require('fs/promises');
fs.readFile('file.txt', 'utf-8').then(console.log).catch(console.error);
```

**What it Does**:
Modern Node.js APIs that return Promises.

## ⚡ Advanced Promise Methods

### `Promise.all()`
Waits for all Promises to fulfill.

```javascript
Promise.all([p1, p2]).then(console.log);
```

### `Promise.allSettled()`
Waits for all Promises, regardless of fulfillment.

```javascript
Promise.allSettled([p1, p2]).then(console.log);
```

### `Promise.race()`
Settles as soon as the first Promise settles.

```javascript
Promise.race([p1, p2]).then(console.log);
```

### `Promise.any()`
Settles as soon as the first Promise fulfills.

```javascript
Promise.any([p1, p2]).then(console.log);
```

### `Promise.resolve()` and `Promise.reject()`

```javascript
Promise.resolve("Resolved!").then(console.log);
Promise.reject("Rejected!").catch(console.error);
```

### `Promise.try()`
Ensures synchronous errors are caught.

```javascript
Promise.try(() => potentiallyFailingFunction())
  .then(console.log)
  .catch(console.error);
```

### `Promise.withResolvers()`
Exposes resolve and reject methods directly.

```javascript
const { promise, resolve, reject } = Promise.withResolvers();
resolve('Done!');
promise.then(console.log);
```

## 🚨 Error Handling with Promises

Properly handle errors with `.catch()` or `try/catch` in async/await.

```javascript
async function safeFetch() {
  try {
    return await apiCall();
  } catch (error) {
    handleError(error);
  }
}
```

## 🎯 Scheduling Tasks in the Event Loop

### `queueMicrotask()`
Schedules tasks immediately after the current operation.

```javascript
queueMicrotask(() => console.log("Microtask"));
```

### `process.nextTick()`
Prioritized callback after current operation.

```javascript
process.nextTick(() => console.log("Next tick"));
```

### `setImmediate()`
Runs after I/O events, before timers.

```javascript
setImmediate(() => console.log("Immediate"));
```

## ⏳ When to Use Each

| Method | When to Use |
| ------ | ----------- |
| `queueMicrotask()` | Immediate follow-up tasks. |
| `process.nextTick()` | High-priority next callback. |
| `setImmediate()` | After I/O, before timers. |

