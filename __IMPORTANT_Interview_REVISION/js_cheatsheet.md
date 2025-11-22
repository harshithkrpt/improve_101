# JavaScript Basics: Variables & Scope

## var, let, const
### var
- Function-scoped. 
- Allows redeclaration.
- Hoisted with initialization to `undefined`.

### let
- Block-scoped.
- No redeclaration in same scope.
- Hoisted but not initialized (temporal dead zone).

### const
- Block-scoped.
- Must be initialized.
- Binding is constant but object/array contents can mutate.

## Temporal Dead Zone (TDZ)
The time between entering a block and the actual declaration of `let`/`const`. Accessing the variable in this window throws a ReferenceError.

## Scope Chain
JS resolves variables by walking outward through nested scopes: local → parent → global.

## Interview Theory Questions
1. Difference between var, let, const?  
   var is function-scoped and hoisted; let/const are block-scoped with TDZ. const prevents reassignment.

2. What is TDZ?  
   A pre-declaration period where let/const exist but cannot be accessed.

3. Can const objects mutate?  
   Yes, the binding is constant, not the contents.

4. How does scope chain work?  
   JS searches identifiers outward through lexical scopes until found.

## Coding Questions
1. Demonstrate TDZ with a small snippet.  
2. Create a function that shows var hoisting behavior.  
3. Write code using nested blocks to observe scope chain resolution.

# JS Basics — Data Types (Primitive vs Reference, Type Coercion, typeof, instanceof)

## 1. Primitive vs Reference Types
Primitives: undefined, null, boolean, number, bigint, string, symbol.  
Immutable, copied by value, compared by value.

Reference Types: objects, arrays, functions, dates, maps, etc.  
Mutable, copied by reference, compared by identity.

### Example
```js
let a = 10;
let b = a;
a = 20;        // b remains 10

let obj1 = { x: 1 };
let obj2 = obj1;
obj1.x = 2;    // obj2.x becomes 2
```

Note: `typeof null === "object"` (language quirk).

---

## 2. Type Coercion
JS performs implicit type conversion in operations such as:
- `+` with a string → string concatenation
- `==` equality → converts both sides to comparable values
- Objects → primitives via `valueOf()` / `toString()` / `Symbol.toPrimitive`

Explicit conversion: `String()`, `Number()`, `Boolean()`, etc.

---

## 3. typeof Operator
Returns a string describing the value type.

Examples:
```js
typeof "hi"         // "string"
typeof 42           // "number"
typeof Symbol()     // "symbol"
typeof null         // "object"
typeof {}           // "object"
typeof []           // "object"
typeof function(){} // "function"
```

Useful for checking primitives and functions. Not useful for distinguishing array vs object.

---

## 4. instanceof Operator
Checks if an object’s prototype chain contains the prototype of a constructor.

Examples:
```js
[] instanceof Array        // true
new Date() instanceof Date // true
({}) instanceof Object     // true
123 instanceof Number      // false
```

Not useful for primitives. Can fail across iframes (different realms).

---

## Interview Questions & Answers

### Q1: What are JS primitives?
A: undefined, null, boolean, number, bigint, string, symbol.

### Q2: Difference between primitive and reference?
A: Primitive is immutable & copied by value. Object is mutable & copied by reference.

### Q3: What is type coercion?
A: Automatic conversion of one type to another (e.g., string + number → string).

### Q4: typeof quirks?
A: `typeof null === "object"`, arrays return "object".

### Q5: When to use typeof vs instanceof?
A: typeof → primitives  
   instanceof → object construction/prototype chain.

### Q6: What will `typeof null` return?
A: "object".

---

## Coding Practice Questions

### 1. Deep Clone Function
Implement a deepClone function that avoids mutation of source.

### 2. Count Primitives vs Objects
Given a mixed array, return `{ primitives: X, objects: Y }`.

### 3. Show + operator behavior
Compare `"5" + 1` vs `5 + 1`.

### 4. Build a typeCheck(value) function
Return labels such as `"primitive-number"`, `"object-array"`, etc.

### 5. Prototype & instanceof
Explore:
```js
function Foo() {}
let x = new Foo();
console.log(x instanceof Foo);
console.log(x instanceof Object);
console.log(typeof x);
console.log(typeof Foo);
```
Then reassign `Foo.prototype = {}` and test again.

---

## Bonus: Common Pitfalls & Advanced Notes

### Wrapper Objects
`new String("x")`, `new Number(5)` create objects, not primitives.

### Symbol.toPrimitive
Allows custom object → primitive conversion:
```js
obj[Symbol.toPrimitive] = function(hint) {
  return hint === "number" ? 42 : "hello";
};
```

### Equality Traps
`[] == ![]` → true  
Reason: implicit coercion of both sides.

---

# JS Basics – Operators Cheat Sheet
## Sub‑Topic: strict equality, nullish coalescing, optional chaining, destructuring

### 1. Theory & Definitions

#### Strict equality (`===`)
- Checks both **type** and **value**.
- If types differ → returns `false`.
- Example: `1 === "1"` → `false`.
- Compared to `==`, `===` does **not** perform type coercion.
- Objects are compared by reference, e.g. `{}` === `{}` is `false`.

#### Nullish coalescing (`??`)
- Syntax: `leftExpr ?? rightExpr`
- Returns `rightExpr` only if `leftExpr` is `null` or `undefined`.
- Other falsy values like `0`, `""`, `false` are *not* replaced.
- Useful for defaults when you want to treat only “missing” values.
- Example:
```js
const x = null ?? "default"; // "default"
const y = 0 ?? "default";    // 0
```

#### Optional chaining (`?.`)
- Syntax: `obj?.prop`, `obj?.[expr]`, `func?.(args)`
- Safely accesses a property or method on `obj` only if `obj` is not `null`/`undefined`.
- If `obj` is `null/undefined`, returns `undefined` instead of throwing.
- Example:
```js
const user = { profile: { name: "Alice" } };
const city = user.profile?.address?.city; // undefined (no error)
```
- Note: `?.` short-circuits only on `null` or `undefined`. If the left side is an undeclared variable, it still throws a ReferenceError.

#### Destructuring assignment
- Unpacks values from arrays or properties from objects into variables.
- Array example:
```js
const [a, b] = [10, 20]; // a = 10, b = 20
```
- Object example:
```js
const { name, age } = { name: "John", age: 30 };
```
- Features:
  - Default values: `const { x = 5 } = obj;`
  - Renaming: `const { prop: alias } = obj;`
  - Nested destructuring: `const { a: { b } } = obj;`
  - Rest properties: `const { a, ...rest } = obj;`

---

### 2. Interview‑Style Q&A (Concise Answers)

1. **Q:** What is the difference between `==` and `===`?
   **A:** `==` performs type coercion before comparison; `===` checks both type and value and does not coerce.

2. **Q:** When would you use the nullish coalescing `??` operator rather than `||`?
   **A:** Use `??` when you want to fallback only if a value is `null` or `undefined`. `||` falls back for any falsy value (e.g., `0`, `""`, `false`).

3. **Q:** Explain optional chaining `?.` and its benefit.
   **A:** `?.` allows safe access to nested properties or function calls—if any step is `null`/`undefined`, the expression returns `undefined` instead of throwing.

4. **Q:** What does object destructuring allow you to do?
   **A:** Extract properties from objects directly into variables, with options for defaults, renaming, and nested extraction.

5. **Q:** Can destructuring have default values? Show an example.
   **A:** Yes. `const { name = "Anonymous", age = 0 } = user;`

---

### 3. Quick Examples & Gotchas

- `null === undefined` → `false`, but `null == undefined` → `true`.
- Using `??` preserves falsy values:
```js
const obj = { a: null, b: 0 };
const x = obj.a ?? 10; // 10
const y = obj.b ?? 20; // 0
```
- Mixing `||` and `??` without parentheses can cause syntax errors or unexpected results.

---

### 4. Practice Coding Questions (with short answers)

**Q1:** Implement `getCity(user)` using optional chaining and nullish coalescing.
```js
function getCity(user) {
  return user?.address?.city ?? "Unknown city";
}
```

**Q2:** Swap two variables `a` and `b` using array destructuring.
```js
let a = 1, b = 2;
[a, b] = [b, a];
```

**Q3:** Destructure nested API response to get `userId`, `userName`, `secondHobby`.
```js
const response = {
  data: {
    user: {
      id: 123,
      profile: { name: "Alice", hobbies: ["reading", "gaming"] }
    }
  }
};
const { data: { user: { id: userId, profile: { name: userName, hobbies: [, secondHobby] } } } } = response;
```

**Q4:** Function that takes `options` and destructures with defaults.
```js
function setup(options = {}) {
  const { timeout = 3000, verbose = false } = options;
  return { timeout, verbose };
}
```

**Q5:** Predict output:
```js
console.log(0 || "fallback");       // "fallback"  (0 is falsy)
console.log(0 ?? "fallback");       // 0           (0 is not null/undefined)
console.log(null || "fallback");    // "fallback"  (null is falsy)
console.log(undefined ?? "fallback"); // "fallback" (undefined triggers ??)
```

---

### 5. Further Reading
- MDN Web Docs: Strict equality, Optional chaining, Nullish coalescing, Destructuring.
- Practice by refactoring small code snippets to use destructuring and optional chaining.

---

# JS Basics – Functions  
## Sub Topic: Function Declarations vs Expressions, Arrow Functions, IIFE

---

## 1. Detailed Explanation

### Function Declarations
A function declaration is the classic way to define a function. JavaScript hoists the entire declaration, meaning the function can be called before it appears in code.

```js
function add(a, b) {
  return a + b;
}
```

Key traits:
- Fully hoisted.
- Has its own `this`, `arguments`, and can be used as constructors.

---

### Function Expressions
A function expression assigns a function to a variable.

```js
const add = function(a, b) {
  return a + b;
};
```

Key traits:
- Only the variable is hoisted, not the assigned function.
- More flexible; can be anonymous or named.
- Useful for callbacks and closures.

---

### Arrow Functions
Arrow functions are compact and lexically bind `this`.

```js
const add = (a, b) => a + b;
```

Key traits:
- No own `this`, `arguments`, `super`, or `new`.
- Cannot be used as constructors.
- Great for callbacks and inline logic.

---

### IIFE (Immediately Invoked Function Expression)
A function that runs the moment it’s created.

```js
(function() {
  console.log("I run instantly!");
})();
```

Why used:
- To create private scopes.
- Historically crucial before block-scope (`let`, `const`).

---

## 2. Theory/Interview Questions with Short Answers

### 1. What is the difference between a function declaration and expression?
A declaration is fully hoisted; an expression only hoists the variable, not the function value.

### 2. Why can’t arrow functions be constructors?
They lack their own `this` and `prototype`, so `new` cannot instantiate them.

### 3. Do arrow functions have an `arguments` object?
No. They inherit `arguments` lexically from their parent scope.

### 4. Why use an IIFE?
To create a private scope and avoid polluting global variables.

### 5. What is lexical `this` in arrow functions?
They capture `this` from the surrounding execution context.

---

## 3. Coding-Based Questions

### Q1: Create a function expression that returns a counter using closures.
```js
const makeCounter = function() {
  let count = 0;
  return function() {
    return ++count;
  };
};
```

### Q2: Convert a normal function into an arrow function.
```js
const multiply = (x, y) => x * y;
```

### Q3: Write an IIFE that returns the square of a number.
```js
const square = ((n) => n * n)(5);
```

---

# JS Basics: Execution Context (Creation Phase, Hoisting, Variable Environment)

## 1. Execution Context
JavaScript code runs inside an execution context (EC) — a container holding the environment, memory, and scope needed to execute code.  
Two main types:
- Global Execution Context (GEC)
- Function Execution Context (FEC)

The JS engine manages ECs using a **call stack**.

