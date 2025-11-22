# ReactJS – Basics  
## Sub Topic: JSX syntax, Virtual DOM, React.createElement, Components vs Elements  

### 1. Theory & Deep Dive  

#### 1.1 JSX syntax  
JSX is a syntax extension for JavaScript that looks like HTML/XML. It transpiles to `React.createElement` calls.

Example:
```jsx
const element = <div className="greeting">Hello, {name}</div>;
```

Equivalent to:
```js
const element = React.createElement(
  "div",
  { className: "greeting" },
  "Hello, ",
  name
);
```

JSX requires expressions in `{}` and enforces closing tags. Lowercase tags become DOM nodes; uppercase tags map to components.

---

#### 1.2 Virtual DOM  
The Virtual DOM (VDOM) is an in-memory representation of the UI. On updates:

1. React builds a new VDOM tree.
2. Diffs it with the previous VDOM.
3. Applies minimal updates to the real DOM.

This boosts performance and supports React’s declarative model.

---

#### 1.3 `React.createElement`  
Core API:  
`React.createElement(type, props, ...children)` returns a React element object:

```js
const element = React.createElement(
  'h1',
  { className: 'greeting' },
  'Hello, world!'
);
```

Elements are immutable objects with `{ type, props, key?, ref? }`.

---

#### 1.4 Components vs Elements  

| Concept    | Description                                                    |
|------------|----------------------------------------------------------------|
| **Element**     | JS object describing what to render (type, props, children) |
| **Component**   | Function/class that returns elements and may include logic |
| **Instance**    | Runtime object for class components (holds state, lifecycle) |

Example:
```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```

`<Greeting name="Harshith" />` produces an element of type `Greeting`.

---

### 2. Theory‑Based Interview Questions & Answers  

1. **What is JSX?**  
   JSX is HTML-like syntax inside JS, converted to `createElement` calls.

2. **How does Virtual DOM work?**  
   React builds a new VDOM on updates, diffs it, and patches real DOM efficiently.

3. **What does `React.createElement` do?**  
   Creates a React element object describing UI.

4. **React element vs component?**  
   Element = description; Component = function/class returning elements.

5. **Benefits of VDOM?**  
   Efficient updates, declarative UI. Drawbacks: diff overhead, large trees can slow down.

6. **What happens internally for `<div>Hello</div>`?**  
   Compiled to `React.createElement("div", null, "Hello")`.

7. **Why avoid JSX sometimes?**  
   Dynamic UI generation, environments without build steps.

8. **Are elements mutable?**  
   No — elements are immutable.

9. **What is reconciliation?**  
   React’s diffing & minimal DOM update process.

10. **Role of keys?**  
    Helps React match list items during diffing to avoid unnecessary re-renders.

---

### 3. Coding Practice

Example translation from JSX → `createElement`:

JSX:
```jsx
<div className="box"><p>Hi</p><p>{count}</p></div>
```

Without JSX:
```js
React.createElement(
  "div",
  { className: "box" },
  React.createElement("p", null, "Hi"),
  React.createElement("p", null, count)
);
```

Example component:
```jsx
function Hello({ name }) {
  return <h1>Hello, {name}</h1>;
}
```

Same without JSX:
```js
function Hello({ name }) {
  return React.createElement("h1", null, "Hello, ", name);
}
```

---

# ReactJS Component Types — Functional vs Class, PureComponent, memo()

## Functional Components
Functional components are plain JavaScript functions returning JSX. They rely on React Hooks for state and lifecycle.

### Key Traits
- Simpler, more concise.
- Hooks give access to state (useState), lifecycle (useEffect), refs (useRef), and context.
- Encouraged for almost all new React code.

### Example
```jsx
function Greeting({ name }) {
  return <h1>Hello {name}</h1>;
}
```

---

## Class Components
Class components extend `React.Component` and have access to lifecycle methods.

### Key Traits
- Older React pattern, still used in legacy codebases.
- Provides lifecycle methods like componentDidMount, shouldComponentUpdate, etc.
- Use `this.state` and `this.setState()`.

### Example
```jsx
class Greeting extends React.Component {
  render() {
    return <h1>Hello {this.props.name}</h1>;
  }
}
```

---

## PureComponent
`React.PureComponent` automatically implements a shallow prop and state comparison to prevent unnecessary renders.

### When useful
- For performance optimization.
- When state/props are immutable.
- Avoid if deep objects frequently change.

### Example
```jsx
class Counter extends React.PureComponent {
  render() {
    return <div>{this.props.value}</div>;
  }
}
```

---

## memo()
`React.memo()` is the functional-component equivalent of `PureComponent`.

### How it works
- Wraps a functional component.
- Prevents re-render unless props change (shallow compare).

### Example
```jsx
const Greeting = React.memo(function Greeting({ name }) {
  return <h1>Hello {name}</h1>;
});
```

---

# Interview Theory Questions & Answers

### What is the difference between functional and class components?
Functional components are simple functions using Hooks for state and lifecycle. Class components use ES6 classes, lifecycle methods, and `this.state`.

### Why did React move toward functional components?
They produce cleaner code, avoid `this` confusion, and Hooks provide powerful lifecycle/state features.

### What does PureComponent do?
It performs a shallow comparison of props/state to skip unnecessary renders.

### When should React.memo() be used?
When the component is pure and performance is an issue; good when props are stable primitives or memoized objects.

### memo() vs PureComponent?
Functional vs class versions of the same optimization technique: shallow comparison of props.

### Can PureComponent or memo() cause bugs?
Yes, if state/props use mutated objects—shallow comparison won’t detect deep changes.

---

# Coding Questions

### Example: Convert class component to a functional equivalent with hooks
```jsx
// Class component
class Timer extends React.Component {
  state = { count: 0 };
  componentDidMount() {
    this.interval = setInterval(() => {
      this.setState({ count: this.state.count + 1 });
    }, 1000);
  }
  componentWillUnmount() {
    clearInterval(this.interval);
  }
  render() {
    return <p>{this.state.count}</p>;
  }
}

// Functional equivalent
function Timer() {
  const [count, setCount] = React.useState(0);
  React.useEffect(() => {
    const id = setInterval(() => setCount(c => c + 1), 1000);
    return () => clearInterval(id);
  }, []);
  return <p>{count}</p>;
}
```

### Implement a memoized functional component manually
```jsx
function MyComponent({ value }) {
  console.log("Rendered");
  return <div>{value}</div>;
}

export default React.memo(MyComponent);
```

### Custom comparison function
```jsx
const Memoized = React.memo(
  MyComponent,
  (prev, next) => prev.value === next.value
);
```

---

# End

# ReactJS — State & Props  
One-way Data Flow, Prop Drilling, defaultProps, useState, Immutability

---

## State & Props Basics

### Props  
Props are inputs passed **from parent to child**. They are read-only values, forming the basis of React’s one‑way data flow.

```jsx
function Welcome({ name }) {
  return <h1>Hello {name}</h1>;
}
```

Props flow downward, never upward—this is React’s directional sanity‑preserver.

---

### State  
State is **internal data** managed inside a component. Updating state triggers a re-render.

Functional components use `useState`.

```jsx
const [count, setCount] = useState(0);
```

State should always be treated as **immutable**—React decides when and how to update the UI based on references, not mutation.

---

## One-Way Data Flow  
React pushes data **top → down** through props.  
Changes happen in the parent, and children receive updated data.

This makes UI predictable, debuggable, and easier to optimize.

---

## Prop Drilling  
Prop drilling happens when props are passed down multiple nested layers just so a distant child can finally use them.

