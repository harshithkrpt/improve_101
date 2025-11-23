# TypeScript Basics Cheat Sheet  
### Topic: TypeScript  
### Sub Topic: Basics – Types vs Interfaces, Type Inference, any / unknown / never  

---

## 1. Types vs Interfaces (Detailed)

TypeScript offers **type aliases** (`type`) and **interfaces** (`interface`) to describe shapes of data.

### Interfaces
- Best for describing **objects, classes, function signatures**.
- Can be **extended** multiple times.
- Supported by TypeScript's structural typing system.

```ts
interface User {
  id: number;
  name: string;
}

interface Admin extends User {
  permissions: string[];
}
```

### Type Aliases
- Can represent **primitive**, **union**, **tuple**, **function signatures**, and also objects.
- Cannot be reopened like interfaces, but can express more complex compositions.

```ts
type ID = number | string;

type User = {
  id: ID;
  name: string;
};
```

### When to use what?
- Use **interface** when modeling object shapes that may need extension.
- Use **type** when working with **unions, primitives, utility types**, or complex compositions.

---

## 2. Type Inference

TypeScript automatically infers types when possible.

```ts
let count = 10;   // inferred as number
const name = "Harshith"; // inferred as "Harshith" literal type
```

### Function inference
```ts
function add(a: number, b: number) {
  return a + b; // inferred return type: number
}
```

Inference reduces verbosity but is still checked statically.

---

## 3. `any` vs `unknown` vs `never`

### `any`
- Opt-out of type checking.
- Disables safety.
- Avoid unless necessary.

```ts
let x: any = "hello";
x = 100; // no error
x();     // ok, no checks
```

### `unknown`
- Safe version of `any`.
- Requires type narrowing before use.

```ts
let y: unknown = "hello";
// y.toUpperCase(); // error
if (typeof y === "string") {
  y.toUpperCase(); // safe
}
```

### `never`
- Represents values that **never occur**.
- Used for:
  - functions that never return (throw or infinite loop)
  - exhaustive switch checks

```ts
function crash(): never {
  throw new Error("boom");
}

function exhaustive(val: string | number) {
  if (typeof val === "string") return;
  if (typeof val === "number") return;
  const _check: never = val; // ensures no other type possible
}
```

---

## 4. Common Theory Questions (Concise Answers)

### Q: Difference between type and interface?
A: Interface is extendable and focused on object shapes; type is more flexible (unions, primitives, tuples).

### Q: When should we prefer interface?
A: When modeling objects expected to be extended or used with classes.

### Q: What is type inference?
A: TypeScript’s ability to automatically deduce types from context.

### Q: Why is `unknown` safer than `any`?
A: `unknown` forces type checking before usage, preserving type safety.

### Q: When is `never` used?
A: For functions that never return or to enforce exhaustive type checking.

---

## 5. Coding-Based Interview Questions

### 1. Implement a function using `unknown` safely:
```ts
function safeLog(value: unknown) {
  if (typeof value === "string") console.log(value.toUpperCase());
  if (typeof value === "number") console.log(value.toFixed(2));
}
```

### 2. Enforce exhaustive checks using `never`:
```ts
type Shape = { type: "circle"; radius: number } |
             { type: "square"; side: number };

function area(shape: Shape) {
  switch (shape.type) {
    case "circle": return Math.PI * shape.radius ** 2;
    case "square": return shape.side ** 2;
    default:
      const _exhaustive: never = shape;
      return _exhaustive;
  }
}
```

### 3. Demonstrate extending interfaces:
```ts
interface A { x: number; }
interface B extends A { y: string; }
```

### 4. Create union type with `type`:
```ts
type Status = "success" | "error" | "loading";
```

---

This file captures conceptual clarity + interview prep + coding practice for TS basics.


# TypeScript Functions & Objects – Cheat Sheet
### Topic: TypeScript  
### Sub Topic: Functions & Objects (function overloads, optional params, readonly, Partial)

---

## 1. Function Overloads

TypeScript supports multiple call signatures for a single function name.  
You declare multiple overload signatures, followed by a single implementation.

```ts
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: any, b: any): any {
  if (typeof a === "number" && typeof b === "number") return a + b;
  if (typeof a === "string" && typeof b === "string") return a + b;
  throw new Error("Invalid arguments");
}
```

**Key points:**
- Overloads provide precise type checking at call sites.
- The implementation must handle all overload cases.
- Order matters; the compiler picks the first matching signature.
- Optional params + overloads can cause ambiguity.

---

## 2. Optional Parameters

Declare a parameter optional using `?`. Optional parameters must be placed after required ones.

```ts
function greet(name: string, greeting?: string) {
  return `${greeting ?? "Hello"}, ${name}`;
}
```

**Default-valued parameters** also count as optional:

```ts
function log(msg: string, level = "info") {
  console.log(level, msg);
}
```

---

## 3. `readonly` and `Partial`

### `readonly`
Prevents reassigning object properties (compile-time).

```ts
interface User {
  id: number;
  name: string;
}

const u: Readonly<User> = { id: 1, name: "Alice" };
// u.name = "Bob"; // Error
```

### `Partial`
Makes all properties optional.

```ts
interface Config {
  host: string;
  port: number;
  secure: boolean;
}

function updateConfig(cfg: Partial<Config>) {}
```

---

## 4. Interview Theory Questions (Concise)

**Q: What is function overloading?**  
A: Multiple call signatures for one function; a single implementation resolves them.

**Q: Optional parameter vs overload?**  
A: Use optional parameters when behavior is mostly similar; overloads when behavior or return type changes.

**Q: What does `readonly` do?**  
A: Marks properties as immutable (compile-time only).

**Q: What does `Partial<T>` do?**  
A: Makes all properties in `T` optional.

**Q: Why can overloads become ambiguous?**  
A: Optional params or broad unions may match multiple signatures; order affects resolution.

---

## 5. Coding-Based Interview Questions

### Overload example with optional param
```ts
function format(date: Date): string;
function format(date: Date, fmt: string): string;
function format(date: Date, fmt?: string): string {
  return fmt ? "formatted:" + fmt : date.toISOString();
}
```

### Safe key accessor
```ts
function getValue<T, K extends keyof T>(obj: Readonly<T>, key: K): T[K] {
  return obj[key];
}
```

### Update object with Partial
```ts
interface User {
  id: number;
  name: string;
  email: string;
}

function updateUser(user: User, updates: Partial<User>): User {
  return { ...user, ...updates };
}
```

### Overloaded merge
```ts
function merge(a: number[], b: number[]): number[];
function merge(a: string, b: string): string;
function merge(a: any, b: any): any {
  if (Array.isArray(a) && Array.isArray(b)) return [...a, ...b];
  if (typeof a === "string" && typeof b === "string") return a + b;
}
```

### Readonly object type
```ts
interface Config {
  host: string;
  port: number;
  secure: boolean;
}

type FrozenConfig = Readonly<Config>;
```

---

# TypeScript – Union & Intersection Types Cheat Sheet
### Topic: TypeScript
### Sub Topic: Union & Intersection Types (combining types, discriminated unions)

---

## 1. Union Types (`|`)

Union types allow a value to be *one of* several types.

```ts
type ID = number | string;
```

Only members common to all union members are accessible unless narrowed.

```ts
interface Bird { fly(): void; layEggs(): void; }
interface Fish { swim(): void; layEggs(): void; }

declare function getPet(): Bird | Fish;

let pet = getPet();
pet.layEggs(); // OK
// pet.swim(); // Error: Bird might not have swim()
```

---

## 2. Intersection Types (`&`)

Intersection types require a value to satisfy *all* types combined.

```ts
interface HasName { name: string; }
interface HasAge { age: number; }

type Person = HasName & HasAge;
```

Good for combining traits, mixins, or multiple interfaces.

---

## 3. Discriminated Unions

A discriminated union (tagged union) uses a shared literal property (`kind`, `type`, etc.) for safe narrowing.

```ts
type Circle = { kind: "circle"; radius: number };
type Rectangle = { kind: "rectangle"; width: number; height: number };
type Shape = Circle | Rectangle;

function area(s: Shape) {
  switch (s.kind) {
    case "circle":
      return Math.PI * s.radius ** 2;
    case "rectangle":
      return s.width * s.height;
    default:
      const _exhaustive: never = s;
      return _exhaustive;
  }
}
```

Ensures exhaustive handling and prevents invalid cases.

---

## 4. Patterns & Pitfalls

- Union = one of many types  
- Intersection = must satisfy all types  
- Discriminated unions simplify narrowing and branching  
- Avoid modeling variants with optional fields; use proper unions  
- Use `never` for exhaustive checks

---

## 5. Interview Theory Questions

**Q: What is a union type?**  
A: A type allowing values to be one of multiple types.

**Q: What is an intersection type?**  
A: A type requiring values to satisfy all combined types.

**Q: What is a discriminated union?**  
A: A union with a shared literal property used to narrow branches safely.

**Q: How does narrowing work in TS?**  
A: Through guards like `typeof`, `instanceof`, `in`, or switching on discriminant.

**Q: Why prefer discriminated unions over optional properties?**  
A: Clearer shapes, safer narrowing, and exhaustive checking.

---

## 6. Coding-Based Interview Questions

### 1. Result type with discriminated union
```ts
type Success<T> = { status: "success"; data: T };
type Failure = { status: "error"; message: string };

type Result<T> = Success<T> | Failure;

function handleResult<T>(r: Result<T>) {
  if (r.status === "success") console.log(r.data);
  else console.error(r.message);
}
```

### 2. Intersection type merging user and admin
```ts
interface User { id: number; name: string }
interface AdminProps { permissions: string[] }

type AdminUser = User & AdminProps;

const admin: AdminUser = { id: 1, name: "Alice", permissions: ["read"] };
```

### 3. Discriminated union of shapes
```ts
type Circle = { type: "circle"; radius: number };
type Square = { type: "square"; side: number };
type Rectangle = { type: "rectangle"; width: number; height: number };

type Shape = Circle | Square | Rectangle;
```

### 4. Intersection with union
```ts
interface X { x: number }
interface Y { y: string }
interface Z { id: string }

type A = (X | Y) & Z;

const a1: A = { id: "1", x: 10 };
const a2: A = { id: "2", y: "hello" };
```

### 5. Error example without narrowing
```ts
interface Bird { fly(): void; layEggs(): void; }
interface Fish { swim(): void; layEggs(): void; }

let pet: Bird | Fish;
// pet.swim(); // Error
```

---


# Topic : TypeScript

## Sub Topic : Generics — function and class generics, constraints, `keyof`

---

### Quick summary
Generics allow you to write reusable, type-safe functions, classes, interfaces and type aliases by introducing type parameters (placeholders like `<T>`). They preserve precise typing while remaining flexible across many concrete types.

---

## 1) Core concepts

