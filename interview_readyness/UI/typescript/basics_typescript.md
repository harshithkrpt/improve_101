
# 🟢 TypeScript Basics: Complete Guide

This document covers all the **basic** TypeScript topics required to build a solid foundation in the language.

---

## ✅ Fundamentals

### 📌 What is TypeScript?
TypeScript is a strongly typed superset of JavaScript that compiles to plain JavaScript. It adds optional static typing, interfaces, and other features to enable better tooling and large-scale application development.

### 📌 Why Use TypeScript?
- Catches errors at compile time
- IDE auto-completion and type inference
- Improves readability and maintainability
- Better integration with modern frameworks like React, Angular

---

### 📌 TypeScript vs JavaScript
| Feature            | JavaScript      | TypeScript        |
|--------------------|------------------|--------------------|
| Typing             | Dynamic          | Static (optional)  |
| Compilation        | Not required     | Required (tsc)     |
| Interfaces/Types   | Not available    | Fully supported    |

---

## ✅ Type Inference
TypeScript can infer the type based on value:

```ts
let name = "Harshith"; // inferred as string
let count = 5;         // inferred as number
```

---

## ✅ Basic Types

### 🧩 Primitive Types
- `string`
- `number`
- `boolean`
- `null`
- `undefined`

```ts
let title: string = "TypeScript";
let isPublished: boolean = true;
```

---

### 🧩 Special Types
- `any`: Turns off type checking
- `unknown`: Safer alternative to `any`
- `void`: No return value (used in functions)
- `never`: Function never returns (e.g., throws error)

```ts
let value: any = 10;
let input: unknown = "text";

function log(): void {
  console.log("Hello");
}

function error(): never {
  throw new Error("Error!");
}
```

---

## ✅ Type Annotations
Explicitly define types for variables, parameters, and return values.

```ts
let userName: string;
function greet(name: string): string {
  return `Hello, ${name}`;
}
```

---

## ✅ Arrays and Tuples

### 🔹 Arrays
```ts
let numbers: number[] = [1, 2, 3];
```

### 🔹 Tuples
```ts
let person: [string, number] = ["Alice", 25];
```

---

## ✅ Enums
```ts
enum Direction {
  Up,
  Down,
  Left,
  Right
}

let move: Direction = Direction.Up;
```

---

## ✅ Type Aliases vs Interfaces

### 🔹 Type Alias
```ts
type User = {
  name: string;
  age: number;
};
```

### 🔹 Interface
```ts
interface User {
  name: string;
  age: number;
}
```

| Feature           | Type Alias | Interface |
|-------------------|------------|-----------|
| Extends           | ❌         | ✅        |
| Merging           | ❌         | ✅        |
| Unions            | ✅         | ❌        |

---

## ✅ Union and Intersection Types

### 🔹 Union Type
```ts
let id: number | string;
```

### 🔹 Intersection Type
```ts
type A = { name: string };
type B = { age: number };
type C = A & B; // { name: string; age: number }
```

---

## ✅ Functions

### 📌 Function Types and Return Types
```ts
function add(x: number, y: number): number {
  return x + y;
}
```

### 📌 Optional and Default Parameters
```ts
function greet(name?: string) {
  return `Hello ${name || "Guest"}`;
}

function welcome(name: string = "Guest") {
  return `Welcome, ${name}`;
}
```

### 📌 Rest Parameters
```ts
function sum(...nums: number[]): number {
  return nums.reduce((a, b) => a + b, 0);
}
```

---

## ✅ Objects & Interfaces

### 📌 Declaring Object Types
```ts
let user: { name: string; age: number } = {
  name: "Harshith",
  age: 25
};
```

### 📌 `readonly` and Optional Properties
```ts
interface User {
  readonly id: number;
  name: string;
  age?: number;
}
```

---

### 📌 Structural Typing (Duck Typing)
```ts
interface Point {
  x: number;
  y: number;
}

function printPoint(p: Point) {
  console.log(p.x, p.y);
}

const obj = { x: 10, y: 20, z: 30 };
printPoint(obj); // valid due to structural typing
```

---

## ✅ Type Narrowing

### 📌 Type Guards
```ts
function print(value: string | number) {
  if (typeof value === "string") {
    console.log(value.toUpperCase());
  } else {
    console.log(value.toFixed(2));
  }
}
```

### 📌 `instanceof` Check
```ts
if (someValue instanceof Date) {
  someValue.getTime();
}
```

### 📌 Custom Type Guard
```ts
function isString(x: unknown): x is string {
  return typeof x === "string";
}
```

---

## ✅ Discriminated Unions
```ts
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; side: number };

function area(shape: Shape) {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.side ** 2;
  }
}
```

---

## ✅ Modules

### 📌 ES Modules and TypeScript Modules
TypeScript supports ES Modules using `import` and `export`.

```ts
// math.ts
export function add(a: number, b: number): number {
  return a + b;
}

// app.ts
import { add } from "./math";
```

---

### 📌 Namespaces (Legacy, Avoid in Modern Code)
```ts
namespace Utils {
  export function log(msg: string) {
    console.log(msg);
  }
}
Utils.log("Hello");
```

---

## ✅ Summary

| Topic              | Description                        |
|--------------------|------------------------------------|
| Types              | Basic & Special Types              |
| Functions          | Return, optional, rest parameters  |
| Objects & Interfaces| Object structure and duck typing |
| Type Guards        | `typeof`, `instanceof`, custom     |
| Modules            | ES Module support & legacy         |

---

## 📚 Further Reading
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Learn TypeScript](https://www.typescriptlang.org/)