```jsx
<Grandparent>
  <Parent>
    <Child />
  </Parent>
</Grandparent>
```

If Child needs data from Grandparent, props get relayed through Parent needlessly.

Common fixes:  
- Context API  
- Redux / Zustand / Jotai  
- useReducer + context combo  
- Custom hooks

---

## defaultProps  
For class components or older React patterns, you can define default prop values.

```jsx
MyComponent.defaultProps = {
  title: "Default Title",
};
```

In functional components with ES6, you typically use default parameters:

```jsx
function Button({ label = "Click" }) {
  return <button>{label}</button>;
}
```

---

## useState In Detail  
`useState` returns a state variable + updater function.

```jsx
const [value, setValue] = useState(initialValue);
```

Updates are asynchronous and batched.

Functional updates avoid stale values:

```jsx
setValue(prev => prev + 1);
```

---

## Immutability  
React state should never be mutated directly.

❌ `state.count++`  
✔️ `setState({ count: state.count + 1 })`

Immutability ensures React correctly detects changes and rerenders.

---

# Interview Theory Questions & Answers

### What is the difference between state and props?  
Props are external and read-only; state is internal and mutable (through setState/useState).

### Why does React enforce one-way data flow?  
It avoids ambiguous UI states and makes updates predictable.

### What is prop drilling?  
Passing props through intermediate components unnecessarily to reach a deeply nested component.

### How to avoid prop drilling?  
React Context, Redux, Zustand, or custom hooks.

### What is immutability and why is it important?  
State must not be mutated directly; immutability allows efficient rendering and clean change detection.

### Why shouldn't we mutate useState values directly?  
React won’t see the change, so the UI may not update.

---

# Coding Interview Questions

### Implement a counter using useState
```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      {count}
    </button>
  );
}
```

### Show how to avoid prop drilling using context
```jsx
const UserContext = React.createContext();

function App() {
  return (
    <UserContext.Provider value="Harshith">
      <Parent />
    </UserContext.Provider>
  );
}

function Child() {
  const user = React.useContext(UserContext);
  return <p>{user}</p>;
}
```

### Immutable state update example
```jsx
const [todos, setTodos] = useState([]);

setTodos(prev => [...prev, { id: Date.now(), text: "Learn React" }]);
```

### Class component with defaultProps
```jsx
class Hello extends React.Component {
  render() {
    return <p>Hello {this.props.name}</p>;
  }
}
Hello.defaultProps = {
  name: "Guest"
};
```

---

# End

# ReactJS Lifecycle Methods – componentDidMount, useEffect Equivalent, Cleanup

## Topic: ReactJS  
## Sub Topic: Lifecycle Methods – componentDidMount, useEffect Equivalent, Cleanup Functions

---

## 1. Understanding Lifecycle in React

React components behave like tiny creatures with a life-cycle rhythm — birth, updates, and final farewell.  
Class components define lifecycle stages using dedicated methods.  
Functional components reach the same milestones using hooks like `useEffect`.

---

## 2. componentDidMount (Class Component)

`componentDidMount()` fires once after the component appears in the DOM.

**Uses:**
- Fetching data  
- Subscribing to events  
- Starting timers  
- Integrating third-party libraries

### Example
```jsx
class Demo extends React.Component {
  componentDidMount() {
    console.log("Mounted!");
  }

  render() {
    return <h1>Hello</h1>;
  }
}
```

---

## 3. Functional Component Equivalent: useEffect(() => {}, [])

A functional component calls `useEffect` after the first render when the dependency array is empty.

### Example
```jsx
import { useEffect } from "react";

function Demo() {
  useEffect(() => {
    console.log("Mounted!");
  }, []);

  return <h1>Hello</h1>;
}
```

The dependency array `[]` creates mount-only behavior.

---

## 4. Cleanup Functions (componentWillUnmount Equivalent)

Anything that opens must close. Cleanup functions prevent memory leaks.

### Class Component
```jsx
class Timer extends React.Component {
  componentDidMount() {
    this.interval = setInterval(() => console.log("tick"), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  render() {
    return <div>Timer</div>;
  }
}
```

### Functional Component
Using `return` inside `useEffect`:

```jsx
function Timer() {
  useEffect(() => {
    const interval = setInterval(() => console.log("tick"), 1000);

    return () => {
      clearInterval(interval);
    };
  }, []);

  return <div>Timer</div>;
}
```

---

## 5. How React Executes useEffect

React’s rhythm looks like this:

Render → Paint → Run `useEffect` → Wait for changes → Run cleanup (if any) → Run next effect.

This gives React space to avoid blocking the UI.

---

## 6. Interview Theory Questions with Answers

**Q1: What is `componentDidMount` used for?**  
A: It runs after the component mounts. Used for API requests, subscriptions, DOM manipulation.

**Q2: What is the functional equivalent of `componentDidMount`?**  
A: `useEffect(() => {}, [])`.

**Q3: Why do we use a cleanup function in `useEffect`?**  
A: To avoid memory leaks by cleaning event listeners, timers, subscriptions.

**Q4: When does a cleanup function run?**  
A: Before the next effect call and when the component unmounts.

**Q5: What happens if you omit the dependency array in `useEffect`?**  
A: The effect runs after every render.

**Q6: How do you simulate `componentDidUpdate` in functional components?**  
A: `useEffect(() => { ... }, [dependencies])`.

---

## 7. Coding-Based Interview Questions

### Question 1: Implement a custom hook that mimics componentDidMount.
```jsx
import { useEffect } from "react";

function useDidMount(callback) {
  useEffect(() => {
    callback();
  }, []);
}

export default useDidMount;
```

### Question 2: Create a component that logs window resize events with cleanup.
```jsx
function ResizeLogger() {
  useEffect(() => {
    const handler = () => console.log(window.innerWidth);
    window.addEventListener("resize", handler);

    return () => window.removeEventListener("resize", handler);
  }, []);

  return <div>Resize Logger</div>;
}
```

### Question 3: Timer component using cleanup.
```jsx
function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(c => c + 1);
    }, 1000);

    return () => clearInterval(id);
  }, []);

  return <h1>{count}</h1>;
}
```

---

## 8. Summary

- `componentDidMount` → `useEffect(() => {}, [])`  
- `componentWillUnmount` → cleanup return in `useEffect`  
- Cleanup functions prevent memory leaks and keep apps stable  
- Hooks provide flexible and clear lifecycle control  

React’s lifecycle is a choreography of renders, effects, and cleanups — simple once you map the beats.

# Topic: ReactJS
## Sub Topic: Hooks — Top 15 (useState, useEffect, useMemo, useCallback, useRef, custom hooks, and more)

---

## Overview & Sources
This cheat-sheet covers 15 important React hooks (built‑in and common advanced hooks), short explanations, minimal examples, interview-style theory Qs with concise answers, and coding questions you can use for practice.

Sources: React official hooks reference and docs. citeturn0search0turn0search9turn0search1turn0search18

---

## Top 15 Hooks (explanation + example)

### 1) `useState`
Local state in function components.
```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

### 2) `useEffect`
Side effects and lifecycle synchronization (mount/update/unmount).  
See React docs for details. citeturn0search9
```jsx
import { useEffect } from "react";

function DataFetcher({ url }) {
  useEffect(() => {
    let cancelled = false;
    fetch(url).then(r => r.json()).then(data => {
      if (!cancelled) console.log(data);
    });
    return () => { cancelled = true; };
  }, [url]);
  return null;
}
```

### 3) `useContext`
Consume React context without `<Context.Consumer>`.
```jsx
import { useContext } from "react";
import { ThemeContext } from "./theme";

