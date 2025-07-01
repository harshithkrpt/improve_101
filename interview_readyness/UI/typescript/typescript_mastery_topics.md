
# Mastering TypeScript: Complete Topics List

This guide outlines all the **basic**, **intermediate**, and **advanced** TypeScript topics needed to master the language.

---

## 🟢 Basic TypeScript Topics

### ✅ Fundamentals
- What is TypeScript and why use it
- TypeScript vs JavaScript
- Type Inference
- Basic Types:
  - `number`, `string`, `boolean`, `null`, `undefined`
  - `any`, `unknown`, `void`, `never`
- Type Annotations
- Arrays and Tuples
- Enums
- Type Aliases vs Interfaces
- Union and Intersection Types

### ✅ Functions
- Function Types and Return Types
- Optional and Default Parameters
- Rest Parameters
- `void` and `never` return types

### ✅ Objects & Interfaces
- Declaring Object Types
- `readonly` and optional properties
- Structural typing (Duck typing)

### ✅ Type Narrowing
- Type Guards: `typeof`, `instanceof`, custom type guards
- Discriminated Unions

### ✅ Modules
- ES Modules and TypeScript modules
- Export/import syntax
- Namespaces (legacy, rarely used now)

---

## 🟡 Intermediate TypeScript Topics

### ✅ Classes
- Public, Private, Protected, Readonly
- Getters and Setters
- Implements (interfaces with classes)
- Abstract Classes

### ✅ Generics
- Generic Functions
- Generic Interfaces & Classes
- Constraints: `T extends U`
- Default Generic Types

### ✅ Type Utilities
- Built-in Utility Types:
  - `Partial`, `Required`, `Pick`, `Omit`
  - `Record`, `Exclude`, `Extract`, `NonNullable`
  - `ReturnType`, `InstanceType`, `Awaited`, `Parameters`
- Custom Utility Types

### ✅ Type Declarations
- Declaration Merging
- Declaration Files (`.d.ts`)
- Working with third-party libraries (`@types/`)

### ✅ Configuration & Compilation
- `tsconfig.json` deep dive
- Strict Mode (`strictNullChecks`, `noImplicitAny`, etc.)
- Module resolution
- Source maps and debugging

---

## 🔴 Advanced TypeScript Topics

### ✅ Advanced Types
- Mapped Types:
  ```ts
  type Readonly<T> = { readonly [K in keyof T]: T[K] }
  ```
- Conditional Types:
  ```ts
  type IsString<T> = T extends string ? true : false;
  ```
- Template Literal Types:
  ```ts
  type EventName = `on${Capitalize<string>}`
  ```
- Key Remapping:
  ```ts
  type Rename<T> = {
    [K in keyof T as `new_${string & K}`]: T[K]
  }
  ```
- Infer keyword:
  ```ts
  type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;
  ```
- Recursive Types
- Branded Types (for nominal typing)
- Distributive Conditional Types

### ✅ Working with Complex Structures
- Deep readonly / deep partial types
- Modeling JSON / dynamic data types
- Currying and variadic tuple types

### ✅ JSX & React with TypeScript
- Typing props and state
- Using `React.FC`, `PropsWithChildren`
- Higher-order components
- Generic React components
- Custom hooks with generics

### ✅ TypeScript + Tools
- TypeScript with ESLint and Prettier
- Babel + TypeScript
- Type checking with CI/CD

### ✅ Libraries & Framework Integration
- TypeScript with:
  - React, Vue, Svelte, Angular
  - Node.js (Express, Fastify)
  - GraphQL
  - Vite, Webpack

---

## 🔵 Expert-Level Topics

### ✅ Type-Level Programming
- Working only at the type level (no runtime code)
- Type manipulation pipelines
- Type-safe builders (fluent APIs)
- Build-time validation using types

### ✅ Plugin and Library Authoring
- Creating `*.d.ts` files for your libraries
- Publishing TypeScript libraries
- Mono-repos and TypeScript project references

---

## 🧠 Bonus: Learning Resources
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- Advanced TS courses (e.g. Total TypeScript)
- Type challenges: https://github.com/type-challenges/type-challenges
