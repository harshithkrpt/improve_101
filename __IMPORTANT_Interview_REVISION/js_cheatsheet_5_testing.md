
# Unit Testing in JavaScript  
### Jest, Mocha, Chai — Complete Interview + Coding Prep Guide

---

## 🧪 Topic: Testing & Tooling  
## 🧪 Subtopic: Unit Testing – Jest, Mocha, Chai Basics (JavaScript)

---

## 1. Detailed Explanation (Theory + Web‑verified Overview)

Unit testing in JavaScript revolves around validating small, isolated pieces of code (functions, classes, modules). The JavaScript ecosystem provides mature testing frameworks, the three most popular being **Jest**, **Mocha**, and **Chai**.

### What Jest Is  
Jest is a full‑featured testing framework built by Meta. It includes a test runner, assertion library, mocking system, and snapshot testing. It works out of the box with zero configuration for most JS or React apps.

Key points:
- Batteries-included: No need for external assertion or mocking libraries.
- Excellent for React apps using the React Testing Library.
- Supports snapshots for verifying UI component rendering.
- Fast test running with parallelization and intelligent test selection.

---

### What Mocha Is  
Mocha is a minimal, flexible testing framework that only provides the test runner. It does *not* include assertions or mocks; developers pair it with **Chai** (assertions) and **Sinon** (mocks/spies).

Key points:
- More customizable than Jest.
- Excellent for backend Node.js testing.
- Works well with Chai, Sinon, Supertest.

---

### What Chai Is  
Chai is an assertion library often used with Mocha.  
It supports three styles:  
- `assert`  
- `expect`  
- `should`

Chai makes tests expressive and readable.

Example:
```js
expect(sum(2, 3)).to.equal(5);
```

---

### Jest vs Mocha+Chai

| Feature | Jest | Mocha + Chai |
|--------|------|---------------|
| Test Runner | ✔️ built‑in | ✔️ Mocha |
| Assertions | ✔️ built‑in | ❌ (use Chai) |
| Mocks / Spies | ✔️ built‑in | ❌ (use Sinon) |
| Snapshots | ✔️ | ❌ |
| Config | Minimal | Medium |
| Ideal For | React + JS projects | Node APIs, custom setups |

---

## 2. Important Interview Questions (With Concise Answers)

### 1. What is unit testing?
Testing individual functions or small modules in isolation to ensure correctness.

### 2. Difference between Jest and Mocha?
Jest is a complete test framework. Mocha needs Chai (assertions) and Sinon (mocks). Jest is easier to set up.

### 3. What is test mocking?
Creating fake implementations of functions/modules to isolate the behavior. Jest has built‑in mocks.

### 4. How do spies differ from mocks?
Spies record function calls. Mocks provide fake implementations. Sinon or Jest can do both.

### 5. What is snapshot testing?
A Jest feature that stores component output and compares future renders against it.

### 6. What is TDD?
Test-Driven Development — write tests first, implement later.

### 7. What is code coverage?
Metrics showing how much code is executed by tests.

### 8. What are hooks in Mocha?
Functions like `before()`, `after()`, `beforeEach()`, `afterEach()` that control lifecycle.

### 9. What is Jest's `describe` block?
A grouping structure for related test cases.

### 10. Why use Chai?
Readable assertions using expect/should/assert styles.

---

## 3. Coding-Based Examples

### Jest Example
```js
// sum.js
export const sum = (a, b) => a + b;

// sum.test.js
import { sum } from './sum';

test('adds numbers', () => {
  expect(sum(2, 3)).toBe(5);
});
```

Run:  
`npm test`

---

### Mocha + Chai Example
```js
// sum.js
const sum = (a, b) => a + b;
module.exports = sum;

// test/sum.test.js
const sum = require('../sum');
const { expect } = require('chai');

describe('sum()', () => {
  it('returns correct value', () => {
    expect(sum(2, 3)).to.equal(5);
  });
});
```

