# Topic: ReactJS
## Sub Topic: Reconciliation — Fiber architecture, diffing algorithm, render batching

---

## 1. Overview (what this is and why it matters)
**Reconciliation** is React's process for determining what changed between two renders and updating the DOM efficiently. React builds a virtual DOM on each render, compares it with the previous one, and applies a minimal set of updates to the real DOM. The Fiber architecture (React's modern reconciler) rewrote the reconciling engine to enable incremental work, priorities, and interruption — which makes animations, time-slicing and smoother rendering possible. citeturn0search7turn0search12

---

## 2. Fiber architecture — key ideas
- **Fiber node = unit of work:** Each Fiber object represents a React element (component instance or DOM node) and contains pointers for parent, child and sibling. Fibers let React break rendering into small interruptible units. citeturn0search12  
- **Work-in-progress (WIP) tree vs current tree:** React keeps the previous committed tree (current) and builds a WIP tree during updates; once finished the WIP tree becomes the new current tree. This separation allows safe, incremental updates. citeturn0search14  
- **Prioritization & scheduler:** Fiber supports different priorities for updates (user input, animation, low-priority background updates) and can yield to the browser to keep UI responsive. citeturn0search14  
- **Effect phase separation (render vs commit):** Rendering computes the changes (diffing, reconciliation) without touching the DOM. The commit phase applies side effects and actual DOM mutations. This keeps calculation and side effects decoupled. citeturn0search12turn0search14

---

## 3. The Diffing Algorithm — practical rules
React's diffing algorithm is heuristic (not a full tree diff) and relies on reasonable assumptions to be O(n) in most cases: citeturn0search7turn0search14
1. **Different root types = replace:** If component types differ at the root (e.g., `<div>` vs `<span>` or different component class/function), React tears down the old subtree and mounts a new one. citeturn0search7  
2. **Same type = update in-place:** If the element type is identical, React keeps the same DOM node and updates props, event handlers, and children. citeturn0search7  
3. **Keyed children optimization:** For lists, React uses `key` to match children between renders. Keys help React detect moves, insertions, and deletions efficiently. Without keys, React falls back to index-based heuristics that can cause unnecessary re-renders. Always provide stable keys for dynamic lists. citeturn0search7  
4. **Minimal reorders assumed:** React assumes sibling subtrees are similar between renders; massive reordering can degrade performance and force more work. Keys mitigate this. citeturn0search7

---

## 4. Render batching (what changed in recent React versions)
- **Batching:** grouping multiple state updates into a single render pass reduces the number of renders. React historically batched updates inside event handlers only. Starting with React 18, **automatic batching** was extended to cover more contexts (promises, timeouts, native events), so unrelated state updates that run within the same tick can be flushed together into one render. This reduces unnecessary renders and improves performance. citeturn0search5turn0search1
- **Concurrent features effect:** With concurrent rendering (time-slicing, transitions), React may delay lower-priority renders and group or interrupt work for higher-priority updates — batching interacts with the scheduler to make UI responsive. citeturn0search14

---

## 5. Common gotchas & performance tips
- Use **stable keys** for lists (avoid `index` when items reorder). citeturn0search7  
- Minimize heavy work inside render functions — Fiber can split work, but rendering large trees still costs CPU. Consider `memo`, `useMemo`, `useCallback` where appropriate. citeturn0search14  
- Avoid creating new object/array literals as props on every render unless necessary (causes children `===` checks to fail). Prefer memoization. citeturn0search14  
- Prefer declarative transitions (React 18 `startTransition`) to mark low-priority updates so important updates aren't blocked. citeturn0search14

---

## 6. Interview-style theory questions (concise answers)

**Q1: What is reconciliation in React?**  
A1: The process React uses to compare the new virtual DOM with the previous one and compute minimal updates to the real DOM. citeturn0search7

**Q2: What is Fiber? Why was it introduced?**  
A2: Fiber is the rewritten reconciler that represents units of work as fiber nodes; it enables incremental, interruptible rendering, priority scheduling, and better handling of animations/layout. citeturn0search12turn0search14

**Q3: How does React decide whether to update or replace a component?**  
A3: If element/component type is the same, React updates in place; if types differ, it unmounts the old subtree and mounts the new one. Keys influence how children are matched. citeturn0search7

**Q4: What are keys and why are they important?**  
A4: Keys are stable identifiers for list items that help React match existing children to new children across renders, enabling efficient moves, insertions, and deletions. citeturn0search7

**Q5: What changed with automatic batching in React 18?**  
A5: Automatic batching broadened what contexts React will batch (promises, setTimeout, native events), allowing multiple state updates across async boundaries to be flushed together into a single render. citeturn0search5turn0search1

---

## 7. Coding / practical questions (with short guidance)

**C1: Implement a small example demonstrating keys vs no-keys (and show the problem).**  
Guidance: Render a list that reorders or splices items; show that with index keys React reuses wrong DOM nodes (visual glitches). Provide stable `id` keys to fix it.

**C2: Show how to batch multiple state updates (React 18 automatic batching vs manual batching).**  
Guidance: Demonstrate two `setState` calls inside `setTimeout` and note that React 18 will batch them automatically; prior versions required `unstable_batchedUpdates` or placing updates inside a React event.

**C3: Use `startTransition` to mark a low-priority state update.**  
Guidance: Wrap a non-urgent update with `startTransition(() => setState(...))` so urgent updates remain responsive.

**C4: Profile and optimize: identify a re-render source using React DevTools and fix with `React.memo` or `useCallback`.**  
Guidance: Inspect component update traces, check prop identity, add memoization where appropriate, avoid over-memoizing.

---

## 8. Quick cheat-sheet (bulleted recap)
- Fiber = incremental work units (nodes) + scheduler. citeturn0search12  
- Reconciliation = diffing virtual DOM -> minimal DOM updates. citeturn0search7  
- Keys are critical for list stability. citeturn0search7  
- Render vs Commit phases: compute then mutate. citeturn0search14  
- React 18 automatic batching reduces renders across async boundaries. citeturn0search5

---

## 9. References / further reading
- React official reconciliation docs and legacy guide. citeturn0search7  
- React v18 blog (Automatic Batching). citeturn0search5  
- acdlite/react-fiber-architecture (GitHub). citeturn0search12  
- LogRocket deep-dive on Fiber. citeturn0search14

---

*File generated:* `react-reconciliation-cheatsheet.md`

# Topic: ReactJS
## Sub Topic: Rendering Types — Client Rendering, Server Rendering, Hydration, Static Rendering

---

## 1. Client Rendering (CSR)
Client Rendering means your JavaScript runs entirely in the browser. The server sends a mostly empty HTML shell and a JS bundle. React then builds the UI using the virtual DOM.

### How it works
- Browser downloads HTML → JS bundle → React executes → UI appears.
- Initial load is slower because JS must download and execute before anything renders.
- Great for highly interactive dashboards or apps where SEO is not a priority.

### Pros
- Fast client-side transitions.
- Very dynamic UIs.
- Simplifies deployment.

### Cons
- Slower first paint.
- Poor SEO unless using prerendering.

---

## 2. Server Rendering (SSR)
Server Rendering (also called **Server-Side Rendering**) generates HTML on the server for each request. The server sends fully rendered HTML to the browser.

### How it works
- Request hits server → server runs React → sends rendered HTML → browser loads JS → hydration attaches events.
- Faster first paint and better SEO.

### Pros
- Great for SEO.
- Faster initial load.
- Content is visible even before JS loads.

### Cons
- Heavier server load.
- Slower navigation between pages unless framework adds client routing.
- Hydration cost still applies.

---

## 3. Hydration
Hydration attaches React's event listeners and internal structures to server-rendered HTML, making it interactive.

### How it works
- Server sends HTML.
- Browser loads JS.
- React walks through DOM to connect components and events.
- After hydration, UI is fully interactive.

### Important details
- DOM must match exactly the HTML generated by the server.
- Mismatches cause React to throw hydration warnings.

---

## 4. Static Rendering (SSG)
Static Site Generation (SSG) pre-renders HTML at build time. No server is required for rendering each request.

### How it works
- React runs at build time → produces static HTML files.
- Pages are served from a CDN.
- Optional hydration adds interactivity.

### Pros
- Ultra-fast (served from CDN).
- Great for blogs, documentation, marketing pages.
- Zero server cost.

### Cons
- Not ideal for frequently changing data.
- Requires rebuilds to update content.

---

## 5. When to Use What?

**CSR**: Apps with heavy interactivity but low SEO needs (dashboards, admin panels).  
**SSR**: SEO-heavy pages with dynamic data (e-commerce, landing pages).  
**SSG**: Content-focused pages with infrequent updates (blogs, docs).  
**Hydration**: Always paired with SSR/SSG to enable interactivity.

---

## 6. Interview Questions (Concise Answers)

**Q1: What is the difference between CSR and SSR?**  
CSR renders UI in the browser using JS. SSR renders HTML on the server and sends it to the browser.

**Q2: Why do we need hydration?**  
Hydration makes server-rendered HTML interactive by attaching React event listeners.

**Q3: Is hydration required for static rendering?**  
Yes, if the static page needs interactivity. Otherwise, hydration is optional.

**Q4: What are advantages of static rendering?**  
Fast load times, CDN-friendly, great for SEO, minimal server load.

**Q5: What problems occur during hydration mismatches?**  
React logs warnings and may rebuild DOM nodes, hurting performance.

---

## 7. Coding-Oriented Practical Scenarios

**C1: Simple SSR example using ReactDOMServer.renderToString()**  
Render a React component on the server and send the result as HTML.

**C2: Hydration example using ReactDOM.hydrateRoot()**  
Client script hydrates the SSR-generated HTML.

**C3: SSG-like build script**  
Use a Node script to run React components at build time and output HTML to files.

**C4: Demonstrate CSR vs SSR timing differences**  
Console.log markers to show when HTML appears vs when JS loads.

---

## 8. Cheat Sheet Summary

- **CSR** → Browser renders everything with JS.  
- **SSR** → Server pre-renders HTML for each request.  
- **Hydration** → React connects interactivity to server/static HTML.  
- **SSG** → HTML generated at build time, best for static content.

---

*File generated:* react-rendering-types.md

# Topic: ReactJS
## Sub Topic: Code Splitting — React.lazy, Suspense, dynamic imports

---

## 1. Overview (what and why)
**Code splitting** breaks your JavaScript into smaller bundles that load on demand instead of one giant file. This reduces initial bundle size and speeds up first paint. In React, the common tools for component-level code splitting are `import()` (dynamic imports), `React.lazy`, and `Suspense`. citeturn0search1turn0search16

---

## 2. Core APIs

### Dynamic `import()`
`import('./module')` returns a Promise that resolves to the module namespace and is the lowest-level building block for code splitting. Bundlers (Webpack, Vite, etc.) turn these calls into split chunks. Use `import()` when you want to load code on demand (e.g., route handlers, heavy components). citeturn0search1turn0search16

### `React.lazy()`
`React.lazy` is a thin wrapper around dynamic `import()` that lets you treat the imported module as a component:

```js
const LazyComp = React.lazy(() => import('./MyComponent'));
```

It must render inside a `<Suspense>` boundary to provide a fallback while the chunk loads. It expects the dynamic import to resolve to a module with a default export that is a React component. citeturn0search0turn0search15

### `<Suspense>`
`Suspense` lets you show a fallback UI while a child "suspends" — typically during code load via `React.lazy`, or (in Suspense-enabled data frameworks) during data fetching. In React 18+ Suspense is more powerful and integrates with server rendering and concurrent features. citeturn0search2turn0search10

---

## 3. How they work together (typical pattern)
1. Wrap lazy components in a `Suspense` with a fallback:
```jsx
<React.Suspense fallback={<Spinner/>}>
  <LazyComp />
</React.Suspense>
```
2. When `LazyComp` is first rendered, the dynamic `import()` begins. `Suspense` shows the `fallback` until the Promise resolves and the component can render. citeturn0search15

---

## 4. Advanced topics & best practices

### Chunking strategy
- Split by route or feature (larger, meaningful chunks) rather than splitting every tiny component. Route-based splitting reduces initial payload and still caches well. citeturn0search16

### Preloading & Pre-fetching
- Use `<link rel="preload">` or `<link rel="prefetch">` for high-likelihood future code paths (e.g., prefetch next-route chunk on hover). Some teams implement `Component.preload()` wrappers around `React.lazy` to kick off a fetch earlier. Preload = high priority, prefetch = low priority. citeturn0search8turn0search16

### Error boundaries
- Lazy-loaded components can fail to load (network errors). Wrap `Suspense` + lazy components with an Error Boundary to show a retry UI. `Suspense` itself doesn't catch loading errors — Error Boundaries do. citeturn0search15

### SSR & Suspense
- React 18 added support for Suspense on the server, enabling streaming HTML and selective hydration. Note: `React.lazy` server support is limited — frameworks like Next.js and Remix provide higher-level patterns for SSR + code splitting. Understand your server renderer's support for dynamic imports and streaming. citeturn0search10turn0search7

### Bundler hints and caching
- Name chunks sensibly in Webpack using `/* webpackChunkName: "name" */` in dynamic imports for debugging and caching. Also use long-term caching strategies for vendor and runtime chunks. citeturn0search16

### Avoid over-splitting
- Each split adds HTTP overhead (though HTTP/2 mitigates this). Too many tiny chunks can harm performance. Measure! Use bundle analyzers and real-user metrics. citeturn0search11

---

## 5. Practical patterns & examples

### Route-based splitting (React Router)
```js
const Home = React.lazy(() => import('./Home'));
const About = React.lazy(() => import('./About'));

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={
          <Suspense fallback={<Loader/>}><Home/></Suspense>
        }/>
        <Route path="/about" element={
          <Suspense fallback={<Loader/>}><About/></Suspense>
        }/>
      </Routes>
    </BrowserRouter>
  );
}
```
Use `Suspense` per-route to limit fallback UI scope. citeturn0search15

