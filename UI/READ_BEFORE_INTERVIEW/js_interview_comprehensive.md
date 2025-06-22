# JavaScript Interview Questions and Answers

Each question includes a concise theory explanation and a practical code example.

---

## 1. Difference between JavaScript and other programming languages
**Theory:** JS is dynamically typed, prototype-based, event-driven, and runs in browser/Node with JIT compilation. Other languages like Java/C++ are class-based, statically typed, and multi-threaded.
```js
// Prototype inheritance
function Person(name) { this.name = name; }
Person.prototype.greet = () => console.log(`Hi, ${this.name}`);
```

---

## 2. Explain execution context and event loop
**Theory:** Execution contexts (global/function) manage scope/hoisting. The event loop processes call stack, microtasks, then macrotasks to handle async non-blocking code.
```js
console.log('start');
setTimeout(() => console.log('timeout'), 0);
Promise.resolve().then(() => console.log('promise'));
console.log('end');
// start, end, promise, timeout
```

---

## 3. Difference between `let`, `const`, and `var`
**Theory:** `var` is function-scoped, hoisted initialized as undefined; `let`/`const` are block-scoped with TDZ; `const` must be initialized and cannot be reassigned.
```js
console.log(a); // undefined
var a = 1;
console.log(b); // ReferenceError
let b = 2;
const c = 3;
// c = 4; // TypeError
```

---

## 4. Primitive vs Non-Primitive data types
**Theory:** Primitives (undefined, null, boolean, number, string, symbol, bigint) are immutable and copied by value. Objects/arrays/functions are reference types, mutable and copied by reference.
```js
let x = 5, y = x;
y = 10; // x remains 5
let obj = {a:1}, ref = obj;
ref.a = 2; // obj.a is now 2
```

---

## 5. Nullish coalescing operator (`??`)
**Theory:** Returns right operand only if left is null or undefined.
```js
const userCount = 0;
console.log(userCount ?? 10);    // 0
console.log(null ?? 10);         // 10
```

---

## 6. Arrow function vs normal function
**Theory:** Arrow functions use lexical `this`, no `arguments` object, cannot be constructors.
```js
const obj = {val:1};
obj.normal = function() { console.log(this.val); };
obj.arrow = () => console.log(this.val);
obj.normal(); // 1
obj.arrow();  // undefined
```

---

## 7. IIFE (Immediately Invoked Function Expression)
**Theory:** Runs immediately, creates private scope.
```js
(function(){
  const secret = 'IIFE';
  console.log(secret);
})();
```

---

## 8. Closures concept in JavaScript
**Theory:** Inner functions retain access to outer scope variables even after outer function returns.
```js
function makeAdder(a) {
  return function(b) {
    return a + b;
  };
}
const add5 = makeAdder(5);
console.log(add5(3)); // 8
```

---

## 9. `this` keyword
**Theory:** `this` refers to context of invocation: global, method-owner, `new` instance, or explicitly bound.
```js
function show() { console.log(this); }
const obj2 = {show};
obj2.show();   // obj2
show();        // global or undefined (strict)
```

---

## 10. Prototype and prototype inheritance
**Theory:** Objects inherit via prototype chain; changes to prototype affect all derived objects.
```js
const parent = {hello: () => console.log('hi')};
const child = Object.create(parent);
child.hello(); // hi
```

---

## 11. Difference between `map`, `filter`, and `find`
**Theory:** `map` transforms arrays, `filter` selects elements, `find` returns first matching element.
```js
const arr = [1,2,3,4];
arr.map(n => n*2);      // [2,4,6,8]
arr.filter(n => n%2);   // [1,3]
arr.find(n => n>2);     // 3
```

---

## 12. Difference between `forEach` and `map`
**Theory:** `forEach` executes callback for each element without return; `map` returns new array of mapped values.
```js
[1,2,3].forEach(n => console.log(n)); // logs 1,2,3
const doubled = [1,2,3].map(n => n*2); // [2,4,6]
```

---

## 13. Callback function and use cases
**Theory:** Function passed to another to be called later. Used in async I/O, events, timers, array methods.
```js
function fetchData(cb) {
  setTimeout(() => cb('data'), 100);
}
fetchData(console.log); // 'data'
```

---