Run:  
`npx mocha`

---

### Mock Example (Jest)
```js
const fetchData = jest.fn(() => Promise.resolve('OK'));

test('mock function returns OK', async () => {
  const data = await fetchData();
  expect(data).toBe('OK');
});
```

---

## 4. Conclusion

This cheat sheet gives a complete technical + interview + coding prep for JavaScript unit testing. Testing foundations like these form the backbone of production-grade software and scale smoothly into CI/CD workflows.

---




# Integration Testing in JavaScript  
### Async Flows, DOM Testing — Complete Interview + Coding Prep Guide

---

## 🧪 Topic: Testing & Tooling  
## 🧪 Subtopic: Integration Testing – Async Flows, DOM Testing (JavaScript)

---

## 1. Detailed Explanation (Theory + Practical Overview)

Integration testing checks whether multiple parts of an application work together correctly.  
In JavaScript apps, this typically means verifying:

- async workflows (API calls, timers, promises)  
- DOM interactions (user events, state updates, UI changes)  
- component–service communication  
- browser + API logic together  

Integration tests sit between unit tests and end-to-end tests.  
They test real behavior without spinning up a full browser automation tool like Cypress.

### Common JS Integration Testing Tools  
- **Jest** — powerful async utilities & mocks.  
- **React Testing Library (RTL)** — DOM testing with user-event simulation.  
- **Testing-library for vanilla JS** — DOM APIs for non-React apps.  
- **Supertest** — integration testing for Node APIs.  

---

## Testing Asynchronous Flows

Async operations (Promises, callbacks, async/await, timers, network operations) often fail silently. Integration tests ensure these flows behave together.

Jest provides utilities like:

- `async/await`
- `done` callback (rarely used now)
- `jest.useFakeTimers()`
- `jest.mock()` for async dependencies

Example async flow:
- user clicks button  
- triggers fetch  
- DOM updates when data arrives  

Integration testing ensures this entire chain works.

---

## DOM Testing Principles

DOM testing focuses on the user experience:

- what the user sees  
- how UI updates  
- how events affect state  
- whether components integrate properly  

React Testing Library follows a philosophy:
“Test behavior, not implementation.”

Prefer querying by:
- text  
- role  
- label  
- placeholder  

Avoid:
- internal selectors  
- component internals  

---

## Jest + RTL Flow

General pattern:

1. Render UI  
2. Simulate user interaction  
3. Wait for async UI updates  
4. Assert visible output  

Example:
```js
const button = screen.getByRole('button', { name: /load data/i });
await userEvent.click(button);
const item = await screen.findByText('Loaded!');
expect(item).toBeInTheDocument();
```

`findBy*` waits for async DOM updates — ideal for integration tests.

---

## 2. Key Interview Questions (Concise Answers)

### 1. What is integration testing?
Testing how multiple components or modules work together in real execution conditions.

### 2. How is integration testing different from unit testing?
Unit tests check isolated pieces; integration tests verify they collaborate correctly.

### 3. How do you test async flows in Jest?
Use `async/await`, `findBy*` queries (RTL), or fake timers with `jest.useFakeTimers()`.

### 4. What is DOM testing?
Testing UI behavior through user-perceived changes, not implementation details.

### 5. Why prefer `findBy` over `getBy` for async?
`findBy` waits for DOM updates; `getBy` fails immediately.

### 6. What is the role of React Testing Library in integration testing?
It simulates real user interactions and checks UI behavior with accessible queries.

### 7. Should you mock APIs in integration tests?
Often yes, using tools like `msw` (Mock Service Worker) or Jest mocks.

### 8. What does “test implementation vs behavior” mean?
Do not assert DOM internals; assert visible behavior like a user would.

### 9. How to test a function that uses timers?
Use `jest.useFakeTimers()` and `jest.advanceTimersByTime()`.

### 10. How to test a Node API integration?
Use `supertest` to call real API routes without running the server.