### Preload on interaction (hover)
```js
const Preloadable = (importFn) => {
  const Comp = React.lazy(importFn);
  Comp.preload = importFn;
  return Comp;
}

const About = Preloadable(() => import('./About'));

// on hover
<button onMouseEnter={() => About.preload()}>About</button>
```
This pattern reduces perceived latency for likely next navigations. citeturn0search8

---

## 6. Interview-style theory questions (concise answers)

**Q1: What does React.lazy do?**  
A1: Wraps a dynamic `import()` so the imported module can be rendered as a component; suspends rendering until the chunk loads. citeturn0search0

**Q2: Why do we need Suspense?**  
A2: Suspense provides a declarative way to show fallback content while children are waiting (loading code or data) and integrates with concurrent rendering. citeturn0search2

**Q3: How do prefetch and preload differ?**  
A3: `preload` requests a resource with high priority for the current navigation; `prefetch` hints the browser to fetch a resource for future navigations with low priority. Use preload for immediate needs, prefetch for "likely later" assets. citeturn0search16turn0search8

**Q4: How do you handle errors when lazy-loading components?**  
A4: Use an Error Boundary around lazy components to catch load failures and show retry/error UI. citeturn0search15

---

## 7. Coding questions / exercises (for interviews)

**C1:** Implement a route-splitting example with `React.lazy` + `Suspense`.  
**C2:** Add a preload-on-hover optimization for the next-route component.  
**C3:** Show how an Error Boundary can retry loading a failed lazy component.  
**C4:** Measure bundle sizes with `webpack-bundle-analyzer` and propose a chunking strategy.

---

## 8. Quick cheat-sheet (bulleted recap)
- Use `import()` to split at module boundaries. citeturn0search1  
- `React.lazy` + `<Suspense>` for easy component-level code splitting. citeturn0search0turn0search15  
- Preload/prefetch to optimize perceived load; prefer preload for likely immediate needs. citeturn0search8turn0search16  
- Wrap lazy components with Error Boundaries. citeturn0search15  
- Don't over-split; measure with bundle analyzers. citeturn0search11

---

*File generated:* react-code-splitting.md

# Topic: ReactJS
## Sub Topic: State Management — Context + Hooks vs Redux, Recoil, Jotai, Zustand

---

## 1. Quick summary (what this covers)
This cheat sheet compares common React state-management approaches: **Context + Hooks** (built-in), **Redux** (modern Redux Toolkit), **Recoil**, **Jotai**, and **Zustand**. It explains when to use each, pros/cons, patterns, interview questions, and practical coding prompts.

---

## 2. High-level differences (short)
- **Context + Hooks:** Built-in React APIs (Context, useState/useReducer/useContext). Great for dependency injection and small-to-medium scoped shared state. Not a full-featured state manager (no built-in time-travel, middleware). citeturn0search16turn0search21  
- **Redux (Redux Toolkit):** Predictable global state with a single store, immutability, middleware, and excellent devtools. Modern `@reduxjs/toolkit` (RTK) removes boilerplate and is the recommended Redux approach. Best for large, complex apps or teams who need strict patterns. citeturn0search5turn0search15  
- **Recoil:** Atom-based graph of state & derived selectors, designed to feel like React, with fine-grained subscriptions and async selectors. Good for complex derived state and scalability while remaining "React-ish". citeturn0search14turn0search1  
- **Jotai:** Minimal atomic state model inspired by Recoil; focuses on simplicity and minimal API surface. Scales from simple local atoms to complex setups with minimal re-renders. citeturn0search2turn0search23  
- **Zustand:** Tiny, hook-based store with a simple API, no provider required; great for straightforward global state with minimal boilerplate and excellent performance. citeturn0search3

---

## 3. Context + Hooks — details and patterns
- Use Context to *provide* a value to nested components. Combine with `useState` or `useReducer` to manage state. Context is effectively a DI (dependency injection) tool, not a full state manager. Overusing it for many pieces of frequently-updated state can cause excessive re-renders. citeturn0search16turn0search21

**Pattern: Scoped provider**
```jsx
const AuthContext = React.createContext();
function AuthProvider({children}) {
  const auth = useProvideAuth(); // custom hook
  return <AuthContext.Provider value={auth}>{children}</AuthContext.Provider>
}
```

**When to avoid:** Large global caches, complex derived state, or massive apps where you'd benefit from tools with selectors and middleware.

---

## 4. Redux (with Redux Toolkit) — details and patterns
- RTK simplifies Redux: `createSlice`, `configureStore`, `createAsyncThunk` and built-in good defaults (Immer, devtools). Use Redux when you need a single source of truth, structured reducers, middleware for logging/thunks/sagas, and advanced debugging. citeturn0search5turn0search9

**Example (slice):**
```js
const counterSlice = createSlice({
  name: 'counter',
  initialState: 0,
  reducers: {
    increment: state => state + 1,
    decrement: state => state - 1
  }
});
```

**Pros:** Predictability, tool ecosystem, middleware, DevTools.  
**Cons:** More boilerplate (though RTK reduces it), mental overhead for small apps.

---

## 5. Recoil — details and patterns
- Recoil uses **atoms** (state units) and **selectors** (derived/computed state). Subscriptions are fine-grained: components only re-render when the atoms they use change. It supports async selectors which integrate with Suspense for data fetching. Good for complex derived state graphs. citeturn0search14turn0search17

**Example:**
```js
const textAtom = atom({key: 'text', default: ''});
const charCount = selector({
  key: 'charCount',
  get: ({get}) => get(textAtom).length
});
```

**Pros:** Fine-grained updates, familiar React mental model.  
**Cons:** Relatively newer, API stability and ecosystem smaller than Redux; verify production readiness for your team. citeturn0search1

---

## 6. Jotai — details and patterns
- Jotai is an atomic-state library influenced by Recoil but intentionally minimal. Atoms are primitive building blocks; components subscribe to atoms they read, minimizing re-renders. Jotai has a small API surface and a strong TypeScript story. citeturn0search2turn0search23

**Example:**
```js
import { atom, useAtom } from 'jotai';
const countAtom = atom(0);
function Counter(){ 
  const [count, setCount] = useAtom(countAtom); 
  return <button onClick={()=>setCount(c=>c+1)}>{count}</button>
}
```

**Pros:** Minimal, easy to learn, low boilerplate.  
**Cons:** Less built-in tooling than Redux; large-scale patterns need planning.

---

## 7. Zustand — details and patterns
- Zustand offers a tiny API: create a store with `create`, then access state with hooks. No Provider required; works well for both local and global state. It focuses on ergonomics and speed. citeturn0search3

**Example:**
```js
import create from 'zustand';
const useStore = create(set => ({
  count: 0,
  inc: () => set(state => ({count: state.count + 1}))
}));
function Counter(){ 
  const {count, inc} = useStore();
  return <button onClick={inc}>{count}</button>
}
```

**Pros:** Tiny, fast, little ceremony.  
**Cons:** Less opinionated; teams must agree on patterns.

---

## 8. Choosing the right tool — decision heuristics
- Use **Context + Hooks** for small to moderate shared state (theme, locale, auth), or where local state is sufficient. citeturn0search16  
- Use **Redux (RTK)** for large applications that need predictable flows, middleware, advanced DevTools, or teams that benefit from strict conventions. citeturn0search5  
- Use **Recoil/Jotai** when you need fine-grained subscriptions and derived async state with minimal boilerplate and don't need full Redux ecosystem. Recoil has strong derived-state primitives; Jotai is minimal and flexible. citeturn0search14turn0search2  
- Use **Zustand** for a simple, fast store with minimal setup—good for apps that want an easy global store without provider boilerplate. citeturn0search3

---

## 9. Interview-style theory questions (concise answers)

**Q1: Is React Context a state manager?**  
A1: No — Context is a dependency injection mechanism to pass values through component trees. State management responsibilities (updates, derived state, caching) still belong to your hooks/logic. Use context to *expose* state, not to implement complex global logic alone. citeturn0search16

**Q2: Why use Redux Toolkit instead of plain Redux?**  
A2: RTK reduces boilerplate, provides safe defaults (Immer, middleware), and supplies helpers like `createSlice` and `createAsyncThunk`, making Redux easier and less error-prone. citeturn0search5

**Q3: How do Recoil atoms/selectors differ from Redux slices/selectors?**  
A3: Atoms are independent units that components subscribe to directly; selectors derive values from atoms and can be async. Redux slices centralize state in one store; selectors compute derived state from that single source. Recoil's model yields finer-grained re-render control. citeturn0search14

**Q4: When is Zustand a better fit than Redux?**  
A4: When you want a tiny API with hook-based access, minimal boilerplate, and good performance for small-to-medium global state without Redux's conceptual overhead. citeturn0search3

---

## 10. Coding tasks / interview exercises

**C1:** Implement a `ThemeProvider` using Context + useReducer for toggling themes; then refactor to Zustand and compare code size & performance.  
**C2:** Create a counter with Redux Toolkit (slice + store) and with Jotai atoms — compare API ergonomics.  
**C3:** Build a derived selector in Recoil that composes multiple atoms and uses an async selector for remote data.  
**C4:** Profile re-renders for the same app implemented with Context vs Recoil vs Zustand; demonstrate render counts and discuss outcomes.

---

## 11. Migration notes (small app -> larger app)
- If starting small with Context and the app grows: extract complex parts into focused stores (Zustand) or adopt RTK when you need middleware and strict patterns. Use feature slices and gradual migration. citeturn0search21turn0search5

---

## 12. Quick cheat-sheet (bulleted recap)
- Context = DI tool; combine with hooks for scoped shared state. citeturn0search16  
- Redux Toolkit = recommended Redux; use for large apps and team conventions. citeturn0search5  
- Recoil = atom/selector graph, great for derived and async state. citeturn0search14  
- Jotai = minimal atoms, simple ergonomics. citeturn0search2  
- Zustand = tiny hook-based store, minimal boilerplate and fast. citeturn0search3

---

*File generated:* react-state-management.md

# ReactJS - Redux Basics Cheat Sheet

**Topic** : Redux Basics  
**Sub Topic** : store, reducer, actions, dispatch, immutability

---

## 1. Core Concepts (concise)

- **Store**: single source of truth that holds the app state. Exposes `getState()`, `dispatch(action)`, and `subscribe(listener)`.
- **State**: plain JavaScript object (or tree) representing app data.
- **Action**: plain object describing *what happened*. Must have a `type` field. Optional `payload`.
  ```js
  { type: 'todos/add', payload: { id: 1, text: 'Buy milk' } }
  ```
- **Action Creator**: function that returns an action. Keeps creation consistent.
  ```js
  const addTodo = (todo) => ({ type: 'todos/add', payload: todo });
  ```
- **Reducer**: pure function `(state, action) => newState`. Never mutate input state; return a new object for changes.
- **Dispatch**: `store.dispatch(action)` sends an action to reducers to update state.
- **Middleware**: extension point between dispatch and reducers (e.g., `redux-thunk`, logging, analytics).
- **Immutability**: reducers must not mutate previous state. Use copies, spread, or Immer.

---

## 2. Minimal examples

### Classic Redux (vanilla) - create store and reducer
```js
import { createStore } from 'redux';

const initialState = { count: 0 };

function counterReducer(state = initialState, action) {
  switch (action.type) {
    case 'counter/increment':
      return { ...state, count: state.count + 1 };
    case 'counter/add':
      return { ...state, count: state.count + action.payload };
    default:
      return state;
  }
}

const store = createStore(counterReducer);
store.dispatch({ type: 'counter/increment' });
console.log(store.getState()); // { count: 1 }
```

### Recommended: Redux Toolkit (modern best practice)
```js
import { configureStore, createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { count: 0 },
  reducers: {
    increment(state) { state.count += 1 }, // uses Immer internally
    add(state, action) { state.count += action.payload }
  }
});

export const { increment, add } = counterSlice.actions;

const store = configureStore({ reducer: { counter: counterSlice.reducer } });

store.dispatch(increment());
```

---

## 3. Immutability patterns (common ops)

- Update object field:
```js
return { ...state, user: { ...state.user, name: 'Asha' } };
```
- Add item to array:
```js
return { ...state, todos: [...state.todos, newTodo] };
```
- Update item in array (by id):
```js
return {
  ...state,
  todos: state.todos.map(t => t.id === id ? { ...t, done: true } : t)
};
```
- Remove item from array:
```js
return { ...state, todos: state.todos.filter(t => t.id !== id) };
```
- With Immer (RTK):
```js
// inside createSlice reducer you can "mutate" safely
state.todos.push(newTodo);
```

---

## 4. When to use Redux (short guidance)
- Useful for global app state shared widely (auth, theme, cached server data).
- Not necessary for local component-only state (keep local with useState/useReducer).
- Prefer Redux Toolkit + RTK Query for data fetching; less boilerplate and better defaults.

---

## 5. Interview-style theory questions (concise answers)

1. **What is Redux?**  
   A predictable state container for JavaScript apps — single source of truth, state updates via actions handled by pure reducers.

2. **What are actions and action creators?**  
   Actions are plain objects with `type` and optional `payload`. Action creators are functions that return actions.

3. **What is a reducer?**  
   A pure function that calculates next state from previous state and an action. Must not mutate inputs.

4. **How does `dispatch` work?**  
   `dispatch(action)` sends the action into the store; middleware runs, then reducers compute new state, and subscribers are notified.

5. **Why immutability?**  
   Enables time-travel debugging, predictable updates, and simple change detection (shallow equality checks).

6. **What is middleware?**  
   Functions that wrap dispatch to intercept, transform, delay, or handle actions (e.g., logging, async thunks).