function Themed() {
  const theme = useContext(ThemeContext);
  return <div style={{ color: theme.foreground }}>Hi</div>;
}
```

### 4) `useReducer`
Alternative to useState for complex state logic.
```jsx
import { useReducer } from "react";

function reducer(state, action) {
  switch (action.type) {
    case "inc": return { count: state.count + 1 };
    default: return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return <button onClick={() => dispatch({ type: "inc" })}>{state.count}</button>;
}
```

### 5) `useRef`
Mutable container for DOM refs or storing mutable values across renders.
```jsx
import { useRef, useEffect } from "react";

function FocusInput() {
  const ref = useRef();
  useEffect(() => { ref.current?.focus(); }, []);
  return <input ref={ref} />;
}
```

### 6) `useMemo`
Memoize expensive calculations.
```jsx
import { useMemo } from "react";

function Fib({ n }) {
  const val = useMemo(() => heavyFib(n), [n]);
  return <div>{val}</div>;
}
```

### 7) `useCallback`
Memoize function references to avoid unnecessary re-renders.
```jsx
import { useCallback } from "react";

function Parent() {
  const handle = useCallback((x) => console.log(x), []);
  return <Child onClick={handle} />;
}
```

### 8) `useLayoutEffect`
Like `useEffect` but runs synchronously after DOM mutations (use for measurements).
```jsx
import { useLayoutEffect, useRef } from "react";

function Measure() {
  const ref = useRef();
  useLayoutEffect(() => {
    const rect = ref.current.getBoundingClientRect();
    console.log(rect.width);
  }, []);
  return <div ref={ref}>box</div>;
}
```

### 9) `useImperativeHandle`
Customize instance value exposed by `forwardRef`.
```jsx
import { forwardRef, useImperativeHandle, useRef } from "react";

const FancyInput = forwardRef((props, ref) => {
  const localRef = useRef();
  useImperativeHandle(ref, () => ({
    focus: () => localRef.current.focus()
  }));
  return <input ref={localRef} />;
});
```

### 10) `useDebugValue`
Show labels in React DevTools for custom hooks.
```jsx
import { useDebugValue } from "react";

function useAuth(user) {
  useDebugValue(user ? "logged-in" : "guest");
  // ...
}
```

### 11) `useId`
Generate unique IDs (useful for accessibility). citeturn0search1
```jsx
import { useId } from "react";

function TextField() {
  const id = useId();
  return (
    <>
      <label htmlFor={id}>Name</label>
      <input id={id} />
    </>
  );
}
```

### 12) `useTransition`
Mark state updates as non-urgent to keep UI responsive.
```jsx
import { useTransition } from "react";

function Search() {
  const [isPending, startTransition] = useTransition();
  const [query, setQuery] = useState("");
  function onChange(e) {
    const v = e.target.value;
    setQuery(v); // immediate
    startTransition(() => {
      // expensive update, e.g., filtering a large list
      setFiltered(filterBy(v));
    });
  }
  return <input onChange={onChange} />;
}
```

### 13) `useDeferredValue`
Defer a value to reduce urgent re-renders.
```jsx
import { useDeferredValue } from "react";

function BigList({ query }) {
  const deferredQuery = useDeferredValue(query);
  // render list filtered by deferredQuery
}
```

### 14) `useSyncExternalStore`
Safe subscription to external stores (for concurrent rendering).
```jsx
import { useSyncExternalStore } from "react";

function useMyStore(subscribe, getSnapshot) {
  return useSyncExternalStore(subscribe, getSnapshot);
}
```

### 15) `useInsertionEffect`
Run CSS-insertion side-effects before layout and paint (advanced).
```jsx
import { useInsertionEffect } from "react";

function useStyleSheet(css) {
  useInsertionEffect(() => {
    const style = document.createElement("style");
    style.textContent = css;
    document.head.appendChild(style);
    return () => style.remove();
  }, [css]);
}
```

---

## Custom Hooks (pattern)
Custom hooks are just functions that use hooks and start with `use`.
```jsx
import { useState, useEffect } from "react";

function useWindowWidth() {
  const [w, setW] = useState(window.innerWidth);
  useEffect(() => {
    const h = () => setW(window.innerWidth);
    window.addEventListener("resize", h);
    return () => window.removeEventListener("resize", h);
  }, []);
  return w;
}
```

---

## Interview Theory Questions (concise answers)

1. **Why must hooks be called at the top level?**  
   Hooks rely on call-order to map state to components. Calling inside conditionals breaks that order.

2. **When to use `useMemo` vs `useCallback`?**  
   `useMemo` memoizes values; `useCallback` memoizes function references. Use to avoid expensive re-calculation or unnecessary child re-renders.

3. **How does `useRef` differ from `useState`?**  
   `useRef` provides a mutable container that doesn't trigger re-renders when changed; `useState` triggers re-renders.

4. **When useLayoutEffect over useEffect?**  
   Use `useLayoutEffect` when you need to measure or synchronously mutate the DOM before paint.

5. **What problem does `useSyncExternalStore` solve?**  
   It provides a concurrency-safe way to subscribe to external stores for concurrent rendering.

---

## Coding Interview Questions (practice)

1. Write a `useLocalStorage(key, initial)` hook that syncs state with `localStorage`.  
2. Implement `usePrevious(value)` that returns the previous value across renders.  
3. Build a `useDebouncedValue(value, ms)` hook for debouncing user input.  
4. Create a `useEventListener(target, event, handler)` hook that cleans up properly.  
5. Given a large list, use `useTransition` to implement a responsive search UI.

---

## Quick Best Practices
- Keep hooks simple and focused. Extract logic into custom hooks when needed.  
- Avoid overusing `useMemo` / `useCallback` without measuring — they have an overhead.  
- Always clean up subscriptions in `useEffect` return.  
- Name custom hooks starting with `use` to follow conventions and enable lint rules.

---

## Download
This file was generated using official React docs and reputable tutorials. Primary references: React docs (hooks), useEffect, useId, freeCodeCamp. citeturn0search0turn0search9turn0search1turn0search18

# ReactJS — Context API
## Topic: ReactJS
## Sub Topic: Context API — createContext, useContext, Provider pattern, avoiding prop drilling

---

## Quick summary
React's Context API provides a way to pass data through the component tree without having to pass props manually at every level. It's ideal for global-ish data such as theme, locale, authenticated user, or feature flags. Use it to avoid "prop drilling" — the practice of passing props through components that don't need them. citeturn0search3turn0search8

---

## Key primitives

### `createContext(defaultValue)`
Creates a Context object. Call it outside components so the same context instance is shared across renders.
```js
import { createContext } from 'react';
const ThemeContext = createContext('light'); // 'light' is the default/fallback value
```
When no Provider is present above a consumer, the defaultValue is used. citeturn0search3

### `Provider`
Every Context object comes with a Provider component: `<MyContext.Provider value={...}>`. The `value` prop is what consumers read.
```jsx
<ThemeContext.Provider value={theme}>
  <App />
</ThemeContext.Provider>
```
Only components inside the Provider subtree see the provided value. Updating `value` causes consumers to re-render. citeturn0search8

### `useContext(Context)`
Hook that lets function components read context value and subscribe to updates:
```jsx
import { useContext } from 'react';
const theme = useContext(ThemeContext);
```
Call `useContext` at top-level of your component. It reads the *current* value from the nearest matching Provider above in the tree. citeturn0search1

---

## Minimal example: Theme provider and consumer

```jsx
// theme-context.js
import { createContext, useState } from 'react';
export const ThemeContext = createContext('light');

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  const toggle = () => setTheme(t => (t === 'light' ? 'dark' : 'light'));

  return (
    <ThemeContext.Provider value={{ theme, toggle }}>
      {children}
    </ThemeContext.Provider>
  );
}
```

```jsx
// App.jsx
import { ThemeProvider } from './theme-context';
import Toolbar from './Toolbar';