## 2. Phases of an Execution Context

### 2.1 Creation Phase
Before executing code:
- Memory is allocated for variables and functions.
- `var` variables are initialized to `undefined`.
- Function declarations are fully stored in memory.
- `let` and `const` are hoisted but uninitialized (Temporal Dead Zone).
- `this` binding is created.
- Scope chain / outer environment is linked.

### 2.2 Execution Phase
JavaScript executes code line by line:
- Assignments occur.
- Function calls push new execution contexts.
- Expressions are evaluated.

## 3. Variable Environment
This is where variables, functions, and arguments live for that execution context.  
Variable lookups start here and move outward through the scope chain.

## 4. Hoisting
Hoisting describes how declarations are processed during the creation phase.

- **Function declarations**: Fully hoisted. Can be called before definition.
- **var**: Declaration hoisted, initialized to `undefined`.
- **let / const**: Hoisted but uninitialized → accessing before initialization throws ReferenceError (TDZ).

## 5. Interview Questions (Concise Answers)

**What is an Execution Context?**  
Environment where JS code runs with memory, scope, and `this`.

**Phases of execution context?**  
Creation phase and execution phase.

**What is hoisting?**  
JS behavior where declarations are processed before code executes.

**Difference in hoisting between var and let/const?**  
`var` → initialized to `undefined`.  
`let/const` → uninitialized (TDZ).

**What is Variable Environment?**  
Memory space inside the EC that stores variables and functions.

**What happens when a function is called?**  
A new FEC is created and pushed onto the call stack.

## 6. Coding Examples

### Example 1: var hoisting
```js
console.log(a); // undefined
var a = 2;
```

### Example 2: let TDZ
```js
console.log(b); // ReferenceError
let b = 3;
```

### Example 3: function declaration hoisting
```js
foo(); // works
function foo() { console.log("hello"); }
```

### Example 4: function expression vs declaration
```js
foo(); // TypeError (foo is undefined)
var foo = function(){};

bar(); // works
function bar(){}
```

### Example 5: inner scope hoisting
```js
var a = 1;
function outer(){
  console.log(a); // undefined
  var a = 2;
  console.log(a); // 2
}
outer();
```

# JS Basics  
## Call Stack & Memory Stack vs Heap, Synchronous Execution

### 1. Theory: What’s going on under the hood in JavaScript  
#### 1.1 Call Stack (Execution Context Stack)  
- Execution context created for global script + each function call.  
- Call stack is a LIFO structure: each invocation pushes a frame, returns pop it.  
- Recursion, nested calls use the stack heavily → risk of stack overflow.  
- JS (in typical usage) is single‑threaded synchronous in its main execution path.

#### 1.2 Memory: Stack vs Heap  
**Memory Stack**  
- Used for primitives, local variables, references to heap‑objects.  
- Fast access, automatic reclaim when function exits.  
- Size limited, best for short‑lived, known size data.

**Memory Heap**  
- Used for objects, arrays, functions (reference types).  
- Variable size, dynamic allocation, slower access.  
- Memory reclaimed by garbage collector when objects become unreachable.  
- Variables referencing heap objects hold pointer/reference (on stack) to the heap location.

**Key differences**  
- Primitive value assignment copies the value; object assignment copies the reference.  
- Heap access is slower, and objects may live longer than the function that created them.  
- Stack frames correspond to function calls; heap is more free‑form.

#### 1.3 Synchronous Execution in JS  
- In synchronous code, instructions execute one after another in the same call stack.  
- Because JS has one main thread (in standard model), long synchronous tasks block other JS tasks or UI.  
- Asynchronous mechanisms (timers, Promises, event loop) work around this, but the base model is synchronous execution.  
- Understanding stack + heap + synchronous execution helps reason about performance, responsiveness, memory usage.

#### 1.4 Bringing them together  
- Global execution context pushed.  
- Variables/functions allocated (stack & heap as appropriate).  
- Function calls push new frames, local contexts created.  
- Heap allocations for objects happen when you create objects.  
- After function returns, its stack frame popped; heap objects may persist if referenced.  
- Heavy synchronous loops = blocking; deep recursion = large stack; many objects/reference = large heap.

---

### 2. Common interview‑theory questions + concise answers

| Question | Answer |
|----------|--------|
| What is the call stack in JavaScript? | The execution context stack of functions; each invocation pushes a frame, functions return by popping. |
| How do stack and heap memory differ in JavaScript? | Stack: fast, LIFO, primitives/local frames; Heap: dynamic, for objects/arrays/functions, slower. |
| When you assign one object variable to another, what happens under the hood? | Both variables refer to the same object in heap; modifying via one affects the other. |
| Why can deep recursion cause a problem in JS? | Because each call consumes stack frame memory; too many = stack overflow. |
| Is JavaScript single‑threaded? How does it handle asynchronous operations then? | Yes, single‑threaded for the main execution context (call stack). Async ops use event loop + callback queue so tasks can be deferred and executed when stack is free. |
| What happens to memory after a function finishes executing? | Its stack frame is popped (stack memory freed). Heap objects persist if references remain; otherwise GC may free them later. |
| Where do primitives and objects live in memory? | Primitives: stack; Objects/arrays/functions: heap (with references on stack). |
| What does synchronous execution mean in JS? | Code runs step‑by‑step in the call stack; no two instructions from the same JS context run concurrently. |
| What is an execution context in JS? | The environment in which code is evaluated: variable object, scope chain, `this`, etc. Each function call has one. |
| How does the call stack enforce execution order? | Because frames are pushed/popped in LIFO order, functions return in reverse order of invocation. |

---

### 3. Coding/Practical questions you might be asked  
#### Q1. Create recursion that causes stack overflow and explain why  
```js
function infinite() {
  console.log("still going");
  infinite();
}
infinite();
```  
Explanation: Each call pushes a new frame; because there’s no base case, frames accumulate until stack limit is reached.

#### Q2. What prints and why?  
```js
let a = { value: 1 };
let b = a;
b.value = 2;
console.log(a.value);
```  
Answer: `2`.

#### Q3. What about this?  
```js
let x = 10;
let y = x;
y = 20;
console.log(x);
```  
Answer: `10`.

#### Q4. Trace the call stack.  
(As above)

#### Q5. What issues if you run a long synchronous loop in JS?  
Answer: It blocks the call stack and freezes UI / event handling.

#### Q6. Memory leak example.  
(As above)

---

## 4. Summary  
Understanding how the call stack, memory (stack vs heap), and synchronous execution interrelate improves performance intuition, helps avoid leaks, and prepares you for JS interviews.

# JS Basics – Arrays  
## Subtopic: Array Methods (map, filter, reduce, find, some, every) & Immutability

### Array Methods Explained

**map**  
Creates a new array by applying a function to each element of the original array.  
Does not mutate the original.

```js
const nums = [1, 2, 3];
const doubled = nums.map(n => n * 2); // [2, 4, 6]
```

**filter**  
Returns a new array containing only elements that pass a truth test.

```js
const nums = [1, 2, 3, 4];
const even = nums.filter(n => n % 2 === 0); // [2, 4]
```

**reduce**  
Collapses an array to a single value.

```js
const sum = [1, 2, 3].reduce((acc, cur) => acc + cur, 0); // 6
```

**find**  
Returns the first element matching a condition.

```js
[5, 12, 8].find(n => n > 10); // 12
```

**some**  
Returns true if any element satisfies the condition.

```js
[1, 3, 5].some(n => n % 2 === 0); // false
```

**every**  
Returns true only if *all* elements satisfy the condition.

```js
[2, 4, 6].every(n => n % 2 === 0); // true
```

### Immutability in JS Arrays
Arrays are mutable, but functional array methods allow *immutable patterns*:  
Creating **new arrays** instead of modifying existing ones.

```js
const arr = [1, 2, 3];
const newArr = [...arr, 4]; // arr unchanged
```

### Interview Theory Questions (Concise Answers)

1. **Difference between map and forEach?**  
   map returns a new array; forEach returns undefined.

2. **Is reduce always numeric?**  
   No. It can accumulate any data type (objects, arrays, strings).

3. **Why use immutability?**  
   Predictability, no side effects, easier debugging, friendlier for React state updates.

4. **When choose find over filter?**  
   When you want only the first matching element, not an array of matches.

5. **Does filter mutate the original array?**  
   No, it returns a new array.

6. **How to ensure immutability when updating arrays?**  
   Use spread (`[...]`), slice, concat, and functional methods.

### Coding Questions

**1. Implement map manually.**
```js
function myMap(arr, fn) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(fn(arr[i], i, arr));
  }
  return result;
}
```

**2. Flatten array using reduce.**
```js
const flat = arr => arr.reduce((acc, cur) => acc.concat(cur), []);
```

**3. Find duplicate numbers using filter + indexOf.**
```js
const duplicates = arr =>
  arr.filter((item, i) => arr.indexOf(item) !== i);
```

**4. Immutable update: replace an item.**
```js
const replaceAt = (arr, idx, value) =>
  arr.map((item, i) => (i === idx ? value : item));
```

# JS Basics — Objects  
## Sub Topic: object creation, property descriptors, spread/rest, Object.assign  

### 1. Theory  
#### Object creation  
- Object literal: `const obj = { a:1, b:2 };`  
- Constructor/new: `function Person(...) { this.name = ... }`  
- `Object.create(proto, [descriptors])` for prototype chain control  
- Dynamic addition of properties via `obj.prop = value`  
- Objects are reference types: `let x = obj;` means `x` and `obj` refer same object.  

#### Property Descriptors  
Each property has metadata:  
- `writable` (boolean)  
- `enumerable` (boolean)  
- `configurable` (boolean)  
- Data descriptor: `value`; accessor: `get`/`set`.  

```js
Object.defineProperty(obj, 'a', {
  value: 42,
  writable: false,
  enumerable: true,
  configurable: false
});
```  

#### Spread / Rest Syntax  
```js
const newObj = { ...oldObj, extra:'value' };
const { a, ...rest } = obj;
```  
Shallow operations; skip prototype; skip non‑enumerable props.

#### Object.assign()  
```js
const merged = Object.assign({}, {a:1,b:1}, {b:2,c:2});
```  
Mutates target; shallow; triggers setters.

---

### 2. Interview Questions  
1. Property descriptors: metadata flags.  
2. defineProperty vs assignment: descriptor control.  
3. Spread vs assign: new object vs mutation.  
4. Shallow copy: nested objects shared.  
5. Rest collects remaining props.  
6. Hide with enumerable:false.  
7. configurable:false prevents deletion/descriptor changes.

---

### 3. Coding Questions  

```js
const person = { name:'Harshith', age:30 };
Object.defineProperty(person, 'ssn', { value:'123-45-6789', enumerable:false });
```

```js
const settings1 = Object.assign({}, defaults, userOpts);
const settings2 = { ...defaults, ...userOpts };
```

```js
function cloneShallow(obj){ return { ...obj }; }
```

```js
Object.defineProperty(user,'fullName',{ get(){...}, set(v){...} });
```

```js
const copy = { ...o1, a:3 };
```

# JavaScript Basics – Date & Math APIs  
## Sub‑Topic: common utilities, timezone handling, formatting

### 1. Detailed Coverage  
#### Date API  
- `Date` stores time as milliseconds since 1970‑01‑01 UTC.  
- Constructors:  
  ```js
  new Date()
  new Date(milliseconds)
  new Date(dateString)
  new Date(year, monthIndex, day, hour, minute, second, ms)
  ```  
- Key getters/setters:  
  ```js
  date.getFullYear(), getMonth(), getDate(), getHours(), …
  date.getUTCFullYear(), getUTCHours(), …
  date.getTime(), date.getTimezoneOffset()
  date.setFullYear(), setMonth(), setHours(), setTime(), …
  ```  