7. **What's the difference between Redux and Context API?**  
   Redux is a full-fledged predictable state container with tooling and middleware. Context is a React feature for passing data through tree — simpler but not a replacement for complex state logic.

8. **What is Redux Toolkit (RTK)?**  
   The official recommended toolset for writing Redux logic — reduces boilerplate, includes `createSlice`, `configureStore`, and integrates Immer.

9. **How to combine multiple reducers?**  
   Use `combineReducers({ a: aReducer, b: bReducer })` or pass an object to `configureStore` in RTK.

10. **How to handle async actions?**  
    Use middleware like `redux-thunk`, `redux-saga`, or prefer RTK's `createAsyncThunk` or RTK Query for data fetching.

---

## 6. Concise coding interview problems (with hints/solutions)

### Problem A — Write a reducer to toggle item `completed` by id
**Hint:** use `.map()` and return a new array.
```js
function todosReducer(state = { todos: [] }, action) {
  switch (action.type) {
    case 'todos/toggle':
      return {
        ...state,
        todos: state.todos.map(t => t.id === action.payload ? { ...t, completed: !t.completed } : t)
      };
    default:
      return state;
  }
}
```

### Problem B — Create a slice with Redux Toolkit for auth (login/logout)
```js
const authSlice = createSlice({
  name: 'auth',
  initialState: { user: null, token: null },
  reducers: {
    login(state, action) { state.user = action.payload.user; state.token = action.payload.token },
    logout(state) { state.user = null; state.token = null }
  }
});
```

### Problem C — Implement `addItem` action and ensure immutability without RTK
```js
const initial = { items: [] };
function itemsReducer(state = initial, action) {
  switch(action.type) {
    case 'items/add':
      return { ...state, items: [...state.items, action.payload] };
    default:
      return state;
  }
}
```

---

## 7. Quick best practices & tips
- Prefer Redux Toolkit for new apps. It’s the official recommendation.
- Keep the store normalized (avoid deeply nested objects; use entities pattern).
- Use selectors (reselect) for derived data.
- Keep reducers pure and small — compose them.
- Use TypeScript for safer action/payload typing.
- Avoid storing non-serializable values in state (functions, class instances, DOM nodes).

---

## 8. References (official + helpful)
- Redux docs — Fundamentals & Style Guide (redux.js.org).  
- Redux Toolkit docs (redux-toolkit.js.org).  
- RTK Query (for data fetching).  

---

*File generated for quick interview prep and code reference.*

# Redux Toolkit Cheat Sheet

**Topic** : ReactJS  
**Sub Topic** : Redux Toolkit — createSlice, createAsyncThunk, Immer, DevTools integration

---

## 1) Overview (short)
Redux Toolkit (RTK) is the officially recommended, batteries-included way to write Redux logic. It reduces boilerplate and provides helpers that follow best practices: `configureStore`, `createSlice`, `createAsyncThunk`, built-in integration with Immer for immutable updates, and easy DevTools integration.

Sources: Redux Toolkit docs (createSlice, createAsyncThunk, configureStore), Immer docs.

---

## 2) Detailed coverage

### `createSlice`
- Purpose: define a slice of state with its name, initial state, reducers (synchronous case reducers), and `extraReducers` to handle external actions (like async thunks).
- Returns: `{ actions, reducer, name, caseReducers }`.
- Reducers can **mutate** `state` directly (e.g., `state.count += 1`) because RTK uses Immer under the hood to produce immutable updates.
- Typical shape:
```js
import { createSlice } from '@reduxjs/toolkit'

const todosSlice = createSlice({
  name: 'todos',
  initialState: { items: [], status: 'idle', error: null },
  reducers: {
    addTodo(state, action) {
      state.items.push(action.payload)
    },
    toggleTodo(state, action) {
      const todo = state.items.find(t => t.id === action.payload)
      if (todo) todo.done = !todo.done
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchTodos.pending, (state) => { state.status = 'loading' })
      .addCase(fetchTodos.fulfilled, (state, action) => {
        state.status = 'succeeded'
        state.items = action.payload
      })
      .addCase(fetchTodos.rejected, (state, action) => {
        state.status = 'failed'
        state.error = action.error.message
      })
  }
})
export const { addTodo, toggleTodo } = todosSlice.actions
export default todosSlice.reducer
```

### `createAsyncThunk`
- Purpose: simplify async logic by creating thunk action creators that dispatch `pending`, `fulfilled`, and `rejected` lifecycle actions automatically.
- Signature: `createAsyncThunk(typePrefix, payloadCreator, options?)`
  - `payloadCreator` receives `(arg, thunkAPI)` where `thunkAPI` includes `dispatch`, `getState`, `signal` (for abort), `rejectWithValue`, etc.
- Error handling:
  - Throwing an exception or returning a rejected promise results in a `rejected` action. Use `rejectWithValue` to return a custom payload for `action.payload`.
  - Use `.unwrap()` on the returned dispatch promise to get the fulfilled value or throw the original error.
- Example:
```js
export const fetchTodos = createAsyncThunk(
  'todos/fetchTodos',
  async (_, thunkAPI) => {
    const res = await fetch('/api/todos')
    if (!res.ok) return thunkAPI.rejectWithValue({ status: res.status })
    const data = await res.json()
    return data
  }
)
```
- Handling in slice: see `extraReducers` example above.

### Immer integration
- RTK uses Immer so reducers can be written with "mutating" syntax while updates remain immutable.
- Immer creates a draft proxy, records mutations, and returns a new immutable state.
- Caveats:
  - You must not mutate values that are not part of the draft (e.g., external objects).
  - If state is a primitive (string/number), return a new value instead of mutating.
  - Avoid non-serializable operations in state (timers, DOM nodes) — RTK middleware warns by default.

### DevTools integration
- `configureStore` enables Redux DevTools by default (in development).
- Disable/configure via `devTools` option:
```js
const store = configureStore({
  reducer: rootReducer,
  devTools: process.env.NODE_ENV !== 'production'
})
```
- You can also pass DevTools options: `devTools: { trace: true, traceLimit: 25 }`.
- Make sure your browser has the Redux DevTools extension for best UX.

---

## 3) Best practices & gotchas
- Use RTK's `configureStore` — it wires up good defaults (redux-thunk, serializability check, immutable check, DevTools).
- Keep slices focused and colocate reducers + actions.
- Prefer `createAsyncThunk` for simple async flows; for complex caching/query needs, consider RTK Query.
- Use `rejectWithValue` to pass structured error data to `rejected` handlers.
- Be mindful with `extraReducers` when responding to many thunks — use `builder` callback form for type-safety and chaining.
- Don’t store non-serializable data in state; use middleware and checks to detect this.

---

## 4) Interview-style theory questions (concise answers)

1. **What does `createSlice` do?**  
   Defines a slice name, initial state, reducers, and generates action creators and a reducer function; allows direct-state mutation via Immer.

2. **How does `createAsyncThunk` simplify async logic?**  
   It auto-generates `pending/fulfilled/rejected` action types and thunk action creators, and standardizes error handling and cancellation support.

3. **Why does RTK allow mutable-looking reducers? Is state mutated?**  
   RTK uses Immer to record mutations on a draft and produce a new immutable state — actual immutable update occurs under the hood.

4. **How do you handle API errors in `createAsyncThunk`?**  
   Use `rejectWithValue` to return custom error payloads; check `action.error` and `action.payload` in `rejected` case reducers. Use `.unwrap()` to throw the original error when awaiting dispatch.

5. **How to enable/disable Redux DevTools in RTK?**  
   Use `devTools` option in `configureStore` (boolean or object for options). By default it's `true` in non-production.

6. **What's the difference between `reducers` and `extraReducers` in a slice?**  
   `reducers` defines action creators local to the slice. `extraReducers` handles actions defined elsewhere (thunks, other slices).

7. **When should you use RTK Query instead of `createAsyncThunk`?**  
   Use RTK Query for server cache, caching policies, automatic refetching, normalized responses — it's built for data fetching layers.

---

## 5) Practical/coding interview questions (with short answers or code hints)

1. **Implement a slice with a `fetchItems` async thunk and loading state.**  
   (Hint: use `createAsyncThunk` and `extraReducers` builder to set `loading`/`succeeded`/`failed` states.)

2. **How do you cancel an in-flight `createAsyncThunk` request?**  
   Use `thunkAPI.signal` with AbortController-aware fetch, or dispatch a separate action to manage cancellation manually.

3. **Show how to use `.unwrap()` with `createAsyncThunk`.**  
   ```js
   try {
     const result = await dispatch(fetchTodos()).unwrap()
     // result is the fulfilled payload or throws the error
   } catch (err) {
     // handle
   }
   ```

4. **Write a reducer that toggles a nested value using Immer-style mutation.**  
   ```js
   toggle(state, action) {
     const item = state.items.find(i => i.id === action.payload)
     if (item) item.active = !item.active
   }
   ```

5. **How to add Redux DevTools trace option in configureStore?**  
   ```js
   configureStore({
     reducer: rootReducer,
     devTools: { trace: true, traceLimit: 25 }
   })
   ```

---

## 6) Quick reference snippets

- `createSlice` boilerplate
- `createAsyncThunk` basic pattern
- `rejectWithValue` usage
- `configureStore` with devTools

(See code examples above.)

---

## 7) Sources & further reading
- Redux Toolkit docs: createSlice, createAsyncThunk, configureStore.  
- Immer docs.  
- Redux official docs on DevTools.

---

## 8) Footer
Generated for interview prep / cheat-sheet use. Keep it handy!


# React Query (TanStack Query) Cheat Sheet

**Topic** : ReactJS  
**Sub Topic** : React Query — Data fetching, caching, invalidation, staleTime, suspense mode

---

## 1) Overview (short)
TanStack Query (formerly React Query) is a powerful data-fetching library for React that provides declarative hooks for fetching, caching, synchronizing, and updating server state. It implements stale-while-revalidate caching, query deduplication, and convenient APIs for invalidation and background refetching.

---

## 2) Detailed coverage

### Core concepts
- **Queries**: Represent a piece of async data (useQuery / useInfiniteQuery). Identified by query keys.
- **Mutations**: write operations (useMutation) that can update server state and be paired with local cache updates / invalidation.
- **QueryClient**: central cache/controller with methods like `invalidateQueries`, `setQueryData`, `refetchQueries`.
- **StaleTime**: duration (ms) for which cached data is considered *fresh* (no background refetches).
- **CacheTime / garbage collection**: how long unused query data stays in memory before being garbage-collected.
- **Suspense mode**: opt-in integration with React Suspense to let React handle loading and error boundaries (experimental in some versions).

### useQuery basics
```js
import { useQuery } from '@tanstack/react-query'

const { data, error, isLoading, isFetching } = useQuery(
  ['todos', userId],
  () => fetch(`/api/users/${userId}/todos`).then(r => r.json()),
  { staleTime: 1000 * 60 } // 1 minute
)
```
- `data` returns cached data immediately if available.
- `isFetching` indicates background refetching.
- Queries are deduped: multiple components using same key share the same request.

### Caching: staleTime vs cacheTime
- **staleTime**: time after which data is considered stale and eligible for background refetch. Set to `Infinity` to never refetch automatically. Setting a non-zero `staleTime` avoids refetches while fresh.  
- **cacheTime** (garbage collection): time an unused query remains in cache before being removed. `cacheTime` starts when no active subscribers are using the query.

### Invalidation & updating cache
- `queryClient.invalidateQueries(queryKeyOrFilter)` marks matching queries as stale and will refetch active ones. Use it after mutations that change server data.
- `queryClient.setQueryData` / `setQueriesData` to optimistically update cache synchronously without refetch.
- `refetchQueries` forces refetching.

### Background refetching & retrying
- Queries refetch on window focus, network reconnect, and on mount if stale (configurable).
- Retry behavior can be customized per-query.

### Suspense mode
- When enabled, hooks will throw Promises for loading which are handled by `<React.Suspense>`; errors are thrown to be caught by error boundaries. Useful for coordinated loading UIs but experimental considerations exist in some releases.

---

## 3) Best practices & gotchas
- Prefer **query keys** that are stable and descriptive arrays like `['todos', { userId }]`.
- Use `staleTime` to control background refetch frequency (longer staleTime for rarely-changing data).
- Use optimistic updates with `setQueryData` when performing mutations, and rollback on error.
- Use `invalidateQueries` to refetch affected queries after mutations (fine-tune with filters).
- Be mindful of `cacheTime` to balance memory usage vs refetch cost.
- Avoid overusing `refetch`/`invalidate` on every action — batch or target keys when possible.
- Suspense is powerful but ensure your app's React version and library version support it for production.

---

## 4) Interview-style theory questions (concise answers)

1. **What is the difference between `staleTime` and `cacheTime`?**  
   `staleTime` controls how long data is fresh before background refetch; `cacheTime` controls how long unused data stays in memory before garbage collection.

2. **How does React Query deduplicate requests?**  
   It identifies queries by key and reuses an in-flight promise for identical active queries so only one network request runs.

3. **When should you use `invalidateQueries` vs `setQueryData`?**  
   Use `invalidateQueries` to mark cache stale and refetch from server. Use `setQueryData` for optimistic local updates when you already know the expected result.

4. **What does `useMutation` provide that `useQuery` doesn't?**  
   `useMutation` is for non-idempotent write operations. It provides mutation-specific lifecycle (onMutate, onSuccess, onError, onSettled) to coordinate optimistic updates and invalidation.

5. **Is Suspense recommended for production?**  
   Suspense for data fetching has been experimental historically; check the current TanStack Query docs and React support before relying on it in production.

---

## 5) Practical/coding interview questions (with hints)

1. **Implement a `useTodos` hook that caches todos per user and sets `staleTime` to 2 minutes.**  
   Hint: useQuery(['todos', userId], fetchFn, { staleTime: 120000 })