- **Type parameter**: a placeholder used like `function identity<T>(arg: T): T { return arg }`.
- **Type inference**: TypeScript can often infer the generic type from arguments, so explicit `<T>` can be omitted during calls.
- **Constraints**: use `extends` to require a type parameter to satisfy a shape, e.g. `<T extends { id: number }>`.
- **`keyof`**: produces a union of keys of a type `keyof T` and is commonly used with constraints: `K extends keyof T`.
- **Indexed access types**: `T[K]` extracts the property type.

---

## 2) Function generics (detailed)

**Identity function (basic)**

```ts
function identity<T>(value: T): T {
  return value;
}

const s = identity('hello'); // inferred as string
const n = identity<number>(42); // explicit
```

**Generic constraints with `extends`**

```ts
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}

longest('short', 'longer string');
```

**Using `keyof` + indexed access**

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { id: 1, name: 'A' };
const name = getProperty(user, 'name'); // string
```

**Default generic type**

```ts
function makeArray<T = string>(len: number, v: T): T[] {
  return Array.from({ length: len }, () => v);
}
```

---

## 3) Class generics (detailed)

**Simple generic class**

```ts
class Stack<T> {
  private items: T[] = [];
  push(v: T) { this.items.push(v); }
  pop(): T | undefined { return this.items.pop(); }
}

const s = new Stack<number>();
```

**Generics with constraints & multiple params**

```ts
class Repository<T extends { id: string | number }> {
  private map = new Map<T['id'], T>();
  add(item: T) { this.map.set(item.id, item); }
  get(id: T['id']): T | undefined { return this.map.get(id); }
}
```

**Polymorphic `this` with generics (fluent APIs)**

```ts
class Builder<T, Self extends Builder<T, Self> = Builder<T, any>> {
  protected value!: T;
  set(v: T): Self { this.value = v; return this as unknown as Self; }
}