- Formatting:  
  ```js
  date.toString()
  date.toUTCString()
  date.toISOString()
  date.toLocaleDateString()
  date.toLocaleTimeString()
  ```  
- Pitfalls: zero‑based months, inconsistent parsing, timezone/DST quirks.  
- Modern alternative: Temporal API (immutable, explicit zones).  
- Utility patterns: add/subtract days/hours, difference in days, start/end of day, timezone conversion, formatting.

#### Math API  
- `Math` is a static namespace (not constructible).  
- Constants: `Math.PI`, `Math.E`, `Math.LN2`, etc.  
- Methods: rounding (`floor`, `ceil`, `round`, `trunc`), absolute/sign, power/log/trig functions, min/max, random, newer methods (`hypot`, `fround`, etc.).  
- Utility patterns: random integer in [min,max], clamp, lerp, deg↔rad conversion, rounding to decimals.

#### Timezone handling & formatting  
- `Date` methods often assume local timezone; special handling needed for converting to/from other zones.  
- Use `Intl.DateTimeFormat` with `timeZone` option for formatting in a specific zone.  
- Helper functions:  
  ```js
  function startOfDay(date){ const d=new Date(date); d.setHours(0,0,0,0); return d; }
  function endOfDay(date){ const d=new Date(date); d.setHours(23,59,59,999); return d; }
  function addDays(date,n){ const d=new Date(date); d.setDate(d.getDate()+n); return d; }
  function diffInDays(d1,d2){ return (d2-d1)/(1000*60*60*24); }
  ```

### 2. Theory Questions (with concise answers)  
1. **How does `Date` store time internally?**  
   As milliseconds since 00:00:00 UTC on Jan 1, 1970.  
2. **Difference between `getHours()` and `getUTCHours()`?**  
   `getHours()` uses local time; `getUTCHours()` uses UTC.  
3. **Why is month index zero‑based?**  
   Legacy design: January = 0.  
4. **Shortcomings of built‑in `Date`?**  
   Parsing inconsistencies, timezone & DST issues, mutability, zero‑based months.  
5. **What is `Math` object?**  
   Static object for mathematical constants & operations.  
6. **Convert degrees → radians?**  
   `deg * Math.PI/180`.  
7. **Random integer between `min` and `max` inclusive?**  
   `Math.floor(Math.random()*(max-min+1))+min`.  
8. **`Intl.DateTimeFormat` usage?**  
   Locale/timezone-aware formatting.  
9. **What is Temporal API?**  
   Modern immutable date/time API with explicit time zones.  
10. **Days diff between two dates?**  
    `(d2 - d1)/(1000*60*60*24)`.

### 3. Coding Questions  
1. `formatDateYYYYMMDD(date)` → `"YYYY‑MM‑DD"`.  
2. `addBusinessDays(date,n)` → skips weekends.  
3. `timeDiffHuman(d1,d2)` → “X days Y hours Z minutes”.  
4. `randomInRange(min,max,decimals)` → random decimal/integer.  
5. Format date in timezone `'YYYY‑MM‑DD HH:mm:ss'`.  
6. `isLeapYear(year)` → leap year check.  
7. `clamp(value,min,max)` using Math.  
8. `degToRad`, `radToDeg`.  
9. `roundTo(value,decimals)`.  
10. `getWeekNumber(date)` ISO week number.

# Advanced JS — Closures & Lexical Scope

## Topic: Advanced JS
## Sub Topic: Closures & Lexical Scope

---

### Quick summary
A **closure** is a function paired with its surrounding lexical environment (scope). In JavaScript, inner functions retain access to variables from the outer function even after the outer function has returned. This enables data privacy, stateful functions, function factories, and many expressive patterns in JS.

---

## 1. Lexical scope (short)
- **Lexical scope** means that the structure of the source code determines variable visibility: where a variable is declared in the source text controls where it can be accessed.
- Functions in JS form scope chains at definition time (not at call time). That chain is captured by closures.

---

## 2. What exactly is a closure?
- A closure is created when a function *remembers* its lexical environment.
- Example: when an inner function references variables from an outer function, that reference (and the values) persist even if the outer function has finished executing.

```js
function outer(x) {
  let count = 0;
  return function inner(y) {
    count += 1;
    return x + y + count;
  };
}

const fn = outer(10);
console.log(fn(5)); // 16 (10 + 5 + 1)
console.log(fn(3)); // 15 (10 + 3 + 2)
```

`fn` holds a closure over `x` and `count`.

---

## 3. How closures capture variables (by reference, not copy)
- Closures capture *bindings*, not just primitive values. For objects, you still reference the same object.
- If the closed-over variable is later mutated, the inner function sees the mutated value.

```js
function make() {
  let obj = {v: 1};
  return function() { return obj.v; };
}
const g = make();
// If outer code mutated obj.v (via other references), g() would see the new value.
```

Note: primitives behave like primitives, but the binding is shared.

---

## 4. Use cases (practical)
- **Data privacy / encapsulation**: hide implementation details behind privileged methods.
- **Function factories**: generate specialized functions.
- **Partial application / currying**: pre-bind arguments.
- **Event handlers / callbacks**: maintain state across asynchronous calls.
- **Memoization & caching**: keep a cache in closure scope.
- **Module pattern**: emulate private and public members (before ES modules).

---

## 5. Common patterns & idioms
### IIFE (Immediately Invoked Function Expression)
Used to create a private scope immediately.

```js
const counter = (function(){
  let n = 0;
  return { inc: () => ++n, val: () => n };
})();
```

### Factory

```js
function makeAdder(x) { return function(y) { return x + y; }; }
const add5 = makeAdder(5);
```

### Module (pre-ES6)

```js
const MyModule = (function(){
  let secret = 42;
  return { get: () => secret };
})();
```

---

## 6. Pitfalls & gotchas
- **Loop capture with `var`**: `var` is function-scoped; closures in loops may all capture the same variable.

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 10); // prints 3,3,3
}
```

Solutions: use `let` (block-scoped), or make a new scope per iteration (IIFE) or pass `i` to a function.

- **Accidental memory retention**: closures keep variables alive — large objects referenced by closures can cause memory pressure.
- **Too many closures**: creating millions of closures can be expensive.

---

## 7. Interview-style theory questions (concise answers)

1. **What is a closure?**
   - A function along with its lexical environment: the inner function retains access to outer variables even after the outer has returned.

2. **How does lexical scope differ from dynamic scope?**
   - Lexical scope is determined at write-time by code layout; dynamic scope depends on call-time execution chain. JS uses lexical scope.

3. **Do closures copy variables or reference them?**
   - They capture bindings (references), so mutations are visible to the closure.

4. **Why do closures cause memory leaks?**
   - Because closures keep references to variables, preventing garbage collection of those values until the closure is unreachable.

5. **How to fix the `var` in loop closure problem?**
   - Use `let` for block scoping, or wrap iteration body in an IIFE that captures the value.

6. **Are closures slow?**
   - Closures have small overhead but are well-optimized in modern engines. Excessive closures or retaining huge objects can be problematic.

7. **Can closures capture `this`?**
   - `this` is not lexically scoped; closures can access `this` from the surrounding scope depending on how functions are declared. Arrow functions capture lexical `this` from the outer scope.

8. **Difference between arrow functions and traditional functions with closures?**
   - Arrow functions inherit `this` lexically. Both can form closures over outer variables.

9. **How do modules use closures for encapsulation?**
   - Modules expose public API while keeping private variables in closure scope (IIFE/module pattern or ES6 modules which are different but achieve privacy differently).

10. **Can you serialize a closure?**
   - No—closures include executable code and runtime environment that cannot be serialized safely.

---

## 8. Coding questions (with sample solutions)

### Q1 — Make a counter factory
**Prompt:** Implement `createCounter()` that returns an object with `increment()`, `decrement()`, and `value()` without exposing the internal count.

```js
function createCounter(init = 0) {
  let n = init;
  return {
    increment() { n++; return n; },
    decrement() { n--; return n; },
    value() { return n; }
  };
}

const c = createCounter(10);
// c.increment(); c.value(); // 11
```

### Q2 — Fix the loop closure problem
**Prompt:** Create an array of functions that log indices 0..2 when invoked.

**Solution (ES6):**

```js
const fns = [];
for (let i = 0; i < 3; i++) {
  fns.push(() => console.log(i));
}
// fns[0](), fns[1](), fns[2]() -> 0,1,2
```

**Solution (ES5 using IIFE):**

```js
var fns = [];
for (var i = 0; i < 3; i++) {
  (function(j){ fns.push(function(){ console.log(j); }); })(i);
}
```

### Q3 — Implement `once(fn)`
**Prompt:** Return a function that calls `fn` at most once and caches the result.

```js
function once(fn) {
  let called = false;
  let result;
  return function(...args) {
    if (!called) { called = true; result = fn.apply(this, args); }
    return result;
  };
}
```

### Q4 — Simple `memoize(fn)`

```js
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const val = fn.apply(this, args);
    cache.set(key, val);
    return val;
  };
}
```

### Q5 — Debounce using closures

```js
function debounce(fn, wait) {
  let timer = null;
  return function(...args){
    if (timer) clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), wait);
  };
}
```

---

## 9. Testing & debugging tips
- Use console logging inside closure to inspect captured values.
- In Chrome DevTools, you can inspect closures via the scope panel (Watch the scope chain). Modern devtools show closed-over variables under the function’s scope.
- For memory issues, take heap snapshots and look for retained objects referencing closures.

---

## 10. Complexity & performance notes
- Creating a closure adds small allocation overhead. The cost is usually negligible compared to the clarity closures provide.
- Avoid holding very large structures in closure scope if not necessary.

---

## 11. Quick reference examples
- Currying, partial application, decorators, and private state are often one-liners with closures.

---

## 12. Interview practice problems (compact list)
- Implement `createLogger(prefix)` that returns a function logging messages with the prefix.
- Implement `wrap(fn, before, after)` that returns a function calling `before()` and `after()` around `fn`.
- Implement `spy(fn)` that returns a wrapper that records call arguments and counts.
- Implement `groupBy(fn)` which uses a closure to build and return the grouping function with internal cache.

---

## 13. Further reading (suggested topics to explore)
- JavaScript engine memory model and garbage collection.
- ES6 `let`/`const` vs `var` and how they affect closures.
- Arrow functions and lexical `this`.

---

## 14. Cheatsheet (one-page)
- Closure = function + lexical environment.
- Captures bindings; mutations visible.
- Useful for privacy, factories, memoization.
- Beware of unintended memory retention.
- Use `let` to avoid loop-capture bugs.

---

*End of document.*

# Advanced JavaScript — Prototype & Inheritance

## Topic: Prototype & Inheritance  
## Sub Topic: __proto__, Prototype Chain, Object.create(), class extends

---

## 1. Understanding `__proto__`
`__proto__` is an internal link (not recommended for production use, but widely seen in debugging) that points to the object's prototype — essentially the object it inherits from.

Example:
```js
const obj = { a: 10 };
console.log(obj.__proto__); // Shows Object.prototype
```

Modern recommended alternative:
```js
Object.getPrototypeOf(obj);
Object.setPrototypeOf(obj, newProto);
```

---

## 2. `prototype` vs `__proto__`
These two get mixed up often.

* `__proto__`: Exists **on objects**, pointing to their prototype.
* `prototype`: Exists **on constructor functions**, used to create the prototype of instances.

Example:
```js
function Car() {}
console.log(Car.prototype);     // Prototype of all Car instances
console.log(new Car().__proto__ === Car.prototype); // true
```

---

## 3. The Prototype Chain
JavaScript uses **prototype-based inheritance**, creating a chain of linked objects.

If JS cannot find a property on an object, it walks up the chain:

```
obj → obj.__proto__ → obj.__proto__.__proto__ → ... → null
```

Example:
```js
const parent = { x: 1 };
const child = Object.create(parent);