## 14. Callback hell and how to avoid it
**Theory:** Nested callbacks reduce readability. Use Promises, `async/await`, or modular functions.
```js
// Avoid
doA(a => {
  doB(b => {
    doC(c => console.log(c));
  });
});
// Better
async function run() {
  const a = await doA();
  const b = await doB(a);
  console.log(await doC(b));
}
```

---

## 15. Promise and example
**Theory:** Represents eventual completion or failure of async operation.
```js
const p = new Promise((res, rej) => {
  setTimeout(() => res('done'), 500);
});
p.then(console.log).catch(console.error);
```

---

## 16. Promise methods
**Theory:** `.then()`, `.catch()`, `.finally()`, and helpers `Promise.all`, `race`, `allSettled`, `any`.
```js
Promise.all([p1, p2]).then(results => console.log(results));
```

---

## 17. `Promise.race` vs `Promise.any`
**Theory:** `race` settles on first settled (resolve/reject). `any` resolves on first fulfillment or rejects if all reject.
```js
Promise.race([Promise.reject(), Promise.resolve(2)]).catch(console.error);
Promise.any([Promise.reject(), Promise.resolve(2)]).then(console.log);
```

---

## 18. Event bubbling and event capturing
**Theory:** Capturing (top-down) then target then bubbling (bottom-up). Listeners specify phase.
```js
element.addEventListener('click', handler, true); // capture
element.addEventListener('click', handler);       // bubble
```

---

## 19. Event delegation
**Theory:** Single listener on parent uses `event.target` to handle child events efficiently.
```js
document.body.addEventListener('click', e => {
  if (e.target.matches('button')) console.log('button clicked');
});
```

---

## 20. localStorage, sessionStorage, and cookies
**Theory:** `localStorage` persists until cleared, `sessionStorage` until tab close, cookies sent to server.
```js
localStorage.setItem('key','val');
sessionStorage.setItem('key','val');
document.cookie = 'user=Joe; max-age=3600';
```

---

## 21. Immutability concept in JavaScript
**Theory:** Avoid mutating data; return new objects/arrays using spread or methods.
```js
const obj = {a:1};
const newObj = {...obj, b:2};
```

---

## 22. Difference between Map and Set
**Theory:** `Map` stores key-value pairs; `Set` stores unique values.
```js
const m = new Map([[1,'a']]);
const s = new Set([1,1,2]); // {1,2}
```

---

## 23. Code splitting
**Theory:** Load code dynamically to reduce initial bundle size.
```js
import('./module.js').then(m => m.doThing());
```

---

## 24. Memoization concepts
**Theory:** Cache function results to optimize repeated calls.
```js
const memo = {};
function fib(n) {
  if (memo[n]) return memo[n];
  return memo[n] = n<2 ? n : fib(n-1)+fib(n-2);
}
```

---

## 25. Strict mode
**Theory:** `'use strict'` enforces safer syntax and errors for bad practices.
```js
'use strict';
undeclared = 5; // ReferenceError
```

---

## 26. `call()`, `bind()`, and `apply()`
**Theory:** Set `this` context and arguments.
```js
function f(a,b) { return this.x + a + b; }
f.call({x:1},2,3);
f.apply({x:1},[2,3]);
const bound = f.bind({x:1},2);
bound(3);
```

---

## 27. Currying
**Theory:** Transform multi-arg function into sequence of unary functions.
```js
const add = a => b => a + b;
console.log(add(2)(3)); // 5
```

---

## 28. Shallow vs deep copy
**Theory:** Shallow copy clones top-level; deep copy recursively clones all levels.
```js
const shallow = {...obj};
const deep = JSON.parse(JSON.stringify(obj));
```

---

## 29. Promise chaining
**Theory:** Chain `.then()` calls to sequence async operations.
```js
fetch('/api')
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(console.error);
```

---

## 30. `Object.freeze` and `Object.seal`
**Theory:** `freeze` makes object immutable; `seal` prevents adding/removing properties.
```js
const o = {a:1};
Object.freeze(o);
o.a = 2; // no change
Object.seal(o);
delete o.a; // false
```

---

## 31. Design patterns in JavaScript
**Theory:** Reusable solutions like Module, Singleton, Observer.
```js
// Module Pattern
const Counter = (function() {
  let count=0;
  return {inc:() => ++count};
})();
```

---

## 32. Debouncing and throttling
**Theory:** Control rate of function execution in rapid events.
```js
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}
function throttle(fn, limit) {
  let inThrottle;
  return (...args) => {
    if (!inThrottle) {
      fn(...args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}
```
