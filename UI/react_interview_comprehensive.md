# React Interview Questions and Answers

For each question below, you’ll find a concise theoretical explanation followed by a practical code example.

---

## 1. What is Reactjs and how is it different from other libraries/frameworks?
**Theory:** React is a declarative, component-based UI library using a virtual DOM for efficient updates, unlike imperative frameworks.
```jsx
import React from 'react';
function App() { return <h1>Hello, React!</h1>; }
```

---

## 2. What is JSX? Difference between JSX and TSX?
**Theory:** JSX embeds HTML in JS; TSX adds TypeScript types.
```jsx
const el = <div>Hello</div>;
// TSX
type Props = { msg: string };
const Msg: React.FC<Props> = ({ msg }) => <p>{msg}</p>;
```

---

## 3. Explain Virtual DOM and Shadow DOM.
**Theory:** Virtual DOM is React’s in-memory UI for diffing; Shadow DOM is browser-scoped styling.
```jsx
// React diffs virtual DOM to update real DOM efficiently
```

---

## 4. Virtual DOM vs real DOM?
**Theory:** Virtual DOM is JS objects; real DOM is browser API.
```jsx
// setState triggers virtual DOM diff
setCount(c => c + 1);
```

---

## 5. Types of React components.
**Theory:** Functional, Class, Pure, HOC, Server.
```jsx
class MyComp extends React.Component { render() { return null; } }
const FuncComp = () => null;
```

---

## 6. Class vs Functional component.
**Theory:** Class uses lifecycle methods; functional uses Hooks.
```jsx
function Func() { const [c,setC]=useState(0); return null; }
```

---

## 7. What is state?
**Theory:** Internal mutable data affecting render.
```jsx
const [count, setCount] = useState(0);
```

---

## 8. Props vs State.
**Theory:** Props are read-only inputs; state is local and mutable.
```jsx
<Child name="Alice" />;
function Child({ name }) { return <p>{name}</p>; }
```

---

## 9. Props drilling and alternative?
**Theory:** Passing props through many children; use Context.
```jsx
const Ctx = React.createContext();
```

---

## 10. Controlled vs Uncontrolled components.
**Theory:** Controlled uses state for value; uncontrolled uses refs.
```jsx
<input value={val} onChange={e=>setVal(e.target.value)} />;
const ref = useRef();
<input ref={ref} defaultValue="hi" />;
```

---

## 11. How re-render on state change?
**Theory:** setState/useState triggers a re-render and diff.
```jsx
setCount(prev => prev + 1);
```

---

## 12. Direct state update?
**Theory:** Direct mutation does not re-render.
```jsx
// Avoid:
state.count = 1;
```

---

## 13. Share data among siblings?
**Theory:** Lift state up or use Context.
```jsx
// Parent holds state, passes via props
```

---

## 14. Styled-components and theming?
**Theory:** CSS-in-JS with theme provider.
```jsx
import styled, {ThemeProvider} from 'styled-components';
const Btn = styled.button`color: ${props=>props.theme.color};`;
```

---

## 15. React Server Components?
**Theory:** Components rendered on server, no client JS.
```jsx
// Server component example omitted for brevity
```

---

## 16. Lifecycle methods.
**Theory:** mounting, updating, unmounting in classes.
```jsx
class C extends React.Component {
  componentDidMount() {}
  componentDidUpdate() {}
  componentWillUnmount() {}
}
```

---

## 17. Lifecycle in functional?
**Theory:** useEffect with deps:
```jsx
useEffect(() => { /* mount/update */ return () => { /* unmount */ } }, [deps]);
```

---

## 18. Handling side effects?
**Theory:** class: lifecycle; functional: useEffect.
```jsx
useEffect(() => { fetchData(); }, []);
```

---

## 19. React Hooks?
**Theory:** Functions for state/effects: useState, useEffect, useContext, useReducer, useRef, useMemo, useCallback.
```jsx
const [data, setData] = useState(null);
```

---

## 20. useState vs useRef?
**Theory:** useState triggers render; useRef persists value without render.
```jsx
const ref = useRef(0);
```

---

## 21. useState, useContext, useReducer?
**Theory:** useState for local state, useContext for global, useReducer for complex logic.
```jsx
const [state, dispatch] = useReducer(reducer, initial);
```

---

## 22. Rules of Hooks?
**Theory:** Call only at top level and in React functions.
```jsx
// Don’t call inside loops or conditionals
```

---

## 23. Custom Hooks?
**Theory:** Reusable logic prefixed with use.
```jsx
function useCounter(init=0) {
  const [c,setC] = useState(init);
  const inc = () => setC(x=>x+1);
  return {c, inc};
}
```

---

## 24. Higher Order Component?
**Theory:** Function that returns enhanced component.
```jsx
const withAuth = Component => props => props.auth ? <Component {...props}/> : null;
```

---

## 25. Reconciliation process?
**Theory:** Diff old and new virtual DOM to apply minimal updates.

---