console.log(child.x); // 1 (inherited)
console.log(child.__proto__ === parent); // true
```

---

## 4. `Object.create()`
Creates a new object with an explicitly defined prototype.

Example:
```js
const human = {
  speak() { return "Hello"; }
};

const student = Object.create(human);
console.log(student.speak()); // "Hello"
```

Useful for:
* Pure prototypal inheritance
* Avoiding constructor functions
* Creating objects without a prototype:
```js
const dictionary = Object.create(null);
```

---

## 5. Classical-style Inheritance using Functions
Before ES6 classes, inheritance was implemented manually:

```js
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function () {
  return `${this.name} makes a sound`;
};

function Dog(name) {
  Animal.call(this, name); // constructor inheritance
}

Dog.prototype = Object.create(Animal.prototype); // prototype inheritance
Dog.prototype.constructor = Dog;

Dog.prototype.speak = function () {
  return `${this.name} barks`;
};

const d = new Dog("Leo");
console.log(d.speak());
```

---

## 6. ES6 `class` and `extends`
Classes are syntactic sugar over prototype inheritance.

Example:
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
  constructor(name) {
    super(name); // calls Animal's constructor
  }
  speak() {
    return `${this.name} barks`;
  }
}

const d = new Dog("Max");
console.log(d.speak());
```

Key points:
* `extends` sets up prototype linkage
* `super()` calls the parent constructor
* Methods still live on prototypes under the hood

---

## Interview Theory Questions (Concise Answers)

1. **Difference between `__proto__` and `prototype`?**  
   `__proto__` is an object's prototype link; `prototype` is used by constructor functions to build that link for new instances.

2. **What is prototype chaining?**  
   It's the lookup process where JS checks the object and then its prototype chain until it finds the property or reaches `null`.

3. **How does `Object.create()` work?**  
   It creates a new object and sets its internal `[[Prototype]]` to the argument provided.

4. **Why use `super()` in classes?**  
   It initializes the parent class and must be called before accessing `this` in derived classes.

5. **Are classes in JS truly classes?**  
   They are syntactic sugar over prototype-based inheritance.

---

## Coding Practice Questions

### Q1: Implement custom `Object.create()`
```js
function myCreate(proto) {
  function F() {}
  F.prototype = proto;
  return new F();
}
```

### Q2: Create a simple inheritance chain without classes
```js
const person = { greet() { return "Hi"; } };
const developer = Object.create(person);
developer.code = () => "Writing JS...";
```

### Q3: Override method in prototype chain
```js
const base = { greet() { return "Hello"; } };
const sub = Object.create(base);

sub.greet = function () {
  return "Hi from child";
};

console.log(sub.greet());
```

### Q4: Demonstrate `class` method overriding
```js
class A { say() { return "A"; } }
class B extends A { say() { return "B"; } }
```

---

This file covers advanced prototype mechanics, ES6 inheritance, and interview-ready content.

# Topic : Advanced JS
## Sub Topic : Classes & OOP (constructor, inheritance, static methods, private fields (#))

---

## Overview
This cheat-sheet covers modern JavaScript classes and object-oriented programming (OOP) features introduced and standardized in ES6+:
- Class syntax, constructors, instance methods
- Inheritance (`extends`, `super`)
- Static methods and properties
- Private instance fields and methods using `#`
- Common patterns, gotchas, and interview-style Q&A
- Practical coding challenges and sample solutions

---

## 1. Class basics

### Declaration
```js
class Person {
  constructor(name, age) {
    this.name = name;       // public instance field
    this.age = age;
  }

  greet() {
    return `Hi, I'm ${this.name}`;
  }
}

const p = new Person('Asha', 30);
p.greet(); // "Hi, I'm Asha"
```

### Notes
- `class` is mostly syntactic sugar over the prototype system.
- Methods declared inside class body are non-enumerable and live on the prototype.
- `constructor` is a special method called when `new` is used. If omitted, an empty constructor is assumed.

---

## 2. Constructor details
- `constructor` can return an object explicitly; if it returns a non-object, `this` is returned.
- In subclass constructors, you **must** call `super(...)` before using `this`.
- Use default parameter values and destructuring for robust constructors:
```js
class Config {
  constructor({ host = 'localhost', port = 80 } = {}) {
    this.host = host;
    this.port = port;
  }
}
```

---

## 3. Inheritance: `extends` and `super`

### Single inheritance example
```js
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a noise.`; }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // call parent constructor
    this.breed = breed;
  }
  speak() { return `${this.name} barks.`; } // overrides
}

const d = new Dog('Rex', 'Labrador');
d.speak(); // "Rex barks."
```

### Important points
- `extends` sets up prototype chain: `Dog.prototype.__proto__ === Animal.prototype`.
- `super.method(...)` calls parent class methods.
- Static inheritance: static properties/methods are inherited by subclasses.

---

## 4. Static methods & properties
- `static` keyword defines methods/properties on the class (constructor) itself, not instances.
```js
class MathUtil {
  static square(x) { return x * x; }
}

MathUtil.square(3); // 9
const m = new MathUtil();
// m.square -> undefined
```
- Use static members as utilities or factories:
```js
class User {
  constructor(name) { this.name = name; }
  static fromJSON(json) {
    const { name } = JSON.parse(json);
    return new User(name);
  }
}
```

---

## 5. Private fields & methods (`#`)
- Private fields use `#name` and are lexical to the class body. They are enforced at the language level.
```js
class Counter {
  #count = 0;                // private field
  increment() { this.#count++; }
  get value() { return this.#count; }
  #secret() { return 'shh'; } // private method
}
const c = new Counter();
c.increment();
c.value; // 1
// c.#count -> SyntaxError
```
- Private fields are not properties on the object's external shape; they are internal slots.
- Private methods and accessors are also supported:
```js
class Example {
  #x = 1;
  get #double() { return this.#x * 2; }
  callDouble() { return this.#double; }
}
```
- You cannot access `#` members from outside or from other objects, even of the same class. However, same-class lexical access (including subclasses) must declare their own private fields; `#` fields are *not* inherited.

---

## 6. Combining features: patterns & best practices

### Encapsulation + Getter/Setter
```js
class BankAccount {
  #balance = 0;
  deposit(amount) {
    if (amount <= 0) throw new Error('invalid');
    this.#balance += amount;
  }
  get balance() { return this.#balance; }
}
```

### Factory + static
```js
class Color {
  constructor(r,g,b) { this.r=r; this.g=g; this.b=b; }
  static fromHex(hex) {
    // parse #RRGGBB
    return new Color(...);
  }
}
```

### Mixins (simple pattern)
```js
const CanEat = Base => class extends Base {
  eat() { return 'eating'; }
};
class Mammal {}
class Dog extends CanEat(Mammal) {}
```

---

## 7. Common gotchas & subtleties
- `typeof class Foo {}` -> `"function"` (classes are functions).
- Class methods are not bound — use arrow functions in fields or manual binding if you need `this`.
```js
class Button {
  handleClick = () => { console.log(this); } // class field arrow
}
```
- Private fields are per-class; subclass cannot access parent `#` fields.
- Beware of accidental shared mutable static properties:
```js
class A { static cache = {}; } // same object for all subclasses unless overridden
```

---

## 8. Interview-style theory Qs (concise answers)

Q: How is `class` different from function constructor?
A: `class` uses prototype under the hood but provides clearer syntax, non-enumerable methods, and strict mode by default. It cannot be called without `new`.

Q: What happens if a subclass constructor doesn't call `super()`?
A: JS throws a ReferenceError when attempting to access `this` before `super()`.

Q: Are private fields (`#`) accessible via reflection?
A: No — `#` fields are not accessible via property names, `Object.keys`, or `Reflect`. They're stored in private slots.

Q: Do class fields run per-instance or on prototype?
A: Public/Private instance fields run per-instance (created during construction). Methods are on prototype unless declared as arrow function fields.

Q: Can static methods be overridden?
A: Yes — subclasses can define static methods that shadow parent static methods. `super` can be used within static methods to access parent static methods.

Q: Is `class` hoisted?
A: Class declarations are not hoisted like function declarations. They behave like `let`/`const` in temporal dead zone.

---

## 9. Coding interview questions (practical)

1. Implement a `Singleton` class in JS (ES6+).
```js
class Singleton {
  static #instance;
  constructor(val) {
    if (Singleton.#instance) return Singleton.#instance;
    this.val = val;
    Singleton.#instance = this;
  }
}
```

2. Implement a `Memoize` decorator using a static method.
```js
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const res = fn.apply(this, args);
    cache.set(key, res);
    return res;
  };
}
// usage: class X { expensive = memoize((n)=>{/*...*/}) }
```

3. Create an extendable `EventEmitter` class with `on`, `off`, `emit`.
```js
class EventEmitter {
  #listeners = new Map();
  on(event, fn) {
    const arr = this.#listeners.get(event) || [];
    arr.push(fn);
    this.#listeners.set(event, arr);
  }
  off(event, fn) {
    const arr = this.#listeners.get(event) || [];
    this.#listeners.set(event, arr.filter(f => f !== fn));
  }
  emit(event, ...args) {
    (this.#listeners.get(event) || []).slice().forEach(fn => fn(...args));
  }
}
```

---

## 10. Short cheat summary (quick recall)
- `class` = syntactic sugar over prototypes.
- Use `constructor` for initialization; `super()` required in derived class constructors.
- `static` members live on the class, not the instance.
- `#private` gives true privacy (language-level).
- Methods are on prototype — fields are per-instance.
- Avoid mutating shared static objects; prefer factory/static initializer patterns.

---

## 11. Further reading (keywords)
- "ECMAScript private fields", "class fields proposal", "class static blocks", "mixins in JS", "prototypes vs classes"

---

## 12. Practice tasks
- Convert a constructor-function codebase to `class` syntax.
- Implement `extend` utility that composes multiple mixins.
- Build a lightweight DI (dependency injection) container using static registries.

---

## End


# Advanced JS — `this` Keyword (Binding rules: default, implicit, explicit, new)

## Topic
Advanced JS

## Sub Topic
`this` Keyword — binding rules (default, implicit, explicit, new)

---

## Core explanation (concise)
In JavaScript, the value of `this` is determined at *call time* based on how a function is invoked. There are four classic binding rules to determine `this`:

1. **Default (or global) binding**  
   - When a function is invoked without any owner object (e.g., a plain function call), `this` falls back to the global object in non‑strict mode (`window` in browsers, `global` in Node). In strict mode `this` becomes `undefined`.  
   - Example:
     ```js
     function show() { return this; }
     show(); // global object (non-strict) or undefined (strict)
     ```

2. **Implicit binding (method invocation)**  
   - When a function is called as a property of an object (`obj.method()`), `this` is bound to the object to the *left of the dot* — the calling object.  
   - Example:
     ```js
     const obj = { name: 'Alice', greet() { return this.name; } };
     obj.greet(); // 'Alice'
     ```

3. **Explicit binding (call/apply/bind)**  
   - You can explicitly set `this` using `fn.call(obj, ...)`, `fn.apply(obj, ...)`, or create a permanently bound function with `fn.bind(obj)`. `call` and `apply` invoke immediately; `bind` returns a new function with `this` fixed.  
   - Example:
     ```js
     function show() { return this.name; }
     show.call({name: 'Bob'}); // 'Bob'
     const bound = show.bind({name: 'Cleo'}); bound(); // 'Cleo'
     ```

4. **`new` binding (constructor invocation)**  
   - When a function is invoked with `new`, JavaScript creates a fresh object and binds `this` to that new instance. If the constructor returns an object explicitly, that object is used instead.  
   - Example:
     ```js
     function Person(name) { this.name = name; }
     const p = new Person('Dana'); // this -> newly created object
     ```

