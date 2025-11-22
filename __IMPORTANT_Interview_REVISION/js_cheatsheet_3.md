# Topic : Advanced Concepts
## Sub Topic : Event Delegation vs Bubbling (JavaScript)

---

## 1. Quick definitions
- **Event Bubbling (and Capturing)**  
  Event propagation in the DOM happens in phases: *capturing* (top → target), *target* (the event on the actual element), and *bubbling* (target → top). By default most event listeners run in the **bubbling** phase. citeturn0search4turn0search12

- **Event Delegation**  
  A pattern that *uses* event propagation (usually bubbling) to handle events for multiple child elements by attaching a single listener to a parent (ancestor). This reduces memory/handler churn and simplifies dynamic element handling. citeturn0search0turn0search20

---

## 2. How propagation works (step-by-step)
1. Browser constructs the event path from `window` → `document` → `html` → ... → target element. citeturn0search12  
2. **Capturing phase**: event travels down the tree and handlers registered with `{capture: true}` are invoked. citeturn0search4  
3. **Target phase**: handlers on the target element run. citeturn0search12  
4. **Bubbling phase**: handlers on ancestors run from closest parent up to `document` (unless propagation is stopped). Default `addEventListener` without capture listens during bubbling. citeturn0search4turn0search12

**Control methods**
- `event.stopPropagation()` — stops further propagation in both capturing and bubbling. Does not stop other handlers on the same node (use `stopImmediatePropagation()` for that). citeturn0search7  
- `event.preventDefault()` — prevents default browser action but does not affect propagation. citeturn0search7

---

## 3. Event Delegation: pattern details & example
**Why use it**
- Fewer listeners → less memory and CPU overhead.
- Works with dynamically added children (no need to rebind).
- Centralized logic for similar child behaviors.

**Example**
```html
<ul id="list">
  <li data-id="1">One</li>
  <li data-id="2">Two</li>
  <li data-id="3">Three</li>
</ul>
<script>
  document.getElementById('list').addEventListener('click', function(event) {
    const li = event.target.closest('li'); // find nearest <li>
    if (!li) return;
    console.log('clicked id:', li.dataset.id);
  });
</script>
```
Here the click on any `<li>` bubbles to the `<ul>` listener. Use `event.target` to find where it started, and `event.currentTarget` if you want the element with the listener. citeturn0search20turn0search2

---

## 4. `event.target` vs `event.currentTarget`
- `event.target`: the actual element that initiated the event (the deepest node). Useful in delegation to know which child was clicked. citeturn0search14turn0search11  
- `event.currentTarget`: the element whose listener is currently running (e.g., the parent you attached the listener to). Often safer when you need to reference the element holding the handler. citeturn0search19turn0search11

---

## 5. Caveats, pitfalls & gotchas
- Some events do **not** bubble (e.g., `focus`, `blur`—use `focusin`/`focusout` if you need bubbling equivalents). Check MDN for specifics. citeturn0search10  
- Delegation requires a stable ancestor — if parent is removed or replaced, delegation breaks.  
- Using `event.target` directly can mislead if clicks land on child elements (images, spans). Use `closest()` or explicit checks. citeturn0search20  
- Order matters: if you add a capturing listener and a bubbling listener, the capturing runs first (top-down), then target, then bubbling runs (bottom-up). citeturn0search4

---

## 6. Interview-style theory questions (concise answers)
1. **Q:** What is event bubbling?  
   **A:** The phase of DOM event propagation where an event moves from the target element upward through ancestors, triggering handlers on them. citeturn0search4

2. **Q:** What is event delegation?  
   **A:** A pattern that attaches a single handler to a parent to manage events from its children by leveraging event propagation. citeturn0search0

3. **Q:** Difference between `event.target` & `event.currentTarget`?  
   **A:** `target` is where the event originated; `currentTarget` is the element whose listener is running. citeturn0search14turn0search19

4. **Q:** How to prevent an event from reaching ancestor handlers?  
   **A:** Call `event.stopPropagation()` inside the handler. Use `stopImmediatePropagation()` to also prevent other handlers on the same element. citeturn0search7

5. **Q:** When would you *not* use delegation?  
   **A:** For events that don’t bubble, when child handlers need independent state or when selector matching is too expensive/complex. citeturn0search10

---

## 7. Coding interview questions (practical)
1. Implement event delegation for a to-do list where clicking the checkbox toggles completed state (no per-item listeners).  
2. Given a table with thousands of rows, how would you attach click handlers for row selection efficiently? (expected: delegation on `<tbody>` and `closest('tr')`).  
3. Build a small modal system where clicking an overlay closes the modal but clicking inside the modal body does not close it (hint: check `event.target` and `stopPropagation`).  
4. Write an accessible keyboard handler: capture `Enter` on dynamically created buttons via delegation and trigger the same handler as `click`.  
5. Debugging question: Clicks on children trigger parent handlers twice — show how you’d find duplicate bindings and demonstrate `stopImmediatePropagation()` if necessary.

---

## 8. Quick cheatsheet (one-line reminders)
- Delegation = single listener on ancestor + use `event.target`. citeturn0search20  
- Bubbling = default upward propagation. Capture = set `{capture:true}` to run early. citeturn0search4  
- `stopPropagation()` stops travel; `preventDefault()` blocks default browser action. citeturn0search7

---

## 9. References (selected)
- MDN: Bubbling and capturing. citeturn0search4  
- MDN: Event.stopPropagation(). citeturn0search7  
- Dmitri Pavlutin — Event Delegation. citeturn0search20  
- GeeksforGeeks — Event Delegation. citeturn0search17  
- StackOverflow — target vs currentTarget. citeturn0search5


# Advanced Concepts — Functional Programming (JavaScript)

## 1. Theory & Coverage

### A. What is Functional Programming (FP)?
Functional Programming is a paradigm where computation is treated as the evaluation of mathematical functions, avoids mutable state and side‐effects, and emphasises functions as first‐class citizens.

### B. Core Concepts

#### 1. Pure Functions
A function that returns the same output for the same inputs and has no side-effects.

#### 2. Higher-Order Functions
A function that takes/returns other functions.

#### 3. Immutability
Data is not mutated; instead new copies are created.

### C. How They Fit Together
Pure functions + immutability + HOFs → predictable declarative code.

## 2. Theory‑Based Interview Questions

1. What is a pure function?  
   A function that always returns the same output for the same input and has no side‑effects.

2. What is a higher-order function?  
   A function that takes or returns another function.

3. Why immutability?  
   Predictability, fewer bugs, easier reasoning.

4. Refactor to FP?  
   Use .reduce instead of mutations.

5. Drawbacks of FP?  
   Copying costs, extra memory, learning curve.

6. Side‑effects?  
   External state modification.

## 3. Coding Questions

### Convert impure to pure
function generateId(currentId) { return currentId + 1; }

### filterMap implementation
function filterMap(arr, predicate, transform) {
  return arr.reduce((acc, item) => {
    if(predicate(item)) acc.push(transform(item));
    return acc;
  }, []);
}

### Immutable update
const updated = { ...user, age: 31 };

### Composition
const compose = (f, g) => x => f(g(x));