## 26. Virtual DOM diffing?
**Theory:** Compares by element type and key.
```jsx
items.map(item => <li key={item.id}>{item.name}</li>);
```

---

## 27. Context API hook?
**Theory:** useContext to consume created context.
```jsx
const Theme = React.createContext('light');
const theme = useContext(Theme);
```

---

## 28. useCallback vs useMemo?
**Theory:** useCallback memoizes function; useMemo memoizes value.
```jsx
const memoVal = useMemo(() => compute(a,b), [a,b]);
const memoFn = useCallback(() => doThing(x), [x]);
```

---

## 29. Context API vs Redux?
**Theory:** Context for simple state; Redux for complex flows.

---

## 30. Redux Toolkit?
**Theory:** Simplifies Redux with createSlice, configureStore.
```js
import { createSlice } from '@reduxjs/toolkit';
```

---

## 31. Redux middleware?
**Theory:** Intercepts actions for side effects.
```js
const logger = store => next => action => { console.log(action); return next(action); };
```

---

## 32. Global state without Redux?
**Theory:** Context + useReducer.
```jsx
const [state,dispatch] = useReducer(reducer, {});
```

---

## 33. Synthetic event?
**Theory:** React’s cross-browser normalized event.
```jsx
<button onClick={e => console.log(e.nativeEvent)}>Click</button>
```

---

## 34. Synthetic vs real DOM event?
**Theory:** Synthetic are pooled and normalized; real are native browser events.

---

## 35. Passing arguments in handlers?
**Theory:** Use arrow or bind.
```jsx
<button onClick={() => handle(id)}>Click</button>
```

---

## 36. Dynamic routing?
**Theory:** React Router with params.
```jsx
<Routes><Route path="/user/:id" element={<User/>}/></Routes>;
const { id } = useParams();
```

---

## 37. Form validation?
**Theory:** Controlled inputs or libraries.
```jsx
import { useForm } from 'react-hook-form';
```

---

## 38. Lazy loading routes?
**Theory:** React.lazy + Suspense.
```jsx
const Dashboard = React.lazy(() => import('./Dashboard'));
<Suspense fallback={<div>Loading...</div>}><Dashboard/></Suspense>
```

---

## 39. Optimize large forms?
**Theory:** Virtualization, split steps, memoization.

---

## 40. Multi-step form?
**Theory:** Track step state and conditional render.
```jsx
{step===1 && <Step1/>}
```

---

## 41. Keys in lists?
**Theory:** Unique key for diffing.
```jsx
items.map(item => <li key={item.id}>{item.name}</li>);
```

---

## 42. React.memo?
**Theory:** Memoizes component render on props change.
```jsx
const MemoComp = React.memo(Comp);
```

---

## 43. PureComponent?
**Theory:** Class with shallow prop/state compare.
```jsx
class PC extends React.PureComponent { /*...*/ }
```

---

## 44. Virtualization?
**Theory:** Render only visible items (e.g., react-window).
```jsx
import { FixedSizeList } from 'react-window';
```

---

## 45. Optimize large lists?
**Theory:** Memo, virtualization, keys.

---

## 46. Avoid re-rendering?
**Theory:** useMemo, useCallback, React.memo.

---

## 47. Error boundaries?
**Theory:** Catch render errors in class components.
```jsx
class EB extends React.Component {
  componentDidCatch(error, info) { /*...*/ }
  render() { return this.state.hasError ? <Fallback/> : this.props.children; }
}
```

---

## 48. Handle async errors?
**Theory:** try/catch in async or .catch, update state.

---

## 49. Fetch data?
**Theory:** useEffect + fetch/axios.
```jsx
useEffect(() => { fetch('/api').then(r => r.json()).then(setData); }, []);
```

---

## 50. Axios vs Fetch?
**Theory:** Axios has interceptors and auto JSON parsing.
```js
axios.get('/api').then(res => console.log(res.data));
```

---

## 51. Secure API keys?
**Theory:** Use env variables at build time prefixed with REACT_APP_.

---

## 52. Retry logic?
**Theory:** Implement retry loop or use axios-retry.
```js
async function fetchWithRetry(url, n=3) { for(let i=0;i<n;i++){ try{return await fetch(url);}catch{} } }
```

---

## 53. Fragments?
**Theory:** Group without extra node.
```jsx
<><ChildA/><ChildB/></>
```

---

## 54. React.StrictMode?
**Theory:** Dev-only checks for unsafe lifecycles and effects.

---

## 55. Memory leaks?
**Theory:** Cleanup in useEffect return, remove listeners.

---

## 56. Production build?
**Theory:** npm run build to minify and optimize.

---

## 57. Webpack vs Babel?
**Theory:** Webpack bundles; Babel transpiles.

---

## 58. Webpack config?
**Theory:** Set entry, babel-loader, css-loader, plugins.

---

## 59. Performance optimization?
**Theory:** Code-splitting, memo, virtualization, analyze bundle.

---

## 60. .env purpose?
**Theory:** Store build-time env variables for configuration.