---

## 3. Coding-Based Examples

### DOM Integration Test (React + Jest + RTL)

```jsx
// FetchComponent.jsx
export default function FetchComponent() {
  const [data, setData] = useState(null);

  async function loadData() {
    const res = await fetch('/api/message');
    const json = await res.json();
    setData(json.message);
  }

  return (
    <>
      <button onClick={loadData}>Load</button>
      {data && <p>{data}</p>}
    </>
  );
}
```

```js
// FetchComponent.test.js
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import FetchComponent from './FetchComponent';

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ message: 'Hello World' }),
  })
);

test('loads and displays data', async () => {
  render(<FetchComponent />);

  await userEvent.click(screen.getByRole('button', { name: /load/i }));

  expect(await screen.findByText('Hello World')).toBeInTheDocument();
});
```

---

### Async Flow Example (Pure JS)
```js
// asyncFlow.js
export const delayedMessage = () =>
  new Promise((resolve) => setTimeout(() => resolve('Done!'), 1000));

// asyncFlow.test.js
import { delayedMessage } from './asyncFlow';

jest.useFakeTimers();

test('resolves after timeout', async () => {
  const promise = delayedMessage();

  jest.advanceTimersByTime(1000);

  await expect(promise).resolves.toBe('Done!');
});
```

---

### API Integration Test (Node.js + Supertest)

```js
// app.js
const express = require('express');
const app = express();

app.get('/welcome', (req, res) => res.json({ msg: 'Welcome!' }));

module.exports = app;
```

```js
// app.test.js
const request = require('supertest');
const app = require('./app');

test('GET /welcome', async () => {
  const res = await request(app).get('/welcome');
  expect(res.status).toBe(200);
  expect(res.body.msg).toBe('Welcome!');
});
```

---

## 4. Conclusion  
Integration testing gives confidence that real user flows work properly — from API calls to DOM updates. These tests form the backbone of robust front‑end and Node.js applications, especially where async behavior and UI interaction matter.

---


# Mocking & Spying in JavaScript  
### Jest Manual Mocks, jest.fn(), Sinon Spies — Complete Interview + Coding Prep Guide

---

## 🎯 Topic: Testing & Tooling  
## 🎯 Subtopic: Mocking & Spying — manual mocks, jest.fn(), sinon spies (JavaScript)

---

## 1. Deep-Dive Explanation (Practical + Conceptual)

Mocking and spying are core testing tools that help isolate code, observe behavior, and ensure integrations behave as expected.

Mocking replaces real implementations with fake versions.  
Spying observes calls made to a function, without necessarily replacing it.

In JavaScript, the two leading ecosystems for these operations are **Jest** and **Sinon**.

---

## Mocking in Jest

Jest includes a powerful built‑in mocking system.

### jest.fn()
Creates a mock function that records:
- how many times it was called  
- with what arguments  
- return values  
- and provided mock implementations

Example:
```js
const mockFn = jest.fn();
mockFn(3, 4);
expect(mockFn).toHaveBeenCalledWith(3, 4);
```

### jest.mock()
Mocks entire modules automatically.

```js
jest.mock('./api', () => ({
  fetchUser: jest.fn(() => Promise.resolve({ name: 'John' }))
}));
```

### Manual mocks (folder `__mocks__`)
Jest will automatically use files from `__mocks__` when a module is mocked with jest.mock().

Project structure:
```
src/
  api.js
  __mocks__/
    api.js
```

Mock file:
```js
module.exports = {
  fetchUser: jest.fn(() => Promise.resolve({ name: 'Mock User' }))
};
```

---

## Spying in Jest – jest.spyOn()

A spy wraps an existing function, recording calls without replacing by default.

Example:
```js
const obj = { greet: () => "Hello" };
const spy = jest.spyOn(obj, "greet");

obj.greet();
expect(spy).toHaveBeenCalled();
```