### Priority of rules
`new` binding > explicit (`call`/`apply`/`bind`) > implicit (dot/owner) > default (global/undefined). `bind`ed functions can override later explicit `call`/`apply` attempts (bound `this` is fixed), and `new` has the highest precedence when combined with bound functions (a bound function used with `new` will ignore the bound `this` and use the newly created instance instead — but the behavior is nuanced).

---

## Practical pitfalls & important notes
- **Arrow functions** do **not** have their own `this`. They lexically capture `this` from the surrounding scope at the time they are defined (similar to lexical scoping of variables). Use arrow functions when you want to preserve the outer `this`.  
- **Strict mode** changes the default binding: plain function calls set `this` to `undefined` instead of the global object.  
- **Losing `this`** often happens when extracting a method reference (e.g., `const f = obj.method; f();` — `this` is lost; use `bind` or call via the object).  
- **Methods on prototypes** behave like implicit binding when invoked via an instance (`instance.method()`), binding `this` to the instance.

---

## Small cheat-table

| Invocation style | Example | `this` value |
|---|---:|---|
| Default | `fn()` | global (non-strict) / undefined (strict). citeturn0search0 |
| Implicit | `obj.fn()` | `obj`. citeturn0search0 |
| Explicit | `fn.call(obj)` / `fn.apply(obj)` / `fn.bind(obj)` | object passed. `bind` returns bound function. citeturn0search6turn0search4 |
| `new` | `new Fn()` | newly created instance object. citeturn0search0 |
| Arrow fn | `() => { ... }` | inherits lexical `this` from surrounding scope. citeturn0search7 |

---

## Interview-style theory questions (concise answers)

1. **What determines the value of `this` in JavaScript?**  
   The call-site. How a function is invoked (default, implicit, explicit, or with `new`) determines `this`. citeturn0search0

2. **How is `this` different in arrow functions?**  
   Arrow functions have no own `this`; they inherit it lexically from the enclosing scope at definition time. citeturn0search7

3. **What happens when you use `call`/`apply`/`bind`?**  
   `call`/`apply` explicitly set `this` for a single invocation. `bind` returns a new function permanently bound to the provided `this` value. citeturn0search4turn0search6

4. **Explain `new` binding and how it interacts with explicit binding.**  
   `new` creates a new object and binds `this` to it; `new` has higher precedence than implicit/default binding. Using `new` with a bound function can produce surprising behavior: a bound function used as a constructor will have `this` set to the new instance (the `bind`ed `this` is ignored for `new`). citeturn0search16turn0search6

5. **Why might `this` be `undefined` inside a function?**  
   Because code is running in strict mode and the function was invoked as a plain function (default binding), which sets `this` to `undefined`. citeturn0search10turn0search0

---

## Common interview coding questions (with short solutions / hints)

1. **Problem:** Given `const obj = { x: 1, getX() { return this.x; } }`, what is the result of `const f = obj.getX; f();` ?  
   **Answer / hint:** `undefined` (or global `x`) — because `f` is called as a plain function, losing implicit binding. Use `f.bind(obj)` or call `obj.getX()`.

2. **Problem:** How to borrow a method from another object?  
   **Answer / hint:** Use `call`/`apply`. e.g., `Array.prototype.slice.call(arguments)`.

3. **Problem:** Implement a `bind` polyfill (short version).  
   **Answer / hint:** Return a function that captures `thisArg` and uses `apply` with the original function; handle `new` by preserving prototype chain—interviewers expect awareness of constructor behavior.

4. **Problem:** Why does `this` inside an event listener refer to the element?  
   **Answer / hint:** Because DOM event handlers are called with the element as the `this` context (implicit binding by the DOM). Use arrow function to preserve outer `this`.

5. **Problem:** Fix code where a callback loses `this` (e.g., `array.map(obj.method)`).  
   **Answer / hint:** Use `array.map(obj.method.bind(obj))` or use an arrow wrapper: `array.map(item => obj.method(item))`.

---

## Short sample code snippets (for reference)

```js
// Implicit
const user = {
  name: 'Eve',
  say() { console.log(this.name); }
};
user.say(); // 'Eve'

// Default
function show() { console.log(this); }
show(); // window or undefined (strict)

// Explicit
function showName() { console.log(this.name); }
showName.call({name: 'Zed'}); // 'Zed'

// new
function Car(make) { this.make = make; }
const c = new Car('Honda'); // c.make === 'Honda'

// Arrow
const obj2 = {
  a: 10,
  fn: () => { console.log(this); } // lexical this (likely global or undefined)
};
```

---

## Further reading (authoritative)
- MDN — `this` in JavaScript. citeturn0search0  
- MDN — `Function.prototype.bind`. citeturn0search6  
- freeCodeCamp article on binding rules. citeturn0search4

---

## File
This content is available as a downloadable Markdown file.


# Advanced JS — call / apply / bind
**Topic:** Advanced JS  
**Sub Topic:** Call / Apply / Bind — method borrowing, explicit binding, currying

---

## 1. Quick definitions
- **`call(thisArg, ...args)`** — immediately calls the function with `this` set to `thisArg` and individual arguments. (Source: MDN).  
- **`apply(thisArg, argsArray)`** — immediately calls the function with `this` set to `thisArg` and arguments provided as an array (or array-like). (Source: MDN).  
- **`bind(thisArg, ...presetArgs)`** — returns a *new function* with `this` permanently bound to `thisArg` and optional preset leading arguments; does **not** call immediately. (Source: MDN).

---

## 2. When to use each
- Use **`call`** when you want to call a function and set `this`, passing arguments normally.  
- Use **`apply`** when you want to call a function and set `this` but you have arguments as an array (useful for `Math.max`/`Math.min` patterns before spread).  
- Use **`bind`** when you need a function with `this` fixed for later use (event handlers, callbacks) or to create a partially applied function.

---

## 3. Examples

### Basic call
```js
function greet(greeting, punctuation) {
  return `${greeting}, I'm ${this.name}${punctuation}`;
}
const person = { name: 'Ada' };
console.log(greet.call(person, 'Hello', '!')); // "Hello, I'm Ada!"
```

### Basic apply
```js
const nums = [5, 6, 2, 8];
console.log(Math.max.apply(null, nums)); // 8
// Modern alternative: Math.max(...nums)
```

### Basic bind (delayed call / preserving this)
```js
const obj = { x: 42, getX() { return this.x; } };
const unbound = obj.getX;
console.log(unbound()); // undefined (or global) in non-strict mode
const bound = unbound.bind(obj);
console.log(bound()); // 42
```

---

## 4. Method borrowing (useful pattern)
```js
const obj1 = { name: 'Alice', show() { return this.name; } };
const obj2 = { name: 'Bob' };

console.log(obj1.show.call(obj2)); // "Bob"  -- borrow obj1.show for obj2
```
`bind` is also used to permanently borrow a method:
```js
const showForBob = obj1.show.bind(obj2);
console.log(showForBob()); // "Bob"
```

---

## 5. Explicit binding vs implicit vs new
- **Implicit**: `obj.method()` → `this` is `obj`.  
- **Explicit**: using `call`/`apply`/`bind` to set `this`.  
- **`new` binding**: when a function is called with `new`, `this` becomes the newly created object; `bind` cannot change the `this` for constructor calls (a bound function used with `new` will ignore the bound `this` and behave like a constructor; see edge cases).

---

## 6. Currying and partial application with `bind`
```js
function multiply(a, b) { return a * b; }
const double = multiply.bind(null, 2); // partially-applies a = 2
console.log(double(8)); // 16
```
Notes:
- `bind` creates partially-applied functions by presetting leading arguments.  
- Currying (transforming `f(a,b,c)` into `f(a)(b)(c)`) is commonly implemented by hand or via utility functions — `bind` helps for partial application but doesn't by itself implement full curry behavior.

---

## 7. Polyfills / Implementations (concise)
**`call` polyfill (conceptual)**
```js
Function.prototype.myCall = function(thisArg, ...args) {
  thisArg = thisArg == null ? globalThis : Object(thisArg);
  const fnSymbol = Symbol();
  thisArg[fnSymbol] = this;
  const result = thisArg[fnSymbol](...args);
  delete thisArg[fnSymbol];
  return result;
};
```
**`bind` polyfill (concise)**
```js
Function.prototype.myBind = function(thisArg, ...presetArgs) {
  const fn = this;
  function bound(...laterArgs) {
    // if used as constructor, use new.target handling (omitted here for brevity)
    return fn.apply(thisArg, [...presetArgs, ...laterArgs]);
  }
  return bound;
};
```

---

## 8. Interview theory questions (short answers)
1. **Q:** What’s the difference between `call`, `apply`, and `bind`?  
   **A:** `call` and `apply` invoke the function immediately; `call` takes arguments separately, `apply` takes an array. `bind` returns a new function with `this` (and optional leading args) fixed; it does not invoke immediately. (MDN)

2. **Q:** How does `this` get determined in JavaScript?  
   **A:** Order of precedence: `new` binding (constructor) > explicit binding (call/apply/bind) > implicit binding (obj.method) > default (global/undefined in strict mode).

3. **Q:** Can `bind` be used to curry a function?  
   **A:** Yes for **partial application** (preset leading args). Full currying (one-arg functions) requires transforming the function; `bind` is a helpful tool but not a complete curry utility.

4. **Q:** What happens if you `bind` a function and then use it with `new`?  
   **A:** The bound `this` is ignored when a function is used as a constructor; the newly created object becomes `this`. (Edge cases exist.)

5. **Q:** Why use `apply` with `Math.max` historically?  
   **A:** `Math.max` accepts individual arguments; `apply` allowed passing an array of values before spread syntax (`...`) existed.

---

## 9. Coding interview questions (practice)
1. **Implement `Function.prototype.myCall` polyfill.** *(medium)*  
2. **Implement `Function.prototype.myBind` which preserves constructor behavior.** *(hard — watch `new` target and prototype links)*  
3. **Write a `curry` function that converts `f(a,b,c)` to `f(a)(b)(c)`.** *(medium-hard)*  
4. **Given an array of arrays, write a function to find the global maximum using `.apply` (no spread).** *(easy)*

---

## 10. References
- MDN: `Function.prototype.call`. citeturn0search0  
- MDN: `Function.prototype.apply`. citeturn0search1  
- MDN: `Function.prototype.bind`. citeturn0search2  
- Explanation/article: javascript.info — bind. citeturn0search15  
- freeCodeCamp — tutorial: apply/call/bind. citeturn0search18


# Topic : Advanced JS
# Sub Topic : Event Loop — microtask vs macrotask, queue order, async behavior

---

## Quick summary (one-liner)
The JS event loop repeatedly runs one macrotask, then drains the microtask queue completely, performs rendering steps (if needed), then picks the next macrotask — microtasks therefore run *before* the next macrotask and can starve macrotasks if they keep enqueuing more microtasks. citeturn0search0turn0search4

---

## Detailed explanation

### What is the event loop?
The event loop is the mechanism that lets JavaScript (single-threaded) interleave I/O, timers, UI events and scripts by repeatedly picking work (jobs/tasks) and executing it when the call stack is empty. Browsers and Node each implement an event loop variant defined by the HTML / runtime specs and their own scheduling rules. citeturn0search6turn0search9

### Tasks (macrotasks) vs Microtasks (jobs)
- **Macrotasks (tasks)**: callbacks scheduled by `setTimeout`, `setInterval`, UI events, I/O callbacks, and other platform-level task sources. They live in one or more task queues (commonly called macrotask queues). citeturn0search2turn0search4  
- **Microtasks (jobs)**: Promise `.then/.catch/.finally` callbacks, `queueMicrotask()`, and `MutationObserver` callbacks. In Node, `process.nextTick()` is a separate, higher-priority queue (even before microtasks). Microtasks live in a single microtask queue that is drained to exhaustion after each macrotask completes. citeturn0search3turn0search11turn0search17

### The per-iteration ordering (browser-style)
A simplified iteration of the event loop in browsers looks like:
1. Pick the oldest macrotask and run it (this may be the "global script" at startup).  
2. When that macrotask finishes (call stack empty), run **all** microtasks, in FIFO order, including any microtasks those microtasks queue, until the microtask queue is empty.  
3. Perform rendering/layout/paint if required.  
4. Repeat: pick next macrotask. citeturn0search0turn0search4

Because the microtask queue is drained fully between macrotasks, promises and other microtasks run *before* the next `setTimeout` callback or other macrotask.

### Important consequences & gotchas
- **Promise callbacks beat timers**: `Promise.resolve().then(...)` runs before `setTimeout(..., 0)` scheduled callbacks that are in the next macrotask. Example: the `then` callbacks execute before `setTimeout` callbacks. citeturn0search4
- **Microtask starvation of rendering**: If microtasks keep enqueuing more microtasks (or are extremely long), the browser can delay rendering and starve macrotasks — causing jank. Do _not_ busy-loop the microtask queue. citeturn0search0
- **Reentrancy & sync work**: If a macrotask synchronously re-enters (e.g., via synchronous postMessage handlers or certain DOM APIs), the spec uses a "currently running task" marker to avoid surprises. The HTML spec defines these behaviors precisely. citeturn0search6
- **Node differences**: Node's scheduling model adds more queues: `process.nextTick()` (highest priority), then microtasks, then timers, I/O callbacks, check/close phases, etc. So `process.nextTick()` callbacks run *even before* Promise microtasks in many Node versions — an important interview nuance. (Check Node docs for the precise order for the Node version you're targeting.) citeturn0search17

---

## Small annotated examples

### Example 1 — order: sync → microtasks → macrotasks
```js
console.log('script start');

