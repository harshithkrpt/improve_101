# JavaScript Interview Questions and Answers

For each question below, you’ll find a concise theoretical explanation followed by a practical code example.

---

## 1. Difference between JavaScript and other programming languages
**Theory:** JavaScript is a dynamically typed, weakly coerced, prototype-based language designed originally for the browser with a single-threaded, event-driven model. Unlike class-based, statically typed languages (e.g., Java, C#), JS uses prototypes for inheritance and JIT compilation at runtime.

```js
// Prototype-based inheritance in JS
function Person(name) {
  this.name = name;
}
Person.prototype.greet = function() {
  console.log(`Hello, ${this.name}`);
};
```

---

## 2. Explain execution context and event loop
**Theory:** An execution context is the environment where JS code runs (global or function). The event loop manages asynchronous operations by processing the call stack, then running microtasks (Promises) before macrotasks (timers, I/O), ensuring non-blocking behavior.

```js
console.log('start');

setTimeout(() => console.log('timeout'), 0);

Promise.resolve().then(() => console.log('promise'));

console.log('end');
// Output: start, end, promise, timeout
```

---

## 3. Difference between `let`, `const`, and `var`
**Theory:**  
- `var`: function-scoped, hoisted and initialized to `undefined`.  
- `let`: block-scoped, hoisted but uninitialized until its declaration (TDZ).  
- `const`: block-scoped, like `let`, but must be initialized and cannot be reassigned.

```js
console.log(a); // undefined
var a = 1;

console.log(b); // ReferenceError
let b = 2;

const c = { x: 1 };
c.x = 2; // OK
c = {};  // TypeError
```

---

## 4. Primitive vs Non-Primitive data types
**Theory:** Primitives (`undefined`, `null`, `boolean`, `number`, `string`, `symbol`, `bigint`) are immutable and stored by value. Non-primitives (objects, arrays, functions) are mutable and stored by reference.

```js
// Primitive example
let x = 10;
let y = x;
y = 20;
console.log(x); // 10

// Reference example
let arr = [1, 2];
let ref = arr;
ref.push(3);
console.log(arr); // [1, 2, 3]
```

---

## 5. Nullish coalescing operator (`??`)
**Theory:** Returns the right-hand operand only if the left-hand side is `null` or `undefined`, avoiding false positives on other falsy values (`0`, `''`, `false`).

```js
let count = 0;
console.log(count ?? 10);       // 0
console.log(undefined ?? 10);    // 10
```

---

## 6. Arrow function vs normal function
**Theory:** Arrow functions (`=>`) offer concise syntax and lexical `this` binding, do not have their own `arguments` object, and cannot be used as constructors.

```js
const obj = {
  val: 5,
  normal() { console.log(this.val); },   // 5
  arrow: () => console.log(this.val)      // undefined
};
obj.normal();
obj.arrow();
```

---

## 7. IIFE (Immediately Invoked Function Expression)
**Theory:** A function expression that runs immediately, creating a private scope and avoiding global namespace pollution.

```js
(function() {
  const secret = 'IIFE';
  console.log(secret);
})();
```

---

## 8. Closures
**Theory:** A closure occurs when an inner function retains access to variables in its outer scope even after that outer function has returned.

```js
function makeCounter() {
  let count = 0;
  return function() {
    return ++count;
  };
}
const counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
```

---

## 9. `this` keyword
**Theory:** `this` refers to the execution context: global in standalone calls, the owning object in method calls, a new instance when using `new`, explicitly set by `.call/.apply/.bind`, and lexically bound in arrow functions.

```js
function show() {
  console.log(this);
}
const obj2 = { show };
obj2.show();  // logs obj2
show();       // global object or undefined in strict mode
```

---

## 10. Prototype and prototype inheritance
**Theory:** Every JS object links to a prototype from which it inherits properties. Changes to the prototype are reflected in all objects linked to it.

```js
const animal = { eats: true };
const rabbit = Object.create(animal);
rabbit.hops = true;
console.log(rabbit.eats); // true
```

---

_(Continue similarly for questions 11 through 32)_  