function App() {
  return (
    <ThemeProvider>
      <Toolbar />
    </ThemeProvider>
  );
}
```

```jsx
// Toolbar.jsx
import { useContext } from 'react';
import { ThemeContext } from './theme-context';

function Toolbar() {
  const { theme, toggle } = useContext(ThemeContext);
  return (
    <div style={{ background: theme === 'dark' ? '#222' : '#fff' }}>
      <button onClick={toggle}>Toggle theme</button>
    </div>
  );
}
```

---

## Patterns & best practices

### 1) Keep contexts small and focused
Create multiple contexts for unrelated data (theme vs auth vs UI state) to minimize unnecessary re-renders. citeturn0search4turn0search18

### 2) Use `useMemo` / stable value objects for Provider `value`
If you pass an object inline to `value`, it will be a new reference each render and cause consumers to re-render. Memoize it:
```jsx
const value = useMemo(() => ({ user, login, logout }), [user]);
<Context.Provider value={value}>...</Context.Provider>
```

### 3) Avoid overusing Context for everything
Context is not a replacement for local state. For isolated component state, prefer `useState`. Context is for data shared across many components. citeturn0search2

### 4) Expose convenience custom hooks
Wrap `useContext` in a small hook to centralize logic and throw helpful errors when used outside a Provider:
```jsx
function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
}
```
This pattern improves developer ergonomics and makes the API clearer.

### 5) Consider derived selectors or splitting contexts to minimize renders
If only part of context changes (e.g., `user.name` vs `user.settings`) split into multiple contexts or use selector patterns to avoid re-rendering everything on small updates. Articles recommend careful scoping to avoid performance pitfalls. citeturn0search9turn0search18

---

## Avoiding prop drilling — alternatives & when to prefer each
- Prop drilling (pass props explicitly) — simplest and most explicit; prefer when only one or two intermediate layers exist.  
- Context API — use when many components across the tree need the same data. citeturn0search8  
- Component composition (render props / children-as-function) — useful when you want to keep components decoupled.  
- Lightweight global stores (Zustand, Jotai) — when you need more scalable state management and selective subscriptions. citeturn0search18

---

## Interview-style theory questions (concise answers)

**Q1 — When should you use Context instead of props?**  
A: When multiple deeply nested components need access to the same data and passing props becomes verbose or brittle. Keep context for global-ish concerns (theme, locale, auth).

**Q2 — What causes unnecessary re-renders with Context?**  
A: Passing non-memoized objects/functions as `value` (new reference each render) or placing high-frequency-changing state in a broad context. Use `useMemo`, split contexts, or selectors.

**Q3 — How does a Provider update affect consumers?**  
A: When Provider's `value` changes (by identity equality), React will re-render all consuming components that read that context. Use stable references to avoid noise. citeturn0search8

**Q4 — Can you use multiple Providers?**  
A: Yes — you can nest Providers for different contexts without conflict:
```jsx
<AuthProvider>
  <ThemeProvider>
    <App />
  </ThemeProvider>
</AuthProvider>
```

**Q5 — Is Context API suitable for large-scale state management?**  
A: Context works fine for many use-cases, but for complex apps with advanced selector needs or async logic, consider a dedicated state library (Redux, Zustand) or use context plus local stores. citeturn0search9turn0search18

---

## Coding exercises (practice)

1. Implement an `AuthProvider` exposing `{ user, login, logout }` using `createContext` and a `useAuth()` hook.  
2. Build a `LanguageProvider` with `useId`-friendly labels and a `useLocale()` hook to read/format messages.  
3. Given a deeply nested tree, refactor prop drilling into a context-based solution and measure render counts before/after.  
4. Create a `useTheme` hook that keeps the theme in Context but stores preference in `localStorage`. (Hint: initialize from `localStorage` and save on changes.)  
5. Optimize a provider that exposes `{user, notifications, settings}` so that updating `notifications` doesn't re-render components that only read `settings`.

---

## Short pitfalls checklist
- Don't pass changing inline objects as `value`.  
- Don't misuse Context for per-component state.  
- Don't rely on Context for waterfall async state updates — keep complex logic in reducers or stores.  
- Always handle the "no provider" fallback in custom hooks for a better DX.

---

## References
React docs: createContext, useContext, Passing Data Deeply with Context. citeturn0search3turn0search1turn0search8  
FreeCodeCamp guide on Context & examples. citeturn0search9

---

## Download
This document saved as `react_context_api.md`.

# ReactJS – Conditional Rendering  
### Topic: ReactJS  
### Sub Topic: Conditional Rendering (ternaries, short‑circuit, render functions, null returns)  

## Theory / Explanation  
Conditional rendering in React means that your UI (JSX) changes depending on state, props, or other conditions. Because components are functions (or classes) returning JSX, you can use normal JavaScript logic to decide what to render.

### Patterns  
1. **Ternary operator (`condition ? A : B`)**  
   ```jsx
   return (
     <div>
       { isLoggedIn ? <LogoutButton /> : <LoginButton /> }
     </div>
   );
   ```

2. **Short‑circuit (`condition && A`)**  
   ```jsx
   return (
     <div>
       { hasError && <ErrorMessage /> }
     </div>
   );
   ```
   Pitfall: if `condition` can be `0`, `""`, `NaN`, you may inadvertently render that value instead of nothing.

3. **Render functions / variables before return**  
   ```jsx
   let content;
   if (loading) {
     content = <Loading />;
   } else if (error) {
     content = <Error message={error} />;
   } else {
     content = <DataView data={data} />;
   }
   return <div>{content}</div>;
   ```

4. **Returning `null` (or nothing)**  
   ```jsx
   function WarningBanner({ warn }) {
     if (!warn) {
       return null;
     }
     return <div className="warning">Warning!</div>;
   }
   ```

### When to use which  
- Ternary → two explicit alternatives.  
- `&&` → render something only if condition true, otherwise nothing.  
- Render‑functions/variables → when logic is more complex.  
- `null` return → when component should render nothing.  

---

## Interview‑style Questions (Theory)  
| Question | Concise Answer |
|---|----------------|
| What is conditional rendering in React? | Rendering different JSX depending on state/props/conditions. |
| How do you implement conditional rendering using a ternary operator? | `{ condition ? <A /> : <B /> }` |
| When is it appropriate to use `&&`? | Render component only when condition is true. |
| Risk of using `&&`? | Falsy-but-renderable values like 0 may output accidentally. |
| How to render nothing? | Return `null`. |
| Does `null` skip lifecycle? | No. |
| When prefer render function? | Multiple branching or complex logic. |
| Best practice? | Avoid nested ternaries; extract logic. |

---

## Coding / Practical Questions  

### Q1. Simple ternary  
```jsx
function UserGreeting({ user }) {
  return (
    <div>
      { user ? <h1>Hello, {user.name}!</h1> : <h1>Please log in.</h1> }
    </div>
  );
}
```

### Q2. Using &&
```jsx
function Warning({ message }) {
  return (
    <div>
      { message && <div className="warning">{message}</div> }
    </div>
  );
}
```

### Q3. Returning null  
```jsx
function Modal({ isOpen, children }) {
  if (!isOpen) return null;
  return <div className="modal">{children}</div>;
}
```

### Q4. Multiple conditions  
```jsx
function DataFetcher({ loading, error, data }) {
  let content;
  if (loading) content = <p>Loading…</p>;
  else if (error) content = <p>Error: {error.message}</p>;
  else content = <p>Data: {JSON.stringify(data)}</p>;
  return <div>{content}</div>;
}
```

### Q5. Avoid rendering 0  
```jsx
function ItemList({ items }) {
  return (
    <div>
      { items.length > 0
        ? <ul>{ items.map((it, idx) => <li key={idx}>{it}</li>) }</ul>
        : <p>No items found.</p>
      }
    </div>
  );
}
```

# Topic : ReactJS

## Sub Topic : List Rendering (map keys, unique keys, fragment shorthand, list optimization)

---

### Overview

Rendering lists is one of the most common UI patterns in React. This guide covers how to turn arrays into JSX lists, why the `key` prop matters, how to use React Fragments (and when you must use the full `<Fragment>`), performance considerations, common bugs, interview-style theory questions with concise answers, and coding problems you can practice in interviews.

---

## 1) Core concepts

### Rendering arrays with `map()`

Use JavaScript array methods (usually `map`) to return JSX for each item.

```jsx
const todos = [{ id: 42, text: 'Buy milk' }, { id: 43, text: 'Write tests' }];