setTimeout(() => console.log('timeout'), 0);

Promise.resolve().then(() => console.log('promise then'));

console.log('script end');
```
Output:
```
script start
script end
promise then
timeout
```
Explanation: synchronous lines run first, then microtasks (.then), then macrotask (setTimeout). citeturn0search4

### Example 2 — microtasks can enqueue microtasks
```js
Promise.resolve()
  .then(() => {
    console.log('p1');
    return Promise.resolve().then(() => console.log('p1.1'));
  })
  .then(() => console.log('p2'));

console.log('sync end');
```
Possible output:
```
sync end
p1
p1.1
p2
```
All promise callbacks run as part of the microtask draining before the next macrotask.

### Example 3 — Node's `process.nextTick`
```js
Promise.resolve().then(() => console.log('promise'));
process.nextTick(() => console.log('nextTick'));
```
On Node, typical output:
```
nextTick
promise
```
because `process.nextTick` runs with higher priority. Always verify against your Node version. citeturn0search17

---

## Interview-style theory questions (concise answers)

1. **Q:** What's the difference between macrotasks and microtasks?  
   **A:** Macrotasks are scheduled work from timers, events, I/O; microtasks are jobs like Promise callbacks and `queueMicrotask`. Microtasks are drained completely between macrotasks. citeturn0search4

2. **Q:** Why do `Promise.then` callbacks run before `setTimeout(..., 0)`?  
   **A:** Because `.then` handlers are microtasks (higher priority) and the event loop drains the microtask queue before running the next macrotask. citeturn0search4

3. **Q:** Can microtasks starve the UI rendering?  
   **A:** Yes — if microtasks keep enqueuing more microtasks or run for long, rendering/layout can be delayed until the microtask queue empties. Avoid long-running microtasks. citeturn0search0

4. **Q:** Where does `async/await` fit?  
   **A:** `await` pauses the async function and schedules the continuation as a microtask (so code after `await` runs as a microtask). citeturn0search4

5. **Q:** How is Node's event loop ordering different?  
   **A:** Node has extra phases and queues (timers, pending callbacks, idle/prepare, poll, check, close) and a `process.nextTick` queue that runs before microtasks — so ordering differs from browsers. Check Node docs for exact phase ordering per version. citeturn0search17

---

## Short coding-interview problems (with answers)

1. **Problem:** Explain output order and why:
```js
setTimeout(() => console.log('A'), 0);
Promise.resolve().then(() => console.log('B'));
console.log('C');
```
**Answer:** `C` → `B` → `A`. Sync `console.log('C')` runs first, then microtask `B`, then macrotask `A`. citeturn0search4

2. **Problem:** Create a function `delay(ms)` returning a promise and use it to run `console.log('done')` after `0` ms but *after* all current microtasks.  
**Solution:**
```js
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// to ensure 'after microtasks' you can:
Promise.resolve().then(() => {}).then(() => console.log('after microtasks?')); // microtask
// or use:
delay(0).then(() => console.log('done after macrotask'));
```
Explanation: `setTimeout(..., 0)` places work in macrotask; to run after microtasks, schedule via macrotask (setTimeout) or await a delay. citeturn0search4

3. **Problem:** Prevent microtask starvation while doing many small async updates in the browser.  
**Approach:** Batch work into macrotasks (use `setTimeout` or `requestAnimationFrame`) and keep microtasks light. Use `requestAnimationFrame` when work is UI-related so rendering can occur. citeturn0search0

---

## Further reading (authoritative)
- HTML Standard — Event loops & microtask queue. citeturn0search6  
- MDN — Microtasks guide and Event Loop docs. citeturn0search0turn0search3  
- Jake Archibald — "Tasks, microtasks, queues and schedules" (great conceptual article). citeturn0search2  
- javascript.info event-loop article (clear examples). citeturn0search4

---

## TL;DR checklist (for interview)
- Synchronous code runs first.  
- Microtasks (Promise.then, queueMicrotask) run *after* the current macrotask finishes and *before* the next macrotask.  
- Microtasks can enqueue microtasks. Run until empty.  
- Node has `process.nextTick` (higher priority) and extra phases.  
- Avoid long microtasks to keep UI responsive. citeturn0search4turn0search17

---


# Topic : Advanced JS
## Sub Topic : Promises & Async/Await

---

## 1. Overview
This cheat-sheet covers advanced usage of JavaScript Promises and `async/await`. It explains promise chaining, error handling, and the differences between `Promise.all`, `Promise.allSettled`, `Promise.race`, and `Promise.any`. Includes interview-style theory questions with concise answers and related coding problems + solutions.

---

## 2. Promise fundamentals (quick recap)
- A **Promise** represents an eventual value or failure.
- States: **pending → fulfilled** or **rejected**.
- Constructor: `new Promise((resolve, reject) => { ... })`
- `.then(onFulfilled, onRejected)` returns a new promise (enables chaining).
- `.catch(onRejected)` is sugar for `.then(null, onRejected)`.
- `.finally(fn)` runs regardless of outcome; it does **not** change the resolved value (but can affect timing if it returns a promise).

---

## 3. Promise chaining — patterns & best-practices

### Basic chaining
```js
doStep1()
  .then(result1 => doStep2(result1))
  .then(result2 => doStep3(result2))
  .then(final => console.log('done', final))
  .catch(err => console.error('error at any step:', err));
```

Key points:
- Always return a value or promise from `.then`.
- If `.then` throws or returns a rejected promise, the next `.catch` will handle it.
- Synchronous returns in `.then` are wrapped in resolved promises automatically.

### Flattening vs nesting
Bad:
```js
doStep1((a) => {
  doStep2(a, (b) => {
    doStep3(b, (c) => {
      // callback hell
    });
  });
});
```

Good: chain promises to keep flat, readable flows.

### Sequential async with `for` loops
When you need sequential execution in a loop:
```js
async function processInOrder(items) {
  for (const item of items) {
    await doSomething(item); // sequential
  }
}
```

If tasks are independent and can run in parallel, use concurrency patterns (see Promise.all, below).

---

## 4. Error handling patterns

### Centralized catch
Place `.catch` at the end of the chain to handle errors from any previous promise:
```js
fetchA()
  .then(fetchB)
  .then(process)
  .catch(err => console.error('caught', err));
```

### Per-step handling
If you want different handling per step:
```js
fetchA()
  .then(a => fetchB(a).catch(err => handleBError(err, a)))
  .then(bOrFallback => process(bOrFallback))
  .catch(err => console.error('final catch', err));
```

### Rethrow when appropriate
If you handle an error but want upstream to know:
```js
somePromise()
  .catch(err => {
    if (shouldRecover(err)) return recover();
    throw err; // rethrow for outer catch
  })
  .catch(finalErr => {});