2. **Perform an optimistic update when adding a todo and rollback on error.**  
   Hint: useMutation with `onMutate` to update `queryClient.setQueryData`, return rollback context, and `onError` to restore.

3. **Invalidate all queries with prefix `['todos']` after a mutation.**  
   Hint: `queryClient.invalidateQueries({ predicate: query => query.queryKey[0] === 'todos' })` or use key filter.

4. **Enable Suspense for a query and show a fallback spinner.**  
   Hint: `<Suspense fallback={<Spinner/>}><MyComponent/></Suspense>` and useQuery(..., { suspense: true })

5. **Explain how to prevent refetch on window focus for a specific query.**  
   Hint: pass `refetchOnWindowFocus: false` in query options.

---

## 6) Quick reference snippets

- Invalidate:
```js
queryClient.invalidateQueries(['todos'])
```
- Optimistic update (simplified):
```js
const mutation = useMutation(addTodo, {
  onMutate: async newTodo => {
    await queryClient.cancelQueries(['todos', userId])
    const prev = queryClient.getQueryData(['todos', userId])
    queryClient.setQueryData(['todos', userId], old => [...old, newTodo])
    return { prev }
  },
  onError: (err, newTodo, context) => {
    queryClient.setQueryData(['todos', userId], context.prev)
  },
  onSettled: () => {
    queryClient.invalidateQueries(['todos', userId])
  }
})
```

---

## 7) Sources & further reading
- TanStack Query guides: caching examples, invalidation, suspense, QueryClient usage.
- React Query (legacy) GitHub & community articles.

---

## 8) Footer
Generated for interview prep / cheat-sheet use. Keep it handy!


# React Error Boundaries Cheat Sheet

**Topic**: ReactJS  
**Sub Topic**: Error Boundaries — why needed, how to create, fallback UIs

---

## 1) Overview
Error Boundaries are React components that catch JavaScript errors in the component tree during **render**, **lifecycle methods**, and **constructor**, preventing the entire UI from crashing. They render a fallback UI instead of letting the error propagate and break the whole app.

React added Error Boundaries in React 16 to provide crash resilience in UI components.

---

## 2) Why Error Boundaries Are Needed
- React components can throw errors inside render or lifecycle logic.
- Without boundaries, a single bad component can break the entire React app.
- Provide a **graceful fallback UI** instead of a blank screen.
- Prevents React from unmounting the whole UI tree.
- Helps with logging and debugging via custom error-handling logic (`componentDidCatch`).

---

## 3) How to Create an Error Boundary
Error Boundaries **must** be class components because they rely on lifecycle methods.

Minimal implementation:

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    console.error("Error caught by boundary:", error, info);
    // You can send logs to a tracking service here
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || <h2>Something went wrong.</h2>;
    }
    return this.props.children;
  }
}
```

Usage:

```jsx
<ErrorBoundary fallback={<ErrorFallback />}>
  <MainApp />
</ErrorBoundary>
```

---

## 4) Fallback UIs
Fallback UIs are components or messages shown when an error is caught.

Example:

```jsx
function ErrorFallback() {
  return (
    <div>
      <h2>Oops! Something broke.</h2>
      <button onClick={() => window.location.reload()}>Reload</button>
    </div>
  );
}
```

Fallback UI ideas:
- A friendly error message
- A retry button
- A log reporting option
- A minimal “something went wrong” page

---

## 5) What Error Boundaries **Do Not Catch**
Important limitations:
- Event handlers (wrap manually with try/catch)
- Asynchronous errors (setTimeout, promises)
- Server-side rendering
- Errors thrown inside Error Boundary itself

Example of handling event handler errors manually:

```jsx
function Button() {
  function handleClick() {
    try {
      riskyFunction();
    } catch (err) {
      console.error("Caught manually:", err);
    }
  }
  return <button onClick={handleClick}>Click</button>;
}
```

---

## 6) Hooks-based Error Capture (Not a Boundary)
Hooks like `useErrorBoundary` (from libraries like `react-error-boundary`) simulate boundary-like behavior but **React itself** still requires a class-based component for real Error Boundaries.

React’s own docs still state: “Error boundaries must be class components.”

Example (library-based):

```jsx
import { ErrorBoundary, useErrorBoundary } from "react-error-boundary";
```

---

## 7) Modern Pattern: react-error-boundary Library
This is a popular library that simplifies boundary creation and provides hooks:

```jsx
<ErrorBoundary
  FallbackComponent={ErrorFallback}
  onError={(error, info) => console.log(error, info)}
>
  <App />
</ErrorBoundary>
```

Offers:
- Hooks (`useErrorBoundary`)
- Reset capability for retriable errors
- Cleaner syntax than class components

---

## 8) Interview Questions (with concise answers)

1. **Why do we need Error Boundaries?**  
   To prevent UI crashes by catching errors in render/lifecycle methods and showing fallback UIs.

2. **Where can Error Boundaries catch errors?**  
   In rendering, lifecycle methods, and constructors of child components.

3. **What errors are NOT caught by Error Boundaries?**  
   Event handlers, async code, SSR errors, boundary’s own errors.

4. **Why must Error Boundaries be class components?**  
   Because React hooks do not offer equivalents for `componentDidCatch` or `getDerivedStateFromError`.

5. **How do you log errors inside an Error Boundary?**  
   Use `componentDidCatch(error, info)` to send logs to monitoring services.

6. **Difference between fallback UI and boundary logic?**  
   The boundary detects + catches errors; the fallback UI displays a safe alternative view.

7. **How do Suspense and Error Boundaries interact?**  
   Suspense handles loading states; Error Boundaries handle error states. They’re complementary.

---

## 9) Practical Coding Tasks

1. **Create a boundary that supports reset on button click.**  
   Hint: store a key in state and re-render children with a new key.

2. **Wrap only unstable components rather than the whole app.**  
   Hint: boundaries can be nested anywhere in the tree.

3. **Log errors to Sentry or a custom API.**  
   Hint: call tracking service inside `componentDidCatch`.

4. **Create a reusable fallback UI component.**  
   Hint: pass fallback via props to the boundary.

---

## 10) Quick Reference Snippet

```jsx
<ErrorBoundary fallback={<h1>Something broke.</h1>}>
  <MyComponent />
</ErrorBoundary>
```

---

## 11) Footer
Use Error Boundaries to keep your React apps resilient and user-friendly.


# ReactJS Testing Cheat Sheet

## Topic: ReactJS Testing  
### Sub Topic: React Testing Library, Mocking Hooks, Snapshot Testing

## React Testing Library (RTL)
React Testing Library focuses on testing UI the way users interact with it. It avoids testing implementation details and emphasizes accessibility-based queries like getByRole, getByText, and getByLabelText.

### Core Principles
- Test components through user behavior and accessible selectors.
- Avoid testing internals like state or component methods.
- Use screen for consistent query access.
- Prefer findBy for async queries.

### Common Queries
- getByRole()
- getByText()
- getByLabelText()
- findByRole() (async)
- queryByRole() (non-throwing)

### Example
```javascript
render(<Login />);
fireEvent.change(screen.getByLabelText(/email/i), { target: { value: "a@b.com" }});
expect(screen.getByRole('button')).toBeEnabled();
```

## Mocking Hooks

### Jest Mock Usage
```javascript
jest.mock("../useAuth", () => ({
  useAuth: () => ({ user: { name: "Harshith" }})
}));
```

### Mocking React Router Hooks
```javascript
jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useNavigate: () => jest.fn(),
}));
```

## Snapshot Testing

### How to use
```javascript
import renderer from 'react-test-renderer';

it("matches snapshot", () => {
  const tree = renderer.create(<Button />).toJSON();
  expect(tree).toMatchSnapshot();
});
```

## Theory Questions for Interviews

1. **What is React Testing Library?**  
   A user-focused testing library built around DOM interactions rather than implementation details.

2. **Why avoid testing component internals?**  
   Internal details change often; behavior is what matters.

3. **Difference between getBy, queryBy, and findBy?**  
   getBy throws, queryBy doesn't, findBy is async.

4. **What is mocking?**  
   Replacing real dependencies with controlled versions during a test.

5. **Why mock hooks?**  
   To isolate components from external state or async logic.

6. **What are snapshots?**  
   Serialized component trees stored to detect UI regressions.

7. **When to avoid snapshot testing?**  
   Dynamic or large UI components produce noisy diffs.

8. **What is act()?**  
   Ensures state updates flush before assertions.

## Coding Questions

### 1. Button increments on click
```javascript
test("increments on click", () => {
  render(<Counter />);
  fireEvent.click(screen.getByRole("button", { name: /add/i }));
  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
```

### 2. Mock API hook and test
```javascript
jest.mock("../useUsers", () => ({
  useUsers: () => ({ data: [{ id: 1, name: "John" }] })
}));

test("renders user", () => {
  render(<Users />);
  expect(screen.getByText("John")).toBeInTheDocument();
});
```

### 3. Snapshot test example
```javascript
it("matches header snapshot", () => {
  const tree = renderer.create(<Header title="Hi" />).toJSON();
  expect(tree).toMatchSnapshot();
});
```

# ReactJS Rendering Optimization Cheat Sheet

## Topic: ReactJS
### Sub Topic: Rendering Optimization — avoiding re-renders, key prop strategy, profiling

---

## 1. Core concepts (short)
- **Why re-renders happen**: state changes, parent re-renders, context updates, and hook changes cause React components to re-render.  
- **Render vs Commit**: React renders the virtual tree, then reconciles and commits DOM updates — profiling helps find costly commit work.  

---

## 2. Strategies to avoid unnecessary re-renders
1. **Lift state minimally**  
   Keep state local when possible. Lifting state up unnecessarily causes many descendants to re-render.  

2. **Split components (single responsibility)**  
   Break big components into smaller ones so updates affect only a small subtree.

3. **React.memo for pure functional components**  
   Wrap components with `React.memo` to shallow-compare props and skip renders when props are stable.

4. **Stabilize callbacks and values**  
   Use `useCallback` for functions and `useMemo` for expensive derived values **only when** re-render avoidance gains outweigh memoization costs.

5. **Avoid creating new object/array literals in render**  
   `const list = []` or `{}` inline will create new references each render — pass stable references or memoize.

6. **Reselect / memoize selectors for derived state**  
   For global state (Redux, Zustand), use memoized selectors (e.g., `reselect`) so map/selectors don't force children to re-render.

7. **Limit context usage**  
   Context updates re-render all consumers — scope contexts narrowly or split them.

8. **Batched updates and avoiding synchronous state churn**  
   Use functional state updates and let React batch related updates.

---

## 3. Key prop strategy (lists)
- **Always prefer a stable, unique ID from data** (not array index) as `key`. Keys allow React to match elements across renders. citeturn0search0turn0search5  
- **When index is acceptable**: use index only for static lists that never reorder or insert/delete items (e.g., a static menu). Otherwise it causes UI re-use bugs and unnecessary DOM changes. citeturn0search9  
- **Avoid random keys** (like `Math.random()`): they defeat reconciliation because keys change every render. citeturn0search5

---

## 4. Memoization: useMemo, useCallback, React.memo
- **Use `React.memo`** to avoid re-rendering pure functional children when props are shallow-equal.  
- **Use `useCallback`** to keep function references stable when passed to memoized children. **But** don't overuse — memo hooks have runtime cost; only apply after profiling shows benefit. citeturn0search11turn0search3  
- **Use `useMemo`** for expensive computations that you don't want to recompute every render. Again, measure first. citeturn0search11

---

## 5. Profiling and measuring
- **React DevTools Profiler**: record interactions, inspect commit durations, and see "why did this render" when enabled. Use flamegraphs and ranked charts to find hotspots. citeturn0search2turn0search14  
- **Browser DevTools Performance**: use CPU flame charts to identify scripting and layout costs across the whole page. citeturn0search6  
- **Measure before optimizing**: premature optimization wastes time — profile, identify the costly render, then apply targeted fixes. citeturn0search6turn0search11

---

## 6. Small checklist to reduce re-renders (quick)
- Use `key` = stable ID.  
- Avoid passing inline functions/objects to memoized children.  
- Split context and state to smallest useful granularity.  
- Wrap expensive lists with virtualization (react-window/react-virtualized) for very long lists.  
- Memoize selectors in state libraries.  
- Run Profiler → Fix → Re-profile.

---

## 7. Interview-style theory questions (concise answers)

1. **Q:** What causes a component to re-render?  
   **A:** State changes, parent re-render, context changes, and hook dependency changes.

2. **Q:** When should you use `React.memo`?  
   **A:** When a component renders often with identical props and its render cost is non-trivial.

3. **Q:** Why is using array index as key often a bad idea?  
   **A:** Index breaks stable identity on insert/delete/reorder, causing wrong DOM reuse and extra updates.

4. **Q:** When should you use `useMemo`/`useCallback`?  
   **A:** Only after profiling shows repeated expensive work or unstable references causing child re-renders.

5. **Q:** How do you find why a component rendered?  
   **A:** Enable "Record why each component rendered" in React DevTools Profiler and inspect the commit.

6. **Q:** What's the difference between render and commit?  
   **A:** Render builds the virtual DOM; commit applies changes to the real DOM (layout, paint).

7. **Q:** How does context impact re-renders?  
   **A:** Any provider value change triggers re-render for all consumers; split context to limit scope.

---

## 8. Coding / practical questions

1. **Wrap a slow child with React.memo**
```javascript
const SlowChild = React.memo(function SlowChild({items}) {
  // expensive rendering logic
  return <ul>{items.map(i => <li key={i.id}>{i.text}</li>)}</ul>;
});
```

2. **Stabilize callback to avoid child re-renders**
```javascript
function Parent({onSave}) {
  const handleClick = useCallback(() => {
    // stable reference across renders unless deps change
    onSave();
  }, [onSave]);

  return <Child onClick={handleClick} />;
}
```

3. **Avoid inline object prop**
```javascript
// bad
<Component options={{a:1,b:2}} />

// better
const options = useMemo(() => ({a:1,b:2}), []);
<Component options={options} />
```

4. **Use Profiler to measure (example)**
```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration) {
  console.log({id, phase, actualDuration});
}

<Profiler id="List" onRender={onRenderCallback}>
  <List items={items} />
</Profiler>
```

---

## 9. Advanced tips
- **Virtualize long lists** (react-window/react-virtualized) to render only visible rows.  
- **Use Immutable data patterns** so shallow equality checks are meaningful.  
- **Consider web workers for heavy computation** to keep main thread responsive.  
- **Server-side rendering / streaming** reduces time-to-first-byte – but client rendering still needs profiling.

---

## References
- React docs — Lists and Keys; Rendering lists.  
- React DevTools Profiler docs.  
- Multiple practical guides and blog posts on useMemo/useCallback and profiling.

---

*Prepared for interview-focused study and quick reference.*  

# ReactJS React 18 Features Cheat Sheet

## Topic: ReactJS  
### Sub Topic: React 18 Features — automatic batching, transitions, concurrent rendering, startTransition

---

## 1. Overview  
React 18 introduced a new concurrent rendering engine and several features that improve performance, responsiveness, and scheduling. The key idea is that rendering is no longer strictly synchronous — React can pause, resume, skip, or interrupt renders to keep the UI responsive.

---

## 2. Automatic Batching  
Batching means React groups multiple state updates into one render for performance.

### Before React 18  
Batching happened only inside React event handlers.

### After React 18  
All updates — including inside promises, setTimeout, fetch callbacks — are automatically batched.

Example:
```javascript
setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
});
// Only one render happens instead of two.
```

Why it matters:
- Fewer renders.
- More predictable performance.
- No need for `unstable_batchedUpdates`.

---

## 3. Transitions  
Transitions let you classify some state updates as “non-urgent.”  
Urgent updates: typing, clicking, dragging — must update immediately.  
Transition updates: expensive UI updates like filtering, pagination, route changes.

### Benefits
- UI stays responsive.
- React can interrupt or deprioritize transitions.

---

## 4. `startTransition`  
Used to mark an update as non-urgent.

Example:
```javascript
function onSearch(value) {
  setInputValue(value);  // urgent
  startTransition(() => {
    setFilteredItems(expensiveFilter(value)); // non-urgent
  });
}
```

Behavior:
- The input updates immediately.
- The filtering work may be delayed to avoid blocking user input.

---

## 5. `useTransition` hook  
Provides a boolean `isPending` to show a loading indicator during transitions.

```javascript
const [isPending, startTransition] = useTransition();