function TodoList() {
  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
}
```

### Why `key` exists

- Keys provide a stable identity for elements across renders so React’s reconciliation algorithm can match old and new children efficiently.
- Without good keys React may re-mount components incorrectly (lost input focus/state), or perform unnecessary DOM operations.

### Choosing keys

- Prefer stable unique IDs from your data (e.g., database IDs).
- **Avoid** using array indices as keys when the list can change order, have inserts, deletes, or is dynamic — because indices don’t represent stable identity and can cause UI/state bugs.
- Using index as key is acceptable for static lists that never reorder or mutate.

### Keys must be unique among siblings — not globally unique across the whole app.

---

## 2) React Fragments and keys

- Use `<>...</>` (shorthand) when you only need to group elements without adding DOM nodes.
- The shorthand fragment **cannot** accept `key`. If you need to set a `key` on a grouped element returned from `map()`, use the long form:

```jsx
import { Fragment } from 'react';

items.map(item => (
  <Fragment key={item.id}>
    <dt>{item.term}</dt>
    <dd>{item.definition}</dd>
  </Fragment>
))
```

This is necessary when each group of returned children needs its own key.

---

## 3) List optimization & reconciliation basics

- React compares children by key during reconciliation. When keys match, React tries to update existing DOM nodes rather than recreate them.
- Good keys reduce DOM churn and help maintain component state (e.g., controlled inputs inside lists keep their values).
- Avoid creating new object/array identities for keys (e.g., `key={Math.random()}`) — that defeats the purpose.

Performance tips:
- Use keys and avoid unnecessary re-renders by ensuring parent components don't re-create arrays or functions every render (memoize data or use `useMemo` when appropriate).
- Consider `React.memo` for expensive list item components.
- Virtualize extremely long lists (e.g., `react-window`, `react-virtualized`) to render only visible items.

---

## 4) Common mistakes & gotchas

- Using the array index as key in a list that can change leads to subtle bugs: input values move to different items, animation/order glitches, wrong state mapping.
- Assigning keys to a parent element when the children need keys (or forgetting to put `key` on the direct children returned from `map`).
- Using non-stable values (like `Date.now()` or `Math.random()`) as keys.
- Forgetting to add a `key` when returning adjacent elements grouped by a fragment — shorthand fragments don’t accept `key`.

---

## 5) Interview-style theory questions (concise answers)

1. **Q:** Why do we need keys in React lists?
   **A:** Keys let React identify items between renders so it can re-use and update nodes efficiently; they maintain identity to avoid remounting and losing component state.

2. **Q:** Is it OK to use array index as key? When?
   **A:** Only for static lists that never reorder, insert, or delete items. For dynamic lists use stable unique IDs.

3. **Q:** What happens if you use `Math.random()` for keys?
   **A:** Each render produces new keys, forcing React to unmount and remount every item each time — losing local state and hurting performance.

4. **Q:** Can fragments accept keys? How?
   **A:** The shorthand `<>...</>` cannot take keys. Use `<React.Fragment key={...}>...</React.Fragment>` or `import { Fragment }` and use `<Fragment key={...}>`.

5. **Q:** How do keys affect controlled inputs inside list items?
   **A:** With stable keys, React preserves the component instance and state (including input values) across reorders. With bad keys, inputs can swap values or lose cursor position.

6. **Q:** How does reconciliation use keys? (short)
   **A:** Reconciliation uses keys to match previous children to new children. If keys match, React updates; if not, it mounts/unmounts.

---

## 6) Practical coding questions (with short answers / hints)

1. **Problem:** Convert an array of user objects into a list of cards showing `name` and `email`. Each card must have a stable key.
   **Hint / sample:** `users.map(u => <UserCard key={u.id} user={u} />)`

2. **Problem:** You have an editable list of items with inputs; items can be reordered. How do you preserve input text when items move?
   **Answer:** Use stable `id` keys for list items; avoid index key. Store input value in component state or pull it up to parent keyed by `id`.

3. **Problem:** Render a table where each row renders two sibling columns (`<th>` and `<td>` returned together). Keys are required per row group. How do you return grouped elements without extra DOM nodes?
   **Answer:** Use `<Fragment key={row.id}>...</Fragment>` to group `<th>` and `<td>` without adding wrapper elements.

4. **Problem:** Optimize a long list of 10k items to avoid freezing the UI.
   **Answer:** Use list virtualization (`react-window`), windowing, or pagination. Also memoize item components and use stable keys.

---

## 7) Example: complete component with fragment keys

```jsx
import React, { Fragment } from 'react';

const glossary = [
  { id: 't1', term: 'Closure', definition: 'Function + lexical environment' },
  { id: 't2', term: 'Hoisting', definition: 'Declaration moves to top' },
];

function Glossary() {
  return (
    <dl>
      {glossary.map(item => (
        <Fragment key={item.id}>
          <dt>{item.term}</dt>
          <dd>{item.definition}</dd>
        </Fragment>
      ))}
    </dl>
  );
}
```

---

## 8) Quick checklist for interviews

- Always mention: \"use stable unique IDs for keys\".
- Explain why index-as-key is problematic for dynamic lists.
- Show a short code example using `map()` with `key={item.id}` and a fragment example with `key`.
- Mention virtualization for very long lists and `React.memo` for item components.

---

## 9) References

(Official docs & articles used when building this cheat-sheet)

- React docs: Rendering lists & Fragments
- Articles on keys and reconciliation


---

_End of cheat sheet_

# ReactJS — Event Handling

**Topic:** ReactJS

**Sub Topic:** Event Handling — synthetic events, event delegation, binding context

---

## Quick summary

This cheat sheet covers React's synthetic event system, how React performs event delegation, common patterns for binding handlers (class components and functional components), performance and best practices, TypeScript typings, and gotchas. Also includes concise interview-style theory questions with answers and coding problems with solutions.

---

## 1) Core concepts

### SyntheticEvent
- React wraps native browser events in a cross-browser wrapper called `SyntheticEvent`. It mirrors the standard DOM `Event` API (e.g., `preventDefault`, `stopPropagation`, familiar properties like `target`, `currentTarget`) so handlers behave consistently across browsers.

### Event delegation in React
- Instead of attaching a native listener to every DOM node, React generally delegates events: handlers are registered at the root of the React render tree and React dispatches them to your component when events bubble. This reduces native listeners and improves performance in large trees.

### Handler binding / `this` context
- **Class components:** methods used as event handlers do not autobind. Common patterns:
  - Bind in constructor: `this.handleClick = this.handleClick.bind(this)`
  - Use class fields with arrow functions: `handleClick = (e) => { ... }`
  - Inline arrow in JSX (works but re-creates function each render): `<button onClick={(e) => this.handleClick(e)} />`
- **Functional components:** use functions (or `useCallback` when necessary) and closures. `this` is not used.

### Event pooling / lifecycle
- Historically React pooled `SyntheticEvent` objects for performance; the event object was reused after the handler returns. If you needed the event asynchronously you had to call `event.persist()`. Modern React's documentation and implementations have changed over time; treat `SyntheticEvent` like a normal event but avoid accessing event properties in async callbacks unless you copy them or persist the event.

### Passing arguments
- Common pattern to pass extra args: `<button onClick={(e) => handleClick(e, id)}>`, or `onClick={handleClick.bind(null, id)}` (but bind creates new function).

---

## 2) Examples (concise)

### Functional component (recommended)
```jsx
import React from 'react';