```

### `finally` caveat
`finally` runs regardless. If `finally` returns a promise that rejects, it overrides previous resolution.

---

## 5. Promise combinators — `all`, `allSettled`, `race`, `any`

### 5.1 `Promise.all(iterable)`
- Waits for **all** promises to **fulfill**.
- If any promise rejects, `Promise.all` rejects immediately with that reason.
- Returns an array of results in input order.
- Use when all results are required.

```js
const [u, v] = await Promise.all([fetch(url1), fetch(url2)]);
```

### 5.2 `Promise.allSettled(iterable)`
- Waits for **all** promises to **settle** (either fulfilled or rejected).
- Never rejects; returns array of `{status: 'fulfilled'|'rejected', value|reason}`.
- Use when you need full outcomes for reporting or partial success.

```js
const results = await Promise.allSettled(tasks);
// examine results[i].status
```

### 5.3 `Promise.race(iterable)`
- Settles as soon as **any** promise settles (fulfills or rejects).
- Useful for timeouts, first-to-respond scenarios.
- Caveat: if the fastest promise rejects, the race rejects.

Timeout example:
```js
function withTimeout(promise, ms) {
  const timeout = new Promise((_, reject) => setTimeout(() => reject(new Error('timed out')), ms));
  return Promise.race([promise, timeout]);
}
```

### 5.4 `Promise.any(iterable)` (ES2021)
- Resolves as soon as **any** promise fulfills.
- If all promises reject, `Promise.any` rejects with an `AggregateError`.
- Useful when you want the first successful result and can ignore failures.

```js
const firstSuccess = await Promise.any([p1, p2, p3]);
```

---

## 6. Async/Await — clearer control flow

### Basic usage
```js
async function main() {
  try {
    const a = await fetchA();
    const b = await fetchB(a);
    return process(a, b);
  } catch (err) {
    console.error('error', err);
  }
}
```

Key points:
- `await` pauses the async function until the promise settles.
- `await` only works inside `async` functions (or top-level in supported environments).
- `await` unwraps the fulfilled value or throws the rejection (so use try/catch).

### Parallelism with await
Bad (sequential but looks simple):
```js
const a = await op1();
const b = await op2(); // waits for op1 to finish
```

Good (run in parallel, then await results):
```js
const p1 = op1();
const p2 = op2();
const [a, b] = await Promise.all([p1, p2]);
```

### Error handling
Use try/catch for expected errors. For multiple awaited operations where one failure shouldn't cancel others, combine with `allSettled` or capture errors per promise.

---

## 7. Common pitfalls & gotchas

- **Unhandled promise rejections**: Always handle rejections or attach a `.catch`.
- **Mixing callback-style APIs and promises**: wrap callbacks with `new Promise(...)` carefully.
- **Forgetting to return in `.then`**: causes the next `.then` to run too early with `undefined`.
- **`async` functions always return a promise** — even if they return non-promise values.
- **`Promise.all` short-circuits on the first rejection**, potentially leaving other tasks running — be mindful of side effects.
- **`finally` behavior**: its returned promise can override previous outcomes.

---

## 8. Performance / resource considerations

- Avoid creating unnecessary long-lived promises that hold resources.
- When firing many requests, throttle/concurrency-limit (e.g., p-limit) instead of `Promise.all` over thousands of items.
- For retry logic, implement exponential backoff and jitter.

---

## 9. Interview-style theory questions (concise answers)

1. **Q:** What is the difference between microtasks and macrotasks in JS?  
   **A:** Microtasks (e.g., promise callbacks) run after the current script but before the next macrotask and before rendering; macrotasks include setTimeout, setInterval, I/O, and UI events.

2. **Q:** Why does `Promise.all` preserve input order in its output?  
   **A:** It collects results into an array using the original indices regardless of completion order; the combinator maps fulfilled values back to their positions.

3. **Q:** How does `async/await` affect the call stack?  
   **A:** `await` suspends the async function without blocking the thread; the rest of the function runs later as a microtask, so call stack unwinds and then resumes.

4. **Q:** When would you use `Promise.allSettled` instead of `Promise.all`?  
   **A:** When you need outcomes of all tasks regardless of failures (partial success reporting) and don't want a single rejection to short-circuit.

5. **Q:** What happens if you `await` a non-promise value?  
   **A:** The value is wrapped in a resolved promise; `await` returns the value immediately.

6. **Q:** What's an `AggregateError`?  
   **A:** Error type thrown by `Promise.any` when all promises reject; contains `errors` property with individual rejection reasons.

7. **Q:** How can you implement timeouts for fetch requests?  
   **A:** Use `AbortController` (preferred) or `Promise.race` with a timeout rejecter.

8. **Q:** Explain "unhandled promise rejection" and its consequences.  
   **A:** If a promise rejects and no handler is attached, it's an unhandled rejection; in Node.js or browsers it can be logged or cause the process to terminate depending on settings.

9. **Q:** How to cancel an ongoing async operation?  
   **A:** Use cancellation primitives like `AbortController` for fetch or design API with cancel tokens. Promises themselves do not support cancellation.

10. **Q:** Why avoid `await` inside `Array.prototype.forEach`?  
    **A:** `forEach` doesn't handle async callbacks; `await` inside doesn't make the outer function wait—use `for..of` or `Promise.all` with `map`.

---

## 10. Related coding problems (with solutions)

### Problem 1 — retry with exponential backoff
**Task:** Implement `retry(fn, retries, delay)` where `fn` returns a promise. On failure, retry with exponential backoff.

```js
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function retry(fn, retries = 3, delay = 100) {
  let attempt = 0;
  while (attempt <= retries) {
    try {
      return await fn();
    } catch (err) {
      if (attempt === retries) throw err;
      const backoff = delay * Math.pow(2, attempt);
      await wait(backoff + Math.random() * 50); // small jitter
      attempt++;
    }
  }
}
```

### Problem 2 — run N promises with concurrency limit
**Task:** Given many async tasks, run at most `limit` concurrently.

```js
async function runWithConcurrency(tasks, limit = 5) {
  const results = [];
  const executing = new Set();

  for (const task of tasks) {
    const p = Promise.resolve().then(() => task());
    results.push(p);

    executing.add(p);
    const clean = () => executing.delete(p);
    p.then(clean).catch(clean);

    if (executing.size >= limit) {
      await Promise.race(executing);
    }
  }
  return Promise.all(results); // wait for all to finish
}
```

### Problem 3 — convert callback API to promise (promisify)
```js
function promisify(fn) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      fn(...args, (err, result) => {
        if (err) return reject(err);
        resolve(result);
      });
    });
  };
}
```

### Problem 4 — timeout wrapper using AbortController (fetch)
```js
async function fetchWithTimeout(url, options = {}, ms = 5000) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), ms);
  try {
    const res = await fetch(url, {...options, signal: controller.signal});
    return res;
  } finally {
    clearTimeout(id);
  }
}
```

---

## 11. Quick reference snippets

- `Promise.all` => fail-fast, returns array of values.
- `Promise.allSettled` => returns array of `{status, value/reason}`.
- `Promise.race` => settle on first settled promise.
- `Promise.any` => resolve on first fulfillment, reject with `AggregateError` if all reject.
- `async function` => always returns a promise.

---

## 12. Recommended further reading
- MDN docs on Promise and async functions.
- Articles about concurrency patterns and backpressure in JS (search "concurrency limit JavaScript", "AbortController").

---

## 13. License
This cheat-sheet is provided as-is for interview prep and learning.



# Advanced JS — Error Handling
**Topic:** Advanced JS  
**Sub Topic:** Error Handling — `try`/`catch`/`finally`, custom errors, stack traces

---

## Summary (short)
This note covers:
- `try` / `catch` / `finally` behavior and patterns (including control-flow gotchas)
- Throwing: best practices (`Error` instances, `cause`, avoiding throwing primitives)
- Custom error classes and how to extend `Error` safely
- Stack traces: structure, `Error.prototype.stack`, preserving stacks when wrapping errors
- Async error handling: Promises + `catch` + `finally`, `async/await` patterns
- Interview-style theory questions with concise answers
- Related coding problems with sample solutions

---

## 1. `try` / `catch` / `finally` — mechanics & examples

### Basic form
```js
try {
  // code that might throw
} catch (err) {
  // handle error; `err` is the thrown value
} finally {
  // always runs (even if `return`/`throw` happened)
}
```

Important notes:
- `finally` runs regardless of whether the `try` block threw an exception or not — even if a `return` happened inside `try` or `catch`. The value returned by `try`/`catch` can be overridden by a `return` inside `finally`.
- If both `catch` and `finally` throw, the exception from `finally` wins (it becomes the propagated exception).
- `catch` will only run if an exception is thrown in `try` or a nested call; synchronous only. For async operations you must `await` or handle promise rejections separately.

Example — `finally` with return override:
```js
function test() {
  try {
    return 'from try';
  } catch (e) {
    return 'from catch';
  } finally {
    return 'from finally'; // this value is returned
  }
}
console.log(test()); // "from finally"
```

(Reference: MDN `try...catch` behavior).  
---

## 2. Throwing values — best practices

- You *can* throw any value (`throw 42`, `throw "oops"`, `throw obj`), but **always prefer throwing `Error` instances** or subclasses. Reasons:
  - `Error` instances have a `.name`, `.message`, and `.stack` (useful for debugging).
  - `instanceof Error` checks work for Error-derived classes.
  - Consistent error shapes simplify handling & logging. (See MDN and community guidance.)
```js
throw new Error('Bad things happened');
```

- `Error` constructor accepts `message` and (in modern runtimes) an options object `{ cause }` to attach the original cause when wrapping errors:
```js
throw new Error('Failed to parse', { cause: originalError });
```

(References: MDN `throw`, MDN `Error`, best-practice discussions).  
---

## 3. Custom Error classes

Prefer `class`-based inheritance from `Error`. Minimal pattern:

```js
class MyError extends Error {
  constructor(message, options) {
    super(message, options); // preserves message and cause
    this.name = this.constructor.name; // optional—gives nicer name
    // maintain proper prototype chain automatically in ES6 classes
  }
}
```

Edge cases / tips:
- When transpiling to older targets, ensure prototype chain is set properly. Native `class` does the right thing in modern engines.
- Use `options.cause` when wrapping another error to keep causal chain visible.
- Create error hierarchies for domains (e.g., `HttpError` → `HttpTimeoutError`) to allow `instanceof` checks.

Example with cause:
```js
try {
  // something
} catch (orig) {
  throw new MyError('Higher-level message', { cause: orig });
}
```

(References: javascript.info custom errors; MDN `Error` showing `cause`).  
---

## 4. Stack traces — read, preserve, and present

- Most JS engines provide `error.stack` as a string. The exact format varies across browsers and Node.js. Treat it as a debugging aid, not a spec-stable API.
- In Node, you can use `Error.captureStackTrace(target)` to create a stack trace on an object.
- When wrapping errors (catch & throw new), if you don't pass the original `cause`, you may lose the original stack. Use the `cause` option or attach the original error to a property like `err.cause` or `err.originalError`. Example:
```js
try {
  something();
} catch (e) {
  throw new Error('Failed to do something', { cause: e });
}
```
- For libraries and logs, include `error.stack` when logging so location info is preserved.

(References: MDN `Error.prototype.stack`; Node-specific practices & StackOverflow examples).  
---

## 5. Async error handling

### Promises
- Use `.catch()` for promises or async/await with try/catch.
- `Promise.prototype.finally()` runs when the promise settles (fulfilled or rejected). It does not receive the promise result; it's for cleanup.
```js
someAsync()
  .then(result => doWork(result))
  .catch(err => handle(err))
  .finally(() => cleanup());
```
### `async/await`
```js
async function run() {
  try {
    const value = await asyncOp();
  } catch (err) {
    // handle both sync and awaited rejection
  } finally {
    // cleanup
  }
}
```
Note: If you await without try/catch, unhandled rejections may occur — prefer structured handling in top-level or use global handlers in Node.

(References: MDN `Promise.prototype.finally`, MDN `catch`).  
---

## 6. Logging & observability recommendations

- Always log `error.stack` (if available) alongside structured metadata (user id, request id).
- For public APIs, avoid leaking internal stack traces to end-users — sanitize messages for clients.
- Consider mapping common errors to HTTP status codes or domain codes for visibility.
- Use `Error` `name` (or custom properties) to programmatically distinguish error types rather than parsing message strings.

---

## 7. Interview-style theory questions (concise answers)

1. **Q:** What does `finally` do if `try` has a `return`?  
   **A:** `finally` executes and its `return` (if present) overrides the earlier `return`. `finally` always runs before leaving the `try/catch` block. (MDN)

2. **Q:** Why prefer `throw new Error('msg')` over `throw 'msg'`?  
   **A:** `Error` instances provide `name`, `message`, and `stack` and behave predictably with `instanceof`. Throwing primitives is poor form.

3. **Q:** How to preserve original stack when wrapping errors?  
   **A:** Use the `cause` option (`new Error(msg, { cause: original })`) or attach the original error to a property on the new error so the chain remains discoverable.

4. **Q:** How to handle async errors in `Promise.all`?  
   **A:** `Promise.all` rejects on the first rejection. Use `Promise.allSettled` to see all results, or wrap each promise to never reject (return object with status).

5. **Q:** How to create a custom error type?  
   **A:** Extend `Error` via `class MyError extends Error { constructor(msg, opts) { super(msg, opts); this.name = 'MyError'; } }`.

6. **Q:** Is `Error.stack` standardized?  
   **A:** No — it's broadly supported but non-standard in shape; treat it as implementation-defined.

---

## 8. Coding interview problems (with solutions)

### Problem 1 — Safe Promise aggregator
Return all results with their statuses (like `allSettled`) but also include reason stacks if present.
```js
async function allWithStacks(promises) {
  const wrapped = promises.map(p => 
    Promise.resolve(p)
      .then(value => ({ status: 'fulfilled', value }))
      .catch(err => ({ status: 'rejected', reason: err, stack: err?.stack }))
  );
  return Promise.all(wrapped);
}
```

### Problem 2 — Custom HTTP error
```js
class HttpError extends Error {
  constructor(statusCode, message, options) {
    super(message, options);
    this.name = 'HttpError';
    this.statusCode = statusCode;
  }
}
```

### Problem 3 — Wrap error preserving original
```js
function wrapError(fn) {
  try {
    return fn();
  } catch (e) {
    const err = new Error('Wrapper failure', { cause: e });
    // preserve original as property (for older engines)
    err.original = e;
    throw err;
  }
}
```

---

## 9. Quick cheat-sheet / TL;DR

- Prefer `throw new Error()`; never throw primitives in production-level code.
- Use `finally` for cleanup — it always runs.
- Extend `Error` for custom types; set `name`.
- Use `Error` `cause` or attach original error to preserve stack when wrapping.
- For promises, use `.catch()` + `.finally()` or `try/catch` with `async/await`.
- Log stacks, but don't leak them to public clients.

---

## 10. Further reading / authoritative sources
- MDN `try...catch` / `throw` / `Error` / `Promise.prototype.finally`.  
- `javascript.info` guides on custom errors.  
- Node.js docs for `Error.captureStackTrace()` and best practices.

---

*Generated on: Advanced JS Error Handling — concise cheat-sheet.*

# Advanced JavaScript – Iterators & Generators

## Topic: Iterators & Generators  
## Sub Topic: Symbol.iterator, for...of, yield, generator use cases

---

## Iterators in JavaScript

An *iterator* is an object that follows the iterator protocol:  
it must have a `next()` method that returns `{ value, done }`.

### Symbol.iterator
Every object that wants to be iterable (usable in `for...of`, spread syntax, etc.) must implement `Symbol.iterator`.

```js
const obj = {
  data: [10, 20, 30],
  [Symbol.iterator]() {
    let i = 0;
    return {
      next: () => ({
        value: this.data[i],
        done: i++ >= this.data.length
      })
    };
  }
};