startTransition(() => {
  setList(filterData(value));
});
```

You can show:
```jsx
{isPending && <Spinner />}
```

---

## 6. Concurrent Rendering  
Concurrent rendering allows React to interrupt long renders to keep the UI responsive.

### Properties
- Work is interruptible.
- Rendering is not tied to synchronous blocking.
- React can prepare UI in the background.
- Only the final committed version updates the DOM.

This engine powers:
- Suspense improvements
- Streaming server rendering
- Transitions
- Better hydration

---

## 7. Example: Without vs With Transition

**Without transition**
```javascript
setSearchTerm(term);
setFilteredItems(expensiveFilter(term));  // blocks UI
```

**With transition**
```javascript
setSearchTerm(term);
startTransition(() => {
  setFilteredItems(expensiveFilter(term));
});
```

Now typing stays smooth even if filtering is expensive.

---

## 8. Key Interview Theory Questions (Concise)

1. **What is concurrent rendering?**  
   A rendering model where React can pause, resume, or abandon a render to prioritize urgent updates.

2. **Why is automatic batching important?**  
   It reduces unnecessary renders and improves performance across async boundaries.

3. **What problem do transitions solve?**  
   They prevent heavy UI updates from blocking urgent interactions.

4. **Difference between urgent updates and transitions?**  
   Urgent updates reflect direct user actions; transitions are deprioritized background updates.

5. **What does `startTransition` do?**  
   Marks updates as non-urgent so React can delay or interrupt them.

6. **Does concurrent rendering change UI behavior?**  
   No — it changes *when* React renders, not *what* it renders.

7. **What happens if a transition is interrupted?**  
   React drops the intermediate work and starts a new transition with the latest data.

8. **When should you not use transitions?**  
   For user-input-driven updates (typing, dragging); they must stay synchronous.

---

## 9. Coding Practice Questions

### 1. Implement a search box using `startTransition`
```javascript
const [query, setQuery] = useState("");
const [results, setResults] = useState([]);

function handleChange(e) {
  const value = e.target.value;
  setQuery(value);

  startTransition(() => {
    setResults(heavySearch(value));
  });
}
```

### 2. Add a loading spinner using `useTransition`
```javascript
const [isPending, startTransition] = useTransition();

function filterList() {
  startTransition(() => {
    setList(expensiveFilter(data));
  });
}

return (
  <>
    {isPending && <Loading />}
    <List items={list} />
  </>
);
```

### 3. Example showing automatic batching
```javascript
setTimeout(() => {
  setA(a + 1);
  setB(b + 1);
});
// Only one render happens.
```

---

## 10. Summary  
React 18’s features are all about responsiveness:
- Automatic batching → fewer renders.
- Transitions → keep UI fluid.
- Concurrent rendering → smarter scheduling.
- startTransition/useTransition → explicit control over priority.

These tools help build large, responsive, user-friendly interfaces.

---

# ReactJS — Concurrent Mode Cheat Sheet

**Topic:** ReactJS  
**Sub Topic:** Concurrent Mode (interruptible rendering, `useDeferredValue`, `startTransition`, `Suspense`)

---

## Quick summary
Concurrent Mode (available by default in React 18's concurrent rendering model) makes rendering interruptible and priority-aware so React can keep the UI responsive during heavy work. It powers features such as transitions, `useDeferredValue`, `useTransition`, automatic batching, and improved `Suspense` behavior.

---

## How it works (short)
- React schedules rendering work with priorities instead of doing one long blocking render.  
- If a higher-priority event occurs (e.g., user input), React can pause the current render, handle the event, then resume the previous render.  
- This is often called *time-slicing* or *cooperative multitasking* under the hood.

---

## Key APIs / Concepts

### `createRoot`
Use `createRoot` from `react-dom/client` to opt in to the concurrent renderer:
```js
import { createRoot } from 'react-dom/client';
const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

### Transitions: `startTransition` and `useTransition`
Mark non-urgent updates (like navigation, list filtering) as transitions so they receive lower priority and won’t block urgent updates (like typing).
```js
import { startTransition } from 'react';

function onFilterChange(e) {
  const next = e.target.value;
  startTransition(() => {
    setFilter(next);
  });
}
```
`useTransition` returns `[isPending, startTransition]` to show pending UI states.

### `useDeferredValue`
Defers a value to let more urgent updates finish first. Useful for keeping typing responsive while a heavy list re-renders.
```js
const deferredQuery = useDeferredValue(query);
```
Render the expensive list against `deferredQuery` while showing immediate UI for `query`.

### `Suspense` (for code + data)
`<Suspense fallback={<Spinner/>}>` shows a fallback when child components suspend (e.g., data not ready or code-splitting). In concurrent mode, Suspense plus transitions prevents janky loading states by keeping previously-visible UI until new content is ready.

### Automatic batching
React groups multiple state updates into a single render for better performance (expanded in React 18+ to cover more event types and async boundaries).

---

## Best practices
- Use `startTransition` for non-urgent updates (filtering, navigation).
- Use `useDeferredValue` when you want to keep an immediate UI (e.g., text input) but delay expensive dependent renders.
- Wrap data-dependent components with `Suspense` to simplify loading states.
- Avoid overusing transitions; only mark genuinely non-urgent updates.
- Prefer progressive rendering: show skeletons/placeholders, not blank screens.

---