### Memoization
function memoize(fn) {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if(cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}


# Currying & Partial Application — Cheat Sheet (JavaScript)

**Topic:** Advanced Concepts  
**Sub Topic:** Currying & Partial Application — use cases, functional composition

---

## Quick summary
- **Currying** transforms a function `f(a, b, c)` into `f(a)(b)(c)` — a sequence of unary functions.  
- **Partial application** fixes one or more arguments of a function and returns a new function with smaller arity (fewer parameters).  
- Currying is a transformation; partial application is an invocation technique. They overlap in usefulness (both help create reusable specialized functions).  

---

## Why care? (High-level use cases)
1. **Configuration and reuse** — fix frequently used parameters (e.g., logging levels, base URLs) and get specialized helpers.  
2. **Function composition** — curried functions compose more naturally in pipelines (`compose`/`pipe`).  
3. **Readability & testability** — small pure functions are easier to reason about and unit test.  
4. **Middleware / handlers** — create chains of handlers that accept one argument at a time.  

---

## Definitions + differences

### Currying
A transformation of a function that takes multiple arguments into a chain of functions that each take a single argument.

```js
// uncurried
const add = (a, b) => a + b;

// curried
const addCurried = a => b => a + b;

const addTwo = addCurried(2);
console.log(addTwo(3)); // 5
```

### Partial application
Fixes some arguments of a function and returns a new function that expects the rest.

```js
const add = (a, b, c) => a + b + c;
const addWith1 = add.bind(null, 1); // fixes first arg
console.log(addWith1(2, 3)); // 6
```

---

## Implementations

### Simple curry utility (supports calling with 1..n args)
```js
function curry(fn, arity = fn.length) {
  return function curried(...args) {
    if (args.length >= arity) return fn.apply(this, args);
    return function (...next) {
      return curried.apply(this, args.concat(next));
    };
  };
}

// usage
const join = (a, b, c) => `${a}-${b}-${c}`;
const cur = curry(join);
console.log(cur('x')('y')('z')); // "x-y-z"
console.log(cur('x','y')('z'));   // "x-y-z"
```

### Simple partial utility
```js
function partial(fn, ...preset) {
  return function (...later) {
    return fn.apply(this, [...preset, ...later]);
  };
}

// usage
const multiply = (a, b, c) => a * b * c;
const mulBy2 = partial(multiply, 2);
console.log(mulBy2(3,4)); // 24
```

---

## Function composition example (with curry)
```js
const compose = (...fns) => x => fns.reduceRight((v, f) => f(v), x);

const toUpper = s => s.toUpperCase();
const exclaim = s => s + '!';
const shout = compose(exclaim, toUpper);
console.log(shout('hello')); // "HELLO!"
```

When functions are curried and arranged correctly, composition pipelines become cleaner (especially when mapping over collections or building transforms).

---

## Practical examples / real-world patterns
- **Partial application for configuration**: `const fetchFrom = partial(fetch, baseUrl)` or use `fetchWithBase(base) => (path, opts) => fetch(base+path, opts)`.
- **Event handlers**: `const handleClick = (id) => (evt) => doSomething(id, evt)`.
- **Validation pipelines**: chain curried validators that each accept the value then return either `true` or an error object.
- **Localization**: `const t = curry((lang, key) => ...)` → `const tEn = t('en')`.

---

## Concise theory interview questions (with answers) — be ready to explain these briefly

1. **Q: What's the difference between currying and partial application?**  
   A: Currying transforms a function into unary functions (`f(a,b)` → `f(a)(b)`); partial application fixes some arguments and returns a function with smaller arity. They’re related but not identical.

2. **Q: When would you prefer partial application over currying?**  
   A: When you want to fix a subset of arguments at once (e.g., configuration object) and still call the resulting function with remaining args in a regular way. Partial is more ergonomic for fixing multiple args.

3. **Q: Does currying improve performance?**  
   A: Not usually — currying is a design/tooling pattern for composability and clarity. It can add slight overhead, so use it where clarity and reuse outweigh micro-performance costs.

4. **Q: How do you curry variadic functions or functions with optional args?**  
   A: Use a flexible `curry` implementation that tracks `arity` (desired number of arguments) and gathers arguments until that arity is reached; optional args complicate the desired arity decision.

5. **Q: How does `Function.prototype.bind` relate to partial application?**  
   A: `bind` can perform partial application by pre-setting initial arguments (and `this`), effectively creating a partially applied function.

---

## Concise coding interview problems (with hints / starter code)

### Problem 1 — Implement `curry` (classic)
Implement `curry(fn)` that returns a curried version of `fn`. Support flexible calls like `cur(1)(2)(3)`, `cur(1,2)(3)`, `cur(1)(2,3)`.

*Hint:* Use recursion and `fn.length` for default arity; collect args until `arity` met.

Starter:
```js
function curry(fn, arity = fn.length) {
  // your code
}
```

### Problem 2 — Implement `partial`
Implement `partial(fn, ...preset)`. Ensure `this` and argument order are preserved.

Starter:
```js
function partial(fn, ...preset) {
  return function(...rest) {
    return fn.apply(this, [...preset, ...rest]);
  };
}
```

### Problem 3 — Compose a pipeline that uses curried functions
Given curried validators `isString`, `minLen(n)`, create `validateName = compose(minLen(3), isString)` and apply to an array of inputs using `map`.

*Hint:* Implement `compose` and ensure function order is correct.

### Problem 4 — Practical debugging
You find a curried function `f = a => b => c => a + b + c;` but someone calls `f(1,2,3)` and gets unexpected behavior. Explain why and how to make the function tolerant of multi-arg calls.

*Hint:* Wrap curried function in a helper that accepts multi-args and distributes them into the curried chain.

---

## Quick checklist when using these patterns
- Favor clear argument order: put frequently fixed (config) args first for easy partial application.  
- Keep curried single-arg functions pure and side-effect free for easy composition.  
- Don’t curry everything — overuse can harm readability.  
- Measure if performance matters; microbenchmarks can detect overhead in hot paths.

---

## Further reading (selected)
- “Currying” — JavaScript Info.  
- DigitalOcean tutorial on Partial Application and Currying.  
- StackOverflow discussion: difference between currying and partial application.  
- GeeksforGeeks article: Currying vs Partial Application (examples).  
- NamasteDev blog: JS currying and partial application explained.

---

## Snippets for copy-paste

**Curry**
```js
function curry(fn, arity = fn.length) {
  return function curried(...args) {
    if (args.length >= arity) return fn.apply(this, args);
    return function (...next) {
      return curried.apply(this, args.concat(next));
    };
  };
}
```

**Partial**
```js
function partial(fn, ...preset) {
  return function (...later) {
    return fn.apply(this, [...preset, ...later]);
  };
}
```

---

## License
This cheat sheet is provided as-is for interview prep and learning.

# Advanced Concepts – JavaScript Design Patterns  
## Topic: Design Patterns  
## Sub Topic: Singleton, Factory, Observer, Module, Proxy

---

## 1. Singleton Pattern  
The Singleton pattern ensures that only one instance of a particular object exists throughout the application.  
In JavaScript, modules naturally enforce singletons because imports are cached.

### Key Ideas  
A singleton keeps a single shared state. You use it when you want a single source of truth—like a global configuration, cache, or database connection manager.

### Example  
```js
class Settings {
  constructor() {
    if (Settings.instance) return Settings.instance;
    this.mode = "dark";
    Settings.instance = this;
  }
}
const s1 = new Settings();
const s2 = new Settings();
console.log(s1 === s2); // true
```

---

## 2. Factory Pattern  
A Factory abstracts object creation. Instead of manually instantiating many types of objects, a factory decides which object to create.

### Example  
```js
class Dog {
  speak() { return "Woof"; }
}
class Cat {
  speak() { return "Meow"; }
}

function animalFactory(type) {
  if (type === "dog") return new Dog();
  if (type === "cat") return new Cat();
}
const pet = animalFactory("dog");
console.log(pet.speak());
```

---

## 3. Observer Pattern  
In this pattern, an object ("subject") maintains a list of observers and notifies them when its state changes.  
This is what powers event systems, reactive libraries, and state management.

### Example  
```js
class Subject {
  constructor() { this.observers = []; }
  subscribe(fn) { this.observers.push(fn); }
  notify(data) { this.observers.forEach(fn => fn(data)); }
}

const sub = new Subject();
sub.subscribe(msg => console.log("Observer:", msg));
sub.notify("Data updated!");
```

---

## 4. Module Pattern  
The Module pattern provides encapsulation—private variables and public APIs.  
IIFE (Immediately Invoked Function Expressions) were the classic way before ES Modules.

### Example  
```js
const Counter = (() => {
  let count = 0;
  return {
    increment() { count++; },
    getCount() { return count; }
  };
})();
Counter.increment();
console.log(Counter.getCount());
```

---

## 5. Proxy Pattern  
Proxy wraps an object to intercept operations like reading, writing, or invoking functions.  
Used today for validations, logging, access control, and frameworks like Vue 3 reactivity.

### Example  
```js
const user = { name: "Alice", age: 25 };

const proxy = new Proxy(user, {
  set(target, key, value) {
    if (key === "age" && value < 0) throw new Error("Invalid age");
    target[key] = value;
    return true;
  }
});
proxy.age = 30; // works
```

---

# Interview Questions + Concise Answers

### Singleton  
Q: How does JavaScript naturally support Singleton behavior?  
A: Module imports are cached; repeated imports return the same instance.

Q: When should you avoid Singletons?  
A: When global state causes testing issues or hidden dependencies.

### Factory  
Q: Why use a Factory instead of `new`?  
A: It centralizes object creation logic and supports polymorphism.

### Observer  
Q: Where is Observer used in JS?  
A: Event listeners, RxJS, Node EventEmitter, browser events.

### Module  
Q: Difference between Module pattern vs ES Modules?  
A: Module pattern uses closures; ES Modules rely on file-based module system.

### Proxy  
Q: Practical use cases of Proxy?  
A: Validations, logging, dynamic APIs, reactive frameworks.

---

# Coding Questions

### 1. Implement a Singleton Logger  
```js
class Logger {
  constructor() {
    if (Logger.instance) return Logger.instance;
    this.logs = [];
    Logger.instance = this;
  }
  log(msg) { this.logs.push(msg); }
}
```

### 2. Build a Factory for Shape Objects  
```js
function shapeFactory(type) {
  const shapes = {
    square: () => ({ area: s => s * s }),
    circle: () => ({ area: r => Math.PI * r * r })
  };
  return shapes[type]?.();
}
```

### 3. Implement an Event Bus (Observer)  
```js
class EventBus {
  constructor() { this.events = {}; }
  on(e, fn) { (this.events[e] ||= []).push(fn); }
  emit(e, data) { (this.events[e] || []).forEach(fn => fn(data)); }
}
```

### 4. Create a Module for User Auth  
```js
const Auth = (() => {
  let token = null;
  return {
    login(t) { token = t; },
    getToken() { return token; }
  };
})();
```

### 5. Use Proxy for Input Validation  
```js
function validator(obj) {
  return new Proxy(obj, {
    set(target, key, value) {
      if (key === "price" && value < 0) throw new Error("Invalid price");
      target[key] = value;
      return true;
    }
  });
}
```

---

This cheat‑sheet blends conceptual depth with ready‑to‑use snippets. Expanding into structural patterns like Adapter or Decorator deepens mastery even more.  


# Advanced Concepts – Proxy & Reflect (JavaScript)

## Topic: Proxy & Reflect  
### Subtopic: Intercepting Operations, Meta-Programming, Traps

---

## 1. Detailed Explanation

### What are Proxy and Reflect?
A Proxy in JavaScript wraps a target object and intercepts fundamental operations such as property access, assignment, deletion, and function invocation. The Reflect API provides a set of methods that mirror these internal object operations, making it ideal for forwarding default behavior inside proxy traps.

### Common Traps in Proxy
- **get(target, prop, receiver)** – intercepts property reads  
- **set(target, prop, value, receiver)** – intercepts property writes  
- **has(target, prop)** – intercepts `prop in obj`  
- **deleteProperty(target, prop)** – intercepts `delete obj[prop]`  
- **apply(target, thisArg, argsList)** – intercepts function calls  
- **construct(target, argsList, newTarget)** – intercepts constructor calls  
- **ownKeys(target)** – intercepts enumeration & listing operations  

Using these traps, you can instrument, validate, virtualize, or entirely reshape object behavior at runtime.

### Why Reflect?
Reflect provides default behavior implementations like `Reflect.get`, `Reflect.set`, `Reflect.apply`, and `Reflect.construct`. Using Reflect ensures that prototype inheritance, receivers, and built‑in invariants remain correct.

### Invariants
Proxies must respect JavaScript engine invariants:
- Non-configurable properties must stay non-configurable.
- You cannot fake properties that violate target’s object shape guarantees.
- Non-extensible objects cannot be extended.

Failing invariants results in a `TypeError`.

---

## 2. Theory-Based Interview Questions (Concise Answers)

**Q1: What is a Proxy in JavaScript?**  
A Proxy wraps a target object and intercepts low-level operations using handler traps.

**Q2: What does Reflect do?**  
Reflect exposes low-level object manipulation methods used to forward the default behavior in proxy traps.

**Q3: Why use Reflect inside proxy traps?**  
It preserves default semantics such as inherited getters, correct `this` binding, and avoids violating invariants.

**Q4: What are invariants in Proxy?**  
Language rules that proxies must not break, such as respecting non-configurable and non-extensible properties.

**Q5: What is the apply trap?**  
A trap that intercepts function calls on a proxied function.

**Q6: What is the construct trap?**  
A trap that intercepts usage of `new` on a proxied constructor.

---

## 3. Coding-Based Questions

### Q1: Logging Proxy
Intercept `get` and `set` to log operations; forward using `Reflect.get` and `Reflect.set`.

### Q2: Prevent Deletion of Private Properties
Block deletion if property starts with `_` via the `deleteProperty` trap.

### Q3: Negative Index Array
Implement negative indexing in the `get` trap.

### Q4: Validator Proxy
Use `set` trap to validate data types based on a schema.

### Q5: Constructor Logger
Wrap a class in a `construct` trap to log construction calls.

### Q6: Revocable Proxy
Use `Proxy.revocable(target, handler)` and demonstrate revocation.

---

## 4. End of Document


# Topic : Advanced Concepts
# Sub Topic : Deep Clone & Equality (structuredClone, JSON limitations, recursion) — JAVASCRIPT

## Overview
Deep cloning creates a copy of a value where nested references are duplicated (not shared). Deep equality checks whether two values are structurally identical (same types, same nested values) rather than the same reference.

This cheat-sheet covers:
- `structuredClone()` (modern native deep clone)
- `JSON.parse(JSON.stringify(...))` (fast but lossy)
- Library-based clones (`_.cloneDeep`, `fast-deep-equal`, `fast-json-stable-stringify`, etc.)
- Custom recursive cloning and deep equality implementations
- Common pitfalls: prototypes, functions, circular references, Dates, Maps/Sets, RegExp, TypedArrays, DOM nodes, errors, and Transferables
- Interview Qs + concise answers and coding questions

---

## 1) Methods to deep-clone (with brief pros/cons)

### 1.1 structuredClone(value)
```js
const copy = structuredClone(original);
```
- Native API implementing the **structured clone algorithm** (used by `postMessage`, `IndexedDB`), supports many built-in types and circular references. Throws on non-cloneable values like functions or some platform-specific objects. Prototypes are not preserved: class instances become plain objects. citeturn0search0turn0search6

### 1.2 JSON.parse(JSON.stringify(obj))
```js
const copy = JSON.parse(JSON.stringify(original));
```
- Very simple and fast for plain data (numbers, strings, booleans, plain objects/arrays). **Lossy**: `undefined`, `functions`, `Symbol`, `BigInt` are lost or throw; `Date` becomes ISO string; `Map`, `Set`, `RegExp`, typed arrays, and circular refs fail. Use only for simple POJOs. MDN notes recommend `structuredClone()` instead when available. citeturn0search1turn0search9

### 1.3 Library-based (e.g., lodash.cloneDeep)
```js
import cloneDeep from 'lodash/cloneDeep';
const copy = cloneDeep(original);
```
- Mature, handles many cases and edge-cases. Adds dependency/bundle size. Behavior depends on implementation details. Useful when you need predictable support across environments. citeturn0search10

### 1.4 Custom recursive clone (with visited map)
- Implement recursion + Map to handle circular refs and preserve identity of repeated references.
- You can special-case known types (`Date`, `RegExp`, `Map`, `Set`, typed arrays) and preserve prototypes if needed by using `Object.create(Object.getPrototypeOf(obj))` and copying properties.

### 1.5 Transferable or serializer alternatives
- In Node.js, you can use `v8.serialize()` / `v8.deserialize()` for binary serialization supporting circular refs (Node-only).
- For IPC/workers, `structuredClone` or `postMessage` with Transferables is common. citeturn0search6turn0search9

---

## 2) What structuredClone supports / doesn't
- Supports: Plain objects, arrays, `Date`, `RegExp`, `Map`, `Set`, `ArrayBuffer`, typed arrays, `Blob`, `File`, `ImageBitmap`, `URL` objects in many engines, and circular references. citeturn0search0turn0search6
- Does NOT support: Functions (throws `DataCloneError`), DOM nodes, some platform-specific objects, and it **does not preserve prototypes** (instances become plain objects). If you need preservation of prototypes or methods, use a custom approach (or reconstruct instances after cloning). citeturn0search3

---

## 3) Deep equality (isEqual) — approaches

### 3.1 Shallow vs deep equality
- `===` tests identity (same reference for objects). For deep structural equality you must compare contents recursively.

### 3.2 Libraries
- `_.isEqual(a,b)` (Lodash): full-featured deep comparison for many JS types.
- `fast-deep-equal`: small & very fast deep equality implementation (common in diff/patch code).
Use libraries unless you have a strict need to implement your own. citeturn0search13turn0search19

### 3.3 Custom deep equality
- Typical algorithm: type check -> primitive compare -> arrays (length + element-wise) -> objects (key-set compare + recursive compare) -> special-case `Date`, `RegExp`, `Map`, `Set`, typed arrays, and use a WeakMap to handle cycles / repeated references.

---

## 4) Pitfalls & gotchas
- **Prototypes lost** with `structuredClone()` and `JSON` approach — class instances become plain objects.
- **Functions** and **Symbols** not preserved in JSON; functions throw in structured clone.
- **Circular references** break `JSON` but are supported by `structuredClone` and v8 serialization.
- **Dates** become strings with JSON. Use `new Date(...)` when reconstructing.
- **Maps/Sets**: JSON loses them; structuredClone preserves them.
- **RegExp**: JSON loses them; structuredClone preserves them.
- **Performance**: `JSON.parse(JSON.stringify)` can be fastest for very simple structures; benchmarks vary — for complex objects structuredClone or specialized libraries may be better. Test in your environment. citeturn0search1turn0search16

---

## 5) Performance tips
- Avoid deep cloning large objects frequently — prefer immutable structural updates (e.g., create new small objects), or libraries that do structural sharing.
- Benchmark in your target environment: Node vs browser JS engines differ.
- Prefer `structuredClone()` on modern runtimes for correctness and often good performance. For tiny shallow copies, use spread `{ ...obj }` or `Array.prototype.slice()` for arrays.

---

## 6) Quick reference code snippets

### 6.1 Safe structured clone with fallback
```js
function deepClone(value) {
  if (typeof structuredClone === 'function') {
    return structuredClone(value);
  }
  // fallback: careful - JSON loses many types
  return JSON.parse(JSON.stringify(value));
}
```

### 6.2 Custom recursive clone (handles Date, RegExp, Map, Set, circular refs, preserves prototypes)
```js
function cloneDeepCustom(val, seen = new Map()) {
  if (val === null || typeof val !== 'object') return val;
  if (seen.has(val)) return seen.get(val);

  // Date
  if (val instanceof Date) return new Date(val.getTime());
  // RegExp
  if (val instanceof RegExp) return new RegExp(val.source, val.flags);
  // Map
  if (val instanceof Map) {
    const m = new Map();
    seen.set(val, m);
    for (const [k, v] of val) m.set(cloneDeepCustom(k, seen), cloneDeepCustom(v, seen));
    return m;
  }
  // Set
  if (val instanceof Set) {
    const s = new Set();
    seen.set(val, s);
    for (const v of val) s.add(cloneDeepCustom(v, seen));
    return s;
  }
  // Typed arrays and ArrayBuffer
  if (ArrayBuffer.isView(val)) return val.slice();
  if (val instanceof ArrayBuffer) return val.slice(0);

  // Generic object/array: preserve prototype
  const out = Array.isArray(val) ? [] : Object.create(Object.getPrototypeOf(val));
  seen.set(val, out);
  for (const key of Reflect.ownKeys(val)) {
    out[key] = cloneDeepCustom(val[key], seen);
  }
  return out;
}
```

### 6.3 Simple deep-equal (conceptual)
```js
function deepEqual(a, b, seen = new WeakMap()) {
  if (a === b) return true;
  if (a && b && typeof a === 'object' && typeof b === 'object') {
    if (seen.has(a)) return seen.get(a) === b;
    seen.set(a, b);
    // compare prototypes
    if (Object.getPrototypeOf(a) !== Object.getPrototypeOf(b)) return false;
    // arrays
    if (Array.isArray(a)) {
      if (!Array.isArray(b) || a.length !== b.length) return false;
      for (let i = 0; i < a.length; i++) if (!deepEqual(a[i], b[i], seen)) return false;
      return true;
    }
    // maps
    if (a instanceof Map) {
      if (!(b instanceof Map) || a.size !== b.size) return false;
      for (const [k, v] of a) if (!deepEqual(v, b.get(k), seen)) return false;
      return true;
    }
    // sets
    if (a instanceof Set) {
      if (!(b instanceof Set) || a.size !== b.size) return false;
      for (const v of a) if (!b.has(v)) return false;
      return true;
    }
    const ka = Reflect.ownKeys(a), kb = Reflect.ownKeys(b);
    if (ka.length !== kb.length) return false;
    for (const k of ka) if (!kb.includes(k) || !deepEqual(a[k], b[k], seen)) return false;
    return true;
  }
  // fallback for NaN
  return Number.isNaN(a) && Number.isNaN(b);
}
```

---

## 7) Interview-style theory questions (concise answers)

**Q1: What's the difference between shallow and deep copy?**  
A: Shallow copy copies top-level properties; nested objects remain referenced. Deep copy duplicates nested structures so changes to clone don't affect original.

**Q2: Why is `JSON.parse(JSON.stringify(obj))` not always safe for deep cloning?**  
A: It's lossy: loses `undefined`, functions, `Symbol`, `BigInt`; converts `Date` to string; fails on circular refs; loses `Map`/`Set`/RegExp/TypedArrays. Use structuredClone or libraries for robust cloning. citeturn0search1turn0search9

**Q3: What does `structuredClone()` do with class instances?**  
A: It clones the object's own properties but **does not preserve the prototype**, so instances become plain objects. Functions inside objects cause a `DataCloneError`. citeturn0search0turn0search3

**Q4: How to handle circular references when cloning?**  
A: Use a `Map`/`WeakMap` to track visited objects and reuse the cloned reference when a cycle is encountered. `structuredClone` handles cycles natively. citeturn0search6

**Q5: When should you prefer deep equality libraries over custom code?**  
A: Prefer libraries (lodash/isEqual or fast-deep-equal) for correctness and performance unless you need a tailored comparison; they handle many corner cases and are battle-tested. citeturn0search13turn0search19

---

## 8) Interview-style coding questions (practice)

1. **Implement `deepClone` that handles circular refs and Dates/RegExp/Map/Set.**  
   - Expectation: use recursion + `Map` to track visited nodes. (See `cloneDeepCustom` above.)

2. **Implement `deepEqual(a,b)` that compares objects including Maps and Sets.**  
   - Expectation: handle prototypes, typed arrays, and cycles via `WeakMap`. (See `deepEqual` above.)

3. **Given an object with methods (class instances), clone it while preserving prototype.**  
   - Approach: create an object with the same prototype (`Object.create(Object.getPrototypeOf(obj))`) and copy properties; for methods that reference private state you may need a custom serializer or factory method.

4. **Benchmark structuredClone vs JSON.parse/stringify vs lodash.cloneDeep**  
   - Approach: create large nested structures (with Maps/Sets/Date) and measure `performance.now()` in browser or `process.hrtime.bigint()` in Node.

---

## 9) Quick summary / rules of thumb
- Use `structuredClone()` when available for correctness and to handle circular references. citeturn0search0turn0search6  
- Use `JSON.parse(JSON.stringify())` only for simple POJOs with primitive values and when performance for simple cases matters. citeturn0search1  
- Use battle-tested libraries (`lodash.cloneDeep`, `fast-deep-equal`) when you need cross-platform consistency, or implement custom clones when you must preserve prototypes or functions. citeturn0search10turn0search19

---

## 10) References
- MDN: `structuredClone()` and Structured Clone Algorithm.  
- MDN: `JSON.stringify()` notes and limitations.  
- Lodash docs and `fast-deep-equal` benchmarks and comparisons.

---

*Generated for interview prep — save this file, run the snippets locally, and benchmark in your runtime (browser vs Node).*

# Advanced Concepts: Destructuring & Rest/Spread (JavaScript)

## Topic
Destructuring & Rest/Spread

## Sub Topic
Usage patterns, edge cases

---

## Overview

Destructuring extracts values from arrays or properties from objects into distinct variables. The rest (`...`) and spread (`...`) syntaxes are visually identical but opposite in purpose: **rest** collects remaining items into a single array/object; **spread** expands elements or properties into lists or new objects. This summary covers common usage patterns, advanced examples, and tricky edge cases with practical guidance.

Key references: MDN Destructuring and Spread docs, TC39 object rest/spread proposal, and resources on rest parameters / spread syntax.  
(See official docs cited in the companion chat response.)

---

## Basic array destructuring

```js
const arr = [1, 2, 3, 4];
const [a, b, ...rest] = arr; // a=1, b=2, rest=[3,4]
```

### Use cases
- Pull leading values and keep the remainder.
- Swap variables: `[x, y] = [y, x]`.
- Skip elements: `const [, second] = arr;`

---

## Basic object destructuring & rest

```js
const user = { id: 1, name: 'A', role: 'admin' };
const { name, ...meta } = user; // name='A', meta={ id:1, role:'admin' }
```

### Notes
- Object rest collects **own enumerable properties** not yet picked by destructuring.
- Rest order is not guaranteed and should not be relied upon for ordering concerns.

---

## Default values & renaming

```js
const { foo = 42, bar: alias = 'x' } = maybeMissing;
// foo gets default 42 if missing; bar is renamed to alias
```

---

## Nested destructuring and safe defaults

When destructuring nested objects that may be `undefined` or `null`, provide defaults at intermediate levels:

```js
const obj = { a: null };
const { a: { b } = {} } = obj; // avoids TypeError; b === undefined
```

If `a` might be `null`, the `= {}` default prevents matching against `undefined`/`null`.

---

## Function parameters: rest and destructuring

```js
function join(separator, ...items) {
  return items.join(separator);
}

function greet({name = 'stranger', age} = {}) {
  console.log(name, age);
}
```

- Rest parameters must be the last parameter. Certain rest patterns are syntax errors (e.g., `function f(...x, y) {}`).
- You can destructure a rest parameter: `function f(...[first, ...rest]) {}` but it's rarely useful.

---

## Spread in arrays and objects

```js
const a = [1, ...[2,3], 4]; // [1,2,3,4]
const o = { x:1, ...other }; // shallow copy + merged props
```

- Object spread creates new own properties and does not invoke setters in the same way `Object.assign` might. (See differences below.) citeturn0search1turn0search3

---

## Edge cases & gotchas

### 1. Order and property enumeration
Object rest/spread operate on own enumerable properties; property order is not something to rely upon for logic. Use arrays when order matters. citeturn0search3

### 2. Nested missing values
Destructuring nested properties without defaults can throw `TypeError` if an intermediate value is `undefined` or `null`. Provide defaults at intermediate levels: `{ a: { b } = {} }`.

### 3. Rest with computed property keys
You cannot directly rest away computed keys in a single destructuring pattern — pick known keys and collect the rest.

### 4. Rest parameters vs arguments object
Rest parameters produce a real array; `arguments` is array-like. Prefer rest parameters in modern code for clarity. citeturn0search6

### 5. Spread vs Object.assign differences
Spread defines properties on the new object and does not trigger setters on the target like `Object.assign` does; there are subtle differences when targets have setters or prototypes. Benchmarks also show small performance differences depending on engine/version—measure for hot paths. citeturn0search2turn0search5

---

## Performance guidance
- For most code, readability and immutability are more important than microbenchmarks.
- For hot loops, `Object.assign` or manual property copying might be marginally faster in some engines; always profile in your environment. citeturn0search5

---

## Common anti-patterns
- Deep destructuring of huge objects for single property access (use a direct property or helper).
- Overusing rest/spread in performance-critical loops without profiling.
- Assuming spread creates deep clones (it is shallow).

---

## Interview-style theory questions (concise answers)

1. **What is the difference between rest and spread?**  
   Rest collects remaining elements/properties into a single array/object; spread expands an iterable or object properties into a literal or function arguments. citeturn0search1

2. **How do defaults work in destructuring?**  
   If the matched value is `undefined`, the default expression is used. For nested destructuring, supply defaults at intermediate levels to avoid `TypeError`. citeturn0search0

3. **Does `...` in object literals produce a deep clone?**  
   No — object spread creates a shallow copy of own enumerable properties. For deep clones use structuredClone or a recursive strategy. citeturn0search3

4. **When is rest in function parameters disallowed?**  
   Rest must be the last parameter and cannot be combined with other parameter patterns after it; certain rest-target destructurings are syntax errors. citeturn0search6

5. **Object spread vs `Object.assign`: key practical differences?**  
   Spread defines properties on a fresh object (doesn't invoke setters on the target) while `Object.assign` sets properties on an existing target and may trigger setters. Also subtle performance differences exist. citeturn0search2turn0search3

---

## Interview-style coding questions (with hints/solutions)

1. **Swap two variables without a temporary variable using destructuring.**  
   `let a = 1, b = 2; [a, b] = [b, a];`

2. **Implement a function `omit(obj, keys)` that returns a shallow copy of `obj` without the listed keys.**  
   Hint: use destructuring rest or Object.keys + reduce.

```js
function omit(obj, keys = []) {
  const result = { ...obj };
  for (const k of keys) delete result[k];
  return result;
}
```

3. **Deep pick with safe defaults:** Given `user`, safely destructure `user.profile.name` with fallback `'Anon'`.  
```js
const { profile: { name = 'Anon' } = {} } = user || {};
```

4. **Collect remaining args except the first two:**  
```js
function f(a, b, ...rest) { /* rest holds remaining args */ }
```

5. **Merge multiple objects immutably and override properties:**  
```js
const merged = { ...defaults, ...options, extra: true };
```

---

## Quick cheatsheet (snippets)

- Array: `const [first, ...rest] = arr;`
- Object: `const {a, b, ...others} = obj;`
- Function: `function f(a, b, ...rest) {}`
- Spread in call: `Math.max(...arr)`
- Rename: `const { oldName: newName } = obj`
- Default: `const { a = 1 } = opts`

---

## Further reading
- MDN Destructuring & Spread docs (recommended).  
- TC39 proposal history for object rest/spread.  
- Benchmarks and engine-specific notes before optimizing.

---

## Notes
This file focuses on ES2015+ features (ES6 and later). For deep cloning and advanced immutability patterns consider `structuredClone`, `immer`, or utility libraries depending on constraints.

---

# Topic : Optional Chaining & Nullish Coalescing

## Sub Topic : practical use, short-circuiting

---

### Quick summary
Optional chaining (`?.`) lets you safely access deeply nested properties (or call functions) without throwing if an intermediate value is `null` or `undefined`. Nullish coalescing (`??`) provides a default _only_ when the left-hand side is `null` or `undefined` (not for other falsy values like `0`, `""`, or `false`). Together they make defensive code concise and intention-revealing.

---

## 1. Syntax and simple examples
```js
// Optional chaining
const name = user?.profile?.name; // undefined if user or profile is null/undefined

// Optional call (safe function call)
const result = maybeFn?.(arg1, arg2);

// Optional index access
const thirdItem = arr?.[2];

// Nullish coalescing
const count = userInput ?? 10; // use 10 only when userInput is null or undefined
```

### Combined pattern
```js
const username = response?.data?.user?.name ?? 'anonymous';
```
This reads as: try to get the name; if any link in the chain is missing produce `undefined`; if the final result is `null`/`undefined`, fall back to `'anonymous'`.

---

## 2. Practical use cases
- Reading API responses that may omit fields.
- Accessing DOM-like nested structures safely in SSR/hydrated code.
- Calling optional callbacks: `onClick?.()` instead of `if (onClick) onClick()`.
- Providing defaults for possibly-missing numeric inputs where `0` is meaningful: `value ?? 0` (important: `||` would incorrectly treat `0` as missing).

---

## 3. Short-circuiting behavior details
- `?.` short-circuits when the value to the left is `null` or `undefined` — the expression yields `undefined` (or, in the case of calls, yields `undefined` without calling).
- `??` evaluates left-to-right and returns the right operand only if the left is `null` or `undefined`. It does not coerce other falsy values.

Important interaction rule: `??` has lower precedence than most operators but higher than `||`? Practically, avoid mixing `||` and `??` without parentheses. Example:
```js
// BAD: syntax error when mixing without parentheses in many contexts
let a = foo ?? bar || baz; // ambiguous — use parentheses to be explicit

// Better
let a = (foo ?? bar) || baz;
```

---

## 4. Common pitfalls & gotchas
- Using `||` when you need `??`: `0 || 10` => `10`, but `0 ?? 10` => `0`. Use `??` when `0`, `false`, or `''` are valid values.
- Optional chaining only checks for `null`/`undefined`. If a property is present but set to `false`, `0`, or `''`, `?.` will not short-circuit.
- Don't overuse optional chaining to mask bugs — if a value should exist, prefer earlier validation or explicit errors.
- Optional chaining with function calls: `obj?.fn()` will not call `fn` if `obj` is `null`/`undefined`, but will still throw if `fn` exists but is not callable.

---

## 5. Readability & style guidance
- Use `?.` at boundaries where you're dealing with external/untrusted data (API results, user-generated shapes).
- Prefer explicit defaults with `??` so intention is clear (you expect `0`/`false` to be valid values).
- Avoid deeply chaining dozens of `?.` — if your data shape is that uncertain, consider a validator or normalizer.

---

## 6. Small examples (realistic)
```js
// Example: settings with fallbacks
const fontSize = userConfig?.theme?.fontSize ?? systemDefaults.fontSize ?? 14;

// Example: optional callback
function submit(data, onDone) {
  // only call if provided
  onDone?.(null, data);
}

// Example: safe nested access with transformation
const firstEmail = (user?.contacts?.emails ?? [])[0] ?? 'no-email@example.com';
```

---

## 7. Interview theory questions (concise answers)
1. **What does optional chaining do?**
   - Safely accesses properties/calls without throwing when an intermediate value is `null`/`undefined`.

2. **When does `??` return the right-hand operand?**
   - Only when the left-hand operand is `null` or `undefined`.

3. **How is `??` different from `||`?**
   - `||` treats all falsy values (`0`, `''`, `false`) as missing; `??` only treats `null` and `undefined` as missing.

4. **Can you chain optional calls and properties?**
   - Yes: `a?.b?.[c]?.()` is allowed (where each step may be `null`/`undefined`).

5. **Does `obj?.fn()` protect you if `obj.fn` is not a function?**
   - No. It only avoids calling if `obj` is `null`/`undefined`. If `obj.fn` exists but isn't callable, it still throws.

6. **Are there performance penalties?**
   - Negligible in normal use; the clarity and safety gains usually outweigh microbenchmarks. If used inside hot loops, consider caching the value.

7. **When should you not use optional chaining?**
   - When missing properties indicate programming errors you want surfaced, or when silent `undefined`s hide bugs.

8. **How to mix `?.` with `&&`/`||`/`??` safely?**
   - Be explicit with parentheses and prefer `??` for defaults. Example: `(obj?.count ?? 0) > 0`.

---

## 8. Related coding / interview exercises (with brief solutions)

### Q1 — Safe property read
**Task:** Given `obj`, return `obj.a.b.c` safely or `null`.
```js
function safeRead(obj) {
  return obj?.a?.b?.c ?? null;
}
```

### Q2 — Default for possibly-zero number
**Task:** Normalize input where `0` is meaningful; default to `5` only when `null`/`undefined`.
```js
function normalize(x) {
  return x ?? 5;
}
```

### Q3 — Optional callback chaining
**Task:** Accept optional `onSuccess` and `onError` callbacks and call safely.
```js
function run(task, onSuccess, onError) {
  try {
    const res = task();
    onSuccess?.(res);
  } catch (err) {
    onError?.(err);
  }
}
```

### Q4 — Transform API shape
**Task:** Extract `street` from `resp.user.address` and default to `"—"`.
```js
const street = resp?.user?.address?.street ?? '—';
```

---

## 9. Checklist for using in production
- Add runtime tests for cases where values are `null`, `undefined`, empty string, zero, and `false`.
- Avoid using optional chaining to silence programming errors — use it for untrusted external data.
- Add lint rules or code review guidance (e.g., prefer `??` over `||` for defaults) where useful.

---

## 10. Further reading (keywords)
- `Optional chaining`, `Nullish coalescing`, `ES2020`, `safe navigation operator`, `defensive programming`.


*End of cheat sheet.*

# WeakMap & WeakSet — Advanced JavaScript Cheat Sheet

## Topic: WeakMap & WeakSet  
## Sub Topic: Memory-Sensitive Data Structures

---

## 1. Detailed Explanation

### WeakMap
WeakMap is a specialized map where keys must be **objects**, and those objects are held **weakly**.  
Weakly held means: if no other references exist to that object, the garbage collector is free to delete it—even if it's still present as a key in the WeakMap.  

This makes WeakMap ideal for **ephemeral metadata**, caching, and attaching hidden data to objects without causing memory leaks.

Key properties:  
- Keys must be **objects only** (no primitive keys)  
- Keys are garbage-collectable  
- Not iterable (for safety: if keys disappear, iteration becomes undefined)  
- Supports: `get`, `set`, `has`, `delete`

A conceptual analogy: attaching secret sticky notes to objects that vanish automatically if the object disappears.

### WeakSet
WeakSet is the weakly referenced version of Set.  
It stores **objects only**, and they are also weakly held.

Characteristics:  
- Only objects allowed  
- Not iterable  
- Ideal for marking objects (e.g., marking visited nodes)  
- Supports: `add`, `has`, `delete`

Think of it as a shadow‑registry of objects—silent, temporary, self‑cleaning.

---

## 2. When to Use Them

### Good use cases:
- Caching computed results based on object identity  
- Keeping private, internal metadata  
- Tracking object presence without preventing garbage collection  
- Avoiding memory leaks when associating data with DOM nodes

### Avoid them when:
- You need enumerability  
- Keys must be primitives  
- You need stable, permanent data storage

---

## 3. Example Usage

### WeakMap Example: Caching
```js
const cache = new WeakMap();

function process(obj) {
  if (cache.has(obj)) return cache.get(obj);

  const result = expensiveComputation(obj);
  cache.set(obj, result);

  return result;
}
```

### WeakSet Example: Marking visited objects
```js
const visited = new WeakSet();

function traverse(node) {
  if (visited.has(node)) return;
  visited.add(node);

  for (const child of node.children) {
    traverse(child);
  }
}
```

---

## 4. Interview Theory Questions (With Short Answers)

**Q1. Why are WeakMaps not iterable?**  
A1. Keys are garbage‑collectable at any moment, so iteration would produce inconsistent and unpredictable results.

**Q2. Why do WeakMap/WeakSet only allow objects as keys?**  
A2. Primitive values cannot be garbage‑collected based on reachability rules, defeating the purpose of “weak” referencing.

**Q3. What problem does WeakMap solve that regular Map might cause?**  
A3. Memory leaks caused by retaining references to objects that should otherwise be eligible for garbage collection.

**Q4. Can you inspect the size of a WeakMap?**  
A4. No, because entries may disappear at any moment, so `size` is not exposed.

**Q5. When should you prefer WeakSet over Set?**  
A5. When you only want to track objects and avoid preventing their garbage collection.

---

## 5. Coding Questions for Practice

**Coding Question 1:**  
Implement a `memoizeObject` function that memoizes results only for object arguments using a WeakMap.

**Coding Question 2:**  
Given a tree-like object structure, use WeakSet to detect cycles.

**Coding Question 3:**  
Build a hidden-property system using WeakMap to store private fields of objects.

Example:
```js
const _private = new WeakMap();

class Person {
  constructor(name, age) {
    _private.set(this, { name, age });
  }

  getName() {
    return _private.get(this).name;
  }
}
```

---

## 6. Summary
WeakMap and WeakSet are the quiet custodians of JavaScript memory management. They give you the ability to attach “invisible” data to objects without accidentally pinning them in memory. Use them when you want data that lives only as long as the objects they’re tied to.

---

# Event Loop Optimization (Advanced Concepts)
Topic: Event Loop Optimization  
Sub Topic: microtasks, macrotasks, requestIdleCallback

## 1. Event Loop Overview
The JavaScript event loop decides *when* code runs. It handles:
- **Macrotasks**: setTimeout, setInterval, DOM events, network callbacks.
- **Microtasks**: Promise callbacks, queueMicrotask, MutationObserver.

Execution order per cycle:
1. Run current macrotask  
2. Run *all* microtasks  
3. Render UI  
4. Move to next macrotask  

## 2. Microtasks
Microtasks run before rendering and have higher priority.  
Used for tiny follow-up logic:

```js
queueMicrotask(() => {
  console.log("Runs before next macrotask");
});
```

Be careful: too many microtasks = UI freeze.

## 3. Macrotasks
Scheduled after current event loop turn:

```js
setTimeout(() => {
  console.log("Next loop turn");
}, 0);
```

Good for yielding control back to the browser.

## 4. requestIdleCallback
Used for low-priority, non‑urgent tasks:

```js
requestIdleCallback(deadline => {
  while (deadline.timeRemaining() > 0 && tasks.length) {
    process(tasks.shift());
  }
});
```

Ideal for prefetching, analytics batching, cleanup.  
Fallback needed for browsers that don’t support it.

## 5. Optimization Techniques

### Break long tasks (Chunking)
```js
function processLargeList(list) {
  let i = 0;
  function run() {
    const end = Math.min(i + 500, list.length);
    while (i < end) doWork(list[i++]);

    if (i < list.length) setTimeout(run, 0);
  }
  run();
}
```

### Avoid microtask starvation
Promise-heavy loops block rendering:

```js
function bad() {
  Promise.resolve().then(bad);
}
```

### Use macrotask yields
Ensure browser can breathe:

```js
await new Promise(r => setTimeout(r, 0));
```

### Use requestIdleCallback for background tasks

### Move heavy CPU tasks to Web Workers

## 6. Interview Theory Questions (Concise Answers)

**Q1. Difference between microtasks & macrotasks?**  
Microtasks run before rendering and before next macrotask. Macrotasks run in the next event-loop cycle.

**Q2. Why can microtasks cause jank?**  
If many microtasks run continuously, rendering is blocked.

**Q3. When to use requestIdleCallback?**  
For low‑priority tasks that should not affect user interactions.

**Q4. How to prevent blocking UI in loops?**  
Chunk large work using setTimeout/requestAnimationFrame/requestIdleCallback.

**Q5. When to use Web Workers?**  
For CPU-heavy computations that would block the main thread.

## 7. Coding Questions

1. Implement chunked processing of big arrays.  
2. Implement a requestIdleCallback polyfill.  
3. Limit concurrency of Promises to N.  
4. Detect long tasks using PerformanceObserver.  
5. Build a scheduler mixing microtasks + macrotasks.

---

# Topic: ES6+ Features
## Sub Topic: Let & Const — scope handling, Temporal Dead Zone (TDZ)

### Quick summary
`let` and `const` were introduced in ES6 to provide block-scoped variable declarations and safer behavior than `var`. Both are bound to the block where they are declared and cannot be accessed before the declaration (they live in the *Temporal Dead Zone*). `let` allows reassignment; `const` prohibits reassigning the binding (but not mutation of objects).  

---

## Detailed explanation

### 1. Scope rules
- `var` has function or global scope; variables declared with `var` are hoisted and initialized to `undefined`.
- `let` and `const` are **block-scoped**: they exist only inside the nearest `{ ... }` block (if, for, function block, etc.). This avoids many accidental leaks to outer scopes.  
- `const` must be initialized at the time of declaration; `let` can be declared without initialization.  
*(Source: MDN docs on `let` and `const`.)* citeturn0search0turn0search4

### 2. Temporal Dead Zone (TDZ)
- TDZ describes the period between entering a scope and the actual declaration/initialization of a `let`/`const` variable.
- Although `let`/`const` are hoisted in the sense their names are known to the environment, they are **uninitialized** until execution reaches the declaration; accessing them before then throws a `ReferenceError`. This behavior helps catch bugs that would otherwise silently reference `undefined`.  
*(Good explainer and examples available from MDN and freeCodeCamp.)* citeturn0search2turn0search5

### 3. Hoisting nuances
- `var` is hoisted and initialized to `undefined`, so reading it before declaration yields `undefined`.
- `let`/`const` are hoisted but not initialized — you cannot read them before the declaration (TDZ). Some people describe this as "non-initialized hoisting" or simply "TDZ behavior." citeturn0search16

### 4. Re-declaration & reassignment rules
- `var`: can be re-declared and reassigned in the same scope.
- `let`: cannot be re-declared in the same scope but can be reassigned.
- `const`: cannot be re-declared or reassigned; for objects/arrays the *binding* is constant but the contents can be mutated (e.g., `const arr = []; arr.push(1)` is allowed).

### 5. Common patterns & best practices
- Prefer `const` by default. Use `let` only when you know the variable will be reassigned (loop counters, temporary accumulators).
- Avoid top-level `var`. Use `let`/`const` to reduce accidental global leakage.
- Declare variables as close as possible to their usage to minimize TDZ window and improve readability.
- For loops: `for (let i = 0; i < n; i++) { ... }` creates a fresh binding each iteration for closures (fixes classic closure-in-loop bug).  

---

## Examples (concise)

**TDZ example**
```js
{
  console.log(x); // ReferenceError (x is in TDZ)
  let x = 5;
}
```

**Block scope vs function/global scope**
```js
if (true) {
  let a = 1;
}
console.log(a); // ReferenceError: a is not defined
```

**const binding vs mutation**
```js
const obj = { a: 1 };
obj.a = 2;         // allowed (mutation)
obj = {};          // TypeError: Assignment to constant variable.
```

**Closure in loops (fixed by let)**
```js
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0); // prints 0,1,2
}
```

---

## Interview — theory questions (concise answers)

1. **What’s the Temporal Dead Zone?**  
   The TDZ is the time from entering a scope until a `let`/`const` variable is initialized; accessing it during this time throws a `ReferenceError`. citeturn0search2turn0search5

2. **Are `let` and `const` hoisted?**  
   They are hoisted in that the bindings are created before code runs, but they aren’t initialized — accessing them before declaration causes a `ReferenceError`. citeturn0search16

3. **When to use `const` vs `let`?**  
   Use `const` by default to signal immutability of the binding; use `let` only when you need to reassign the variable.

4. **Can `const` objects be mutated?**  
   Yes — `const` protects the binding, not the value. Objects and arrays declared with `const` can have their contents changed.

5. **Why did ES6 introduce block scoping?**  
   To reduce bugs from `var`’s function/global scoping and to make closures and loops behave more predictably.

---

## Interview — coding / practical questions

1. **Fix the bug:** Explain why this prints `3 3 3` and how to fix it.
```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```
*Answer:* `var` creates a single function-scoped `i`; by the time callbacks run, `i` is 3. Use `let` to create per-iteration bindings: `for (let i=0; i<3; i++) { ... }`.

2. **Detect TDZ error:** Given code, find why `ReferenceError` occurs.
```js
let x = 1;
{
  console.log(x); // ?
  let x = 2;
}
```
*Answer:* The inner `let x` creates a new `x` whose TDZ starts at block entry. The `console.log` tries to access inner `x` before initialization → ReferenceError.

3. **Immutable binding puzzle:** Implement a function that returns an array but prevents external mutation of its contents.
*Short solution:* return a shallow copy or freeze:
```js
function safe(arr) {
  return Object.freeze([...arr]);
}
```

4. **Closure capture challenge:** Create three functions in an array that return 0,1,2 respectively using a loop.
*Solution:* Use `let` or an IIFE:
```js
const fns = [];
for (let i=0;i<3;i++) fns.push(() => i);
```

---

## Pitfalls & gotchas
- Don’t assume `const` makes objects immutable.
- Beware TDZ when refactoring variable declarations — moving declarations can introduce ReferenceErrors.
- `let`/`const` and `var` cannot be mixed for the same identifier in overlapping scopes (re-declaration errors).

---

## Short checklist (for interviews / code reviews)
- Prefer `const` by default.
- Use `let` for reassignable locals.
- Avoid `var` unless maintaining legacy code.
- Keep declarations close to usage to reduce TDZ confusion.
- Use `let` in loops to avoid closure traps.

---

## References (primary)
- MDN — `let`. citeturn0search0  
- MDN — `const`. citeturn0search4  
- MDN — Hoisting & TDZ. citeturn0search2  
- freeCodeCamp — What is TDZ. citeturn0search5  
- StackOverflow — hoisting with let/const. citeturn0search16

# ES6+ Arrow Functions — Lexical `this` & Implicit Return

## Topic: ES6+ Features  
## Sub Topic: Arrow Functions — lexical `this`, implicit return

---

## 1. Detailed Explanation

### Arrow Functions  
Arrow functions are a more concise way to write functions in JavaScript.  
They do **not** bind their own `this`, `arguments`, `super`, or `new.target`.

### Lexical `this`  
Traditional functions decide `this` based on **how** they're called.  
Arrow functions decide `this` based on **where** they’re written.  
They *inherit* `this` from the surrounding (lexical) scope.

Example:
```js
function Counter() {
  this.count = 0;

  setInterval(() => {
    this.count++;   // Arrow fn uses `this` from Counter
    console.log(this.count);
  }, 1000);
}
new Counter();
```

A normal function would lose the `this` context unless manually bound.

### Implicit Return  
Arrow functions allow returning expressions without writing `return`, provided the function body is a single expression without `{ }`.

```js
const add = (a, b) => a + b; // implicit return
```

To return an object implicitly:
```js
const makeUser = (name) => ({ name });
```

---

## 2. Interview Theory Questions (Concise Answers)

### What is lexical `this` in arrow functions?
Arrow functions don’t create their own `this`; they capture it from the enclosing scope.

### Can arrow functions be used as constructors?
No, because they have no `[[Construct]]` method and no `new.target`.

### Do arrow functions have their own `arguments` object?
No, they use the outer function’s `arguments`.

### Difference between implicit and explicit return in arrow functions?
Implicit return returns the evaluated expression without `return`.  
Explicit return requires a block `{}` and a `return` statement.

### Should you use arrow functions in object methods?
Generally no, because arrow fns don’t bind their own `this`, so object method context breaks.

---

## 3. Coding-Based Questions

### Q1: Convert a regular function to arrow function while preserving `this`
```js
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    setTimeout(() => {
      console.log(`Hello, ${this.name}`);
    }, 500);
  }
}
```

### Q2: Write a function that filters even numbers using implicit return
```js
const evens = arr => arr.filter(n => n % 2 === 0);
```

### Q3: Fix the bug where `this` becomes undefined inside a callback
```js
function Logger() {
  this.logs = [];

  // Fix: use arrow function
  ['a', 'b', 'c'].forEach(item => this.logs.push(item));
}
```

---

# ES6+ Features: Template Literals (Interpolation & Tagged Templates)

## 1. Template Literals — Detailed Explanation

Template literals are a modern JavaScript syntax introduced in ES6 that use backticks (`` ` ``) instead of quotes. They allow multi‑line strings, string interpolation, and tagged templates for custom string processing.

### Interpolation
Interpolation means embedding values directly inside a string using `${expression}`.  
The expression can be variables, function calls, arithmetic, or even conditional logic.

**Example**
```js
const name = "Harshith";
const score = 42;
const msg = `Player ${name} has scored ${score} points`;
```

### Multi-line Strings
Template literals naturally support multi-line strings.

```js
const poem = `
Roses are red,
Violets are blue,
Template literals rock,
And so do you!
`;
```

### Expressions Inside Interpolation
```js
const price = 100;
const tax = 0.18;
const total = `Total: ₹${price + price * tax}`;
```

---

## 2. Tagged Templates

Tagged templates allow you to process a template literal with a function *before* JavaScript creates the final string.

The syntax looks like:
```js
tagFunction`template literal here`;
```

The function receives:
- Raw string segments as an array
- Each interpolated value as parameters

### Example: A Simple Tag
```js
function shout(strings, ...values) {
  return strings[0] + values.map(v => v.toUpperCase()).join("!");
}

const result = shout`hello ${"world"} and ${"javascript"}`;
```

### Example: Sanitizing Inputs (XSS Protection)
```js
function safe(strings, ...values) {
  const escape = str =>
    str.replace(/</g, "&lt;").replace(/>/g, "&gt;");

  return strings.reduce(
    (acc, str, i) => acc + str + (values[i] ? escape(values[i]) : ""),
    ""
  );
}

const dangerous = "<script>alert('xss')</script>";
const output = safe`User input: ${dangerous}`;
```

### Example: Internationalization (i18n)
```js
function i18n(strings, ...values) {
  return strings.reduce((out, str, i) => out + str + (values[i] || ""), "");
}

const greeting = i18n`Welcome, ${"Harshith"}!`;
```

---

## 3. Interview Prep — Theory Questions (with concise answers)

### What are template literals?
Strings defined using backticks that support multi-line text, interpolation, and tagging.

### How is interpolation different from concatenation?
Interpolation embeds expressions inside `${}` directly in the string, making it cleaner and avoiding `+` operators.

### Can template literals contain expressions?
Yes. Any JS expression is valid: arithmetic, function calls, ternary operations, and more.

### What are tagged templates?
A feature allowing a function to intercept and transform the template literal before creating the final output.

### Why use tagged templates?
For custom string processing—useful in i18n, sanitization, styling, logging, and DSL-like APIs.

### Do template literals escape values automatically?
No. They do not escape HTML or sanitize input unless you implement a tagged template for that.

---

## 4. Coding-Based Questions

### Q1: Create a tag function that formats numbers as currency.
```js
function currency(strings, ...values) {
  return strings.reduce(
    (acc, str, i) =>
      acc + str + (values[i] != null ? `₹${values[i].toFixed(2)}` : ""),
    ""
  );
}

const price = 499;
console.log(currency`The final price is ${price}`);
```

### Q2: Build a translation tag for multiple languages.
```js
const dict = {
  en: { greet: "Hello" },
  es: { greet: "Hola" }
};

function tr(lang) {
  return function(strings, ...values) {
    return strings.reduce(
      (acc, str, i) => acc + str + (values[i] ? dict[lang][values[i]] : ""),
      ""
    );
  };
}

console.log(tr("es")`Greeting: ${"greet"}`);
```

### Q3: Write a tag that highlights variables for debugging.
```js
function debug(strings, ...values) {
  return strings.reduce(
    (acc, str, i) =>
      acc + str + (values[i] ? `[${values[i]}]` : ""),
    ""
  );
}

const user = "Harshith";
console.log(debug`Logged in user: ${user}`);
```

---

## End
This document covers template literals, interpolation, tagged templates, interview questions, and applied coding exercises.

# ES6+ Features – Destructuring (objects, arrays, nested, defaults)

## Theory & Detailed Explanation  
Destructuring in JavaScript (ES6 / ECMAScript 2015) is a syntax that lets us unpack values from arrays or object properties into variables.

### Array Destructuring  
```js
const arr = [10, 20, 30];
const [a, b, c] = arr;
```
Skipping elements:
```js
const [first,, third] = [1,2,3];
```
Rest syntax:
```js
const [x, ...others] = [1,2,3,4];
```
Nested arrays:
```js
const nested = [1, [2,3], 4];
const [one, [two, three], four] = nested;
```

### Object Destructuring  
```js
const person = { name:"Alice", age:30, city:"NY" };
const { name, age, city } = person;
```
Renaming:
```js
const { name: personName, age: personAge } = person;
```
Defaults:
```js
const { country = "Unknown" } = person;
```
Nested:
```js
const user = {
  profile: {
    username: "harshith",
    details: { email: "h@example.com" }
  }
};
const { profile:{ username, details:{ email } } } = user;
```
Rest in object:
```js
const { a, b, ...restProps } = { a:1, b:2, c:3, d:4 };
```

### Mixed Destructuring & Function Parameters  
```js
const data = {
  name: "X",
  scores: [10,20,30],
  meta: { active: true }
};
const { name, scores:[ firstScore, , thirdScore ], meta:{ active } } = data;

function greet({ name, age = 18 }) {
  console.log(`Hi ${name}, you are ${age}`);
}
```

## Interview‑Style Questions & Answers  
1. **What is destructuring assignment in JS?**  
   A syntax to unpack arrays/objects into distinct variables.  
2. **How to skip elements in array destructuring?**  
   Using extra commas: `[a, , b] = arr`.  
3. **How to provide default values?**  
   For objects: `{ x = defaultX } = obj`. For arrays: `[a = defaultA] = arr`.  
4. **What if you destructure a property that doesn’t exist without default?**  
   The resulting variable is `undefined`.  
5. **How to rename variable during object destructuring?**  
   Use `{ propName: newVarName } = obj`.  
6. **Can you destructure nested objects/arrays?**  
   Yes. e.g., `const { nested:{ inner } } = obj` or `[ , [b] ] = arr`.  
7. **What is the rest syntax in destructuring?**  
   Arrays: `[a, ...rest] = arr`. Objects: `const { a, ...restProps } = obj`.  
8. **Why is destructuring valuable in React or modern JS frameworks?**  
   Because components often receive props/objects, and destructuring extracts only needed fields in a clearer way.

## Coding‑Based Questions (with solutions)  
1. Given `const arr = [5,10,15,20]`, extract `first = 5`, `third = 15`, and `remaining` array.  
   ```js
   const [ first, , third, ...remaining ] = arr;
   ```  
2. Given:
   ```js
   const user = {
     id: 123,
     profile: {
       name: "Alice",
       contact: {
         email: "alice@example.com",
         phone: "12345"
       }
     },
     roles: ["admin", "user"]
   };
   ```
   Extract `id`, `name`, `email`, and first role.  
   ```js
   const {
     id,
     profile: {
       name,
       contact: { email }
     },
     roles: [ firstRole ]
   } = user;
   ```  
3. Write `updateSettings(settings)` where `settings` may have `theme`, `version`, `debug`, all defaulting to `"light"`, `1`, `false` respectively.  
   ```js
   function updateSettings({ theme = "light", version = 1, debug = false } = {}) {
     // ...
   }
   ```  
4. Swap values of `a` and `b` using destructuring.  
   ```js
   [a, b] = [b, a];
   ```  
5. Given `const obj = { x:10, y:20, z:30 }`, pick `x`, `z` and rest into `others`.  
   ```js
   const { x, z, ...others } = obj;
   // others = { y:20 }
   ```


# ES6+ Features: Rest & Spread (arrays, objects, function params) in JavaScript

## 1. Theory – What, Why & How

### What are they?
- Both use `...` but different semantics depending on context.
- **Spread operator** expands (“unpacks”) an iterable or object’s properties.
- **Rest parameter** collects (“packs”) multiple arguments or remaining elements/properties into an array or object.

### Spread in arrays
```js
const arr1 = [1,2,3];
const arr2 = [...arr1, 4,5];
const merged = [...a1, ...a2];
const copy = [...originalArray];
```

### Spread in objects
```js
const obj = { a:1, b:2 };
const clone = { ...obj };
const merged = { ...obj1, ...obj2 };
```

### Spread in function calls
```js
function sum(x,y,z) { return x+y+z; }
const nums = [1,2,3];
sum(...nums);
```

### Rest in function parameters
```js
function showAll(...args) { console.log(args); }
function greet(greeting, ...names) { console.log(greeting, names); }
```

### Rest in destructuring
```js
const [first, ...rest] = [1,2,3,4];
const { a, ...others } = { a:1, b:2, c:3 };
```

---

## 2. Interview Questions

**Difference between rest and spread?**  
Spread expands; rest collects.

**Clone array/object?**  
`[...arr]`, `{...obj}` (shallow).

**Rest params vs arguments?**  
Rest is a real array; arguments is array‑like.

---

## 3. Coding Questions

- Merge & dedupe arrays using spread + Set.  
- Write `logAll(prefix, ...values)`.  
- Extract id, name, put remaining props using rest.  
- Use spread for React props.  
- Immutable nested update using spread.