function Item({ id, onDelete }) {
  function handleClick(e) {
    e.preventDefault();
    onDelete(id);
  }

  return <button onClick={handleClick}>Delete</button>;
}
```

### Class component
```jsx
class Item extends React.Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(e) {
    e.preventDefault();
    this.props.onDelete(this.props.id);
  }

  render() {
    return <button onClick={this.handleClick}>Delete</button>;
  }
}
```

### Using `useCallback` to avoid re-created handlers
```jsx
const Parent = ({ onDelete }) => {
  const handleDelete = useCallback((id) => {
    onDelete(id);
  }, [onDelete]);

  return <Item id={5} onDelete={handleDelete} />;
};
```

---

## 3) Performance & best practices
- Prefer functional components and hooks where possible.
- Avoid creating new inline functions in large lists on every render; use `useCallback` or move handler logic into child components.
- For many interactive elements (e.g., thousands of rows), rely on React's delegation — attaching many native listeners is unnecessary.
- Use event delegation intentionally in user-land only when you need specialized behavior across non-React-managed DOM.

---

## 4) TypeScript tips
```ts
function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
  console.log(e.target.value);
}

<input onChange={handleChange} />
```
- Use specific event types: `React.MouseEvent<HTMLButtonElement>`, `React.ChangeEvent<HTMLInputElement>`, or the generic `React.SyntheticEvent` when unsure.

---

## 5) Common gotchas
- Accessing `e.target` inside an async callback may fail if the event was pooled. Copy the value (`const val = e.target.value`) or call `e.persist()` (older guidance).
- `onClick` on custom components does not map to DOM elements automatically; you must forward the handler to an underlying DOM element or explicitly accept it as a prop.
- Differences in how React 17+ changed event delegation root (container vs document) — be careful when mixing raw `addEventListener` handlers and React-managed handlers.

---

## 6) Interview-style theory questions (concise answers)

**Q1: What is a SyntheticEvent in React?**
A: A cross-browser wrapper around native events that provides a consistent API (`preventDefault`, `stopPropagation`, properties like `target`) across browsers.

**Q2: How does event delegation work in React?**
A: React typically attaches a small set of native listeners at the root and dispatches events to components as events bubble up, avoiding many per-node native listeners.

**Q3: Why do you sometimes need to bind event handlers in class components?**
A: Class methods are not auto-bound to the class instance; binding ensures `this` inside the handler points to the component instance.

**Q4: How do you pass extra arguments to an event handler?**
A: Use an inline arrow: `onClick={(e) => handleClick(e, id)}`, or `onClick={handleClick.bind(null, id)}` but prefer the arrow for clarity.

**Q5: What is `event.persist()`?**
A: Historically used to remove React's pooling for a `SyntheticEvent` so its properties can be accessed asynchronously. Modern React usage often copies needed properties instead.

---

## 7) Coding interview questions (with hints)

**C1:** Implement a `List` component that renders 1000 items and handles clicks on each item without creating 1000 distinct handler functions on every render. *Hint:* use a single handler and data attributes or memoized callbacks.

**C2:** Write a `Form` component with controlled inputs that logs the final form values on submit. Ensure no stale closures when using hooks.

**C3:** Create a `Dropdown` component that closes when clicking outside the dropdown. Implement using React refs and a single document `click` listener added/removed in `useEffect`.

---

## 8) Solutions / patterns (brief)

**C1 (pattern):** Attach `onClick` to the container element and use `data-id` on each item; inside handler, use `e.target.closest('[data-id]')?.dataset.id` to find which item was clicked. This leverages event delegation inside React.

**C2 (pattern):** Use `useState` for inputs and submit handler that reads the current state.

**C3 (pattern):** `useEffect` to `addEventListener('click', handler)` on mount and cleanup on unmount; the handler checks `ref.current.contains(event.target)`.

---

## 9) Quick reference snippets

- Prevent default: `e.preventDefault()`
- Stop propagation: `e.stopPropagation()`
- Synthetic event typing (TS): `React.MouseEvent<HTMLButtonElement>`

---

## 10) Further reading
- React official docs: handling events and synthetic events (react.dev / reactjs.org)
- Guides on event delegation, performance, and useCallback patterns

---

*File generated: `ReactJS - Event Handling Cheat Sheet.md`*


# ReactJS — Forms
**Topic:** ReactJS  
**Sub Topic:** Forms — controlled vs uncontrolled components, Formik, react-hook-form

---

## 1. Overview: controlled vs uncontrolled components

**Controlled components**  
- React state (or props) is the single source of truth for form inputs. Every input's value is driven by component state and updated via `onChange`. This enables immediate validation, formatting, conditional logic, and easy integration with the rest of your app.  

**Uncontrolled components**  
- The DOM (native input) holds the value; React reads it via refs when needed (e.g., on submit). This is closer to plain HTML forms and can be simpler and more performant for large forms where you do not need to react to every keystroke.

### Quick rules / gotchas
- An input **cannot** be both controlled and uncontrolled at the same time — choose one and keep it consistent for that input's lifetime.  
- If you pass a `value` prop to an `<input>` it becomes controlled; use `defaultValue` / `defaultChecked` for uncontrolled inputs.

---

## 2. Code examples

### Controlled input (simple)
```jsx
import { useState } from "react";