## Common pitfalls
- Expecting `useDeferredValue` to debounce; it defers but does not guarantee strict timing semantics.
- Over-marking everything as transition hides perceived responsiveness and can lead to confusing UX.
- Forgetting to memoize heavy lists when using deferred values (so that unnecessary re-renders don't happen).

---

## Interview Theory Questions (concise answers)

1. **What is React's Concurrent Mode?**  
   A rendering model introduced in React 18 that makes rendering interruptible and priority-based so the UI remains responsive during heavy work.

2. **How does `startTransition` differ from `setState`?**  
   `startTransition` marks updates as low-priority (transitions) so high-priority updates (like user inputs) are handled first; `setState` alone enqueues an update with normal priority.

3. **When would you use `useDeferredValue` vs `useTransition`?**  
   Use `useDeferredValue` when you want to derive a deferred value from state (e.g., filtering a large list). Use `useTransition`/`startTransition` to wrap state updates that you want to mark as low-priority.

4. **What is Suspense for data fetching?**  
   A declarative pattern that lets components “suspend” while waiting for data; Suspense boundaries show fallbacks until data is ready and work seamlessly with concurrent rendering.

5. **What is time-slicing?**  
   Breaking rendering work into small units that can be paused and resumed so React can interleave higher-priority tasks.

---

## Short coding interview questions (practical)

1. **Implement a responsive search input that filters a large list without blocking typing.**
```js
function SearchableList({items}) {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);

  const filtered = useMemo(() => {
    return items.filter(it => it.includes(deferredQuery));
  }, [items, deferredQuery]);

  return (
    <>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      <ul>
        {filtered.map(i => <li key={i}>{i}</li>)}
      </ul>
    </>
  );
}
```

2. **Use `startTransition` to mark a heavy update as low priority.**
```js
function App() {
  const [filter, setFilter] = useState('');
  const [isPending, startTransition] = useTransition();

  function onChange(e) {
    const next = e.target.value;
    startTransition(() => setFilter(next));
  }

  return (
    <>
      <input onChange={onChange} />
      {isPending ? <div>Updating…</div> : <List filter={filter} />}
    </>
  );
}
```

3. **Wrap data-fetching component with Suspense (example using React experimental data fetching libraries).**
```js
<Suspense fallback={<div>Loading...</div>}>
  <Profile id={userId} />
</Suspense>
```

---

## Further reading
- Official React docs: hooks and Suspense (react.dev)
- React 18 blog post (reactjs.org/blog)
- Migration guides and performance patterns

---

## File
This document is a compact reference and interview prep sheet for React Concurrent Mode.

# Topic: ReactJS
## Sub Topic: React 19 (Preview) — `useOptimistic`, Actions API, and Form Handling Changes

---

## Overview
React 19 introduces several new primitives focused on better async workflows, optimistic UI updates, and simpler form handling. The key pieces covered here are:
- `useOptimistic` — a hook for optimistic updates and local pending state.
- Actions API — a new pattern for colocated async "actions" (server/client) with pending/error state.
- Form handling changes — new helpers like `useFormState` / `useFormStatus` and tighter integration with Actions to simplify submission, validation, and status handling.

---

## `useOptimistic` — what it is and how to use it
`useOptimistic` is a React hook that lets you present an *optimistic view* of state while an asynchronous action is pending. Instead of waiting for a network response to update the UI, you apply a predicted update immediately and automatically revert if the action fails.

Basic pattern:

```jsx
import { useOptimistic } from 'react';

function LikeButton({ initial }) {
  const [likes, addOptimistic] = useOptimistic(initial, (state, delta) => state + delta);

  async function handleLike() {
    // Trigger optimistic update
    addOptimistic(1);

    // Perform the real action (e.g. server call via an Action)
    try {
      await sendLikeToServer();
    } catch (err) {
      // on error, React will revert optimistic state automatically if using Actions
      console.error(err);
    }
  }

  return <button onClick={handleLike}>Likes: {likes}</button>;
}
```

Tips:
- Keep optimistic update logic simple and deterministic (pure functions).
- Use optimistic updates for small, local changes (likes, toggles, list inserts).
- Combine with Actions for automatic pending/error integration.

---

## Actions API — colocated async work with lifecycle
Actions are a core React 19 concept for colocating async logic near the component that triggers it. An Action is an async function that can be invoked from UI (or forms) and provides:
- a **pending** state for the duration of the action,
- **error** handling integrated with Error Boundaries,
- easy use with optimistic updates, and
- simpler form submission patterns.

Example (sketch):

```jsx
// server/actions.js (or colocated)
export async function addComment(data) {
  // server-side logic: validate, persist, return new state
  return await fetch('/api/comments', { method: 'POST', body: JSON.stringify(data) });
}

// client component
import { useActionState } from 'react';
import { addComment } from './server/actions';

function CommentForm() {
  const action = useActionState(addComment);

  async function onSubmit(formData) {
    await action(formData);
    // action exposes pending and error states via hooks like useActionState/useFormStatus
  }

  return (
    <form onSubmit={onSubmit}>
      {/* form fields */}
      <button disabled={action.pending}>Submit</button>
    </form>
  );
}
```

---

## Form handling changes
React 19 reduces boilerplate around forms by providing:
- `useFormState` / `useFormStatus` hooks to read form-level status (dirty, submitting, pending).
- Built-in integration between `<form>` elements and Actions so you can submit forms directly to an Action without manual fetch/cancel logic.
- Better error propagation: failed Actions can show Error Boundary UIs and the runtime can revert optimistic updates.

Pattern:

```jsx
function MyForm() {
  const action = useActionState(myAction); // wraps Action
  const status = useFormStatus(); // read form pending / errors

  return (
    <form action={myAction}>
      {/* inputs with name attributes to be serialized */}
      <button disabled={status.submitting}>Save</button>
      {status.error && <div role="alert">{status.error.message}</div>}
    </form>
  );
}
```

---

## Migration & compatibility notes
- React 18.3 was released as a transitional step to warn about deprecations before React 19; follow upgrade guides and run codemods if provided.
- Not all code needs Actions — you can incrementally adopt Actions and `useOptimistic`.
- Server/client boundary: Actions may run server-side in server components or be proxied to the server; pay attention to environment-specific APIs.

---

## Interview-style theory questions (concise answers)

**Q1: What problem does `useOptimistic` solve?**  
A: It improves perceived responsiveness by applying a predicted state update immediately while an async action runs, reverting automatically on failure.

**Q2: How do Actions differ from traditional fetch/async handlers in components?**  
A: Actions are colocated async functions with built-in pending/error lifecycle, integrated with React’s runtime, and can be wired directly into forms and optimistic updates — reducing boilerplate and making error/pending handling declarative.

**Q3: When should you *not* use optimistic updates?**  
A: Avoid optimistic updates for non-deterministic operations, large transactional flows, or when server validation can drastically alter the final state — use pessimistic updates instead.

**Q4: How do Error Boundaries interact with Actions?**  
A: Actions expose errors to React’s error handling model so a thrown error during an Action can be caught by Error Boundaries to show fallback UI and revert optimistic changes.

**Q5: What are the risks of using Actions with server-side code?**  
A: Actions that run on the server must avoid accessing client-only APIs (e.g., window, localStorage) and must handle authentication/CSRF carefully. Also ensure serialization boundaries are respected.

---

## Concise coding interview prompts (exercise-style)

1. **Implement a `LikeButton` with `useOptimistic` and an Action `sendLike`**  
   - Requirements: show immediate increment, disable button while pending, revert if action fails, show inline error message.

2. **Build a `TodoList` that supports optimistic add and delete using `useOptimistic` and Actions**  
   - Requirements: local optimistic changes, pending indicator per item, and error recovery.

3. **Create a form using the new `form` + Action pattern**  
   - Requirements: use `action={myAction}` on `<form>`, display `useFormStatus()` info, and validate on server returning field errors.

4. **Edge-case task:** Convert an existing component that uses `fetch` + `useState` for submissions into Actions + `useOptimistic`, and describe migration steps.

---

## Resources & further reading
- Official React 19 release post and overview on react.dev.
- `useOptimistic` reference in the React docs.
- React 19 upgrade guide and changelog on react.dev.
- Community writeups and tutorials (freeCodeCamp, Vercel blog, Dev.to).

---

## Short changelog summary
- New hooks: `useOptimistic`, `useActionState`, `useFormStatus`, `useAction` patterns.
- Actions API for colocated async work with pending/error lifecycle.
- Simplified form handling with `<form action={...}>` integration.

---

# Topic: ReactJS
## Sub Topic: Portals — Rendering Outside DOM Tree, Modals, Tooltips

---

## What Are Portals?

React Portals let you render a component’s output into a DOM node **outside** its parent DOM hierarchy while keeping it logically inside the React component tree.

```jsx
import { createPortal } from "react-dom";

function PortalExample() {
  return createPortal(
    <div>This is rendered elsewhere in the DOM</div>,
    document.getElementById("portal-root")
  );
}
```

Portals solve layout issues caused by `overflow`, stacking contexts, and deeply nested DOM structures.

---

## Why Use Portals?

- Render modals above all UI layers  
- Escape clipping (`overflow: hidden`) for tooltips and dropdowns  
- Display floating UI like toasts, context menus, and popovers  
- Prevent parent CSS from interfering with overlay components  

---

## Key Behaviors

**1. Event Bubbling Works Normally**  
Even though the DOM node moves, events bubble through the *React tree* — not the DOM tree.

**2. DOM Container Is Separate**  
React renders into the specified DOM node (`portal-root`, `modal-root`, etc.).

**3. Useful for Breaking Layout Constraints**  
Great for components requiring absolute positioning or high z-index.

---

## Example: Modal Using a Portal

```jsx
import { createPortal } from "react-dom";

function Modal({ open, onClose, children }) {
  if (!open) return null;

  return createPortal(
    <div className="overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        {children}
        <button onClick={onClose}>Close</button>
      </div>
    </div>,
    document.getElementById("modal-root")
  );
}
```

---

## Example: Tooltip Using a Portal

```jsx
function Tooltip({ targetRef, text, visible }) {
  const [pos, setPos] = useState({ top: 0, left: 0 });

  useEffect(() => {
    if (visible && targetRef.current) {
      const rect = targetRef.current.getBoundingClientRect();
      setPos({
        top: rect.bottom + window.scrollY + 8,
        left: rect.left + window.scrollX + rect.width / 2
      });
    }
  }, [visible]);

  if (!visible) return null;

  return createPortal(
    <div className="tooltip" style={{ position: "absolute", ...pos }}>
      {text}
    </div>,
    document.getElementById("tooltip-root")
  );
}
```

---

## Interview Theory Questions (Concise)

**Q1: What is a portal in React?**  
A portal is a way to render a child component into a different DOM node outside its parent DOM hierarchy.

**Q2: Do portal components keep React context?**  
Yes, context flows from the original component tree, not the DOM tree.

**Q3: Why are portals used for modals and tooltips?**  
They escape layout issues like clipping and stacking contexts.

**Q4: Do portal events bubble normally?**  
Yes — events bubble through the React tree, not the DOM hierarchy.

**Q5: What problems can portals cause?**  
Accessibility issues, misplaced container nodes, and managing focus/scroll.

---

## Coding Exercise Prompts

1. Build a Modal using a portal with focus trapping and ESC‑to‑close support.  
2. Create a Dropdown that renders inside a portal when open and positions itself relative to its trigger.  
3. Implement a Toast Manager using portals that queues multiple toast notifications.  
4. Build a PortalManager that dynamically mounts portals for different UI layers.

---

# Topic : ReactJS
## Sub Topic : React Router — DOM vs Data Router, Nested Routes, loader, useParams, useNavigate

---

## 1) Overview (short)
React Router is the standard routing library for React apps. There are two commonly discussed "modes" or packages for web apps:

- **react-router-dom (DOM)** — the web-specific binding that provides BrowserRouter, Link, NavLink, etc. Use this for traditional client-side routing inside the browser.
- **Data Router / react-router (Data Mode)** — route configuration is moved outside render; routes can define `loader`, `action`, and other data-aware primitives to perform data loading, form actions, optimistic UI, pending states, and server-friendly behaviors. Data routers are used with `createBrowserRouter` + `RouterProvider`.

(For authoritative details see the React Router docs.)

---

## 2) DOM Router vs Data Router — when to use which
- **DOM Router (react-router-dom)**:
  - Simpler: declare `<BrowserRouter>` (or `<HashRouter>`) and use `<Routes>/<Route>` nested under React component tree.
  - Use when you control data fetching in components (e.g., fetch in `useEffect`) and want straightforward client-side routing.

- **Data Router (createBrowserRouter + RouterProvider)**:
  - Best when you want route-level data fetching and form handling baked into the routing layer via `loader`, `action`, `defer` and `useFetcher`.
  - Loaders run before route renders, and loader data is injected into route components automatically.
  - Encourages moving side-effects out of rendering and into route definitions, improving SSR/streaming support and giving explicit pending/transition mechanics. citeturn0search3turn0search2

---

## 3) Nested routes (concept + example)
- Nested routes allow parent route components to render layout and child route components via `<Outlet />`.
- Child route paths are appended to parent path automatically.

Example (DOM-style route tree):

```jsx
// App.jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./Dashboard";
import Home from "./Home";
import Settings from "./Settings";

function App(){
  return (
    <BrowserRouter>
      <Routes>
        <Route path="dashboard" element={<Dashboard />}>
          <Route index element={<Home />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
```

Inside `Dashboard`:

```jsx
import { Outlet } from "react-router-dom";
export default function Dashboard(){
  return (
    <div>
      <h1>Dashboard</h1>
      <Outlet /> {/* renders Home or Settings based on nested route */}
    </div>
  );
}
```

Nested routes are documented in the official routing guide. citeturn0search1

---

## 4) `loader` (what it is, how it works, patterns)
- A `loader` is a function you attach to a route (Data Router) that runs before the route renders and returns the data the route needs.
- Loaders can return primitives, objects, promises, or throw `Response` for redirects/errors. Loader data is accessible in components via `useLoaderData()` hook.
- Use loaders to centralize data fetching at the route level and to enable better SSR and pending state UX. They only work with Data Routers (createBrowserRouter / RouterProvider). citeturn0search11turn0search2

Example:

```js
// routes.js
import { createBrowserRouter } from "react-router";
import Root from "./Root";
import Users, { loader as usersLoader } from "./Users";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    children: [
      { path: "users", element: <Users />, loader: usersLoader }
    ]
  }
]);

export default router;

// Users.jsx
import { useLoaderData } from "react-router";
export default function Users(){
  const users = useLoaderData();
  return <UserList users={users} />;
}

// usersLoader.js
export async function loader(){
  const res = await fetch("/api/users");
  if (!res.ok) throw new Response("Failed", { status: 500 });
  return res.json();
}
```

---

## 5) `useParams` (simple)
- `useParams()` returns the route parameters object for the current matched route (e.g., `{ id: '123' }` for `/items/:id`).
- Use it inside components rendered by routes to read dynamic segments. Keep in mind types when using TypeScript. citeturn0search1

Example:

```jsx
import { useParams } from "react-router-dom";
export default function ItemDetail(){
  const { id } = useParams();
  // fetch or use loader data for the given id
}
```

---

## 6) `useNavigate` (programmatic navigation)
- `useNavigate()` returns a `navigate` function for imperative navigation: `navigate("/path")`, `navigate(-1)` to go back, and options like `{ replace: true }`.
- In Data Router scenarios it's often preferable to `redirect` from loaders/actions rather than navigate in side effects. citeturn0search4turn0search10

Example:

```jsx
import { useNavigate } from "react-router-dom";
export default function SaveButton(){
  const navigate = useNavigate();
  async function onSave() {
    await saveSomething();
    navigate("/saved", { replace: true });
  }
  return <button onClick={onSave}>Save</button>;
}
```

---

## 7) Best practices & gotchas
- Prefer route `loader` for data your route always needs; use `useFetcher` or client-side hooks for optional/interactive fetches.
- Use `<Outlet/>` and layout routes for DRY UI.
- When migrating from classic DOM setup to Data Router, move fetches into `loader`s and use `RouterProvider`.
- Don’t call `useParams()` outside of components rendered by a `Route`.
- For navigation after form submission, prefer `action` + redirect in Data Router for clearer intent and server-like behavior. citeturn0search2turn0search3

---

## 8) Interview theory questions (concise answers)

1. **Q:** What's the difference between `react-router` and `react-router-dom`?  
   **A:** `react-router` is the core routing logic; `react-router-dom` is the web-specific binding that exports browser components (`BrowserRouter`, `Link`, etc.). In newer versions the packages are more unified but the DOM package remains the web entrypoint. citeturn0search5turn0search9

2. **Q:** What is a Data Router?  
   **A:** A router configuration style (createBrowserRouter + RouterProvider) that supports route-level `loader`, `action`, deferred data, and explicit pending states—moving data concerns into route definitions. citeturn0search3

3. **Q:** When should you use `loader` vs `useEffect`?  
   **A:** Use `loader` for data the route must have before rendering (centralized, SSR-friendly). Use `useEffect` for client-only, optional, or on-interaction fetches.

4. **Q:** How do nested routes render multiple components on the same page?  
   **A:** Parent route renders layout and includes `<Outlet/>` where the child route element is rendered; the path hierarchy is combined automatically. citeturn0search1

5. **Q:** How does `useNavigate` differ from `<Link>`?  
   **A:** `<Link>` is declarative navigation in JSX. `useNavigate` is imperative (e.g., navigate from handlers/effects) and accepts history deltas or path + options. citeturn0search4

---

## 9) Coding-based interview questions (practical)

1. **Task:** Build a nested route layout for a blog with `posts`, `posts/:id`, and `posts/:id/edit` where `posts/:id` uses a loader that fetches the post.  
   **Hint:** Use a parent `PostsLayout` components with `<Outlet/>`, attach `loader` to the `posts/:id` route, call `useLoaderData()` in detail view.

2. **Task:** Implement optimistic navigation after creating a new item using Data Router actions.  
   **Hint:** Use `action` to handle the form submission, return a redirect, and use `useNavigation()` to show pending state.

3. **Task:** Create a protected route that reads an auth token in a `loader` and redirects to `/login` if unauthenticated.  
   **Hint:** Throw a `redirect("/login")` from the loader or return a `Response` with redirect status.

4. **Task:** Migrate component-level `useEffect` fetches into `loader`s — what changes?  
   **Hint:** Move fetch to loader, replace `useEffect` data state with `useLoaderData()`, handle errors via `errorElement` on the route.

---

## 10) Quick code snippets (cheat-sheet)

- Data Router bootstrap:

```js
import { createBrowserRouter, RouterProvider } from "react-router";
import routes from "./routes";

const router = createBrowserRouter(routes);

ReactDOM.createRoot(root).render(
  <RouterProvider router={router} />
);
```

- Access loader data:

```jsx
import { useLoaderData } from "react-router";
const data = useLoaderData();
```

- Read params:

```jsx
import { useParams } from "react-router-dom";
const { id } = useParams();
```

- Programmatic navigation:

```jsx
import { useNavigate } from "react-router-dom";
const navigate = useNavigate();
navigate("/path", { replace: true });
```

---

## References
- React Router docs — Routing / Nested Routes / Data Loading / Hooks.  
- Various community writeups and tutorials on loaders/actions and nested route patterns. citeturn0search1turn0search2turn0search3turn0search4

# Topic : ReactJS
## Sub Topic : Component Patterns — render props, HOC, compound components, controller pattern

---

## 1) Overview (short)
This note covers four common React component patterns used to share logic, separate concerns, and create flexible component APIs:

- **Render Props** — passing a function prop that returns UI so a parent decides rendering while child provides behavior. citeturn0search0turn0search3  
- **Higher-Order Components (HOC)** — a function that takes a component and returns a new component with added behavior (wrapper). citeturn0search1  
- **Compound Components** — a set of cooperating components (parent + children) that share implicit state (commonly via Context) to create expressive, flexible APIs. citeturn0search9turn0search21  
- **Controller Pattern** — separate business logic (controllers) from presentation; often implemented as controller components or hooks that provide state & callbacks to presentational components. citeturn0search7turn0search15

---

## 2) When to use which
- Use **render props** when you want to expose internal state/behavior to a consumer so the consumer controls rendering.
- Use **HOCs** to reuse cross-cutting behavior (analytics, data fetching, auth) across many components (but prefer hooks in modern code for many cases).
- Use **compound components** to build rich, semantically grouped UI libraries (menus, tabs, selects) where children need implicit ties to a parent.
- Use the **controller pattern** to keep components thin: controllers handle effects/state, presentation focuses on markup/props — helps testing and reuse.

---

## 3) Examples (concise, copy-paste ready)

### A. Render Props
```jsx
// MouseTracker.jsx
import React, { useState, useEffect } from "react";
export default function MouseTracker({ children }) {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  useEffect(() => {
    const onMove = e => setPos({ x: e.clientX, y: e.clientY });
    window.addEventListener("mousemove", onMove);
    return () => window.removeEventListener("mousemove", onMove);
  }, []);
  return children(pos); // render prop via children
}

// Usage
// <MouseTracker>{({x,y}) => <div>Pointer at {x}, {y}</div>}</MouseTracker>
```
Pattern refs: render props examples and docs. citeturn0search0turn0search3

### B. Higher-Order Component (HOC)
```jsx
// withUser.js
import React from "react";
export function withUser(Component) {
  return function WithUser(props) {
    const user = { name: "Harshith" }; // imagine fetched / context
    return <Component {...props} user={user} />;
  };
}

// Usage
// function Greeting({ user }) { return <div>Hello {user.name}</div> }
// export default withUser(Greeting);
```
HOCs wrap and return enhanced components; React docs discuss tradeoffs and evolution away from HOCs for many cases. citeturn0search1

### C. Compound Components (with context)
```jsx
// Tabs.jsx
import React, { createContext, useContext, useState } from "react";
const TabsCtx = createContext();
export function Tabs({ children, defaultIndex = 0 }) {
  const [index, setIndex] = useState(defaultIndex);
  return <TabsCtx.Provider value={{ index, setIndex }}>{children}</TabsCtx.Provider>;
}
export function TabList({ children }) { return <div role="tablist">{children}</div>; }
export function Tab({ children, tabIndex }) {
  const { index, setIndex } = useContext(TabsCtx);
  return <button role="tab" aria-selected={index===tabIndex} onClick={()=>setIndex(tabIndex)}>{children}</button>;
}
export function TabPanel({ children, panelIndex }) {
  const { index } = useContext(TabsCtx);
  return index === panelIndex ? <div role="tabpanel">{children}</div> : null;
}
```
Compound components let you design ergonomic APIs like `<Tabs><TabList><Tab/><TabPanel/></TabList></Tabs>`. citeturn0search9turn0search21

### D. Controller Pattern (controller + presentational)
```jsx
// useTodoController.js
import { useState, useEffect } from "react";
export function useTodoController() {
  const [todos, setTodos] = useState([]);
  useEffect(() => {
    let mounted = true;
    fetch("/api/todos").then(r=>r.json()).then(data => mounted && setTodos(data));
    return () => { mounted = false; };
  }, []);
  function addTodo(item) { setTodos(s => [...s, item]); }
  return { todos, addTodo };
}

// TodoView.jsx (presentation)
export default function TodoView({ todos, onAdd }) {
  return (
    <div>
      <ul>{todos.map(t => <li key={t.id}>{t.text}</li>)}</ul>
      <button onClick={()=>onAdd({ id:Date.now(), text: "New" })}>Add</button>
    </div>
  );
}

// Composition in a container component
import { useTodoController } from "./useTodoController";
import TodoView from "./TodoView";
export default function TodoController() {
  const ctrl = useTodoController();
  return <TodoView todos={ctrl.todos} onAdd={ctrl.addTodo} />;
}
```
Controller pattern separates business logic (controller/hook) from UI (presentational component), improving testability and reuse. citeturn0search7turn0search15

---

## 4) Pros / Cons & modern alternatives
- **Render Props**
  - Pros: Flexible render-control. Cons: verbose nesting (prop drilling), may require wrappers.
  - Modern alt: hooks + composition for most cases.
- **HOC**
  - Pros: Reuse logic, keep components clean. Cons: wrapper hell, lost static methods, harder to debug display names.
  - Modern alt: hooks and component composition.
- **Compound Components**
  - Pros: expressive APIs, implicit state sharing. Cons: Can be tricky to type in TypeScript; hidden coupling between children/parent.
- **Controller Pattern**
  - Pros: Clear separation, easier testing. Cons: More files/indirection; could be overkill for tiny components.

---

## 5) Interview theory questions (concise answers)

1. **Q:** What is the render props pattern?  
   **A:** A technique where a component receives a function prop that returns React elements; the function is called inside the component to determine what to render. Useful for sharing behavior while letting the caller control UI. citeturn0search3

2. **Q:** How does a HOC differ from render props?  
   **A:** A HOC wraps a component and returns an enhanced component (declarative wrapper). Render props pass a function to control rendering. HOCs change the component identity; render props keep identity but change render-time behavior. Hooks are often preferred now.

3. **Q:** Why use compound components?  
   **A:** To build related pieces of UI that need to share state implicitly (e.g., tabs, selects) while exposing a natural developer API that mirrors native HTML patterns.

4. **Q:** What problem does the controller pattern solve?  
   **A:** It separates business logic and side effects from presentation, making UI components purely presentational and easier to unit test and reuse. citeturn0search7

---

## 6) Coding-based interview questions (practical)

1. **Task:** Implement a Dropdown using the compound component pattern that supports `<Dropdown><Dropdown.Toggle/><Dropdown.Menu/><Dropdown.Item/></Dropdown>` and keyboard navigation.  
   **What to show:** Context usage, focus management, aria attributes.

2. **Task:** Convert a class-based HOC that fetches data into a hook-based controller + presentational component. Explain tradeoffs.

3. **Task:** Write a `withAuth` HOC that redirects to `/login` if `user` prop is missing. Then rewrite it as a hook + component wrapper and compare.

4. **Task:** Implement a `MouseTracker` using render props and then refactor it into a custom hook + component composition. Discuss when each is preferable.

---

## 7) Quick patterns checklist (copy for interviews)
- Prefer hooks for logic reuse; use render props or HOCs for library-level APIs when consumers need to control rendering or consumer identity. citeturn0search1turn0search0  
- Use Context + compound components for grouped UI primitives. citeturn0search21  
- Controller pattern helps separate concerns — implement as hooks or controller components. citeturn0search7

---

## 8) References
- Patterns.dev — Render Props, HOC, Compound Pattern. citeturn0search0turn0search4turn0search9  
- React docs — Higher-Order Components. citeturn0search1  
- James K. Nelson — Controller Components article. citeturn0search7  
- Kent C. Dodds — Compound Components (blog). citeturn0search21


# Topic : ReactJS
## Sub Topic : Styling Approaches — CSS Modules, Styled Components, Emotion, TailwindCSS

---

## 1) Overview (short)
This note compares four popular styling approaches used in modern React apps:

- **CSS Modules**: Locally scoped CSS files where class names are hashed to avoid collisions. Works with regular CSS syntax and tooling.
- **Styled Components**: A CSS-in-JS library using tagged template literals; styles are attached to components and can use props for dynamic styles.
- **Emotion**: Another CSS-in-JS solution similar to Styled Components with a focus on performance, APIs for `css` prop, and SSR support.
- **Tailwind CSS**: A utility-first CSS framework that exposes atomic utility classes used directly in markup to compose styles.

Each approach has tradeoffs in ergonomics, performance, bundle size, and design system friendliness.

---

## 2) When to use which
- **CSS Modules**
  - Use when you want simple, predictable CSS with local scoping and minimal runtime cost.
  - Great for migrating legacy code or teams that prefer traditional CSS authoring.
- **Styled Components**
  - Use when component-local styles and prop-driven styling improve developer ergonomics.
  - Good for component libraries where colocated styles and theming matter.
- **Emotion**
  - Similar to Styled Components; choose when you want more flexible APIs (`css`, `sx`, `ClassNames`) or finer performance tuning.
- **Tailwind CSS**
  - Use when you prefer utility-driven design, fast iteration, and consistency via design tokens. Excellent for teams that embrace atomic class composition and want small custom CSS.

---

## 3) Core differences (quick table)

- Scoping: CSS Modules (file-level hashed classes), Styled Components / Emotion (component-scoped via runtime), Tailwind (global utility classes).
- Runtime: CSS Modules (no runtime extra JS), Tailwind (no runtime), Styled Components / Emotion (runtime style injection; Emotion can be compiled).
- Theming: Styled Components & Emotion have first-class theming; Tailwind supports theming through configuration; CSS Modules relies on CSS variables or separate mechanisms.
- Learning curve: Tailwind (new mental model), CSS Modules (familiar), CSS-in-JS (learning tagged templates / API).

---

## 4) Examples

### A. CSS Modules
`Button.module.css`:
```css
.button {
  padding: 0.5rem 1rem;
  background: var(--primary);
  border-radius: 6px;
}
```
`Button.jsx`:
```jsx
import styles from './Button.module.css';
export default function Button({ children }) {
  return <button className={styles.button}>{children}</button>;
}
```

### B. Styled Components
```jsx
import styled from 'styled-components';

const Button = styled.button`
  padding: 0.5rem 1rem;
  background: ${props => props.primary ? 'var(--primary)' : 'transparent'};
  border-radius: 6px;
`;

export default function App(){ return <Button primary>Click</Button>; }
```

### C. Emotion
```jsx
/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react';

const buttonStyle = css`
  padding: 0.5rem 1rem;
  border-radius: 6px;
`;

export default function Button(){ return <button css={buttonStyle}>Click</button>; }
```

### D. Tailwind CSS
```jsx
export default function Button(){ 
  return <button className="px-4 py-2 rounded-md bg-primary text-white">Click</button>; 
}
```

---

## 5) Pros & Cons

### CSS Modules
- Pros: No runtime cost, familiar CSS, strong scoping, easy tooling (linters, PostCSS).
- Cons: Limited runtime theming (needs CSS variables), global styles still possible if misused.

### Styled Components
- Pros: Co-located styles, dynamic props-based styling, theming, readable component APIs.
- Cons: Runtime overhead, larger bundle size, debugging style order sometimes tricky (but devtools help).

### Emotion
- Pros: Flexible APIs (`css`, `styled`, `ClassNames`), good SSR support, can be compiled for zero-runtime.
- Cons: Similar runtime concerns unless using Babel/compile optimizations.

### Tailwind CSS
- Pros: Fast UI development, consistent design tokens, small custom CSS, great for prototyping.
- Cons: Verbose class lists (can be managed with `clsx` or `@apply`), different mental model — can feel like mixing markup & presentation.

---

## 6) Performance considerations
- CSS Modules and Tailwind (pure CSS) avoid runtime JS cost for styling.
- Styled Components / Emotion inject styles at runtime (though Emotion offers extraction/compilation to reduce runtime cost).
- Critical CSS, code-splitting, and server-side rendering strategies differ per approach; for large apps measure bundle size and runtime style injection overhead.

---

## 7) Theming & design systems
- Styled Components and Emotion: built-in `ThemeProvider` patterns make design tokens straightforward.
- Tailwind: central configuration (`tailwind.config.js`) becomes the single source of truth for spacing, colors, and scales.
- CSS Modules: combine with CSS variables (custom properties) or a separate theming layer.

---

## 8) Migration tips
- From global CSS -> CSS Modules: rename files to `*.module.css` and update imports; gradually convert components.
- From CSS-in-JS -> Tailwind: map tokens to Tailwind config, use `@apply` for complex repeated styles.
- From CSS Modules -> Styled Components/Emotion: copy rules into styled components and replace class usage — watch for specificity and order.

---

## 9) Interview theory questions (concise answers)

1. **Q:** What are the tradeoffs between CSS Modules and CSS-in-JS?  
   **A:** CSS Modules offer near-zero runtime cost and familiar CSS authoring; CSS-in-JS provides colocated, dynamic styles and easier prop-driven theming but can add runtime overhead unless compiled.

2. **Q:** How does Tailwind differ conceptually from other approaches?  
   **A:** Tailwind is utility-first: instead of creating semantic CSS classes, you use small utility classes in markup to compose UI, shifting the mental model from authoring stylesheets to composing utilities.

3. **Q:** When might you prefer Emotion over Styled Components?  
   **A:** When you need the flexible `css` prop, better build-time extraction options, or prefer Emotion's API surface and performance characteristics.

4. **Q:** How do you handle global styles and resets with CSS Modules?  
   **A:** Keep a global CSS file for resets (imported once at app root) and use CSS Modules for component-scoped styles. Use CSS variables for tokens that need app-wide reach.

---

## 10) Coding-based interview tasks (practical)

1. **Task:** Implement a theme switcher that toggles light/dark themes using each approach:
   - CSS Modules: swap root CSS variables.
   - Styled Components / Emotion: use `ThemeProvider`.
   - Tailwind: toggle a `class="dark"` on `<html>` and use the `dark:` variants.

2. **Task:** Build a reusable `Card` component library using Styled Components and then provide a Tailwind-based alternative. Discuss bundle-size and DX tradeoffs.

3. **Task:** Migrate a small component library (Button, Input, Modal) from Styled Components to Emotion with zero visual regressions. Show tests and visual diff steps.

4. **Task:** Create a responsive layout using Tailwind utilities and then refactor to use CSS Modules + media queries — compare maintenance cost.

---

## 11) Quick cheat-sheet (copy for interviews)

- Use **CSS Modules** for predictable, low-runtime-cost scoping.  
- Use **Styled Components/Emotion** for prop-driven styles and theming; prefer Emotion if you want `css` prop and compile-time optimizations.  
- Use **Tailwind** for fast UI assembly, strict design tokens, and consistent spacing scales.  
- Measure bundle/runtime cost if app is performance-sensitive; consider compiling CSS-in-JS to avoid runtime injection.

---

## 12) References & further reading
- Official docs: Tailwind CSS, Styled Components, Emotion.  
- Articles: CSS Modules patterns, migrating CSS-in-JS, runtime vs compile-time styling strategies.


1. Theory / Detailed Explanation
1.1 What is Server-Side Rendering (SSR) in React

In a typical client-side rendered (CSR) React app, the browser fetches a minimal HTML page (often just a <div id="root"></div>), then downloads JavaScript, parses & executes it, and only then React builds the UI and injects it into the DOM. This may lead to a blank screen for some time, and sometimes poorer SEO (search engines may struggle with heavy JS). 
DEV Community
+2
Medium
+2

With SSR, you shift the initial render to the server: the server executes your React components, renders them into HTML (strings) and sends that to the browser. The browser receives fully-formed HTML which can be displayed immediately (or at least sooner). This improves perceived load time and SEO. 
DEV Community
+2
Sphinx Solutions
+2

1.2 The role of ReactDOMServer

The package ReactDOMServer (from react-dom/server) provides APIs for rendering React elements (components) on the server into HTML strings or into streaming output. 
React
+1

Key methods:

renderToString(element) — converts a React element into an HTML string (including data-reactid info) suitable for hydration. 
React
+1

renderToStaticMarkup(element) — similar but produces HTML without extra React attributes (less overhead) when you don’t need React to “take over” on the client. 
React

Newer streaming APIs (e.g., renderToPipeableStream(), renderToReadableStream()) allow streaming HTML chunks for better performance / progressive rendering. 
React

1.3 Hydration

Once the server-rendered HTML arrives at the client, we still want interactive behavior (event handlers, state updates, etc). That’s where hydration comes in: the client‐side React code attaches (or “hydrates”) the static DOM (sent from server) with event handlers, internal state, and enables updates. 
Saeloun Blog

In React, you’ll often see something like:

```js
// On the server:
const html = ReactDOMServer.renderToString(<App initialData={...} />);
// … send html wrapped in full HTML page …

// On the client:
ReactDOM.hydrate(<App initialData={...} />, document.getElementById('root'));

```

hydrate() (or newer hydrateRoot() in React 18+) differs from render() because it expects existing markup and tries to reuse it rather than discarding and re-rendering from scratch. 
Saeloun Blog
+1

Important note: If the markup rendered on the server doesn’t match what React expects on the client, you may get hydration mismatches or warnings. So you must ensure consistency of props, state, environment. 
Saeloun Blog

1.4 Static Generation (a.k.a Static Site Generation – SSG) & relation to SSR

Static Generation (SSG) is a variant of server-side rendering, where you pre-render pages at build time (rather than at every request). That means during your build step you run React components on the server, generate HTML files for routes ahead of time, and then serve those as static files. This still gives many benefits of SSR (fast initial HTML, SEO) but with less server runtime cost

1.4 Static Generation (a.k.a Static Site Generation – SSG) & relation to SSR

Static Generation (SSG) is a variant of server-side rendering, where you pre-render pages at build time (rather than at every request). That means during your build step you run React components on the server, generate HTML files for routes ahead of time, and then serve those as static files. This still gives many benefits of SSR (fast initial HTML, SEO) but with less server runtime cost. 
Josh W. Comeau
+1

So you can think of the rendering spectrum:

CSR (client only)

SSR at request time (generate HTML on each request)

SSG / pre-render at build time
Some frameworks even mix these (hybrid) based on page needs. 
Medium

1.5 Why do SSR / Hydration / SSG matter?

Performance / perceived speed: User sees content faster, less “white screen” waiting.

SEO / indexability: Search engine bots (and social media scrapers) see real HTML, not just an empty shell waiting for JS. 
Sphinx Solutions

Better UX: Users on slow networks / older devices benefit.

Flexibility: SSG helps if your data is static or doesn’t change often; SSR helps if data is dynamic per user request.

1.6 Things to watch out for / trade-offs

SSR / SSG adds complexity: you need server infrastructure or build pipelines, need to handle data fetching on server etc. 
DEV Community
+1

Hydration cost: although HTML is ready-to-display, the JS still has to load to enable interactivity. If your bundle is big, you may still see delays.

Data mismatch or hydration mismatch bugs if server and client props differ.

For truly dynamic interactivity, you may need client-side logic anyway — so SSR alone is not a panacea.

2. Interview-Style Questions & Concise Answers

| Question                                                                | Answer (concise)                                                                                                                                                                                 |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| What is SSR in React?                                                   | Rendering React components to HTML on the server and sending that HTML to the client, instead of relying solely on client-side JavaScript.                                                       |
| What does `ReactDOMServer.renderToString()` do?                         | Converts a React element into an HTML string for server-side rendering, including React markup needed for hydration.                                                                             |
| What is hydration in React?                                             | The process by which React attaches event handlers and internal logic to a DOM tree that was rendered by the server, converting a “static” HTML into an interactive app.                         |
| How does static generation (SSG) differ from SSR?                       | SSG pre-renders pages at build time (ahead of any request) whereas SSR renders on each request (or dynamically) on the server. SSG is a form of SSR done at build time.                          |
| Why might you use SSR/SSG instead of pure CSR?                          | For faster initial page loads, better SEO/indexability, improved user experience on slow devices/networks.                                                                                       |
| What could go wrong with hydration?                                     | If server-rendered HTML doesn’t match what the client expects (props/state mismatch), you may get errors or warnings. Also, hydration still requires JS to load, so interactivity delay remains. |
| When would you choose static generation vs request-time SSR?            | Use SSG when data is mostly static and doesn’t change per request; use SSR when each user’s view or data is dynamically generated per request.                                                   |
| What APIs in ReactDOMServer support streaming?                          | Methods like `renderToPipeableStream()` and `renderToReadableStream()` (in modern React) allow streaming HTML from server to client.                                                             |
| How does hydration differ from render?                                  | `render()` creates the DOM from scratch; `hydrate()` assumes existing HTML and attaches React to it to enable interactivity without throwing away the markup.                                    |
| What is the relation between SSR and frameworks like Next.js or Gatsby? | These frameworks build on React’s SSR / SSG capabilities to provide higher-level routing, data-fetching, and build time/static generation features. They abstract many SSR/SSG details.          |

3. Related Coding / Practical Questions

Let’s propose some application / coding style questions you might face, especially given your software engineer role (React, Java, Rust, Python, AI — though this is React-JS territory).

Coding Questions

Show a minimal example of server-side rendering a React component with Express and ReactDOMServer.

Modify the example so that the client uses ReactDOM.hydrate to attach to the server-sent HTML.

How would you handle initial data fetching during SSR (e.g., fetch from API on server, embed into HTML, then client uses that data)?

In a framework like Next.js, what is the difference between getStaticProps, getServerSideProps, and how do they relate to SSG vs SSR?

How can you prevent hydration mismatch warnings in React (e.g., when server and client render differ)?

How would you implement streaming SSR using renderToPipeableStream()? (Sketch code)

Suppose you have a page that rarely changes (say “About Us”). Which rendering strategy would you pick (CSR/SSR/SSG) and why?

If you have user-specific data (like a dashboard after login) that changes per user, how would SSR be used? What trade-offs?

How would you optimize hydration performance (e.g., defer non-critical JS, lazy-load components, break down into islands)?

In a React app built with SSG, how do you handle dynamic routes (e.g., blog posts fetched from CMS) — what build-time vs run-time considerations?

Sample Code Snippet for SSR + Hydration

Here’s a simplified example (you could code similar in interview):

```js
// server.js
import express from 'express';
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import App from './App';

const app = express();

app.get('/', (req, res) => {
  const initialData = { message: 'Hello from SSR!' };
  const appHtml = ReactDOMServer.renderToString(<App initialData={initialData} />);
  const html = `
    <!DOCTYPE html>
    <html>
      <head><meta charset="utf-8"><title>SSR App</title></head>
      <body>
        <div id="root">${appHtml}</div>
        <script>window.__INITIAL_DATA__ = ${JSON.stringify(initialData)}</script>
        <script src="/client_bundle.js"></script>
      </body>
    </html>
  `;
  res.send(html);
});

app.use(express.static('public')); // serve client bundle

app.listen(3000, () => console.log('Listening on port 3000'));

// client/index.js
import React from 'react';
import { hydrateRoot } from 'react-dom/client';
import App from '../App';

const initialData = window.__INITIAL_DATA__;
hydrateRoot(document.getElementById('root'), <App initialData={initialData} />);

// App.js
import React from 'react';

export default function App({ initialData }) {
  const [message, setMessage] = React.useState(initialData.message);
  return (
    <div>
      <h1>{message}</h1>
      <button onClick={() => setMessage('Clicked!')}>Click me</button>
    </div>
  );
}

```

- This shows SSR (server side rendering) plus hydration (client side attaching). You’d adjust for data-fetching, routing, streaming, etc.


# ReactJS Project Architecture Cheat Sheet

## Topic: ReactJS  
## Sub Topic: Project Architecture (Atomic Design, Folder Structure, Reusable Hooks, Feature-Based Layout)

---

## 1. React Project Architecture Overview

A well‑structured React project acts like a good library: everything has its shelf, and nothing screams from a random drawer. Modern teams lean toward **feature‑based**, **atomic**, and **hook‑driven** structures to keep the codebase scale‑friendly.

---

## 2. Atomic Design in React

Atomic Design splits UI into five conceptual layers:

### **Atoms**
Small, indivisible components like buttons, inputs, icons.

### **Molecules**
Compositions of atoms: an Input + Label + Error message bundle.

### **Organisms**
Sections of UI: navbars, cards, sidebars.

### **Templates**
Page-level skeletons defining structure but not content.

### **Pages**
Final screens with real data.

**Why atomic design?**  
Keeps components consistent, reusable, and easy to extend.

---

## 3. Ideal React Folder Structure

A widely used structure combining feature-based layout + atomic design + reusable hooks:

```
src/
 ├── assets/
 │    └── images/
 ├── components/        # Global atomic components
 │    ├── atoms/
 │    ├── molecules/
 │    └── organisms/
 ├── hooks/
 │    └── useFetch.js
 ├── features/
 │    ├── auth/
 │    │    ├── components/
 │    │    ├── hooks/
 │    │    └── services/
 │    ├── dashboard/
 │    └── products/
 ├── pages/
 ├── services/
 ├── utils/
 ├── store/
 └── App.js
```

**Why feature-based layout?**  
Everything related to one feature sits together — components, API calls, hooks.

---

## 4. Reusable Hooks

Hooks let logic travel lightly between components. A few common reusable ones:

### **useFetch**
Handles async calls: loading, error, data.

### **useDebounce**
Ideal for search bars and input-heavy UX.

### **useLocalStorage**
Wraps browser APIs with React state magic.

### **usePrevious**
Tracks previous value of a prop or state.

**Pattern for reusable hooks:**
Encapsulate logic → expose minimal API → keep it pure → avoid UI coupling.

---

## 5. Feature-Based Architecture (Recommended Standard)

This layout orients around **business domains**, not component types.

Each feature may contain:

```
featureName/
  components/
  hooks/
  services/
  reducers/
  types.js
```

Benefits:
- Reduces cross-folder chaos.
- Makes features independently maintainable.
- Easier onboarding: “want to work on cart? open /cart”.

---

## 6. Interview Theory Questions + Short Answers

**1. Why use atomic design in React?**  
It enforces consistency and reusability by breaking UI into predictable layers.

**2. What is the benefit of feature-based folder structure?**  
It groups domain logic together, making features modular, scalable, and readable.

**3. Why create reusable hooks?**  
To abstract shared logic so multiple components can reuse it without duplication.

**4. Should global components be placed in `/components` or inside features?**  
Global ones go to `/components`; feature‑specific ones stay inside their feature folder.

**5. What problem does atomic design solve?**  
It prevents giant, inconsistent component libraries and helps scale large UI systems.

---

## 7. Coding Questions Related to Project Architecture

### **1. Build a Reusable useFetch Hook**

```javascript
import { useState, useEffect } from "react";

export function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;

    async function load() {
      try {
        const res = await fetch(url);
        if (!res.ok) throw new Error("Network error");
        const json = await res.json();
        if (isMounted) setData(json);
      } catch (e) {
        if (isMounted) setError(e);
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    load();
    return () => (isMounted = false);
  }, [url]);

  return { data, loading, error };
}
```

### **2. Example of Atomic Component Structure**

```javascript
// atoms/Button.js
export const Button = ({ children, ...props }) => (
  <button {...props}>{children}</button>
);

// molecules/SearchBar.js
import { Button } from "../atoms/Button";

export const SearchBar = ({ value, onChange }) => (
  <div>
    <input value={value} onChange={onChange} />
    <Button>Search</Button>
  </div>
);
```

### **3. Feature-Based Example**

```
features/todos/
  components/TodoList.js
  hooks/useTodos.js
  services/todoApi.js
```

---

## End of Document
