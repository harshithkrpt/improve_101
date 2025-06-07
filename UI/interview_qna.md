# JavaScript and React Interview Questions and Answers

## JavaScript

1. **Difference between JavaScript and other programming languages.**  
JavaScript is a dynamically-typed, weakly-coerced, prototype-based language primarily designed for the browser with an event-driven, single-threaded model, unlike class-based, statically typed, multi-threaded languages like Java or C++.

2. **Explain execution context in JavaScript; how the event loop works.**  
Execution contexts (global, function, eval) manage code evaluation, creating variable and lexical environments. The event loop handles async tasks by processing the call stack, then draining microtask queues (Promises), then running macrotasks (timers, I/O).

3. **Difference between `let`, `const` and `var`.**  
`var` is function-scoped and hoisted initialized to `undefined`; `let`/`const` are block-scoped, hoisted but uninitialized until declaration (TDZ). `let` allows reassignment; `const` prevents reassignments.

4. **What are primitive and non-primitive data types?**  
Primitives (`undefined`, `null`, `boolean`, `number`, `string`, `symbol`, `bigint`) are immutable and stored by value. Non-primitives (objects, arrays, functions) are mutable and stored by reference.

5. **What is the Nullish coalescing operator?**  
`a ?? b` returns `a` if it’s not `null` or `undefined`; otherwise it returns `b`, avoiding fallback on other falsy values like `0` or `''`.

6. **What is an arrow function and how is it different from a normal function?**  
Arrow functions use `()=>{}` syntax, have lexical `this`, lack their own `arguments` object, cannot be used as constructors, and do not have a `prototype` property.

7. **What is IIFE?**  
Immediately Invoked Function Expression `(function(){ /*...*/ })()` runs once immediately, creating a private scope and avoiding global namespace pollution.

8. **What is the closures concept in JavaScript?**  
A closure occurs when an inner function retains access to its outer function’s variables even after the outer function has returned, enabling data privacy and function factories.

9. **What is the `this` keyword?**  
`this` refers to the invocation context: global object in default calls, the owning object in method calls, a new instance with `new`, explicitly set by `.call/.apply/.bind`, and lexically bound in arrow functions.

10. **What is prototype and prototype inheritance?**  
Every object links to a prototype object from which it inherits properties; changes to the prototype reflect in all linked instances (prototypal delegation).

11. **Difference between `map`, `filter` and `find` methods.**  
`map` returns a new array of transformed values, `filter` returns a new array of elements meeting a condition, and `find` returns the first element matching the condition or `undefined`.

12. **What is the difference between `forEach` and `map` methods?**  
`forEach` executes a callback for each element without returning a value; `map` returns a new array of results.

13. **What is a callback function? List down use cases.**  
A callback is a function passed as an argument to be called later, commonly used for async tasks (timers, I/O), event handlers, array processing, and function composition.

14. **What is callback hell? How to avoid it?**  
Nested callbacks creating unreadable code; avoid by using named functions, Promises, `async/await`, or flow-control libraries.

15. **What is a Promise? Explain with an example.**  
A Promise represents an async operation’s eventual result.  
```js
const p = new Promise((resolve, reject) => {
  setTimeout(() => resolve('done'), 1000);
});
p.then(console.log).catch(console.error);
```

16. **What are promise methods?**  
Core methods: `.then()`, `.catch()`, `.finally()`. Helpers: `Promise.all()`, `Promise.race()`, `Promise.allSettled()`, `Promise.any()`.

17. **Difference between `Promise.race` and `Promise.any`.**  
`race` settles with the first settled Promise (fulfilled or rejected). `any` fulfills with the first fulfilled Promise or rejects if all reject.

18. **What is event bubbling and event capturing?**  
Capturing phase runs from the window down to the target; bubbling phase runs from target up to the window; handlers can listen in either phase.

19. **What is the event delegation concept in JavaScript?**  
Attach a single event listener on a parent to handle events on child elements by checking `event.target`, improving performance and dynamic content handling.

20. **Difference between `localStorage`, `sessionStorage` and cookies.**  
`localStorage` persists data with no expiry, `sessionStorage` clears on tab close, cookies can expire and are sent to the server with each request, limited size.

21. **What is the immutability concept in JavaScript?**  
Treat data structures as read-only; create new copies on change using spread operators, `Object.assign`, or libraries like Immutable.js.

22. **Explain the difference between `Map` and `Set`.**  
`Map` stores key-value pairs with any value type as key; `Set` stores unique values without keys.

23. **What is the code splitting concept in JavaScript?**  
Divide code into smaller chunks that load on demand (via dynamic `import()` or bundler config) to reduce initial bundle size.

24. **Explain memoization concept in JavaScript with examples.**  
Cache results of expensive function calls based on arguments:
```js
const memo = {};
function fib(n) {
  if (memo[n]) return memo[n];
  return memo[n] = n < 2 ? n : fib(n-1) + fib(n-2);
}
```

25. **What is strict mode in JavaScript?**  
`'use strict'` enables stricter parsing and error handling: disallows undeclared variables, silent failures, and certain legacy features.