function ControlledForm() {
  const [name, setName] = useState("");

  return (
    <form onSubmit={(e) => { e.preventDefault(); console.log(name); }}>
      <label>
        Name:
        <input value={name} onChange={e => setName(e.target.value)} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}
```

### Uncontrolled input (ref)
```jsx
import { useRef } from "react";

function UncontrolledForm() {
  const nameRef = useRef();

  return (
    <form onSubmit={(e) => {
      e.preventDefault();
      console.log(nameRef.current.value);
    }}>
      <label>
        Name:
        <input defaultValue="Harshith" ref={nameRef} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}
```

---

## 3. Libraries: Formik and React Hook Form (brief)

### Formik
- Formik uses React state to store form values and helpers (though it exposes hooks such as `useFormik`) and is designed around controlled inputs and explicit state updates. It integrates well with schema validators (e.g., Yup) and provides a structured API for complex forms.

### React Hook Form (RHF)
- React Hook Form is designed with performance in mind and prefers using uncontrolled inputs (refs) to avoid unnecessary re-renders. RHF offers a `Controller` component to integrate controlled UI libraries (like Material UI) when needed, and keeps bundle size small while providing flexible validation options.

---

## 4. Pros / Cons (summary)

**Controlled**
- Pros: Full control, instant validation, easy to orchestrate dependent fields.
- Cons: More re-renders, boilerplate for large forms.

**Uncontrolled**
- Pros: Simpler for basic forms, fewer re-renders, more native-like typing UX.
- Cons: Harder to implement live validation or to react to input changes.

**Formik**
- Pros: Familiar API, great validation schema support, good for complex forms.
- Cons: Can cause more re-renders; larger bundle than minimalist libs.

**React Hook Form**
- Pros: High performance, minimal re-renders, small bundle, works well with uncontrolled inputs.
- Cons: Different mental model (refs) might be unfamiliar; controlled integration needs `Controller`.

---

## 5. When to choose what
- Use **controlled** inputs when you need real-time validation, formatting, dependent updates (e.g., live previews), or tight integration with app state.
- Use **uncontrolled** inputs or **React Hook Form** when you have many fields and performance / typing smoothness matter, or when you mostly handle values at submit time.
- Use **Formik** when you want a predictable, schema-driven approach with built-in patterns and prefer its ergonomics.

---

## 6. Short interview-style theory questions (with concise answers)

1. **Q:** What is a controlled component in React?  
   **A:** An input whose value is controlled by React state; every change flows through `onChange` into state.

2. **Q:** What is an uncontrolled component?  
   **A:** An input that stores its own value in the DOM; accessed via refs when necessary.

3. **Q:** Can an input switch between controlled and uncontrolled?  
   **A:** No — switching leads to warnings and buggy behaviour; set either `value` (controlled) or `defaultValue` (uncontrolled) and stick with it.

4. **Q:** Why does React Hook Form perform better than Formik in large forms?  
   **A:** Because RHF leverages uncontrolled inputs and refs to avoid re-rendering the whole form on each keystroke; Formik stores form state in React which can cause more re-renders.

5. **Q:** When would you use Formik over RHF?  
   **A:** When you prefer a schema-based, opinionated API or when you value its form-building patterns and community integrations.

---

## 7. Coding interview prompts (practical)

1. **Implement** a login form with email and password using controlled components, add inline validation for email format and password length. (Expect `useState`, `onChange`, and simple regex or `HTML5` validation).

2. **Convert** a small uncontrolled form to use React Hook Form and demonstrate validating with a schema (Yup or custom), plus showing error messages.

3. **Build** a dynamic form where selecting an option shows a different sub-form; ensure values persist correctly across switches (test mount/unmount behaviour).

4. **Implement** a reusable `useFormField` hook that abstracts validation and change handling for controlled inputs.

---

## 8. Useful links & references
- React docs — Uncontrolled components guide and input reference.  
- React Hook Form — official docs, API and performance notes.  
- Formik — official docs, `useFormik`, examples.  
(Detailed references omitted in the file; see your assistant's chat response for sources.)

---

## 9. Notes & best practices
- Prefer `defaultValue` for uncontrolled inputs and `value` for controlled.  
- Keep expensive work out of `onChange` (debounce if needed).  
- For libraries and UI component integration, prefer the library's recommended pattern (e.g., use RHF's `Controller` for Material UI).  
- Always test typing & UX for complex forms — cursor jumps and input lag are telltale signs of over-rendering.

---

*Cheat-sheet generated for quick interview prep and implementation reference.*


# ReactJS — Error Handling  
**Topic:** ReactJS  
**Sub Topic:** Error Boundaries, componentDidCatch, Fallback UIs

---

## 1. What Are Error Boundaries?

Error Boundaries are special React components that catch JavaScript errors **anywhere in their child component tree** during:

- rendering  
- lifecycle methods  
- constructors of child components  

…and replace the crashed UI with a **fallback UI** instead of breaking the entire React app.

They were introduced in **React 16**.

Important:  
**They do NOT catch errors in event handlers, async code (promises, timeouts), SSR, or errors thrown inside the boundary itself.**

---

## 2. API: `getDerivedStateFromError` & `componentDidCatch`

### `static getDerivedStateFromError(error)`
A lifecycle method used to update state so React can show the fallback UI on the next render.

### `componentDidCatch(error, errorInfo)`
Used to perform side effects (logging, analytics, external monitoring).  
Receives `error` and `errorInfo.componentStack`.

### Example Error Boundary

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    console.error("Error captured:", error, info.componentStack);
  }

  render() {
    if (this.state.hasError) {
      return <h2>Something went wrong.</h2>;
    }
    return this.props.children;
  }
}
```

Usage:

```jsx
<ErrorBoundary>
  <MyComponent />
</ErrorBoundary>
```

---

## 3. Fallback UIs

Fallback UI = the UI shown when part of the component tree crashes.  
Examples:

- Simple message (`<h2>Oops!</h2>`)
- Retry button
- “Report issue”
- Redirect or reload UI

Characteristics of a good fallback UI:

- Human‑friendly  
- Provides recovery options  
- Logs error behind the scenes  

---

## 4. Limitations & Gotchas

Error boundaries **do not** catch errors:

- in event handlers  
- in async operations (`setTimeout`, `fetch`, promises)  
- during server‑side rendering  
- in the error boundary's own code  

You must handle async/event errors manually (try/catch + error reporting).

Functional components **cannot define** error boundary lifecycle methods directly.  
You can use libraries like `react-error-boundary` to simulate boundaries with hooks.

---

## 5. Where to Use Error Boundaries

Use boundaries around:

- Entire app root  
- Individual routes  
- Widgets (charts, maps, 3rd‑party components)  
- Any unstable or experimental feature  

Granularity matters:  
A boundary too high hides too many errors; too many boundaries obscure real failures.

---

## 6. Interview Q&A (Concise)

**Q:** What makes a component an Error Boundary?  
**A:** It must be a class component implementing `getDerivedStateFromError` or `componentDidCatch`.

**Q:** What errors do boundaries catch?  
**A:** Render errors, lifecycle errors, constructor errors of descendants.

**Q:** Why don't error boundaries catch event handler errors?  
**A:** Because React treats event handlers separately; you must use try/catch manually.

**Q:** What is the purpose of `componentDidCatch`?  
**A:** Logging/reporting the error and component stack.

**Q:** Can functional components be error boundaries?  
**A:** Not natively; must use class components or external wrappers.

---

## 7. Coding Interview Exercises

1. Build an `ErrorBoundary` that includes a retry button to reset state.
2. Wrap each Route in React Router with a boundary and show custom fallback per route.
3. Demonstrate handling an async error inside `useEffect` using try/catch + boundary for UI-level issues.
4. Integrate `react-error-boundary` to create a hook-friendly boundary with reset conditions.

---

## 8. Best Practices

- Combine boundaries with logging tools (Sentry, LogRocket).  
- Keep fallback UIs clear & actionable.  
- Reset boundary state on retry or navigation.  
- Use meaningful granularity — don’t wrap every tiny component.  
- For async/event errors: use manual try/catch + global JS error events.

---

## 9. Summary

Error boundaries allow React apps to fail gracefully by catching render‑tree errors and showing fallback UIs. They improve UX, stability, and debugging. They are class‑component–only but can be integrated into hook‑based apps through libraries.

---

*End of React Error Handling Cheat Sheet.*


# ReactJS Cheat Sheet: Refs & DOM  
## Topic: ReactJS  
## Sub Topic: Refs & DOM (accessing DOM, forwarding refs, useImperativeHandle)

---

## 🌿 1. Understanding Refs in React  
Refs provide a direct handle to DOM nodes or React elements. They bypass React’s declarative flow when you need to “reach into” components.

### When refs shine:
- Focusing an input.
- Triggering imperative animations.
- Measuring element dimensions.
- Integrating with non-React libraries.

### How to create a ref  
```javascript
import { useRef } from "react";

function Example() {
  const inputRef = useRef(null);

  const focusInput = () => {
    inputRef.current.focus();
  };

  return (
    <>
      <input ref={inputRef} />
      <button onClick={focusInput}>Focus</button>
    </>
  );
}
```

---

## 🌱 2. Accessing the DOM with Refs  
React doesn’t expose DOM nodes directly, but attaching a ref to a DOM element gives access.

### Ref flow:
`useRef()` → `{ current: null }` initially → React assigns DOM node after render.

Example:
```javascript
const divRef = useRef();
useEffect(() => {
  console.log(divRef.current.getBoundingClientRect());
}, []);
```

---

## 🌾 3. Forwarding Refs  
Usually, parent refs don’t penetrate child components. `forwardRef` allows this—like giving the parent VIP backstage access.

### Example: Forwarding a ref to an input inside a child component
```javascript
import { forwardRef } from "react";

const CustomInput = forwardRef((props, ref) => {
  return <input ref={ref} {...props} />;
});

function Parent() {
  const inputRef = useRef();
  return <CustomInput ref={inputRef} placeholder="Type here..." />;
}
```

---

## 🌻 4. useImperativeHandle  
This hook customizes what the parent gets when using a ref with `forwardRef`.  
It’s like giving the parent a curated API instead of the raw DOM.

### Example:
```javascript
import { useRef, forwardRef, useImperativeHandle } from "react";

const FancyInput = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus() {
      inputRef.current.focus();
    },
    clear() {
      inputRef.current.value = "";
    }
  }));

  return <input ref={inputRef} />;
});

function Parent() {
  const ref = useRef();

  return (
    <>
      <FancyInput ref={ref} />
      <button onClick={() => ref.current.focus()}>Focus</button>
      <button onClick={() => ref.current.clear()}>Clear</button>
    </>
  );
}
```

---

## 🧠 5. Interview Theory Questions (Concise Answers)

### 1. What are refs in React?  
Refs let you access DOM nodes or React elements directly without relying on state updates.

### 2. When should you use a ref?  
When performing imperative DOM actions—focusing, scrolling, measuring, or working with non-React libraries.

### 3. What is `forwardRef`?  
A method that enables passing a ref through a component to a child element.

### 4. Why does `useImperativeHandle` exist?  
To restrict or customize what a parent can access when using refs—preventing overexposure of internal implementation.

### 5. Do refs cause rerenders?  
No. Updating `.current` doesn’t trigger re-renders.

### 6. Can refs store data like variables?  
Yes. Refs persist across renders and do not cause re-renders.

### 7. What's the difference between callback refs and object refs?  
Callback refs use a function; object refs come from `useRef()`. Callback refs run on mount/unmount.

---

## 💻 6. Coding-Based Interview Questions

### Q1. Create a custom button component whose click method can be triggered from a parent.
```javascript
const CustomButton = forwardRef((props, ref) => {
  const buttonRef = useRef();

  useImperativeHandle(ref, () => ({
    click: () => buttonRef.current.click()
  }));

  return <button ref={buttonRef} {...props}>Click Me</button>;
});
```

### Q2. Implement a component that exposes scroll-to-bottom behavior via ref.
```javascript
const ScrollBox = forwardRef((props, ref) => {
  const boxRef = useRef();

  useImperativeHandle(ref, () => ({
    scrollToBottom() {
      boxRef.current.scrollTop = boxRef.current.scrollHeight;
    }
  }));

  return (
    <div ref={boxRef} style={{ height: 150, overflow: "auto" }}>
      {props.children}
    </div>
  );
});
```

### Q3. Build an input component that auto-focuses using `useRef`.
```javascript
function AutoFocusInput() {
  const ref = useRef();
  useEffect(() => ref.current.focus(), []);
  return <input ref={ref} />;
}
```

---

## ✅ All content included  
This cheat sheet covers: accessing DOM, forwarding refs, useImperativeHandle, interview questions, and coding tasks.

# ReactJS Performance Optimization  
## Topic: ReactJS  
## Sub Topic: Performance Optimization — React.memo, useMemo, useCallback, Lazy Loading

---

## 1. React Performance Optimization — In Depth

Performance issues in React often come from unnecessary re-renders, heavy computations inside render cycles, and large bundle sizes. These four tools—`React.memo`, `useMemo`, `useCallback`, and lazy loading—address these issues.

---

## React.memo

`React.memo` is a higher-order component that prevents a functional component from re-rendering when its props haven’t changed (based on shallow comparison).

### Usage:
```javascript
const MyComponent = React.memo(function MyComponent(props) {
  return <div>{props.value}</div>;
});
```

### Notes:
- Best for pure components.
- Avoid using when props always change by reference (new objects/functions each render).
- Can introduce overhead if used excessively.

---

## useMemo

`useMemo` memoizes the *result of a computation*.

### Syntax:
```javascript
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

### When to use:
- Expensive calculations
- Filtering, sorting, or transforming large datasets
- Stabilizing object references to help `React.memo`

---

## useCallback

`useCallback` memoizes a *function reference*.

### Syntax:
```javascript
const memoizedFn = useCallback(() => {
  doSomething();
}, [dependencies]);
```

### When to use:
- Passing functions to memoized children
- Stabilizing callbacks used in dependency arrays

---

## Lazy Loading / Code Splitting

Lazy loading reduces bundle size by loading components only when needed.

### Usage:
```javascript
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

### Benefits:
- Faster initial load
- Only load routes/components when accessed

---

## 2. Interview Theory Questions (Concise Answers)

### 1. What does `React.memo` do?
Prevents re-rendering of a component when its props haven't changed.

### 2. When is `useMemo` useful?
When you need to avoid recalculating expensive computations on every render.

### 3. What problem does `useCallback` solve?
Prevents child components from re-rendering due to unstable function references.

### 4. How does lazy loading improve performance?
It splits code into chunks and loads only what’s needed, improving startup performance.

### 5. Difference between `useMemo` and `useCallback`?
`useMemo` memoizes values; `useCallback` memoizes functions.

### 6. When should you avoid memoization?
When computations are cheap or dependencies change too often.

### 7. What triggers unnecessary re-renders?
Parent re-renders, new prop references, context changes, or state updates.

---

## 3. Coding-Based Questions

### Q1. Optimize filtering with `useMemo` + `React.memo`
```javascript
const Item = React.memo(({ name }) => <li>{name}</li>);

function ItemList({ items, filter }) {
  const filtered = useMemo(() => {
    return items.filter(item => item.name.includes(filter));
  }, [items, filter]);

  return (
    <ul>
      {filtered.map(item => <Item key={item.id} name={item.name} />)}
    </ul>
  );
}
```

---

### Q2. Prevent child re-renders using `useCallback`
```javascript
const Child = React.memo(({ onClick }) => {
  return <button onClick={onClick}>Click</button>;
});

function Parent() {
  const [count, setCount] = useState(0);

  const stableHandler = useCallback(() => {
    console.log("clicked");
  }, []);

  return (
    <>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      <Child onClick={stableHandler} />
    </>
  );
}
```

---

### Q3. Lazy load a heavy component
```javascript
const HeavyComponent = React.lazy(() => import("./HeavyComponent"));

function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <HeavyComponent />
    </Suspense>
  );
}
```

---

All core optimization techniques covered: React.memo, useMemo, useCallback, lazy loading, interview questions, and coding tasks.