class StringBuilder extends Builder<string, StringBuilder> {
  append(s: string) { this.value += s; return this; }
}
```

---

## 4) Patterns & best practices

- **Push type parameters down**: prefer to constrain the most specific function instead of making higher-level types generic unnecessarily.
- **Keep type param count small**: more than 2–3 generic parameters often indicates the need for a type alias or rethinking the API.
- **Prefer `extends` for safety**: constrain to the minimal contract you need (e.g. `{ length: number }` or `Record<string, unknown>`).
- **Use `keyof` + indexed access for safe property access**.
- **Combine with utility types** (e.g. `Partial<T>`, `Readonly<T>`, `Pick<T, K>`).
- **Avoid overuse of `any`** in generic defaults; prefer a sensible default like `unknown` or a narrow default.

---

## 5) Interview-style theory questions (concise answers)

1. **What are generics and why use them?** — Placeholders for types; let you write reusable, type-safe code without losing type info.

2. **How does `extends` work in generics?** — It constrains a type parameter to types that satisfy the given shape.

3. **Why use `keyof`?** — Produces a union of property keys of a type; helps write type-safe property accessors.

4. **When to prefer `unknown` over `any` in generics?** — `unknown` forces you to narrow types before usage and preserves type safety; `any` bypasses checking.

5. **What's the difference between `T[]` and `Array<T>`?** — None semantically; both denote arrays of `T` (stylistic choice).

6. **How to type a function that takes an object and a list of keys and returns their values?** — Use `<T, K extends keyof T>(o: T, keys: K[]): T[K][]`.

7. **Explain covariance/contravariance concerns with generics.** — Function parameter positions are contravariant; return positions are covariant. TypeScript uses structural typing and has specific variance rules (be cautious with mutable generics).

---

## 6) Coding interview tasks (with short solutions)

**Q1 — Generic `pluck` function**

```ts
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
  return items.map(i => i[key]);
}
```

**Q2 — Generic `memoize` wrapper (simple)**

```ts
function memoize<T extends (...args: any[]) => any>(fn: T): T {
  const cache = new Map<string, ReturnType<T>>();
  return ((...args: any[]) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key) as ReturnType<T>;
    const res = fn(...args);
    cache.set(key, res);
    return res;
  }) as T;
}
```

**Q3 — Strongly-typed `get` for nested objects (simple)**

```ts
function get<T, K1 extends keyof T>(o: T, k1: K1): T[K1];
function get<T, K1 extends keyof T, K2 extends keyof T[K1]>(o: T, k1: K1, k2: K2): T[K1][K2];
function get(o: any, ...keys: string[]) {
  return keys.reduce((res, k) => res?.[k], o);
}
```

---

## 7) Cheatsheet (snippets)

- Generic fn: `function f<T>(x: T): T {}`
- Constrained: `function f<T extends Foo>(x: T)`
- keyof: `type Keys = keyof MyType`
- Indexed access: `type V = MyType[\"a\"] | MyType[\"b\"]` or `type V = MyType[K]`
- Default: `type Foo<T = string> = ...`

---

*Created as an interview-ready cheat sheet — includes explanations, succinct theory answers, and coding tasks.*

# Topic : TypeScript

## Sub Topic : Type Guards

---

## 1. Quick overview

**Type guards** are runtime checks that allow TypeScript to narrow the static type of a value within a specific control-flow region. They bridge runtime behavior and compile-time type narrowing so you can write safer code without excessive `as` casts.

Built-in narrowing mechanisms include `typeof`, `instanceof`, discriminated unions (literal properties), and the `in` operator. You can also write *user-defined type guards* using type predicates (`x is T`) and assertion signatures (`asserts x is T`).

---

## 2. Built-in type guards (with examples)

### `typeof` (primitives)

Use for primitives: `"string"`, `"number"`, `"bigint"`, `"boolean"`, `"symbol"`, `"undefined"`, `"object"`, `"function"`.

```ts
function format(x: string | number) {
  if (typeof x === 'string') {
    return x.trim(); // x is string here
  }
  return x.toFixed(2); // x is number here
}
```

### `instanceof` (class/constructor checks)

Checks prototype chain; works for classes/constructors, not interfaces.

```ts
class Dog { bark() {} }
class Cat { meow() {} }

function speak(a: Dog | Cat) {
  if (a instanceof Dog) {
    a.bark(); // narrowed to Dog
  } else {
    a.meow(); // narrowed to Cat
  }
}
```

### `in` (property existence)

Narrow by checking a property name on an object. Useful for discriminating union members that don't use a dedicated tag.

```ts
type A = { kind: 'a'; foo: string };
type B = { bar: number };
function f(x: A | B) {
  if ('foo' in x) {
    // x is A (or at least has foo)
    console.log(x.foo);
  } else {
    console.log(x.bar);
  }
}
```

### Discriminated unions (recommended)

Use a shared literal `tag` property to let TypeScript narrow automatically.

```ts
type Circle = { kind: 'circle'; r: number };
type Square = { kind: 'square'; side: number };

type Shape = Circle | Square;

function area(s: Shape) {
  if (s.kind === 'circle') return Math.PI * s.r * s.r;
  return s.side * s.side;
}
```

---

## 3. User-defined type guards (type predicates)

A function with a return type of the form `paramName is Type` tells TypeScript that when the function returns `true`, the parameter has the specified type.

```ts
interface Person { name: string; age: number }
interface Company { companyName: string }

function isPerson(x: any): x is Person {
  return typeof x === 'object' && x !== null && 'name' in x && 'age' in x;
}

function greet(x: Person | Company) {
  if (isPerson(x)) {
    console.log(x.name); // narrowed to Person
  } else {
    console.log(x.companyName); // narrowed to Company
  }
}
```

**Notes:**
- The parameter name in the predicate (`x is Person`) must match the function parameter name.
- The runtime check must be implemented carefully; TypeScript trusts the predicate but does not verify its runtime correctness.

### `asserts` style (assertion signatures)

You can write assertion functions that throw if the check fails, and return `void` with an `asserts` signature. This is useful when you want to guarantee a type after running the function or else halt execution.

```ts
function assertIsPerson(x: any): asserts x is Person {
  if (!(x && typeof x === 'object' && 'name' in x && 'age' in x)) {
    throw new Error('Not a Person');
  }
}

function doSomething(x: any) {
  assertIsPerson(x);
  // here x is treated as Person
  console.log(x.name);
}
```

---

## 4. Narrowing rules & control-flow

TypeScript narrows types based on control-flow analysis. The narrowed type is only valid inside the block where the guard succeeded. After assignments or when the compiler cannot guarantee immutability, narrowing may be lost.

```ts
let u: string | number = 5;
if (typeof u === 'string') {
  // u is string here
}
// after assignment or mutation, narrowing may not hold
u = Math.random() ? 'hello' : 42; // narrowing must be re-established
```

**Important**: For object properties, TypeScript narrows based on property access pattern and may widen again if the property is mutated or the object is aliased.

---

## 5. Common pitfalls & best practices

- **`instanceof` vs interfaces**: `instanceof` checks constructors at runtime, interfaces don't exist at runtime — use classes or custom guards.
- **Don't over-rely on `any`**: custom guards are less useful if inputs are `any` everywhere; prefer `unknown` for safer checking.
- **Keep guards simple & fast**: expensive checks inside hot paths hurt performance; prefer simple predicates and create helper caches where necessary.
- **Prefer discriminated unions**: they are the cleanest, safest, and easiest-to-maintain approach for multiple variants.
- **Name your predicate parameter consistently**: the parameter name in `x is T` must match the function's parameter.
- **Use `asserts` for runtime-required invariants**:  good when you must stop execution on invalid input.

---

## 6. Interview-style theory questions (concise answers)

**Q1: What is a type guard in TypeScript?**
A: A runtime check that narrows the type of a value within a control-flow branch, enabling safer access to properties/methods.

**Q2: How does `typeof` differ from `instanceof`?**
A: `typeof` checks primitive type categories at runtime (`'string'`, `'number'`, etc.). `instanceof` checks an object's prototype chain against a constructor/class and only works with values constructed from that constructor.

**Q3: What is a user-defined type guard? Give its signature.**
A: A function that returns a type predicate like `param is Type`. Example: `function isFoo(x: any): x is Foo { /* check */ }`.

**Q4: When would you use `asserts x is T`?**
A: When you want a function that throws on failure and guarantees the type on success; useful for validating invariants and stopping execution if they fail.

**Q5: Why prefer discriminated unions?**
A: They provide explicit tags for variants, letting TypeScript automatically narrow without custom runtime checks and making code clearer.

**Q6: How does TypeScript perform narrowing across functions?**
A: TypeScript uses control-flow analysis. Narrowing happens in the scope where a guard check is visible; it won’t automatically carry across to unrelated functions unless those functions use predicates or assertions.

**Q7: Can you use `in` to check array elements or string primitives?**
A: `in` checks property names on objects (including arrays via numeric keys), not primitive types like strings for membership — use `typeof` or other checks instead.

---

## 7. Interview-style coding questions (with solutions)

### Question 1 — Simple custom guard
**Prompt:** Write an `isNumberArray` function that checks whether a value is an array of numbers.

**Solution:**

```ts
function isNumberArray(x: any): x is number[] {
  return Array.isArray(x) && x.every(v => typeof v === 'number');
}
```

**Usage:**
```ts
function avg(x: number[] | string) {
  if (isNumberArray(x)) {
    return x.reduce((a, b) => a + b, 0) / x.length;
  }
  return parseFloat(x);
}
```

---

### Question 2 — Discriminated union switch
**Prompt:** Given `type Result = { status: 'ok'; value: number } | { status: 'err'; error: string }`, write a function that extracts `value` or throws.

**Solution:**

```ts
type Result = { status: 'ok'; value: number } | { status: 'err'; error: string };

function unwrap(r: Result) {
  if (r.status === 'ok') return r.value;
  throw new Error(r.error);
}
```

---

### Question 3 — Assertion guard
**Prompt:** Implement `ensureIsHTMLElement` that asserts a value is `HTMLElement`.

**Solution:**

```ts
function ensureIsHTMLElement(x: unknown): asserts x is HTMLElement {
  if (!(x instanceof HTMLElement)) throw new Error('Not an HTMLElement');
}

// usage
function appendChildIfElement(x: unknown, parent: HTMLElement) {
  ensureIsHTMLElement(x);
  parent.appendChild(x); // x is HTMLElement now
}
```

---

### Question 4 — Mixed object guard
**Prompt:** For `type A = { foo: string } | { bar: number }`, write a guard using `in`.

**Solution:**

```ts
function hasFoo(x: any): x is { foo: string } {
  return x != null && typeof x === 'object' && 'foo' in x;
}

function demo(x: { foo: string } | { bar: number }) {
  if (hasFoo(x)) {
    console.log(x.foo);
  } else {
    console.log(x.bar);
  }
}
```

---

## 8. Advanced tips & patterns

- **Combine guards**: small composable guards are easier to test and reuse.
- **Prefer `unknown` over `any` for inputs**: `unknown` forces you to check before use.
- **Type predicates with generics**: you can write `function isRecord<K extends string, V>(x: any): x is Record<K, V> { ... }` but be careful — runtime checks need to be implemented explicitly.
- **Use branded types** for nominal typing and guards to check a brand.
- **Guarding library data (JSON)**: write thin validators (or use runtime validation libs like `zod` / `io-ts`) and then assert the type with `asserts` signatures.

---

## 9. Cheat-sheet summary (TL;DR)

- Use `typeof` for primitives, `instanceof` for class instances, `in` for property checks, and discriminated unions for clean variant handling.
- Write user-defined guards using `x is T` when automatic narrowing isn’t enough.
- Use `asserts x is T` when you need to throw on invalid data and guarantee the type afterwards.
- Prefer discriminated unions and `unknown` as inputs for safer code.

---

## 10. Suggested practice exercises

1. Implement `isPlainObject(x: unknown): x is Record<string, unknown>` (careful with arrays and `null`).
2. Create guards for nested structure: `{ user?: { id: string, email?: string } } | null` and safely access `email`.
3. Create a small JSON validator that returns `asserts value is MyType`.

---

_End of document._

# Topic : TypeScript

## Sub Topic : Utility Types (Partial, Pick, Omit, Exclude, Record, ReturnType)

---

## 1. Quick overview

TypeScript ships with several **utility types** — prebuilt, generic types that transform existing types to save repetition and express intent. Common utilities include `Partial`, `Pick`, `Omit`, `Exclude`, `Record`, and `ReturnType`. These are implemented using mapped types, conditional types, and `keyof`.

---

## 2. Core utility types with examples

### `Partial<T>`
Makes every property of `T` optional.

```ts
interface User { id: string; name: string; email: string }

function updateUser(id: string, patch: Partial<User>) {
  // patch may contain any subset of User properties
}

updateUser('1', { name: 'Alice' });
```

Use when creating update/patch payloads or building objects incrementally.

---

### `Pick<T, K>`
Constructs a type by selecting a set of properties `K` from `T`.

```ts
type UserPreview = Pick<User, 'id' | 'name'>; // { id: string; name: string }
```

Good for view models and APIs that need limited fields.

---

### `Omit<T, K>`
Constructs a type by excluding properties `K` from `T`.

```ts
type NewUserForm = Omit<User, 'id'>; // { name: string; email: string }
```

Often used to remove database-specific fields like `id` when defining create payloads.

---

### `Exclude<T, U>`
Removes from union `T` those types that are assignable to `U`.

```ts
type T = 'a' | 'b' | 'c';
type WithoutB = Exclude<T, 'b'>; // 'a' | 'c'
```

Useful when manipulating unions or filtering out unwanted members.

---

### `Record<K, T>`
Creates an object type whose keys are `K` (usually a union of string literals) and values are `T`.

```ts
type Role = 'admin' | 'user' | 'guest';
type Permissions = Record<Role, string[]>;

const perms: Permissions = {
  admin: ['read','write'],
  user: ['read'],
  guest: []
};
```

`K` can be `string | number | symbol` or a union of literal types.

---

### `ReturnType<T>`
Extracts the return type of a function type `T`.

```ts
function fetchUser() { return Promise.resolve({ id: '1', name: 'a' }) }

type R = ReturnType<typeof fetchUser>; // Promise<{ id: string; name: string }>
```

Handy for deriving types from factory functions or older APIs.

---

## 3. How they work (short internals)

- `Partial`, `Readonly`, and similar are implemented with **mapped types** (`{ [P in keyof T]?: T[P] }`).
- `Pick`/`Omit` rely on `keyof` and mapped types to select or exclude keys.
- `Exclude` is a **conditional type** that filters union members (`T extends U ? never : T`).
- `Record` is just a convenience mapped type (`{ [K in Keys]: Type }`).
- `ReturnType` is implemented with conditional type inference (`T extends (...args: any) => infer R ? R : any`).

Understanding these implementations helps you build custom utility types.

---

## 4. Common patterns & best practices

- Prefer `Pick`/`Omit` over re-declaring similar types — keeps types DRY and updates propagate automatically.
- Use `Partial<T>` for patch/update DTOs, but combine with `Required` or validation when necessary before saving.
- Be careful with `ReturnType` on overloaded functions — it picks the union of possible returns or `any` if it can't infer cleanly.
- Use `Record` for dense lookups where every key is required. If keys are optional, prefer `{ [k in Key]?: V }` or `Partial<Record<...>>`.
- When transforming deep structures, consider building small mapped/conditional helpers rather than many ad-hoc mapped types.

---

## 5. Interview-style theory questions (concise answers)

**Q1: What does `Partial<T>` do?**
A: Converts all properties of `T` to optional (i.e., `?`). Useful for partial updates.

**Q2: How does `Pick<T, K>` differ from `Omit<T, K>`?**
A: `Pick` selects only the listed keys `K` from `T`. `Omit` removes the listed keys `K` from `T`.

**Q3: What is `Exclude<T, U>` used for?**
A: Removes from union `T` any members that are assignable to `U`.

**Q4: When should you use `Record<K, T>`?**
A: When you want an object type with a fixed set of keys `K` mapped to a single value type `T`.

**Q5: How does `ReturnType<T>` infer the return type?**
A: It uses conditional type inference (`infer`) — if `T` is a function type, `ReturnType<T>` extracts its return type.

---

## 6. Interview-style coding questions (with solutions)

### Q1 — Transforming a DTO
**Prompt:** Given `interface User { id: string; name: string; password: string }`, create a type for a safe API response that excludes `password` and a type for a partial update.

**Solution:**
```ts
type UserResponse = Omit<User, 'password'>;
type UserUpdate = Partial<Omit<User, 'id'>>; // id cannot be updated, other fields optional
```

---

### Q2 — Lookup table
**Prompt:** Create a `Record` type for weekday schedules with keys `'mon'|'tue'...'sun'` and values `string[]`.

**Solution:**
```ts
type Weekday = 'mon'|'tue'|'wed'|'thu'|'fri'|'sat'|'sun';
type Schedule = Record<Weekday, string[]>;
```

---

### Q3 — Extracting return type
**Prompt:** Given `function createThing(): { id: number; createdAt: string }`, derive a type `Thing` using `ReturnType`.

**Solution:**
```ts
function createThing() { return { id: 1, createdAt: new Date().toISOString() } }

type Thing = ReturnType<typeof createThing>;
```

---

## 7. Advanced examples & custom utilities

### DeepPartial (partial recursively)
```ts
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P]
}
```

### ToggleKeys: make some keys optional and keep others required
```ts
type ToggleKeys<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;
```

These patterns combine mapped types and `keyof` to build flexible utilities.

---

## 8. TL;DR (cheat summary)

- `Partial<T>` — make properties optional.
- `Pick<T,K>` — select properties.
- `Omit<T,K>` — remove properties.
- `Exclude<T,U>` — remove union members.
- `Record<K,T>` — map keys to a value type.
- `ReturnType<T>` — extract a function's return type.

---

## 9. Practice exercises

1. Implement `RequiredExcept<T, K>`: make all props required except keys in `K` which are optional.
2. Build `Mutable<T>` to remove `readonly` modifiers from a type.
3. Create `Values<T>` that returns a union of a type's property value types (hint: `T[keyof T]`).

---

_End of document._

# Topic : TypeScript

## Sub Topic : Enums & Tuples (const enums, tuple inference, readonly tuples)

---

## 1. Quick overview

**Enums** provide a way to name a set of numeric or string constants. TypeScript supports regular `enum` and `const enum` (inlined at compile time). Many teams prefer literal unions or `as const` objects for simpler interop, but enums remain useful when you need a runtime object or reverse mapping.

**Tuples** are fixed-length arrays where each index has a specific type. Modern TypeScript improves inference for tuple operations (spreads, rest parameters) and supports `readonly` tuples to prevent mutation.

---

## 2. Enums

### Numeric enums

```ts
enum Direction {
  Up = 1,
  Down,
  Left,
  Right
}

const d = Direction.Up; // 1
```

Numeric enums support auto-incrementing members and reverse mappings (from value back to name) at runtime.

### String enums

```ts
enum Status {
  Ok = 'OK',
  Err = 'ERR'
}
```

String enums don't have reverse mapping, but are clearer when you need stable values across systems.

### Const enums

```ts
const enum Color { Red, Green, Blue }

const c = Color.Green; // compiled as 1 (inlined)
```

`const enum` tells the compiler to inline enum members where used instead of emitting an object. This reduces runtime cost but means the enum has no runtime representation; it also can cause issues with some build tools and `--isolatedModules` or when emitting declaration files.

---

## 3. When to use enums vs alternatives

- Use `enum` when you need a runtime object, reverse mapping, or to interoperate with code that expects an object.
- Prefer `as const` + literal unions (`type Dir = typeof obj[keyof typeof obj]`) for pure compile-time sets and better tree-shaking.
- Use `const enum` for performance-critical code where inlining is safe and your build pipeline supports it.

---

## 4. Tuples: syntax and inference

### Basic tuple

```ts
let point: [number, number] = [10, 20];
```

### Tuple inference

TypeScript can infer tuple types in many cases, especially with helper `tuple` functions or when using `as const` on literals.

```ts
const coords = [10, 20] as const; // readonly [10, 20]

function tuple<T extends any[]>(...args: T) { return args; }

const pair = tuple('a', 1); // inferred type ['a', number]
```

### Rest and spread with tuples

TypeScript 4.x improved support for variadic tuple types, so you can write functions that preserve tuple shapes across spreads and rest parameters.

```ts
type Prepend<T extends any[], U> = [U, ...T];

function prepend<T extends any[], U>(arr: T, head: U): Prepend<T, U> {
  return [head, ...arr] as Prepend<T, U>;
}
```

---

## 5. Readonly tuples

Mark tuples `readonly` to prevent mutation:

```ts
type ReadonlyPair = readonly [number, number];

function foo(p: ReadonlyPair) {
  // p[0] = 1; // error
}
```

`as const` on an array literal produces a `readonly` tuple with literal element types — great for defining fixed data constants.

---

## 6. Pitfalls & best practices

- `const enum` can break when using Babel or `--isolatedModules`. Check your toolchain.
- Enums produce runtime code for non-const enums; they are not erased, unlike type-only constructs.
- Prefer literal unions and `as const` when you only need type-level representation.
- Use `readonly` tuples to signal immutability and catch accidental mutations early.
- Watch tuple widening: mutable arrays may widen from tuple to array types unless you use `as const` or const assertions.

---

## 7. Interview-style theory questions (concise answers)

**Q1: What’s the difference between `enum` and `const enum`?**
A: `enum` emits a runtime object and supports reverse mapping. `const enum` is inlined at compile time (no runtime object), which reduces code size but restricts some toolchain scenarios.

**Q2: How does `as const` help with tuples?**
A: `as const` turns an array literal into a `readonly` tuple with narrow literal types, preventing mutation and preserving exact values.

**Q3: When should you prefer unions over enums?**
A: Prefer unions (e.g., `type Dir = 'up' | 'down'`) when you only need compile-time type checking and want better interoperability and smaller emitted JS.

**Q4: What are variadic tuple types?**
A: Variadic tuple types let you express tuple shapes that include rest elements (`...T`) and enable correct inference through spreads and higher-order utilities.

---

## 8. Interview-style coding questions (with solutions)

### Q1 — Convert enum to union
**Prompt:** Given `enum Color { Red, Green, Blue }`, derive a union type of its values.

**Solution:**
```ts
enum Color { Red, Green, Blue }

type ColorValue = Color.Red | Color.Green | Color.Blue; // numeric union
// or if using const-like object
const Colors = { Red: 'RED', Green: 'GREEN' } as const;
type ColorStr = typeof Colors[keyof typeof Colors];
```

---

### Q2 — Prevent tuple mutation
**Prompt:** Given `const t = [1, 2]`, make a function accept only tuples that cannot be modified.

**Solution:**
```ts
const t = [1, 2] as const; // readonly [1,2]

function usePoint(p: readonly [number, number]) {
  // p[0] = 3; // error
}

usePoint(t);
```

---

### Q3 — Preserve tuple types through a helper
**Prompt:** Write a `tuple` helper that preserves element types.

**Solution:**
```ts
function tuple<T extends any[]>(...args: T) { return args; }

const x = tuple('a', 1); // type ['a', number]
```

---

## 9. TL;DR

- `enum` creates a runtime object; `const enum` is inlined and has no runtime representation.
- Tuples are fixed-length arrays with known types per index; modern TS infers tuples well and supports variadic tuples.
- Use `readonly` tuples (and `as const`) to prevent widening/mutation.

---

## 10. Practice exercises

1. Rewrite an existing `enum` as a `const` object + union and note the advantages/disadvantages.
2. Create a `zip` function that takes two tuples of the same length and returns a tuple of pairs, preserving types.
3. Demonstrate a case where `const enum` breaks a build pipeline (research your toolchain).

---

_End of document._


# TypeScript: Modules & Namespaces Cheat Sheet  
**Topic:** TypeScript  
**Sub Topic:** Modules & Namespaces (import/export, declaration merging)

---

## 1. Modules in TypeScript (ES Modules)

Modules are files. Each file with **import** or **export** becomes a module.  
They help create isolated scopes and explicit dependencies.

### Exporting
```ts
// Named exports
export const pi = 3.14;
export function add(a: number, b: number) { return a + b; }

// Default export
export default class Logger {}
```

### Importing
```ts
import { pi, add } from "./math";
import Logger from "./logger";
import * as Utils from "./utils";
```

### Re-exporting
```ts
export * from "./math";
export { add as sum } from "./math";
```

### Why modules?
- Strict isolation  
- No global pollution  
- Good tree-shaking  
- Works with bundlers and Node (ESM or CommonJS)

---

## 2. Namespaces in TypeScript

Namespaces (old TS feature) create scoped groups of variables, functions, types.  
Mainly used before ES modules became standard.

### Creating a namespace
```ts
namespace Shapes {
  export interface Circle { radius: number; }
  export function area(c: Circle) { return Math.PI * c.radius * c.radius; }
}
```

### Accessing
```ts
const c: Shapes.Circle = { radius: 10 };
console.log(Shapes.area(c));
```

### Why namespaces are discouraged?
- Harder to bundle  
- Not standard JS  
- Modules are preferred for everything in modern TS

---

## 3. Declaration Merging

TypeScript can merge multiple declarations with the same name.  
Useful for augmenting libraries or adding custom properties.

### Interface merging
```ts
interface User { name: string; }
interface User { age: number; }

const u: User = { name: "A", age: 20 };
```

### Namespace + Function merging
```ts
function greet(name: string) { return "Hi " + name; }

namespace greet {
  export const version = "1.0";
}

console.log(greet.version);
```

### Class + Namespace merging
```ts
class Car {}
namespace Car {
  export const brand = "Tesla";
}
```

---

## 4. Interview Theory Questions (Concise Answers)

1. **How do modules differ from namespaces?**  
   Modules rely on files and imports; namespaces are global scope containers meant for pre-module JS.

2. **When should you avoid namespaces?**  
   Avoid them in modern apps; ES modules are the standard.

3. **What is declaration merging?**  
   TS feature combining multiple declarations into one final shape.

4. **Where is declaration merging used practically?**  
   Library augmentation, adding properties to global objects, React namespace merging.

5. **Difference between default and named exports?**  
   Default = one per file, imported without braces; named exports are explicit and many per file.

---

## 5. Coding Questions

### Q1: Implement a module that exports utility functions and import it elsewhere.
```ts
// utils.ts
export function isEven(n: number) { return n % 2 === 0; }
export const greet = (name: string) => `Hello ${name}`;

// index.ts
import { isEven, greet } from "./utils";
```

### Q2: Demonstrate declaration merging with interfaces.
```ts
interface Config { url: string; }
interface Config { retry: number; }

const c: Config = { url: "/api", retry: 3 };
```

### Q3: Merge a function and namespace.
```ts
function log(msg: string) { console.log(msg); }
namespace log { export const level = "info"; }

log("hello");
console.log(log.level);
```

---

## Download Info  
This file contains the full cheat sheet.  

# TypeScript: Type Inference & Assertion  
**Topic:** TypeScript  
**Sub Topic:** Type Inference & Assertion (as, non-null assertion `!`, satisfies operator)

---

## 1. Type Inference

TypeScript automatically infers types based on assigned values.

```ts
let count = 10;      // inferred as number
const name = "TS";   // inferred as "TS" (string literal)
```

Inference happens in:
- Variable declarations  
- Function returns  
- Object/array literals  
- Contextual typing  
- Generic default inference  

### Function return inference
```ts
function add(a: number, b: number) {
  return a + b;  // inferred as number
}
```

### Contextual typing example
```ts
window.addEventListener("click", (e) => {
  // e inferred as MouseEvent
});
```

---

## 2. Type Assertions (`as` keyword)

Type assertions tell TS what type _you believe_ a value has.  
They don't change the runtime value; only influence the type system.

```ts
const value: unknown = "hello";
const len = (value as string).length;
```

### Angle-bracket syntax (avoid in JSX)
```ts
const el = <HTMLDivElement>document.getElementById("box");
```

### Unsafe assertions
```ts
const n = "hi" as unknown as number; // forced, not safe
```

---

## 3. Non‑Null Assertion Operator (`!`)

Used when you're certain a value is NOT null or undefined.

```ts
function print(msg?: string) {
  console.log(msg!.toUpperCase());
}
```

Why risky?  
Because you skip TS safety, and runtime may still throw an error if you're wrong.

---

## 4. `satisfies` Operator

Introduced in TS 4.9 — a safer way to validate object shapes without narrowing their literals too much.

```ts
const user = {
  name: "Harshith",
  age: 26
} satisfies { name: string; age: number };
```

### Why `satisfies` is better than `as`?

`as` asserts the type blindly.

`satisfies` checks compatibility **without losing literal detail**.

```ts
const config = {
  method: "GET",
  retries: 3
} satisfies Record<string, string | number>;

// "GET" remains a literal "GET"
```

---

## 5. Interview Theory Q&A (Concise)

1. **What is type inference?**  
   TS automatically infers the most specific type from context.

2. **Difference between type assertion and type casting?**  
   TS assertions do not convert values; only inform the compiler.

3. **Why avoid non‑null `!` operator?**  
   It bypasses safety and can cause runtime crashes.

4. **How is `satisfies` different from `as`?**  
   `satisfies` validates compatibility while preserving literal types; `as` forces the type.

5. **When to use type assertions?**  
   DOM manipulation, narrowing `unknown`, interop with JS libraries.

---

## 6. Coding Questions

### Q1: Convert unknown to typed object using assertion.
```ts
const data: unknown = JSON.parse('{"id":1}');
const obj = data as { id: number };
```

### Q2: Use non-null assertion with DOM.
```ts
const input = document.querySelector("input")!;
input.value = "Hello";
```

### Q3: Demonstrate `satisfies` to enforce object shape.
```ts
const env = {
  mode: "prod",
  debug: false
} satisfies { mode: string; debug: boolean };
```

### Q4: Infer function return types correctly.
```ts
function getUser() {
  return { id: 1, name: "TS" };
}
type User = ReturnType<typeof getUser>;
```

---

## Download Info  
This file contains the full cheat sheet in markdown format.

# TypeScript: Interfaces vs Types Cheat Sheet
**Topic:** TypeScript  
**Sub Topic:** Interfaces vs Types (differences, merging, extension)

---

## 1. Overview — when to use what
- **`interface`** — ideal for describing object shapes and public APIs. They're *open* (can be extended and merged) and map closely to JS object semantics.
- **`type` (type alias)** — more general: can name primitives, unions, intersections, tuples, mapped/conditional types. They are *closed* once declared (no declaration merging).  

*(Short rule of thumb: use `interface` for objects/APIs, use `type` for unions/complex type expressions.)*

---

## 2. Key differences (short)
- **Declaration merging:** only `interface` supports it. You can declare the same interface multiple times and TypeScript merges members.  
- **Expressiveness:** `type` can represent unions, intersections, tuples, primitives, conditional/mapped types; `interface` cannot express unions or mapped/conditional types directly.  
- **Extending/implementing:** Both can be extended/implemented by classes, but `interface` uses `extends` while `type` often uses `&` (intersection) to compose.
- **Error messages & printing:** Historically interfaces often give nicer named errors; type printing behavior has improved over TS versions.

---

## 3. Declaration merging (interfaces only)
```ts
// file A
interface User {
  name: string;
}

// file B (or later in same file)
interface User {
  age: number;
}

// Resulting User = { name: string; age: number; }
const u: User = { name: "Harshith", age: 26 };
```
Declaration merging is a core reason libraries (and lib.dom) use interfaces. citeturn0search0

---

## 4. `type` vs `interface` examples

### Object shape with `interface`
```ts
interface Point {
  x: number;
  y: number;
}
```

### Same with `type`
```ts
type PointT = {
  x: number;
  y: number;
}
```

### Union with `type` (can't with interface)
```ts
type ID = string | number;
```

### Intersection composition
```ts
interface A { a: number }
type B = { b: string }

type AandB = A & B; // works with type aliases
```

Use `extends` for interfaces:
```ts
interface Animal { name: string }
interface Dog extends Animal { bark(): void }
```

For types, use intersections:
```ts
type AnimalT = { name: string }
type DogT = AnimalT & { bark(): void }
```
TS handbook explains composition and when interfaces vs intersections differ. citeturn0search3turn0search8

---

## 5. Practical rules & recommendations
- Prefer `interface` for public library APIs and object-shape declarations — they are open and friendly for merging/extension. citeturn0search4  
- Use `type` when you need unions, tuples, mapped types, or conditional types (advanced type-level programming). citeturn0search1turn0search8  
- Avoid `type` if you rely on declaration merging or want maintainable augmentation of global shapes (like `Window`, library augmentation). citeturn0search0

---

## 6. Interview Theory Q&A (Concise)

1. **Q:** Can `type` aliases be declaration-merged like interfaces?  
   **A:** No — type aliases cannot participate in declaration merging. Use `interface` for merging. citeturn0search1

2. **Q:** When should you prefer an `interface` over a `type`?  
   **A:** When designing object-shaped public APIs, or when you expect others to augment or extend the type (declaration merging). citeturn0search4

3. **Q:** Can classes implement `type` aliases?  
   **A:** Yes, if the `type` describes an object shape, classes can `implements` them. But merging behaviors differ. citeturn0search1

4. **Q:** Can an `interface` represent unions or tuples?  
   **A:** No — interfaces model object shapes. Use `type` for union or tuple expressions. citeturn0search8

5. **Q:** Are there performance or compiler differences?  
   **A:** In some complex cases, `interface` `extends` can be slightly faster than deep intersections; but this is a micro-optimization. Prefer clarity. citeturn0search15

---

## 7. Coding Questions (with answers)

### Q1: Merge two interface declarations across files (showing merged result).
```ts
// user.d.ts
interface Config { url: string }

// user-aug.d.ts
interface Config { timeout: number }

// usage.ts
const cfg: Config = { url: "/api", timeout: 3000 };
```
Result: `Config` has both `url` and `timeout`. citeturn0search0

### Q2: Create a union type for API response.
```ts
type Success = { ok: true; data: string[] }
type Failure = { ok: false; error: string }
type ApiResponse = Success | Failure

function handle(r: ApiResponse) {
  if (r.ok) console.log(r.data);
  else console.error(r.error);
}
```

### Q3: Use `implements` with a `type` alias (works if shape matches).
```ts
type Point = { x: number; y: number }

class MyPoint implements Point {
  constructor(public x: number, public y: number) {}
}
```

### Q4: Convert an intersection type to interface extends (equivalent).
```ts
type A = { a: number }
type B = { b: string }

type AB = A & B

// Equivalent with interfaces:
interface IA { a: number }
interface IB { b: string }
interface IAB extends IA, IB {}
```

---

## 8. Short summary for quick memory
- `interface` = open, mergeable, best for object APIs.  
- `type` = closed, expressive (unions/tuples/mapped types), best for complex type-level constructs.  
- Use whichever makes code clearer; prefer interfaces for public shapes and types for advanced type machinery. citeturn0search4turn0search1

---

## Sources
- TypeScript Handbook — Declaration Merging.  
- TypeScript Handbook — Everyday Types & Objects.  
- TypeScript Handbook — Unions & Intersections.  
(official docs and community resources.)

# TypeScript: Decorators Cheat Sheet
**Topic:** TypeScript  
**Sub Topic:** Decorators (class decorators, property decorators, experimental decorators)

---

## 1. Quick summary
Decorators are functions prefixed with `@` that can annotate and *meta-program* classes and their members at runtime — class, method, accessor, property, and parameter. They’re an *experimental* language feature in TypeScript and require compiler opts to enable. citeturn0search0turn0search1

---

## 2. Enable in your project
In `tsconfig.json`:
```json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true, // optional — emits design-time types (works with reflect-metadata)
    "target": "ES5"
  }
}
```
`emitDecoratorMetadata` helps libraries read runtime type metadata but depends on `reflect-metadata` or similar. Be aware some toolchains mark these flags deprecated or evolving — check your environment. citeturn0search1turn0search22turn0search5

---

## 3. Decorator kinds & signatures

- **Class decorator**  
  Called with the class constructor. Can replace or augment the constructor.
  ```ts
  type ClassDecorator = <TFunction extends Function>(target: TFunction) => TFunction | void;
  ```

- **Property decorator**  
  Called with the target (prototype for instance members or constructor for static) and property key.
  ```ts
  type PropertyDecorator = (target: Object, propertyKey: string | symbol) => void;
  ```

- **Method decorator**  
  Receives target, property key, and `PropertyDescriptor` allowing modification of the method.
  ```ts
  type MethodDecorator = (target: Object, propertyKey: string | symbol, descriptor: PropertyDescriptor) => PropertyDescriptor | void;
  ```

- **Accessor decorator**  
  Same signature as method decorator but used for getters/setters.

- **Parameter decorator**  
  Receives target, property key, and parameter index — useful for DI metadata.
  ```ts
  type ParameterDecorator = (target: Object, propertyKey: string | symbol, parameterIndex: number) => void;
  ```
All signatures and behavior are described in the TypeScript handbook. citeturn0search0

---

## 4. Decorator factories
Decorators are often implemented as *factories* so you can pass arguments:

```ts
function Role(roleName: string) {
  return function (target: any) {
    target.role = roleName;
  }
}

@Role("admin")
class User {}
```

---

## 5. Common patterns & examples

### a) Class decorator — add static metadata
```ts
function sealed(constructor: Function) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
}

@sealed
class Greeter {}
```

### b) Method decorator — logging / timing
```ts
function log(target: any, key: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`call ${key}`, args);
    return original.apply(this, args);
  };
}

class X { @log hello(name: string) { return `hi ${name}` } }
```

### c) Property decorator — register fields (no descriptor)
Property decorators cannot directly change property descriptors for instance properties (they run at declaration time). Use them to record metadata.
```ts
function field(target: any, key: string) {
  const ctor = target.constructor;
  ctor._fields = (ctor._fields || []).concat(key);
}
```

### d) Parameter decorator — DI token
```ts
function inject(token: string) {
  return function (target: any, key: string | symbol, index: number) {
    Reflect.defineMetadata(`inject_${String(key)}_${index}`, token, target);
  };
}
```

---

## 6. Metadata & `reflect-metadata`
TypeScript can emit design-time type metadata (types of parameters, return type, property types) when `emitDecoratorMetadata` is enabled. To **read** that metadata at runtime you typically use the `reflect-metadata` polyfill and the `Reflect` API (`Reflect.getMetadata`, `Reflect.defineMetadata`). This is commonly used for dependency injection, serialization, and validation. citeturn0search22turn0search3

**Example:**
```ts
import "reflect-metadata";

class Service {}

class C {
  constructor(private s: Service) {}
}

Reflect.getMetadata("design:paramtypes", C); // -> [Service]
```

---

## 7. Evaluation & application order
- Decorators are evaluated top-to-bottom when **declared**, but the decorator *expressions* are evaluated bottom-to-top when multiple are applied. Method / parameter decorators execute before class decorators. Details in the handbook. citeturn0search0

---

## 8. Caveats & best practices
- **Experimental:** Decorators in TypeScript are based on older decorator proposal semantics. The ECMAScript decorator proposal evolved (stage 3+), and the exact shape/semantics differ; follow TypeScript docs for compatibility notes. citeturn0search1turn0search19  
- **Class fields interaction:** When targeting modern `ES2022+` and using `useDefineForClassFields`, some runtime behaviors change — libraries (e.g., Lit) recommend settings to avoid surprises. citeturn0search11  
- **emitDecoratorMetadata pitfalls:** It produces design-time type metadata which can leak implementation details and increase bundle size; use judiciously. citeturn0search22

---

## 9. Interview Theory Q&A (concise)

1. **What are decorators?**  
   Functions using `@` syntax that annotate/modify classes and members at runtime. citeturn0search0

2. **How do you enable decorators in TypeScript?**  
   Set `"experimentalDecorators": true` in `tsconfig.json`. For metadata also set `"emitDecoratorMetadata": true`. citeturn0search1turn0search22

3. **Can a property decorator change a property descriptor?**  
   Not for instance properties; property decorators are executed at declaration time and don't receive a descriptor for instance fields. Use an accessor or define the property in the class constructor. citeturn0search0

4. **Why use `reflect-metadata`?**  
   To read emitted design-time type metadata at runtime (e.g., parameter types for DI). citeturn0search3turn0search22

5. **Are decorators standard JS?**  
   Decorators were (and are) a TC39 proposal; TS supports an older/de facto version via `experimentalDecorators`. Check current ECMAScript decorator spec for differences. citeturn0search1turn0search19

---

## 10. Coding / practical interview questions

### Q1 — Implement a `@deprecated` decorator for methods that warns when called.
**Answer sketch:**
```ts
function deprecated(target: any, key: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.warn(`${key} is deprecated`);
    return original.apply(this, args);
  };
}
```

### Q2 — Create a class decorator that registers classes in a registry.
**Answer sketch:**
```ts
const registry: any[] = [];
function register(name?: string) {
  return function (ctor: Function) {
    registry.push({ name: name || ctor.name, ctor });
  }
}
@register() class A {}
```

### Q3 — Use `reflect-metadata` to auto-inject constructor params (DI-lite).
**Answer sketch:** Enable `emitDecoratorMetadata`, import `reflect-metadata`, read `"design:paramtypes"` and map types to instances.

### Q4 — Why might decorators break with `useDefineForClassFields: true`?  
Because class field semantics (when fields are defined using `Object.defineProperty` behavior) affect at-creation property assignment timing and may change how decorators interact with initializers. Use conservative tsconfig settings or test with your target. citeturn0search11

---

## 11. TL;DR (two lines)
Decorators are powerful instrumentation tools for classes and members but are still experimental; enable them in `tsconfig`, use `reflect-metadata` for runtime type info, and prefer clear, minimal decorator logic for maintainability. citeturn0search0turn0search22

---

## Sources
- TypeScript Handbook — Decorators. citeturn0search0  
- TypeScript tsconfig reference — `experimentalDecorators`, `emitDecoratorMetadata`. citeturn0search1turn0search22  
- `reflect-metadata` npm & blogs (usage patterns). citeturn0search3turn0search2

# TypeScript: Advanced Types & Strict Mode Cheat Sheet
**Topic:** TypeScript  
**Sub Topics:** Advanced Types (template literal types, `infer`, conditional types)  & Strict Mode (noImplicitAny, strictNullChecks, strictBindCallApply)

---

## Part A — Advanced Types

### 1. Template Literal Types
Template literal types let you build new string literal types by combining other literal types using JS template syntax. Useful for encoding structural constraints in string types (e.g. `id${number}` or event names like `on${Capitalize<string>}`).

```ts
type Id = `id${number}`;
const a: Id = "id123"; // OK
// const b: Id = "abc"; // Error
```

They power patterns like key remapping, string parsing at the type level, and constrained string factories. See the handbook for examples. citeturn0search2

#### Common patterns
- Prefix/suffix matching: `type Ev = \`on${string}\`;`
- Constrained numeric strings: `type Hex = \`${number}x\`;`
- Key remapping in mapped types: `type Camel<T> = { [K in keyof T as \`${K & string}Changed\`]: T[K] }`

---

### 2. Conditional Types
Conditional types provide `T extends U ? X : Y` logic in the type system and are distributive over unions by default (when the checked type is a naked type parameter).

```ts
type NonNullable<T> = T extends null | undefined ? never : T;
```

You can use them to branch the resulting type based on input shapes, implement utility types (like `ReturnType<T>`), and compute derived types. citeturn0search0turn0search6

---

### 3. `infer` keyword (type inference inside conditional types)
`infer` introduces a type variable inside a conditional type so you can extract parts from a type.

```ts
type ElementType<T> = T extends (infer U)[] ? U : T;
type E = ElementType<string[]>; // string

type FnReturn<T> = T extends (...args: any[]) => infer R ? R : never;
```

Use `infer` when you want to pull out a nested type (array element, promise resolved type, function return type). citeturn0search6turn0search8

---

### 4. Practical examples

**Extract promise resolution type**
```ts
type UnwrapPromise<T> = T extends Promise<infer R> ? R : T;
type T1 = UnwrapPromise<Promise<number>>; // number
```

**Convert snake_case keys to camelCase (sketch)**
```ts
type Split<S extends string, D extends string> = 
  S extends `${infer L}${D}${infer R}` ? [L, ...Split<R, D>] : [S];

type CamelCase<S extends string> = /* recursive template/infer + mapped type logic */;
```
(Real implementation uses recursion, template literal types, and mapped types.)

---

### 5. Gotchas & tips
- Conditional types are **distributive** over unions only when the checked type is a plain type parameter; wrap it with a tuple to avoid distribution.
- `infer` can only be used inside conditional types.
- Template literal types can explode into very large unions if misused—watch complexity.
- These features enable powerful type-level programming but can make compiler performance worse for extremely complex types. citeturn0search18turn0search6

---

### 6. Interview Q&A (concise)

1. **What are template literal types?**  
   Types that build string literal types using template syntax (e.g., ``type T = `id${number}```). citeturn0search2

2. **When do conditional types distribute over unions?**  
   They distribute when the checked type is a *naked* type parameter (e.g., `T extends ...`). Wrap in `[T]` to prevent distribution. citeturn0search6

3. **What does `infer` do?**  
   Introduces a type variable inside a conditional type so you can extract a sub-type (like return type, element type). citeturn0search6

4. **Why avoid very deep recursive types?**  
   They increase compile-time complexity and can blow up IDE responsiveness or tsc time.

---

### 7. Coding questions (practice)

- Implement `Flatten<T>` that flattens a nested array type:  
  `type Flatten<T> = T extends (infer U)[] ? U : T;`

- Create `Paths<T>` mapping nested object keys into dot-delimited string literal types using template literal types and conditional recursion.

- Implement `DeepReadonly<T>` using conditional types and mapped types.

---

## Part B — Strict Mode (tsconfig strict flags)

### 1. What is `--strict`?
`--strict` is a convenience flag that enables a set of stricter type-checking options (`noImplicitAny`, `strictNullChecks`, `strictBindCallApply`, `alwaysStrict`, `noImplicitThis`, and `strictFunctionTypes`, among others). It pushes the compiler to require explicitness and reduces chances of runtime errors. citeturn0search17turn0search1

Enable in `tsconfig.json`:
```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

---

### 2. `noImplicitAny`
When enabled, the compiler errors on expressions and declarations that have an implicit `any` type. Forces you to explicitly type things rather than rely on unsafely inferred `any`. Good for catching missing annotations and preventing type-unsafe code. citeturn0search7

**Example**
```ts
function f(x) { return x + 1 } // Error under noImplicitAny
function f(x: number) { return x + 1 } // OK
```

---

### 3. `strictNullChecks`
When `true`, `null` and `undefined` are distinct types and cannot be assigned to other types unless explicitly allowed. This forces handling of absent values and reduces `TypeError` at runtime. Example: `string | null` vs `string`.

```ts
let s: string = null; // Error if strictNullChecks true
let t: string | null = null; // OK
```
This flag is one of the most impactful for code safety. citeturn0search3

---

### 4. `strictBindCallApply`
Tightens type checking for `Function.prototype.bind`, `call`, and `apply` so that argument lists and `this` types are validated more strictly. This helps catch incorrect `this` or parameter usage when binding/calling functions. citeturn0search11

**Example**
```ts
function add(a: number, b: number) { return a + b; }
add.call(null, 1, "x"); // Error under strictBindCallApply
```

---

### 5. Practical migration tips
- Turn on `noImplicitAny` first and fix errors incrementally (add types, use `unknown` instead of `any` where appropriate).
- Use `strictNullChecks` to surface nullability bugs; refactor code to explicitly `| null` or guard use sites.
- Prefer `strict: true` for new projects. Note: there are discussions about making `--strict` the default in TS future versions; check TypeScript releases for exact behavior. citeturn0search13

---

### 6. Interview Q&A (concise)

1. **What does `strict` enable?**  
   A bunch of flags that tighten type checking including `noImplicitAny`, `strictNullChecks`, etc. citeturn0search17

2. **Why enable `strictNullChecks`?**  
   It forces you to handle `null`/`undefined` explicitly, preventing many runtime crashes. citeturn0search3

3. **How to gradually adopt strict mode?**  
   Turn on specific flags (start with `noImplicitAny`, `strictNullChecks`) and fix errors incrementally.

---

## TL;DR
- Advanced types (`template literal types`, `conditional types`, `infer`) let you compute and transform types programmatically — extremely powerful but capable of hurting compile performance if abused. citeturn0search2turn0search6  
- `--strict` and its subflags (`noImplicitAny`, `strictNullChecks`, `strictBindCallApply`) increase correctness by forcing explicitness and safer assumptions. Prefer enabling them for new projects. citeturn0search17turn0search3

---

## Quick references
- Template literal types — TypeScript Handbook. citeturn0search2  
- Conditional types & `infer` — TypeScript Handbook. citeturn0search0turn0search6  
- `tsconfig` strict flags — TypeScript docs. citeturn0search17turn0search1


1. Theory & Deep Dive

Here we’ll walk through the key pieces: how to type functional components (FC), props, state, events and refs in a React + TypeScript setting. (Yes—nerdy details ahead.)

1.1 Typing Functional Components (FC)

In React with TS you often write components as functions (.tsx files). The simplest way:

```ts
type Props = {
  title: string;
};

const MyComponent = ({ title }: Props) => {
  return <h1>{title}</h1>;
};

```

You can also explicitly annotate the component with React.FC<Props> (or React.FunctionComponent<Props>):

```ts
const MyComponent: React.FC<Props> = ({ title }) => {
  return <h1>{title}</h1>;
};

```

But note: using React.FC adds implicit children prop (by default) and has some quirks (e.g., defaultProps behaviour).

Some best-practice commentary: many prefer not to use React.FC because the added benefits are minimal and some drawbacks appear. Example: the children prop is implicitly included even if you don’t want it.

1.2 Typing Props

Declare a type or interface for props:

```ts
interface ButtonProps {
  label: string;
  disabled?: boolean;  // optional
  onClick: () => void;
}

const Button = ({ label, disabled, onClick }: ButtonProps) => (
  <button disabled={disabled} onClick={onClick}>
    {label}
  </button>
);


```

Useful prop-type patterns:

Union types: status: "idle" | "loading" | "success"; 
React TypeScript Cheatsheets

Arrays: names: string[];

Objects: user: { id: string; name: string; }

Functions: onChange: (value: number) => void or onClick: (event: React.MouseEvent<HTMLButtonElement>) => void 
React TypeScript Cheatsheets
+1

Optional props: use ?

1.3 Typing State (in Functional Components / Hooks)

Since you’re covering React with TS, you’ll often use hooks like useState, useReducer.

useState infers type from initial value:

Since you’re covering React with TS, you’ll often use hooks like useState, useReducer.

useState infers type from initial value:

```ts
const [count, setCount] = useState(0); // count: number

```

- If you initialise with null or a more complex type, you might need to provide the type explicitly:

```ts
const [user, setUser] = useState<User | null>(null);

```

Where type User = { id: string; name: string; }.

If you use useReducer, you’ll define State and Action types. Example omitted here for brevity.

1.4 Event Types

When handling events (clicks, changes, forms), TS + React supply types:

Common event types:

React.MouseEvent<HTMLButtonElement> for button click events. 


React.ChangeEvent<HTMLInputElement> for input change events. 

React.FormEvent<HTMLFormElement> for form submission. 
Convex

Use React.SyntheticEvent for generic events. 

```ts
interface InputProps {
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Input = ({ onChange }: InputProps) => (
  <input type="text" onChange={onChange} />
);

```

1.5 Ref Types

Refs give you access to DOM elements (or component instances). With TS, you type them explicitly.

```ts
const inputRef = useRef<HTMLInputElement>(null);

const handleClick = () => {
  if (inputRef.current) {
    inputRef.current.focus();
  }
};

return <input ref={inputRef} />;

```

- Use React.RefObject<Type> or React.MutableRefObject<Type> depending on scenario. 
- If you forward refs (React.forwardRef), you’ll need to use generic ref typing appropriately.

1.6 “Putting it together” small full example

```ts
import React, { FC, useState, useRef, ChangeEvent, MouseEvent } from 'react';

interface MyComponentProps {
  initialValue: number;
  onSubmit: (value: number) => void;
}

const MyComponent: FC<MyComponentProps> = ({ initialValue, onSubmit }) => {
  const [value, setValue] = useState<number>(initialValue);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleChange = (e: ChangeEvent<HTMLInputElement>): void => {
    setValue(Number(e.target.value));
  };

  const handleSubmit = (e: MouseEvent<HTMLButtonElement>): void => {
    e.preventDefault();
    onSubmit(value);
  };

  const focusInput = (): void => {
    inputRef.current?.focus();
  };

  return (
    <form>
      <input ref={inputRef} type="number" value={value} onChange={handleChange} />
      <button onClick={handleSubmit}>Submit</button>
      <button type="button" onClick={focusInput}>Focus</button>
    </form>
  );
};

```

2. Interview-Style Questions & Concise Answers

| Question                                                                    | Answer                                                                                                                                                                                                                                                                                                   |               |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| What is `React.FC<Props>` and should you always use it?                     | `React.FC<Props>` is a type alias for a functional component with props of type `Props`, includes implicit `children` prop. You do ·not· always need to use it—some prefer simple function with typed props because `React.FC` adds quirks (children, defaultProps) and verbosity. ([Stack Overflow][1]) |               |
| How do you type props with optional and callback props?                     | Use `?` for optional, e.g. `disabled?: boolean`. For callback: e.g. `onClick: () => void` or `onChange: (value: number) => void`.                                                                                                                                                                        |               |
| If you call `useState(null)` what issue arises in TS and how do you fix it? | TS infers type as `null`, so you cannot later set it to something else (e.g., an object). Fix by providing generic: `useState<MyType                                                                                                                                                                     | null>(null)`. |
| How to type a change event on an `<input>` element?                         | Use `React.ChangeEvent<HTMLInputElement>` as the event type.                                                                                                                                                                                                                                             |               |
| How to type a ref for a DOM element in React TS?                            | Use `useRef<HTMLDivElement>(null)` or similar. The ref type is `RefObject<HTMLDivElement>`.                                                                                                                                                                                                              |               |
| What is `React.ReactNode` vs `React.ReactElement`?                          | `React.ReactNode` is any valid React child (string, number, element, array, fragment, null). `React.ReactElement` is a React element (JSX) specifically. Useful when you type `children`. ([React][2])                                                                                                   |               |

[1]: https://stackoverflow.com/questions/59988667/typescript-react-fcprops-confusion?utm_source=chatgpt.com "TypeScript React.FC<Props> confusion - javascript"
[2]: https://react.dev/learn/typescript?utm_source=chatgpt.com "Using TypeScript"

3. Coding Questions (Application)

Here are coding-style questions you might face in an interview or practise exercise. Try solving (coding) them.

Create a functional component UserCard in TS which takes props: { user: { id: string; name: string; email: string }, onSelect: (id: string) => void }. Include a button that calls onSelect(user.id) when clicked.

Write a component TextInputWithFocusButton which has an input and a “Focus” button. Use useRef to focus the input when button clicked. Typing must ensure inputRef is of correct type.

Implement a hook useToggle in TS: const [on, toggle] = useToggle(initial: boolean). Ensure types for state and toggle function.

Build a simple form component LoginForm with props: { onSubmit: (credentials: { username: string; password: string }) => void }. Use local state for username/password. Type the state, event handlers correctly.

Given a list of items of generic type T, design a component List<T> that takes props { items: T[], renderItem: (item: T) => JSX.Element }. Show how you’d type List using generics in TS + React.


# Topic : TypeScript Generics with React
## Sub Topic : HOC typing, useState generic, polymorphic components

---

## Overview
This cheat-sheet covers practical patterns for using **TypeScript generics** in React with a focus on:
- **Higher-Order Components (HOC)** typing
- **useState** with generics
- **Polymorphic components** (components that can render different element types via an `as`/`component` prop)

Generics let you write reusable code that adapts to different types while preserving type safety. (See TypeScript generics docs for the core concepts.)

---

## 1. Basics: Generics recap
```ts
function identity<T>(value: T): T {
  return value;
}
```
`T` is a type parameter; the function works for any `T`. In React, generics are commonly used on props, component factories, hooks and utility types.

---

## 2. useState with generics
Type inference often saves you — but when initial state is ambiguous or `null`/`undefined` is involved, explicitly provide the type.

Examples:

```tsx
// inferred
const [count, setCount] = useState(0); // number inferred

// explicit generic (for complex objects)
interface User { name: string; age: number }
const [user, setUser] = React.useState<User | null>(null);

// arrays
const [items, setItems] = React.useState<string[]>([]);
```

When initial value is `null` but you plan to set an object later:
```tsx
const [profile, setProfile] = React.useState<Profile | null>(null);
```

If the initial value is derived but inference fails, you can pass a generic:
```tsx
const [state, setState] = React.useState<MyState>(() => computeInitialState());
```

---

## 3. HOCs with TypeScript generics
A robust pattern for HOCs is to make the HOC generic over the wrapped component's props.

```tsx
import React from "react";

function withLogger<P extends object>(WrappedComponent: React.ComponentType<P>) {
  return function WithLogger(props: P) {
    React.useEffect(() => {
      console.log("props:", props);
    }, [props]);
    return <WrappedComponent {...props} />;
  };
}

// Usage:
type MyProps = { name: string };
const Hello: React.FC<MyProps> = ({ name }) => <div>Hello {name}</div>;
const HelloWithLogger = withLogger(Hello);
// HelloWithLogger expects { name: string } as props — types preserved.
```

For HOCs that add props, use `Omit` to remove injected prop names from the consumer-facing props:

```tsx
function withAuth<P extends object>(WrappedComponent: React.ComponentType<P & { user: User }>) {
  return function WithAuth(props: Omit<P, "user">) {
    const user = getUserFromContext();
    return <WrappedComponent {...(props as P)} user={user} />;
  };
}
```

Notes:
- Prefer `ComponentType<P>` to accept both function and class components.
- Use `Omit` when the HOC injects props so callers can't supply them.

---

## 4. Polymorphic components (the `as` pattern)
Polymorphic components adapt their rendered element via an `as` prop, while keeping attribute typings consistent.

Minimal pattern:

```tsx
type AsProp<C extends React.ElementType> = {
  as?: C;
};

type PropsToOmit<C extends React.ElementType, P> = P & Omit<React.ComponentPropsWithoutRef<C>, keyof P>;

type PolymorphicComponentProps<C extends React.ElementType, P = {}> = P & AsProp<C> & Omit<React.ComponentPropsWithoutRef<C>, keyof P | "as">;

const Box = <C extends React.ElementType = "div">(
  { as, children, ...rest }: PolymorphicComponentProps<C, { children?: React.ReactNode }>,
  ref: React.ForwardedRef<any>
) => {
  const Component = as || "div";
  // @ts-ignore
  return <Component ref={ref} {...rest}>{children}</Component>;
};

const ForwardedBox = React.forwardRef(Box);
```

Usage:
```tsx
<ForwardedBox as="a" href="/home">Link</ForwardedBox>
<ForwardedBox as="button" type="button">Button</ForwardedBox>
```

Important details:
- Use `React.ElementType` and `React.ComponentPropsWithoutRef<C>` to derive correct props for the underlying element.
- Combine with `forwardRef` to keep ref typing correct.
- This pattern is used by component libraries (Chakra UI, MUI) for their `as`/`component` props.

---

## 5. Common pitfalls and tips
- **Overly complex types**: Polymorphic components can be tricky; keep utility types small and well-commented.
- **Generic JSX components**: When declaring a generic functional component, use the `const Comp = <T,>(props: Props<T>) => {}` syntax so TypeScript parses the `<` correctly.
- **HOCs + generics**: Generic wrapped components need careful typing; consider wrapper factories when needed.
- **Prefer composition/hooks** over HOCs when possible — easier typing and better performance.

---

## Interview-style theory Q&A (concise)
Q: When should you provide an explicit generic to `useState`?  
A: When the initial value cannot be inferred (e.g., `null`, empty array where shape matters), or when you want a specific union type like `T | null`. fileciteturn0file_placeholder

Q: What's a safe HOC typing pattern?  
A: Make the HOC generic over `P extends object` and accept `React.ComponentType<P>`; use `Omit` for injected props. (Keeps props intact.) fileciteturn0file_placeholder

Q: Why are polymorphic components hard to type?  
A: Because the underlying element type changes the allowed props (e.g., `href` for `a`, `type` for `button`), and the types must reflect that to avoid invalid props. fileciteturn0file_placeholder

---

## Practical coding interview tasks
1. **Write a `useLocalStorage<T>` hook** that uses a generic type for stored item and handles `null`/`undefined`.  
2. **Implement a `withLoading` HOC** which injects `loading` prop and preserves wrapped component props.  
3. **Create a polymorphic `Box` component** supporting `as` and forwarding refs with correct prop inference.

Short starter for `useLocalStorage<T>`:
```ts
function useLocalStorage<T>(key: string, initialValue: T) {
  const [state, setState] = React.useState<T>(() => {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) as T : initialValue;
  });

  React.useEffect(() => {
    localStorage.setItem(key, JSON.stringify(state));
  }, [key, state]);

  return [state, setState] as const;
}
```

---

## References & further reading
- TypeScript handbook — Generics.  
- Guides and blog posts on HOC typing, polymorphic components, and useState generics.

---

## License
Feel free to copy, tweak, and use in interviews or study notes.

# TypeScript Cheat Sheet: Error Handling & Config Mastery

## Topic: TypeScript  
## Sub Topic: Error Handling (try/catch with `unknown`) & `tsconfig.json` Mastery

---

# 1. TypeScript Error Handling with `try/catch` + `unknown`

TypeScript treats anything caught in a `catch` block as `unknown` (recommended) or `any` (unsafe).  
Using `unknown` forces proper type‑narrowing before accessing properties.

### Why `unknown`?
`unknown` ensures type‑safety so you don’t accidentally assume an error is always `Error`.

### Safe Narrowing Pattern
```ts
try {
  riskyOperation();
} catch (err: unknown) {
  if (err instanceof Error) {
    console.error("Error message:", err.message);
  } else {
    console.error("Unexpected error:", err);
  }
}
```

### Custom Error Types
```ts
class ApiError extends Error {
  constructor(public status: number, msg: string) {
    super(msg);
  }
}

try {
  throw new ApiError(404, "Not Found");
} catch (err: unknown) {
  if (err instanceof ApiError) {
    console.log(err.status, err.message);
  }
}
```

### When to Avoid `any`
Using `any` in `catch` disables safety checks, making hidden bugs likely.

---

# 2. TypeScript Config Mastery — `tsconfig.json`

A well-tuned `tsconfig.json` improves performance, code quality, and DX.

### Most Important Fields

### `target`
Determines JavaScript output version.
- `"ES5"`: Legacy browser support  
- `"ES2015+"`: Modern JS (recommended)  
- `"ESNext"`: Latest features

### `lib`
Controls built-in type definitions available.
```json
"lib": ["ES2021", "DOM"]
```

### `paths` + `baseUrl`
Enables module path aliasing.
```json
{
  "compilerOptions": {
    "baseUrl": "src",
    "paths": {
      "@utils/*": ["utils/*"],
      "@components/*": ["components/*"]
    }
  }
}
```

### `skipLibCheck`
Skips type-checking `.d.ts` files for faster builds (common in large apps).
```json
"skipLibCheck": true
```

### Common Useful Settings
```json
{
  "strict": true,
  "esModuleInterop": true,
  "forceConsistentCasingInFileNames": true,
  "resolveJsonModule": true,
  "noImplicitAny": true
}
```

### Example `tsconfig.json` Template
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM"],
    "baseUrl": "./src",
    "paths": {
      "@/*": ["*"]
    },
    "strict": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "moduleResolution": "Node",
    "resolveJsonModule": true
  }
}
```

---

# 3. Interview Theory Questions (Concise Answers)

### 1. Why does TypeScript treat `catch` error as `unknown`?
Because an error can be anything, not guaranteed to be `Error`. `unknown` ensures safety and narrowing.

### 2. How is `unknown` different from `any`?
`unknown` requires type checks; `any` bypasses type safety.

### 3. How do you safely narrow unknown errors?
`instanceof`, `typeof`, property checks.

### 4. What does `skipLibCheck` do?
Skips type-checking declaration files to speed up builds.

### 5. What is the role of the `target` field?
Controls JS version TypeScript emits.

### 6. Why use `paths`?
To configure alias imports for cleaner and maintainable folder structures.

### 7. What is the impact of `"strict": true`?
Enables the strictest type-checking mode.

---

# 4. Coding Interview Tasks

### Task 1: Safely handle an unknown error and extract custom fields.
```ts
function parseUserData(json: string) {
  try {
    return JSON.parse(json);
  } catch (err: unknown) {
    if (err instanceof SyntaxError) {
      console.log("Invalid JSON:", err.message);
    }
    return null;
  }
}
```

### Task 2: Implement a function with custom Error class.
```ts
class ValidationError extends Error {
  constructor(public field: string, msg: string) {
    super(msg);
  }
}

function validateUser(user: any) {
  if (!user.name) {
    throw new ValidationError("name", "Name is required");
  }
}
```

### Task 3: Configure a `tsconfig.json` with aliasing.
```json
{
  "compilerOptions": {
    "baseUrl": "src",
    "paths": {
      "@models/*": ["models/*"],
      "@services/*": ["services/*"]
    }
  }
}
```

---

This file is your compact but complete interview-ready reference for TypeScript error handling and configuration mastery.

# TypeScript Cheat Sheet: Performance & Build; Best Practices; Tooling

## Topic: TypeScript
## Sub Topic: Performance & Build — Best Practices — Tooling

---

## 1) Performance & Build (emit options, incremental build, declaration files)

### Key concepts
- **Incremental builds**: Enable `incremental: true` (creates `.tsbuildinfo`) to cache compilation state and speed up subsequent builds. Useful for iterative development and large projects. See TypeScript docs for details.  
- **Project references / composite builds**: Break a large codebase into smaller TypeScript projects and use `tsc -b` to build only changed projects; `composite: true` enables faster inter-project builds. This is the recommended approach for monorepos or large libraries.  
- **Emit options**: `outDir`, `declaration`, `sourceMap`, `emitDeclarationOnly`, `declarationMap` and `removeComments` control what compiler outputs. For libraries, enable `declaration` and `declarationMap` to ship `.d.ts` files for consumers. For applications, you often disable declarations and focus on `sourceMap`/`outDir`.  
- **.tsbuildinfo**: Produced by `incremental` builds; safe to keep in CI caches for faster CI builds or ignore in VCS, depending on your workflow.

### Recommended tsconfig settings (example)
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "outDir": "dist",
    "rootDir": "src",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "incremental": true,
    "tsBuildInfoFile": "./.tsbuildinfo",
    "composite": false,
    "skipLibCheck": true,
    "strict": true,
    "moduleResolution": "Node",
    "esModuleInterop": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

### Practical tips
- Turn on `incremental` locally and in CI caches to avoid recompiling unchanged files. citeturn0search0turn0search17  
- Use **project references** (`composite: true`, `references`) for multi-package repos to get deterministic and fast `tsc -b` builds. citeturn0search4  
- Only generate `.d.ts` files for packages you publish; unnecessary declaration generation in apps increases build time. citeturn0search2  
- Use `emitDeclarationOnly` if you want to generate only `.d.ts` files (useful in some packaging flows). citeturn0search16

---

## 2) Best Practices (type-safe API calls, DTO types, avoiding `any`)

### Core principles
- Prefer **exact types** (interfaces, `type` aliases) for public APIs and DTOs (Data Transfer Objects) rather than `any` or very loose types.  
- Use `unknown` for external/untyped inputs and narrow with type guards before use.  
- Keep runtime validation separate from TypeScript types. Types are design-time guarantees — for runtime safety, use validators (e.g., `zod`, `io-ts`, `superstruct`) and transform into typed values.  
- Use `Readonly`, `Pick`, `Omit`, mapped and conditional types to keep DTOs precise and minimal.

### API and DTO patterns
- Define DTOs for inbound/outbound shapes:
```ts
type CreateUserDTO = {
  name: string;
  email: string;
  age?: number;
};
```
- Validate incoming JSON at runtime:
```ts
import { z } from "zod";
const CreateUserSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  age: z.number().optional()
});
type CreateUserDTO = z.infer<typeof CreateUserSchema>;
```
- Keep API client typings generated from OpenAPI/GraphQL when possible to avoid drift.

### Avoiding `any`
- Use `unknown` in `catch` blocks and narrow before usage:
```ts
try {
  // ...
} catch (err: unknown) {
  if (err instanceof Error) {
    console.error(err.message);
  }
}
```
- Add `noImplicitAny` and `strict` in `tsconfig` to force safer typing.

---

## 3) Tooling (ESLint with TypeScript, tsc watch, type coverage tools)

### ESLint + TypeScript
- Use the `@typescript-eslint` family (parser + plugin). Follow the official quickstart to wire ESLint to parse TypeScript and enable recommended rules. citeturn0search5
- For rules that need type information (e.g., `@typescript-eslint/no-unnecessary-condition`), configure ESLint to load your `tsconfig` with the parserOptions.project setting (typed linting). Note: typed linting increases ESLint cost — consider running it as part of CI rather than on every keystroke.

### tsc watch and developer experience
- `tsc --watch` recompiles on file changes and keeps the compiler in memory for fast incremental notifications. Use `--watch` for iterative development or integrate with `nodemon`/`tsc-watch` for restarting servers on changes. citeturn0search8turn0search1

### Type coverage & measurement
- Tools like `type-coverage` and coverage-reporters can show the percentage of identifiers that are not `any` and help enforce typing standards. Integrate them into CI or pre-commit checks for repositories that require strict typing metrics. citeturn0search6turn0search11

---

## Interview Theory Questions (concise answers)

1. **What does `incremental: true` do?**  
   Saves compilation state to a `.tsbuildinfo` file to speed up subsequent compilations. citeturn0search0

2. **When should you use project references?**  
   When a repo is large or multi-package — they allow building only the changed parts with `tsc -b`. citeturn0search4

3. **Why generate `.d.ts` files?**  
   They provide type metadata to consumers of your library and enable editor intellisense. citeturn0search2

4. **Difference between `any` and `unknown` in `catch` blocks?**  
   `unknown` forces narrowing and is safer; `any` bypasses the type system. (TypeScript design principle)

5. **Why use runtime validators like `zod` together with TypeScript?**  
   Types are erased at runtime; validators ensure the data actually matches the expected shape at runtime.

6. **What is typed linting in ESLint?**  
   Running ESLint rules that use type information by pointing the parser at your `tsconfig`—more accurate but costlier.

---

## Coding Interview Tasks

1. **Implement incremental tsbuild caching (tsconfig snippet)**  
```json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo",
    "outDir": "dist"
  }
}
```

2. **Write a typed API client function with DTO and runtime validation**
```ts
import fetch from "node-fetch";
import { z } from "zod";

const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string()
});
type User = z.infer<typeof UserSchema>;

export async function getUser(id: string): Promise<User> {
  const res = await fetch(`https://api.example.com/users/${id}`);
  const json = await res.json();
  const parsed = UserSchema.parse(json); // throws on invalid
  return parsed;
}
```

3. **ESLint typed-lint example (partial `.eslintrc.js`)**
```js
module.exports = {
  parser: "@typescript-eslint/parser",
  parserOptions: {
    project: "./tsconfig.json"
  },
  plugins: ["@typescript-eslint"],
  extends: ["plugin:@typescript-eslint/recommended", "plugin:@typescript-eslint/recommended-requiring-type-checking"]
};
```

4. **Simple `tsc --watch` npm script**
```json
{
  "scripts": {
    "build": "tsc -p tsconfig.json",
    "watch": "tsc -w -p tsconfig.json"
  }
}
```

---

## Quick checklist before shipping a TypeScript package
- [ ] `declaration: true` and `declarationMap: true` for libraries.
- [ ] Ensure `rootDir` and `outDir` are configured and consistent.
- [ ] Add `skipLibCheck: true` to speed up CI builds when safe.
- [ ] Consider `incremental` with CI cache of `.tsbuildinfo`.
- [ ] Add typed lint or type-coverage checks in CI if you need to enforce typing level.

---

## Sources
Key docs and references used to compile this cheat sheet:
- TypeScript tsconfig `incremental` and `.tsbuildinfo` docs. citeturn0search0  
- TypeScript Project References handbook. citeturn0search4  
- `declaration` option documentation. citeturn0search2  
- `tsc --watch` / watch configuration docs. citeturn0search8  
- `@typescript-eslint` getting started guide. citeturn0search5  
- `type-coverage` tool repository. citeturn0search6turn0search11

---

*File generated for download.*