You can also override implementation:
```js
jest.spyOn(obj, "greet").mockReturnValue("Mocked!");
```

---

## Mocking & Spying in Sinon

Sinon is a standalone library specializing in mocks, stubs, and spies.  
Useful when using Mocha or other custom setups.

### sinon.spy()
Observes calls to a function.

```js
const spy = sinon.spy(obj, "greet");
obj.greet("hi");
sinon.assert.calledOnce(spy);
```

### sinon.stub()
Replaces a function.

```js
const stub = sinon.stub(api, "getUser").returns({ id: 1 });
```

### sinon.mock()
Creates expectations on methods.

```js
const mock = sinon.mock(api);
mock.expects("getUser").once().returns({ id: 1 });
mock.verify();
```

---

## Jest vs Sinon

| Feature | Jest | Sinon |
|--------|------|--------|
| Mock functions | ✔️ built‑in | ✔️ |
| Spies | ✔️ | ✔️ |
| Stubs | ✔️ via mockImplementation | ✔️ |
| Manual mocks | ✔️ (__mocks__) | ❌ |
| Assertions | ✔️ via Jest | ❌ (requires Chai) |
| Best for | Modern JS + React | Mocha + Node setups |

---

## 2. Key Interview Questions (Concise Answers)

### 1. What is mocking?
Replacing real functions/modules with fake implementations during testing.

### 2. What is a spy?
A wrapper that tracks calls to a function without fully replacing it.

### 3. Why mock instead of using real APIs?
To isolate logic, avoid network calls, and test deterministically.

### 4. Difference between jest.fn() and jest.spyOn()?
- jest.fn() creates a standalone mock function  
- jest.spyOn() wraps an existing function

### 5. What are manual mocks?
Mock files placed in `__mocks__` that Jest automatically uses when modules are mocked.

### 6. When use sinon.stub()?
When you want full control over a function’s behavior and return values.

### 7. What does calling mockRestore() do?
Restores original implementation wrapped by jest.spyOn().

### 8. How to mock an async function?
Use jest.fn():
```js
jest.fn(() => Promise.resolve(value))
```

### 9. What are mock implementations?
Custom return values or behaviors injected into mocks.

### 10. Should integration tests use mocks?
Only for network boundaries; avoid over‑mocking internal flows.

---

## 3. Coding Examples

### Jest Mock Function Example

```js
function greet(fn) {
  return fn("Hello");
}

test("calls callback with Hello", () => {
  const mockFn = jest.fn();
  greet(mockFn);
  expect(mockFn).toHaveBeenCalledWith("Hello");
});
```

---

### Jest Module Mock Example

```js
// api.js
export const getUser = () => fetch("/user").then(r => r.json());

// userService.js
import { getUser } from "./api";
export const loadUser = async () => (await getUser()).name;

// userService.test.js
jest.mock("./api", () => ({
  getUser: jest.fn(() => Promise.resolve({ name: "Mock User" }))
}));

test("loads user", async () => {
  const name = await loadUser();
  expect(name).toBe("Mock User");
});
```

---

### Sinon Spy Example

```js
const sinon = require("sinon");

const obj = {
  greet(name) { return `Hi ${name}`; }
};

const spy = sinon.spy(obj, "greet");
obj.greet("Alice");

sinon.assert.calledWith(spy, "Alice");
```

---

### Sinon Stub Example

```js
const sinon = require("sinon");
const api = { fetch: () => "real" };

const stub = sinon.stub(api, "fetch").returns("stubbed");

console.log(api.fetch()); // "stubbed"
stub.restore();
```

---

## 4. Conclusion

Mocking clears the noise, spying reveals the truth—together they make testing precise. They help slice through interconnected complexity and verify how pieces communicate, especially in async-heavy JavaScript systems.

---


# Code Coverage & Profiling in JavaScript  
### NYC (Istanbul), Coverage Tools, Chrome Profiler — Complete Interview + Coding Prep Guide