26. **Difference between `call()`, `bind()` and `apply()` methods with example.**  
`call` invokes with a given `this` and args list; `apply` uses an arg array; `bind` returns a new function permanently bound to a `this` context.

27. **What is the currying concept in JavaScript?**  
Transform a function with multiple arguments into a chain of unary functions:
```js
const add = a => b => a + b;
add(2)(3); // 5
```

28. **Difference between shallow and deep copy in object.**  
Shallow copy duplicates top-level properties (via spread or `Object.assign`), but nested objects remain shared; deep copy recursively clones all levels (using `structuredClone()` or recursive logic).

## React

1. **What is Reactjs and how is it different from other libraries/frameworks?**  
React is a declarative, component-based library for building UIs using a virtual DOM for efficient updates, unlike imperative MVC frameworks.

2. **What is JSX? What is the difference between JSX and TSX in Reactjs?**  
JSX is a JavaScript syntax extension allowing HTML-like code; TSX is JSX with TypeScript typing support.

3. **Explain the concept of virtual DOM, Shadow DOM in Reactjs.**  
Virtual DOM is an in-memory UI representation that React diffs to the real DOM. Shadow DOM is browser technology for encapsulating component markup and style, unrelated to React core.

4. **How is virtual DOM different from real DOM?**  
Virtual DOM updates are batched and diffed in memory before applying minimal changes to the slower real DOM.

5. **What are the different types of components in Reactjs?**  
Class components, functional components, pure components, higher-order components, and (in future) server components.

6. **Difference between class and functional component.**  
Class components use ES6 classes with lifecycle methods; functional components are plain functions using Hooks for state and effects.

7. **What is the state of Reactjs?**  
State is a component’s private data object that determines its rendered output and can be updated via `setState` or `useState`.

8. **What are props and the difference between props and state.**  
Props are read-only inputs passed from parents; state is internal and mutable data managed by the component.

9. **What is props drilling and alternative to it?**  
Passing props through multiple levels; alternatives include Context API, Redux, or custom state management.

10. **Difference between controlled and uncontrolled components.**  
Controlled components have their value controlled by React state; uncontrolled manage their own internal value accessed via refs.

11. **How re-render happens when states change in Reactjs?**  
Calling `setState` or updating a Hook state schedules a re-render; React diffs old and new virtual DOM to update the real DOM.

12. **What happens if you try to update the state directly in Reactjs?**  
Direct mutation (`state.x = value`) bypasses React’s change detection, causing inconsistencies and no re-render.

13. **How to share data among sibling components?**  
Lift state up to the nearest common ancestor or use Context/Redux for global state.

14. **What is a styled component? Have you implemented theming in Reactjs?**  
Styled-components is a CSS-in-JS library using tagged templates; theming via `<ThemeProvider>` and theme objects.

15. **What is the React server component?**  
Server components are rendered on the server without sending JS to the client, enabling smaller client bundles.

16. **Explain lifecycle methods of components.**  
Mount: `constructor`, `componentDidMount`; update: `shouldComponentUpdate`, `componentDidUpdate`; unmount: `componentWillUnmount`.

17. **How do functional components handle the lifecycle methods of class components?**  
Using `useEffect` with dependency arrays to mimic mount, update, and unmount behaviors.

18. **How to handle side effects in class and functional components?**  
Class: in lifecycle methods; functional: inside `useEffect`, with cleanup via return.

19. **What are React hooks? List out hooks you have used till date.**  
Functions like `useState`, `useEffect`, `useContext`, `useReducer`, `useMemo`, `useCallback`, `useRef`, enabling state and side effects in functional components.

20. **Difference between `useState` and `useRef` hooks in form handling.**  
`useState` triggers re-render on updates; `useRef` holds mutable values without rerendering.

21. **What are the differences between `useState`, `useContext` and `useReducer`?**  
`useState` for local state, `useContext` for accessing global context, `useReducer` for complex state logic with actions and reducers.

22. **What are the rules of hooks in React?**  
Only call Hooks at the top level and only inside React function components or custom hooks.

23. **What are custom hooks? Have you used it in a project? Provide an example.**  
Custom hooks are functions starting with `use` that encapsulate reusable Hook logic, e.g., `useFetch` to fetch data on mount.

24. **What is a Higher Order Component? Explain with examples.**  
A function that takes a component and returns an enhanced component, e.g., `withRouter` for React Router or `connect` in Redux.

25. **What is the React reconciliation process?**  
React compares old and new virtual DOM trees using a diffing algorithm to update only changed parts in the real DOM.

26. **How does React compare virtual DOM with real DOM?**  
React diffs two virtual DOM nodes by key and type, then applies minimal necessary updates to the real DOM.

27. **What are Context API hooks? Explain with an example.**  
`useContext(MyContext)` consumes a context value created via `React.createContext`, avoiding prop drilling.

28. **What is the difference between `useCallback` and `useMemo` hooks?**  
`useCallback` memoizes a function reference; `useMemo` memoizes a computed value result.

29. **Difference between Context API and Redux.**  
Context API is built-in for simple global state; Redux is a standalone library with a strict unidirectional data flow, middleware, and devtools.