for (const num of obj) {
  console.log(num);
}
```

---

## for...of Loop

`for...of` works only on iterable objects (arrays, strings, maps, sets, custom iterables).

```js
for (const val of ["a", "b", "c"]) {
  console.log(val);
}
```

---

## Generators

Generators are special functions marked by `function*`.  
They *yield* values one at a time and pause/resume execution.

```js
function* generatorExample() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = generatorExample();
gen.next(); // { value: 1, done: false }
```

### yield Keyword
`yield` pauses generator execution and returns a value.

```js
function* idGenerator() {
  let id = 0;
  while (true) {
    yield id++;
  }
}
```

---

## Generator Use Cases

### Lazy Evaluation (infinite sequences)
```js
function* naturals() {
  let n = 1;
  while (true) yield n++;
}
```

### Custom Iterables
```js
const range = {
  start: 1,
  end: 5,
  *[Symbol.iterator]() {
    for (let i = this.start; i <= this.end; i++) yield i;
  }
};
```

### Async Flow Control (before async/await era)
Generators were used with libraries like `co()`.

### Stateful Iteration
```js
function* counter() {
  let c = 0;
  while (true) {
    const inc = yield c;
    if (inc) c += inc;
    else c++;
  }
}
```

---

## Theory-Based Interview Q&A

### What is an iterator?
An object with a `next()` method returning `{ value, done }`.

### What is Symbol.iterator used for?
It defines how an object becomes iterable for `for...of`.

### Difference between iterator and iterable?
Iterable implements `Symbol.iterator`.  
Iterator implements `next()`.

### Are generators iterable?
Yes, generators implement both iterator and iterable protocols.

### What does yield do?
Pauses generator execution and returns a value.

### Can generators be infinite?
Yes, they support lazy infinite sequences.

---

## Coding Interview Questions

### Implement a custom iterator for Fibonacci numbers.
```js
const fibonacci = {
  [Symbol.iterator]() {
    let a = 0, b = 1;
    return {
      next() {
        const value = a;
        [a, b] = [b, a + b];
        return { value, done: false };
      }
    };
  }
};

for (const num of fibonacci) {
  if (num > 50) break;
  console.log(num);
}
```

### Implement a range generator.
```js
function* range(start, end, step = 1) {
  for (let i = start; i <= end; i += step) {
    yield i;
  }
}
```

### Convert a callback-based function into a generator flow.
```js
function* asyncFlow() {
  const data = yield fetchData();
  console.log(data);
}
```

---

## End of Cheat Sheet  

# Advanced JS — Symbol & BigInt

**Topic:** Advanced JS  
**Sub Topic:** Symbol & BigInt

---

## Overview

This cheat-sheet covers JavaScript `Symbol` (unique property keys, well‑known symbols, registry) and `BigInt` (arbitrary‑precision integers), with examples, interview-style theory questions + answers, and coding problems. Use the examples directly in Node or browser consoles.

---

## Symbol (detailed)

### What is a Symbol?
A `Symbol` is a primitive value that is guaranteed to be unique. It is commonly used as an object property key when you want a property that won't collide with other keys and is skipped by many enumeration mechanisms. See MDN for full reference.  
(Reference: MDN Symbol).  

### Creating Symbols
```js
const s1 = Symbol('desc'); // unique every time
const s2 = Symbol('desc');
console.log(s1 === s2); // false

const g = Symbol.for('app.name'); // global symbol registry
const g2 = Symbol.for('app.name');
console.log(g === g2); // true
```

### Symbol properties as object keys
Symbol-keyed properties are not returned by `Object.keys()` or `for...in`. Use `Object.getOwnPropertySymbols()` or `Reflect.ownKeys()` to read them.
```js
const sym = Symbol('hidden');
const obj = { [sym]: 42, visible: 'yes' };

console.log(Object.keys(obj)); // ["visible"]
console.log(Object.getOwnPropertySymbols(obj)); // [ Symbol(hidden) ]
console.log(Reflect.ownKeys(obj)); // ["visible", Symbol(hidden)]
```

### Non-enumerability & JSON
Symbol-keyed properties are skipped during JSON serialization and most enumeration. `JSON.stringify()` ignores symbol properties. Use explicit extraction if you need to serialize symbol values.

### Well-known Symbols (metaprogramming hooks)
These are symbols the engine looks for to implement protocols. Useful ones:
- `Symbol.iterator` — makes an object iterable for `for...of`. citeturn0search7
- `Symbol.toStringTag` — customize `Object.prototype.toString()` output. citeturn0search4
- `Symbol.toPrimitive` — control primitive coercion.
- `Symbol.hasInstance`, `Symbol.match`, `Symbol.replace`, `Symbol.search`, etc. (all exposed via `Symbol` static properties). citeturn0search0

### Global symbol registry
`Symbol.for(key)` stores/returns symbols from a runtime-wide registry; `Symbol.keyFor(symbol)` retrieves a key for a symbol from the registry. Useful for cross-module shared keys. citeturn0search19

### Common pitfalls
- You cannot use `new Symbol()` — `Symbol` is not a constructor.
- Converting a Symbol to string directly throws if you coerce implicitly; use `String(sym)` or `sym.toString()`.
- Symbol properties are not hidden security-wise — they're discoverable with `Object.getOwnPropertySymbols()`.

---

## BigInt (detailed)

### What is BigInt?
`BigInt` is an integer primitive that can represent arbitrarily large integers (limited by memory), introduced to handle integers beyond `Number.MAX_SAFE_INTEGER`. Create with `n` suffix or `BigInt()` constructor. See MDN for reference. citeturn0search1

### Creating BigInts
```js
const a = 9007199254740991n; // literal with 'n'
const b = BigInt("123456789012345678901234567890");
```

### Arithmetic & types
- BigInts support `+ - * / % **` with other BigInts.
- You cannot mix `Number` and `BigInt` directly in arithmetic: `1n + 2` throws `TypeError`. Convert explicitly.  
```js
1n + BigInt(2); // 3n
Number(1n) + 2; // 3
```

### Comparisons
- `==` between Number and BigInt will coerce for numeric comparison (e.g., `1 == 1n` is true), but `===` is false because types differ.

### JSON & serialization
`JSON.stringify()` throws on encountering BigInt without custom serialization (`TypeError: BigInt value can't be serialized in JSON`). Use `.toString()` or a replacer to serialize. citeturn0search12

### Typed arrays & BigInt
There are typed arrays for BigInt like `BigInt64Array` / `BigUint64Array` for platform-sized 64-bit integers. Use when interoperating with binary formats or WebAssembly. citeturn0search18

### Edge cases & gotchas
- Exponentiation with negative BigInt exponent is invalid and throws.
- Some libraries and older runtimes may not support BigInt — check compatibility.

---

## Quick examples

### Custom iterable using Symbol.iterator
```js
const range = {
  from: 1,
  to: 3,
  [Symbol.iterator]() {
    let current = this.from;
    const end = this.to;
    return {
      next() {
        if (current <= end) {
          return { value: current++, done: false };
        }
        return { value: undefined, done: true };
      }
    };
  }
};

for (const v of range) console.log(v); // 1 2 3
```

### BigInt in practice (factorial for large n)
```js
function factorialBig(n){
  let res = 1n;
  for (let i = 2n; i <= BigInt(n); i++) res *= i;
  return res;
}
console.log(factorialBig(30)); // big integer
```

---

## Interview-style theory questions (concise answers)

1. **Q:** What's a Symbol and why use it?  
   **A:** A primitive for unique keys to avoid collisions and enable metaprogramming hooks (well-known symbols). citeturn0search0

2. **Q:** Difference between `Symbol()` and `Symbol.for()`?  
   **A:** `Symbol()` creates a new unique symbol; `Symbol.for(key)` uses a global registry and returns the same symbol for the same key. citeturn0search19

3. **Q:** Are symbol properties enumerable?  
   **A:** Not via `Object.keys` or `for...in`; use `Object.getOwnPropertySymbols()` or `Reflect.ownKeys()`.

4. **Q:** Name three well-known symbols and their use.  
   **A:** `Symbol.iterator` (iteration), `Symbol.toPrimitive` (coercion), `Symbol.toStringTag` (custom type tag). citeturn0search7turn0search4

5. **Q:** What is BigInt and when should you use it?  
   **A:** A primitive for arbitrary-size integers; use when numbers exceed `Number.MAX_SAFE_INTEGER` or you need exact integer math. citeturn0search1

6. **Q:** Can you mix `Number` and `BigInt` in arithmetic?  
   **A:** No — mixing throws `TypeError`. Convert explicitly.

7. **Q:** How to serialize BigInt to JSON?  
   **A:** Convert to string (e.g., `big.toString()`) or provide a `JSON.stringify` replacer that converts BigInts.

8. **Q:** Is `1n === 1` true?  
   **A:** No; `==` may coerce but `===` is false (different types).

9. **Q:** Can `Symbol`s be used as object property names in JSON?  
   **A:** No; symbol-keyed properties are ignored by `JSON.stringify()`.

10. **Q:** How to expose a value to `for...of`?  
    **A:** Implement `[Symbol.iterator]()` that returns an iterator object (with `next()`).

---

## Coding interview questions (with hints / short answers)

1. **Implement a custom iterable range (from, to).**  
   Hint: use `Symbol.iterator`. (See example above.)

2. **Write a function to deep-clone an object including symbol properties.**  
   Hint: copy `Object.getOwnPropertyNames(obj)` + `Object.getOwnPropertySymbols(obj)` and preserve descriptors.

3. **Serialize an object containing BigInt values to JSON-safe form and restore it.**  
   Hint: use `JSON.stringify(obj, replacer)` where replacer maps BigInt → `{"__bigint": big.toString()}` and a reviver in `JSON.parse`.

4. **Implement `memoize` that uses `Symbol` to cache internal data without leaking into enumeration.**  
   Hint: create a unique symbol per function and store cache on the function object: `fn[cacheSym] = new Map()`.

5. **Given a very large integer as string, compute its mod with a 32-bit integer (use BigInt).**  
   Hint: `BigInt(str) % BigInt(2**32)`.

6. **Find if an object is iterable.**  
   Hint: check `typeof obj[Symbol.iterator] === 'function'`.

7. **Make an object that returns different behavior when used in numeric vs string contexts.**  
   Hint: implement `Symbol.toPrimitive` with hint handling.

8. **Compare two objects with symbol-keyed properties for equality.**  
   Hint: compare symbol lists and corresponding values using `Object.getOwnPropertySymbols()`.

---

## References / Further reading
- MDN: `Symbol` reference. citeturn0search0  
- MDN: `BigInt` reference. citeturn0search1  
- MDN: `Symbol.iterator` (iterables). citeturn0search7  
- MDN: `Symbol.for` and global registry. citeturn0search19  
- MDN: BigInt JSON serialization error. citeturn0search12

---

## Copy / Download
This file is saved as **Advanced_JS_Symbol_BigInt.md** — use the download link provided by the environment.