---

## 🎯 Topic: Testing & Tooling  
## 🎯 Subtopic: Code Coverage & Profiling — nyc, Istanbul, Chrome Profiler (JavaScript)

---

## 1. Detailed Explanation (Theory + Practical)

Code coverage and profiling help understand how thoroughly your code is tested and how efficiently it runs.

Coverage answers:  
“Which parts of my code are being tested?”

Profiling answers:  
“Where is my code spending time or memory?”

Both are essential for production-grade JavaScript and Node apps.

---

## Code Coverage

Coverage tools measure how much code executes during tests.

The leading JS ecosystem tool is **Istanbul**, with its CLI wrapper **nyc**.

### Istanbul  
Istanbul instruments JavaScript code and tracks coverage data.  
It measures:

- Statement coverage — executed statements  
- Branch coverage — if/else and logical branches  
- Function coverage — called vs uncalled  
- Line coverage — lines executed  

Example report:
```
Statements: 88%
Branches:   75%
Functions:  92%
Lines:      88%
```

### NYC (Istanbul’s CLI)

`nyc` is the command-line wrapper for Istanbul.

Installation:
```
npm install --save-dev nyc
```

Use with Jest, Mocha, Node scripts.

Example command:
```
nyc mocha
```

Or with npm scripts:
```json
"scripts": {
  "test": "nyc mocha"
}
```

NYC outputs:
- text-summary  
- lcov report  
- HTML report (open in browser)  

---

## Coverage with Jest

Jest has built-in Istanbul instrumentation.

Run:
```
jest --coverage
```

Config:
```json
"jest": {
  "collectCoverage": true,
  "coverageDirectory": "coverage"
}
```

---

## Why Coverage Matters

Coverage is a signal, not a goal.  
High coverage does *not* guarantee correctness.  
Missing coverage indicates untested logic.

Typical good baseline:
- 80–90% for statements/functions  
- 60–80% for branches  

---

## Profiling in JavaScript

Profiling helps identify bottlenecks in execution time or memory usage.

### Chrome DevTools Profiler

For browser apps:

- CPU profiler  
- Performance monitor  
- Memory snapshots  
- Allocation timeline  
- Flame charts  

Typical uses:
- Identify expensive re-renders  
- Analyze layout thrashing  
- Spot large memory leaks  
- Track long-running JS operations  

Steps:
1. Open DevTools  
2. Go to Performance tab  
3. Record  
4. Interact with the app  
5. Stop recording  
6. Read flamechart  

---

## Node.js Profiling

Node has built-in V8 profiling.

Run:
```
node --prof app.js
```

Generate readable output:
```
node --prof-process isolate-*.log
```

Or use Chrome DevTools with:
```
node --inspect
```

Inspect via chrome://inspect.

---

## 2. Key Interview Questions (Concise Answers)

### 1. What is code coverage?
A measure of how much of your code executes when running tests.

### 2. What does Istanbul do?
Instruments code and produces coverage reports.

### 3. What does NYC do?
CLI wrapper around Istanbul to generate test coverage.

### 4. What is branch coverage?
Percentage of if/else or logical branches tested.

### 5. Why isn’t 100% coverage always good?
Coverage says code ran, not that tests were meaningful.

### 6. How to generate coverage in Jest?
`jest --coverage` or `collectCoverage: true`.

### 7. What is lcov?
A common coverage output format readable by many CI tools.

### 8. What is profiling?
Measuring performance characteristics (CPU, memory, execution time).

### 9. How to profile a web app?
Use Chrome Performance tab and analyze flamecharts.

### 10. How to profile Node?
Use `--prof`, `--inspect`, or Chrome DevTools.

---

## 3. Coding-Based Examples

### Using NYC with Mocha

```json
{
  "scripts": {
    "test": "nyc mocha"
  }
}
```

Test run:
```
npm test
```

HTML report in:
```
coverage/index.html
```

---