30. **What is the Redux Toolkit? How does it simplify Redux?**  
Redux Toolkit provides utilities like `createSlice`, `configureStore`, and `createAsyncThunk` to reduce boilerplate and enforce best practices.

31. **What are middleware in Redux?**  
Functions that intercept dispatched actions before reaching reducers, used for logging, async flows (`redux-thunk`, `redux-saga`), etc.

32. **How would you implement a global state without Redux?**  
Use Context with `useReducer` or third-party libs like Zustand, Jotai, or Recoil.

33. **What is a synthetic event in React?**  
A cross-browser wrapper around native events providing consistent API, pooling, and performance optimizations.

34. **Difference between a synthetic event and a real DOM event.**  
Synthetic events are React’s normalized event objects pooled for efficiency; real events are native browser events.

35. **How to pass arguments to the event handler in React?**  
Use an inline arrow: `onClick={() => handleClick(id)}` or `onClick={handleClick.bind(null, id)}`.

36. **How do you handle dynamic routing in React?**  
Use React Router’s `<Route path="/user/:id">` and the `useParams` hook to access route parameters.

37. **How do you manage form validation in React? Explain with examples.**  
Use controlled components with validation logic in state or libraries like Formik/React Hook Form with schema validation (Yup).

38. **How would you implement lazy loading with routes?**  
Wrap dynamic imports with `React.lazy` and `Suspense`:  
```jsx
const Dashboard = React.lazy(() => import('./Dashboard'));
<Suspense fallback={<Spinner />}><Dashboard /></Suspense>
```

39. **How do you optimize forms with hundreds of input fields in React?**  
Virtualize inputs, split into steps, memoize fields, and use libraries optimized for large forms.

40. **How would you implement a multi-step form with conditional rendering between steps?**  
Track step index in state and render different form sections; advance steps on validation.

41. **What are keys in React? Why are they important in lists?**  
Keys are unique IDs for sibling elements; they help React match items during reconciliation to minimize re-renders.

42. **What is `React.memo` and how does it work?**  
`React.memo(Component)` memoizes a functional component, re-rendering it only when its props shallowly change.

43. **What is the React pure component? Explain with roles and use cases.**  
A class component extending `PureComponent` implements shallow prop/state comparisons in `shouldComponentUpdate` to prevent unnecessary renders.

44. **What is the concept called virtualization in React?**  
Virtualization renders only visible list items (e.g., via `react-window`) to improve performance for large datasets.

45. **How do you optimize rendering of large lists in React?**  
Use keys, memoize item components, windowing/virtualization, and avoid inline functions/objects as props.

46. **How to avoid unnecessary re-rendering in React?**  
Apply `React.memo`, `useCallback`, `useMemo`, and lift state appropriately to minimize prop changes.

47. **What is the purpose of error boundaries in React?**  
Catch and handle render errors in a component tree, displaying a fallback UI instead of crashing the app.

48. **How do you handle errors in asynchronous operations in React?**  
Use `try/catch` in `async` functions or `.catch` on Promises and propagate errors to error boundaries or UI state.

49. **How do you fetch data in React? Explain with examples.**  
Use `useEffect` to call fetch/Axios on mount, set state on response, and handle loading/error states.

50. **What is Axios and how is it different from Fetch API?**  
Axios is a promise-based HTTP client with interceptor support and automatic JSON handling; Fetch is a native low-level API requiring manual JSON parsing and lacks built-in interceptors.

51. **How do you securely store API keys in React?**  
Store secrets in environment variables (`.env`), accessed at build time (`process.env.REACT_APP_KEY`), never checked into source control or exposed in client code.

52. **How would you implement retry logic for failed API requests in React?**  
Wrap requests in retry loops or use libraries like `axios-retry` with configurable backoff strategies.

53. **What are Fragments in React? Why are they used?**  
`<></>` or `<React.Fragment>` group multiple elements without extra DOM nodes, keeping markup clean.

54. **What is the significance of `React.StrictMode`?**  
A development-only wrapper that highlights deprecated APIs, side-effect issues, and potential problems by invoking certain functions twice.

55. **How do you identify and fix memory leaks in React?**  
Use profiling tools, ensure cleanup of timers/subscriptions in `useEffect` cleanup or `componentWillUnmount`.

56. **How do you build React applications for production?**  
Run `npm run build` (for CRA) or configure webpack for `mode: 'production'` to minify, tree-shake, and optimize assets.

57. **What is the major difference between Webpack and Babel?**  
Webpack is a module bundler packaging assets; Babel is a JavaScript compiler/transpiler converting modern syntax to compatible versions.

58. **How do you configure Webpack for React projects?**  
Set entry/output, use `babel-loader` for JS/JSX, `css-loader`/`style-loader` for CSS, and plugins like `HtmlWebpackPlugin` and `DefinePlugin`.

59. **How do you optimize a React application for performance?**  
Code-splitting, lazy loading, memoization, virtualization, and analyzing bundle size with tools like `webpack-bundle-analyzer`.

60. **Explain the purpose of `.env` file in React?**  
Store environment-specific variables (prefixed with `REACT_APP_`) that are injected at build time for configuration without hardcoding.