### CPU Profiling Example (Node)

```bash
node --inspect server.js
```

Then open Chrome → chrome://inspect → Start profiling.

---

### Simple Performance Measurement in JS

```js
console.time("loop");
for (let i = 0; i < 1e6; i++) {}
console.timeEnd("loop");
```

---

## 4. Conclusion

Coverage shows how widely tests explore your code; profiling shows where your code slows down or hogs memory. Together they create a fuller picture of software quality and performance, essential for any modern JavaScript system.

---

# Testing & Tooling – Linting & Formatting (JavaScript)
## Topic: Testing & Tooling  
## Sub Topic: Linting & Formatting (ESLint, Prettier, Style Consistency)

---

## 1. Detailed Explanation

Linting and formatting are the quiet guardians of codebases. A linter inspects the structure and logic of your code, noticing things humans tend to overlook—unused variables, suspicious equality checks, odd spacing that might indicate bugs. A formatter cares about aesthetic harmony: consistent indentation, quotation style, semicolons, and line length. Together they keep codebases readable, predictable, and less error-prone.

### ESLint  
ESLint is a static analysis tool for JavaScript. It parses your code, walks the abstract syntax tree (AST), and checks it against rules you configure. These rules can warn or error out when your code drifts away from standards. ESLint is far more than whitespace nagging—it detects logical hazards like reassigning constants, unreachable code, and accidental use of `==` instead of `===`.

### Prettier  
Prettier purely formats code. It doesn’t judge your logic, it judges shape. It takes your messy source and prints it back in a consistent style. In contrast to ESLint’s precision, Prettier takes a maximalist opinionated approach—there are few configuration options on purpose so formatting becomes universal.

### ESLint + Prettier Together  
These tools complement each other, but they can conflict if ESLint tries to enforce formatting rules at the same time Prettier is allowed to reshape your code. The modern setup disables ESLint’s formatting rules and lets Prettier rule that domain. ESLint remains in charge of correctness and best practices.

---

## 2. Theory-Based Interview Questions & Answers

**Q1: What is the difference between a linter and a formatter?**  
A linter analyzes the structure and logic of code to catch errors or bad practices. A formatter rewrites code for consistent style without altering logic.

**Q2: Why do ESLint and Prettier conflict?**  
ESLint has rules about code style, while Prettier enforces its own style automatically. If both try to format code, they overwrite each other’s decisions.

**Q3: What is an AST in the context of ESLint?**  
An Abstract Syntax Tree is a structured representation of code. ESLint walks this tree to identify rule violations.

**Q4: Why is Prettier considered opinionated?**  
It intentionally restricts configuration to minimize style debates and create automatic, uniform formatting.

**Q5: Should formatting rules be handled by ESLint?**  
No. Best practice is to delegate formatting to Prettier and let ESLint focus on code quality and correctness.

---

## 3. Coding-Based Questions

### 3.1 Provide a basic `.eslintrc.js` for a React project:
```js
module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "plugin:prettier/recommended",
  ],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: "module",
  },
  rules: {
    "no-unused-vars": "warn",
    "react/prop-types": "off",
  },
};
```

### 3.2 How to configure Prettier for JS/React?
`.prettierrc`:
```json
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 80
}
```

### 3.3 Create a script to auto-lint and format code:
`package.json`:
```json
{
  "scripts": {
    "lint": "eslint .",
    "format": "prettier --write ."
  }
}
```

### 3.4 Example: ESLint catching logical issues:
```js
// ESLint will warn: no-unused-vars
function area(r) {
  const pi = 3.14; // unused
  return r * r * Math.PI;
}
```

### 3.5 Example: Prettier transforming the code:
Before:
```js
function greet(name){console.log("Hello "+name)}
```
After:
```js
function greet(name) {
  console.log("Hello " + name);
}
```

---

## 4. Downloadable Cheat-Sheet  
This file contains all details and examples, ready for study or sharing.

