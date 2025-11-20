# HTML CSS Cheat Sheet Interview

A complete quick-glimpse + concept revision guide for experienced frontend engineers preparing for Front End Interviews.

---

## 🧠 FRONTEND INTERVIEW REVISION BLUEPRINT

### 🔹 HTML — Semantic, Accessibility, and Performance

**Concepts to Revise**
- Semantic HTML5 tags (`header`, `nav`, `main`, `section`, `article`, `aside`, `footer`)
- Forms: validation attributes (`required`, `pattern`, `novalidate`)
- Accessibility (a11y): `aria-label`, roles, tab order, landmarks
- SEO: meta tags, title, canonical, Open Graph
- `<script>` attributes: `defer` vs `async`
- Storage: LocalStorage vs SessionStorage vs Cookies
- Shadow DOM and Web Components
- Critical Rendering Path

**Deep Knowledge**
- `<link rel="preload">` vs `<link rel="prefetch">`
- How browsers parse HTML → DOM
- CSR vs SSR HTML structures

---

### 🎨 CSS — Layout, Architecture, and Optimization

**Core Concepts**
- Box model (margin collapsing, `box-sizing`)
- Flexbox and CSS Grid
- Positioning: relative, absolute, sticky, fixed
- Specificity, inheritance, cascade layers
- Pseudo-elements (`::before`, `::after`)
- Responsive design, media queries
- CSS units: `em`, `rem`, `%`, `vh`, `vw`
- CSS transitions, keyframe animations
- CSS architecture: BEM, CSS Modules, Styled Components, Tailwind
- Repaint vs Reflow (render performance)

**Tricky Topics**
- Difference: `visibility: hidden` vs `opacity: 0` vs `display: none`
- Why avoid inline styles
- GPU acceleration: `will-change`, `transform: translateZ(0)`

---

### ⚙️ JavaScript — ES6+ and Core Mechanics

**ES6+ Features**
- `let`, `const`, block scoping, TDZ
- Template literals, destructuring, spread/rest
- Arrow functions (`this` binding)
- Promises, async/await, event loop
- Modules (`import/export`, dynamic imports)
- Default parameters, enhanced object literals
- Generators & Iterators
- Classes, private fields (`#`)
- Optional chaining (`?.`), nullish coalescing (`??`)

**Core JS Concepts**
- Execution Context, Scope Chain, Hoisting
- Closures and Lexical Scope
- Event Loop: macro vs microtasks
- Prototype chain and inheritance
- `call`, `apply`, `bind`
- Debouncing and Throttling
- Currying
- Polyfills (e.g., for `Promise`, `bind`, `map`)
- Garbage collection
- Shallow vs Deep copy (`structuredClone`, `lodash`)

**Common Interview Traps**
- Why `this` differs in arrow functions
- Event delegation
- How JS handles async operations internally

---

### ⚛️ React — Core, Hooks, Lifecycle, Performance

**Fundamentals**
- Virtual DOM & Reconciliation
- JSX → `React.createElement()`
- Function vs Class components
- Component lifecycle
- Controlled vs Uncontrolled components
- Props vs State
- Keys in lists
- Synthetic events

**Hooks**
- `useState`: batching, stale closures
- `useEffect`: dependency array, cleanup
- `useRef`: mutable values, DOM refs
- `useMemo`, `useCallback`: memoization
- `useContext`: global state sharing
- `useReducer`: redux-like logic
- Custom Hooks: reuse and abstraction

**Advanced React**
- React Fiber Architecture
- Concurrent Rendering (React 18+)
- Suspense & Lazy Loading
- Error Boundaries
- `React.memo`, `PureComponent`
- Reconciliation algorithm
- Portals
- React Server Components

**Performance**
- Re-render triggers
- Avoiding prop drilling (Context, Zustand, Redux)
- Code splitting
- Profiling with React DevTools

---

### 🧩 Custom Hooks

**Concepts**
- Encapsulate stateful logic
- Follow naming convention (`useSomething`)
- Common examples:
  - `useFetch`
  - `useDebounce`
  - `usePrevious`
  - `useTimeout`
  - `useLocalStorage`

**Key Points**
- When to use hooks vs components
- Avoid infinite re-renders

---

### 🏗️ State Management — Context, Redux, Recoil, Zustand

**Redux**
- Action, Reducer, Store, Dispatch
- Middleware: Thunk, Saga
- Redux Toolkit: `createSlice`, `createAsyncThunk`
- Memoized Selectors with Reselect

**Context API**
- Avoid prop drilling
- Understand performance costs

**Modern Alternatives**
- Zustand, Jotai, Recoil basics

---

### 🌐 API Integration & Async Flows

- `fetch` vs `axios`
- Error handling (`try/catch`, response codes)
- `AbortController` for request cancellation
- React Query / TanStack Query
- SWR: stale-while-revalidate strategy

---

### ⚡ Performance & Optimization

- Lazy loading, dynamic imports
- `React.memo`, `useMemo`, `useCallback`
- Avoiding expensive computations
- Virtualization: `react-window`, `react-virtualized`
- SSR vs CSR vs SSG (Next.js)
- Image optimization
- Tree shaking, bundle splitting (webpack, Vite)

---

### 🧰 Testing & Tooling

- Unit Testing: Jest, React Testing Library
- Snapshot testing
- Integration vs E2E: Cypress, Playwright
- Babel & Webpack basics
- ESLint, Prettier
- CI/CD pipelines

---

### ☁️ Next.js Ecosystem

- Pages vs App Router
- Server Components
- `getStaticProps`, `getServerSideProps`, API routes
- Dynamic routing
- Middleware & Edge functions
- Image and font optimization

---

### 🔒 Security, Networking & Deployment

- XSS, CSRF prevention
- Sanitizing user input
- HTTPS, CORS
- JWT authentication
- Environment variable handling

---

### 🧮 Frontend System Design

- SPA Architecture
- Component-driven development
- Microfrontends (Module Federation)
- WebSockets & SSE
- Caching (Service Workers, LocalStorage)
- CDN and asset optimization

---

## ✅ Final Checklist Before Interview

- [ ] Can explain the event loop clearly
- [ ] Knows all major hooks and when to use each
- [ ] Can describe virtual DOM and reconciliation
- [ ] Understands React performance optimizations
- [ ] Can write a custom hook from scratch
- [ ] Knows SSR/CSR/SSG differences
- [ ] Comfortable with Redux Toolkit and Context
- [ ] Has practiced common JS coding patterns (closures, async, currying)
- [ ] Understands CSS layout deeply (Flex, Grid)
- [ ] Can explain accessibility and semantic HTML
- [ ] Can debug React app with DevTools profiler

---

### 🧩 Bonus Reading Topics

- React Server Components (RFC)
- Signals (Future React optimization model)
- Web Vitals (LCP, FID, CLS)
- TypeScript with React
- Vite vs Webpack build internals

---

**🔥 Tip:** In interviews, focus on *why* and *how React works internally* rather than just API knowledge. Senior-level interviews dig into:
- rendering pipeline,
- reconciliation strategy,
- async updates,
- and architectural tradeoffs.

---

_Keep this file handy for rapid revision before interviews._


# ⚛️ Frontend Developer Interview Prep Notes (5+ YOE)

A complete tiered roadmap for HTML, CSS, JavaScript, and React-based interviews.

---

## 🧱 HTML — Semantic, Accessibility, and Performance

### 🟩 Tier 1 — Must Know
- Structure of an HTML5 document (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`)
- Semantic tags (`header`, `main`, `section`, `article`, `aside`, `footer`, `nav`)
- Inline vs Block elements
- Semantic vs Non-semantic tags (`div` vs `section`)
- Forms: attributes (`required`, `pattern`, `novalidate`)
- Input types (`email`, `number`, `date`, etc.)
- Accessibility (`alt`, `aria-*`, `role`)
- SEO tags (`meta`, `title`, `canonical`, `viewport`)
- `<script>` loading: `defer` vs `async`
- LocalStorage vs SessionStorage vs Cookies

### 🟨 Tier 2 — Should Know
- Shadow DOM (encapsulation and styling)
- Web Components (`customElements.define`, `<template>`)
- DOM parsing and rendering flow
- Critical Rendering Path
- Lazy loading (`loading="lazy"`)
- `<picture>` and `<source>` tags
- `<video>` and `<audio>` tags
- `<link rel="preload">`, `<link rel="prefetch">`
- Repaint vs Reflow concepts

### 🟥 Tier 3 — Advanced / Senior Topics
- Drag and Drop API
- ContentEditable
- Clipboard API
- Geolocation API
- Intersection Observer
- Web Workers & Service Workers
- XSS and HTML sanitization
- Progressive Enhancement vs Graceful Degradation
- i18n: `lang`, `dir="rtl"`, charset
- Content Security Policy (CSP)

---

## 🎨 CSS — Layout, Architecture, and Optimization

### 🟩 Tier 1 — Must Know
- CSS Box Model (`content-box` vs `border-box`)
- Positioning (`relative`, `absolute`, `fixed`, `sticky`)
- Display types (inline, block, inline-block)
- Flexbox (justify, align, flex-grow, flex-shrink)
- CSS Grid basics (template-rows/columns, gap)
- Selectors & specificity
- Pseudo-classes (`:hover`, `:focus`) and pseudo-elements (`::before`, `::after`)
- Units (`em`, `rem`, `%`, `vh`, `vw`)
- CSS variables (`--var` and `var(--var)`)
- Responsive design & media queries

### 🟨 Tier 2 — Should Know
- CSS transitions & animations (performance awareness)
- Repaint vs Reflow
- CSS architecture: BEM, SMACSS
- CSS-in-JS (Styled Components, Emotion)
- CSS Modules
- TailwindCSS basics
- Z-index and stacking context
- `overflow`, `clip-path`, and `object-fit`
- CSS Filters & Blend modes
- Custom fonts and `@font-face`

### 🟥 Tier 3 — Advanced / Senior Topics
- Critical CSS & lazy CSS loading
- CSS Grid deep dive (auto-fit, minmax)
- Logical properties (e.g. `margin-inline`)
- Container Queries
- Cascade layers (`@layer`)
- Performance optimizations (GPU compositing, `will-change`)
- Accessibility styling (focus-visible, prefers-reduced-motion)
- Theming (CSS vars, context-based theming)
- CSS Houdini APIs

---

## ⚙️ JavaScript — ES6+ and Core Mechanics

### 🟩 Tier 1 — Must Know
- `let`, `const` vs `var`
- Arrow functions and lexical `this`
- Template literals
- Destructuring, spread/rest
- Promises, async/await
- Default parameters
- Modules (`import`, `export`)
- Classes and inheritance
- `map`, `filter`, `reduce`
- JSON basics (parse/stringify)

### 🟨 Tier 2 — Should Know
- Execution Context, Scope, and Hoisting
- Closures and Lexical Scope
- Event Loop (macro vs microtasks)
- Prototypes and inheritance
- `call`, `apply`, `bind`
- Currying
- Debouncing & Throttling
- Polyfills (implementing `map`, `Promise`, `bind`)
- Shallow vs Deep copy (`structuredClone`, `lodash`)
- `this` in arrow vs regular functions

### 🟥 Tier 3 — Advanced / Senior Topics
- Generators and Iterators
- WeakMap, WeakSet
- Garbage collection
- Event delegation
- Async patterns (parallel vs sequential execution)
- Modules and tree shaking
- Memory leaks and performance optimization
- Design patterns (Observer, Singleton, Module)
- Functional programming concepts
- Type Coercion and Equality (`==` vs `===`)

---

## ⚛️ React — Core, Hooks, Lifecycle, and Performance

### 🟩 Tier 1 — Must Know
- Virtual DOM and reconciliation
- JSX (how it compiles to `React.createElement`)
- Functional vs Class components
- State and Props
- Controlled vs Uncontrolled components
- Conditional rendering
- Lists and Keys
- Event handling and synthetic events
- Component composition
- useState, useEffect hooks

### 🟨 Tier 2 — Should Know
- useRef, useMemo, useCallback
- Context API
- Custom Hooks (reusable logic)
- useReducer
- useLayoutEffect vs useEffect
- Error boundaries
- React.memo and PureComponent
- Lazy loading and Suspense
- Code splitting
- Performance optimization (memoization)

### 🟥 Tier 3 — Advanced / Senior Topics
- React Fiber architecture
- Concurrent rendering
- Server Components (React 19+)
- Portals
- Reconciliation algorithm (diffing)
- Hydration and SSR concepts
- Controlled re-renders
- React Profiler usage
- Suspense for data fetching
- Future features (Signals, Offscreen)

---

## 🧩 Custom Hooks — Encapsulating Stateful Logic

### 🟩 Tier 1 — Must Know
- Why Custom Hooks exist
- Naming conventions (`useSomething`)
- Example: `useFetch`, `useLocalStorage`

### 🟨 Tier 2 — Should Know
- Managing async operations within hooks
- Avoiding infinite loops
- Sharing stateful logic between components
- Hooks composition patterns

### 🟥 Tier 3 — Advanced / Senior Topics
- Hooks factory patterns
- Dependency array optimizations
- Complex hooks with reducers
- Integrating custom hooks with libraries (e.g., React Query)
- Performance optimization via memoization

---

## 🏗️ State Management — Context, Redux, Recoil, Zustand

### 🟩 Tier 1 — Must Know
- Context API (Provider, Consumer)
- Lifting state up
- Prop drilling and how to avoid it

### 🟨 Tier 2 — Should Know
- Redux: Action, Reducer, Store, Dispatch
- Redux Toolkit (`createSlice`, `createAsyncThunk`)
- Middleware (Thunk, Saga)
- Memoized selectors (Reselect)
- Zustand, Jotai, Recoil overview

### 🟥 Tier 3 — Advanced / Senior Topics
- Normalizing state
- Server State vs Client State
- Optimistic updates
- Comparing Redux vs Context performance
- Persisted stores (Redux Persist)
- State design in large-scale applications

---

## 🌐 API Integration & Async Data

### 🟩 Tier 1 — Must Know
- `fetch` API
- Axios basics
- Async/await with error handling

### 🟨 Tier 2 — Should Know
- Aborting requests (`AbortController`)
- Handling loading and error states
- React Query basics
- SWR (stale-while-revalidate)

### 🟥 Tier 3 — Advanced / Senior Topics
- Request deduplication
- Cache invalidation
- Background refetching
- Infinite scrolling (React Query)
- GraphQL (Apollo basics)

---

## ⚡ Performance Optimization

### 🟩 Tier 1 — Must Know
- Avoiding unnecessary re-renders
- `React.memo`, `useCallback`, `useMemo`
- Code splitting
- Lazy loading

### 🟨 Tier 2 — Should Know
- Virtualization (`react-window`, `react-virtualized`)
- Profiling with React DevTools
- Image optimization
- Debouncing expensive operations

### 🟥 Tier 3 — Advanced / Senior Topics
- SSR vs CSR vs SSG (Next.js)
- Pre-rendering and hydration
- Web Vitals (LCP, CLS, FID)
- Bundle analysis and tree shaking
- Browser caching strategies

---

## 🧰 Testing & Tooling

### 🟩 Tier 1 — Must Know
- Jest basics
- React Testing Library (render, screen, fireEvent)
- Snapshot testing

### 🟨 Tier 2 — Should Know
- Mocking API calls
- Integration vs E2E testing
- Cypress / Playwright basics
- Babel, Webpack fundamentals

### 🟥 Tier 3 — Advanced / Senior Topics
- CI/CD pipelines
- Unit test design principles
- Visual regression testing
- Performance testing

---

## ☁️ Next.js Ecosystem

### 🟩 Tier 1 — Must Know
- Pages vs App router
- `getStaticProps`, `getServerSideProps`
- Dynamic routing

### 🟨 Tier 2 — Should Know
- Middleware & Edge functions
- API routes
- Image optimization
- Fonts optimization

### 🟥 Tier 3 — Advanced / Senior Topics
- Server Components
- ISR (Incremental Static Regeneration)
- Streaming SSR
- Deployment strategies (Vercel, Netlify)

---

## 🔒 Security, Networking, and Deployment

### 🟩 Tier 1 — Must Know
- HTTPS and CORS basics
- XSS prevention
- Sanitizing inputs

### 🟨 Tier 2 — Should Know
- CSRF protection
- JWT-based authentication
- Securely handling environment variables

### 🟥 Tier 3 — Advanced / Senior Topics
- CSP (Content Security Policy)
- SameSite cookies
- OAuth flows
- Security headers and helmet middleware

---

## 🧮 Frontend System Design

### 🟩 Tier 1 — Must Know
- SPA vs MPA
- Component-driven development
- Routing and navigation

### 🟨 Tier 2 — Should Know
- Microfrontends (Module Federation)
- Caching strategies (service workers, localStorage)
- CDN basics

### 🟥 Tier 3 — Advanced / Senior Topics
- Scalability in frontend architecture
- Communication between microfrontends
- Performance budgeting
- Observability (logging, monitoring, tracing)

---

## ✅ Final Full-Stack Checklist

- [ ] HTML: semantics, accessibility, performance
- [ ] CSS: layout, architecture, responsive design
- [ ] JS: event loop, async, closures, prototypes
- [ ] React: hooks, lifecycle, reconciliation
- [ ] State: Redux, Context, Zustand, Recoil
- [ ] API: async data handling
- [ ] Performance: re-renders, profiling
- [ ] Testing: Jest, RTL, Cypress
- [ ] Next.js: SSR, SSG, RSC
- [ ] Security: XSS, CORS, JWT
- [ ] Deployment: CI/CD, caching, optimization

---

### 💡 Interview Tip
Senior-level frontend interviews focus on:
- **System understanding**, not just syntax.
- **Why React works a certain way**, not only “how”.
- **Tradeoffs**: CSR vs SSR, Context vs Redux, memoization cost vs benefit.

Be prepared to **reason** and **architect**, not just implement.

---

_Keep this file as your go-to revision doc for frontend interviews._




## HTML

### Semantic HTML5 tags (`header`, `nav`, `main`, `section`, `article`, `aside`, `footer`)

Semantic tags make your HTML more readable and accessible (for both developers and assistive technologies like screen readers).

| Tag         | Meaning / Purpose                                                                                                           | Common Usage Example                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `<header>`  | Represents the **introductory section** of a page or a section. Usually contains logos, navigation, titles, or search bars. | `html<br><header><h1>My Blog</h1><nav>...</nav></header>`              |
| `<nav>`     | Defines a **section for navigation links** (menus, tables of contents, etc.).                                               | `html<br><nav><a href="/">Home</a> <a href="/about">About</a></nav>`   |
| `<main>`    | Contains the **main content** unique to the page. There should be only **one `<main>`** per page.                           | `html<br><main><article>...</article></main>`                          |
| `<section>` | Groups related content under a **thematic grouping**, usually with its own heading. Think of it as a “chapter.”             | `html<br><section><h2>Features</h2><p>Details...</p></section>`        |
| `<article>` | Represents **self-contained content** that could stand alone — like a blog post, news article, or forum entry.              | `html<br><article><h2>Post Title</h2><p>Post content...</p></article>` |
| `<aside>`   | Contains **indirectly related content** — sidebars, ads, related links, etc.                                                | `html<br><aside><h3>Related Posts</h3><ul>...</ul></aside>`            |
| `<footer>`  | Represents the **footer section** of a page or a section. Commonly includes author info, copyright, or contact links.       | `html<br><footer><p>© 2025 My Blog</p></footer>`                       |

- improves accessibility
- seo friendlt
- maintainability
- standard structure


### Forms: validation attributes (`required`, `pattern`, `novalidate`)

- HTML forms are used to collect user input and send it to a server for processing.


```html
<form action="/submit" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="username" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="useremail">

  <button type="submit">Submit</button>
</form>
```

#### Key Attributes of <form>

- action: URL where form data is sent.

- method: HTTP method — "GET" (appends data to URL) or "POST" (sends in body).

- target: Where to display the response (_self, _blank, _parent, _top).

- novalidate: Disables browser’s built-in validation.

#### Form Validation Attributes

1. required

- ensures field must be filled before submiting
```html
<input type="text" name="username" required>
```

2. pattern 

- ensures a field must match a regex

```html
<input type="text" pattern="[A-Za-z]{3,10}" title="Enter 3–10 letters only">

```

3. novalidate

- placed on form to disable html5 validation and add from js

```html
<form novalidate>
    <label for="name" >Name</label>
    <input type="text" id="name" name="username" />

    <button type="submit">Submit</button>
</form>
```


### - Accessibility (a11y): `aria-label`, roles, tab order, landmarks

- developing webcontent for everyone including disablities , (visual , auditory, motor, cognitive)

1. aria label

- adds a text label to the screen readers like icons where text is not available

```html
<button aria-label="Search Button">
    <svg>...</svg> 
</button>
```

- aria-labelledby → references another element as its label.
- aria-describedby → adds extra descriptive info (like tooltips).

2. role

- we can make few non semantic html elements act as our intended ones using role

```html
<div role="button" tabindex="0">Click me</div>
```

- Use native HTML elements (like <button>, <nav>) whenever possible — add role only when necessary.

3. tab order

- Keyboard users navigate using the Tab key.

- tabindex="0" → Makes an element focusable in normal tab order.
- tabindex="-1" → Makes an element focusable via JavaScript, not by tab.
- tabindex="positive number" → Sets custom order (avoid unless necessary).

```html
<button>1</button>
<button tabindex="2">3</button>
<button tabindex="1">2</button>

```

4. Landmarks

- Landmarks help screen readers navigate major page sections quickly.
- tools like axe will help us in making these changes


### - SEO: meta tags, title, canonical, Open Graph

- SEO (Search Engine Optimization) helps search engines understand your webpage’s content and improve its visibility in search results.

<!-- 1. <title> tag -->

- Defines the title of the page — displayed in browser tabs and search engine results.

2. <meta> tag

- Meta tags give metadata (information about the page) to browsers and search engines.

- meta dscription

```html
<meta name="description" content="Learn easy homemade pizza recipes with step-by-step guides.">
```

- meta robots

```html
<meta name="robots" content="index, follow">
```

- index , noindex -> whether to index this page or not
- follow, nofollow -> whether to follow the index or not

3. Canonical Tag (<link rel="canonical">)

```html
<link rel="canonical" href="https://example.com/pizza-recipes">
```

- If your page is accessible at multiple URLs (e.g., /pizza and /pizza?ref=homepage), the canonical tag ensures only one version is indexed.


4. Open Graph (OG) Tags

- Used mainly by social media platforms (Facebook, LinkedIn, X/Twitter) to display rich previews when links are shared.

```html
<meta property="og:title" content="Best Pizza Recipes">
<meta property="og:description" content="Discover delicious homemade pizza recipes with fresh ingredients.">
<meta property="og:image" content="https://example.com/pizza.jpg">
<meta property="og:url" content="https://example.com/pizza-recipes">
<meta property="og:type" content="article">
```


### - `<script>` attributes: `defer` vs `async`

- Let’s break down everything about the script tag, especially defer, async, and how scripts are imported and executed in the browser.

<!-- 1. <script> tag  -->

- used to load and execute javascript on a web page

```html
<script src="app.js"></script>
```

- what above does
    - pauses html parsing
    - downloads & executes the script immediately
    - then resumes rendering

- so these always block rendering 


2. defer attribute

```html
<script src="main.js" defer></script>
```

- behaviour: 
    - scripts downloads in parallel to html parsing
    - executes only after the html is fully parsed but before DOMContentLoaded
    - execution order is preserved

- Use when:
    - Your script depends on the DOM being ready
    - Scripts must execute in sequence
    - You want non-blocking but ordered execution


3. async attribute

```html
<script src="analytics.js" async></script>
```

- behavior:
    - script downloads in parallel with html parsing
    - exexutes as soon as it finishes downloading without waiting for html 
    - execution order is not guaranteed

✅ Use when:

Script is independent (no DOM or other script dependency)

Example: analytics, ads, or tracking scripts

```html
<script src="a.js" async></script>
<script src="b.js" async></script>

```

#### comparision

| Attribute | HTML Parsing | Script Download | Script Execution        | Execution Order | Use Case                   |
| --------- | ------------ | --------------- | ----------------------- | --------------- | -------------------------- |
| *(none)*  | Blocked      | Sequential      | Immediately when loaded | Preserved       | Inline or critical scripts |
| `defer`   | Continues    | Parallel        | After HTML parsing      | Preserved       | DOM-dependent scripts      |
| `async`   | Continues    | Parallel        | As soon as loaded       | Unpredictable   | Independent scripts        |


4. inline scripts

```html
<script>
  console.log("Hello world");
</script>
```

- runs immediately during parsing


5. ES Modules (type="module")

- Modern browsers support JavaScript modules, allowing import and export between files.

```html
<script type="module" src="main.js"></script>
```

- Automatically deferred (acts like defer by default)
- Supports imports and exports
- Each module has its own scope (not global)
- import paths must be absolute or relative URLs

```js
// main.js
import { greet } from './utils.js';
greet();
```

```js
// utils.js
export function greet() {
  console.log('Hello from module!');
}

```

7. Key Interview Insights

Which loads first — async or defer?
→ Both download in parallel.

async executes immediately when ready

defer waits until HTML parsing completes

What if both async and defer are present?
→ Browser will treat it as async (defer ignored).

How does DOMContentLoaded interact?

defer scripts run before DOMContentLoaded

async scripts may run before or after — unpredictable

Are module scripts blocking?
→ No, type="module" scripts are deferred by default.

What happens if you put scripts at the end of <body>?
→ Similar effect to defer: HTML is already parsed, so no blocking.


### - Storage: LocalStorage vs SessionStorage vs Cookies

All three store data in the browser — but differ in lifetime, scope, and usage.

| Feature             | **localStorage**                         | **sessionStorage**         | **Cookies**                                |
| ------------------- | ---------------------------------------- | -------------------------- | ------------------------------------------ |
| **Storage Limit**   | ~5–10 MB                                 | ~5 MB                      | ~4 KB                                      |
| **Persistence**     | Until manually cleared                   | Until browser/tab closes   | Can have expiration date                   |
| **Accessible From** | Any tab of same origin                   | Only current tab/window    | Both client (JS) and server (HTTP headers) |
| **Sent to Server?** | ❌ No                                     | ❌ No                       | ✅ Yes (on every request)                   |
| **API**             | `localStorage.getItem()`                 | `sessionStorage.getItem()` | `document.cookie`                          |
| **Use Case**        | Save user settings, tokens, caching data | Temporary UI state per tab | Authentication, session tracking           |


### - Shadow DOM and Web Components

- Web Components

A set of modern browser APIs that allow you to create reusable, encapsulated custom elements — like your own <date-picker> or <modal-dialog>.

They consist of:

Custom Elements – define your own tags.
Shadow DOM – encapsulates styles and DOM structure.
HTML Templates – reusable HTML chunks.


```js
class MyButton extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.innerHTML = `
      <style>
        button { background: purple; color: white; border: none; }
      </style>
      <button>Click Me</button>
    `;
  }
}
customElements.define('my-button', MyButton);
```


### Critical Rendering Path (CRP)

- The Critical Rendering Path is the sequence of steps the browser takes to convert HTML, CSS, and JS into pixels on the screen.
- It affects how fast your page becomes visible and interactive.

Steps : 
1. HTML Parsing -> DOM Tree
2. CSS Parsing -> CSSOM Tree
3. DOM + CSSOM -> Render Tree
4. Layout (calculate positiions / sizes)
5. Paint
6. Composite

- optimisation techniques
  - minimise render blocking
    - use link rel="preload" , script defer for js
  - reduce css complexity and size
  - inline critical css
  - lazy load images & non critical scripts
  - Use HTTP/2 or CDNs to reduce latency.

```html
<head>
  <link rel="preload" href="styles.css" as="style">
  <link rel="stylesheet" href="styles.css">
  <script src="main.js" defer></script>
</head>
```

Interview Question Angles

What blocks the CRP? → Render-blocking CSS/JS.

How to reduce First Paint / First Contentful Paint times?

How do async and defer differ?


### ⚙️ 1. <link rel="preload"> vs <link rel="prefetch">

Both are resource hints that instruct the browser how and when to load resources — but they serve different timing purposes.

| Feature                        | **preload**                                       | **prefetch**                                          |
| ------------------------------ | ------------------------------------------------- | ----------------------------------------------------- |
| **When used**                  | During current navigation (critical resources)    | For future navigations or routes (predictive loading) |
| **Priority**                   | **High** — blocks rendering if needed             | **Low** — background loading                          |
| **Use case**                   | Fonts, CSS, JS needed **immediately**             | Next-page assets, images, routes                      |
| **Browser behavior**           | Loads *now*, makes available in cache immediately | Loads *in background*, caches for later               |
| **Affects performance metric** | Improves **First Contentful Paint (FCP)**         | Improves **Subsequent Navigation** speed              |


```html
<!-- Preload: used for current page -->
<link rel="preload" href="/main.css" as="style">
<link rel="preload" href="/app.js" as="script">

<!-- Prefetch: used for next page -->
<link rel="prefetch" href="/next-page.js" as="script">

```

- as attribute tells the browser what kind of resource it is (important for prioritization & CORS).
- Misusing preload (too many) can actually hurt performance — it competes with critical resources.
- Common strategy: preload critical, prefetch future.


### 🧠 2. How Browsers Parse HTML → DOM

This is a core browser pipeline concept. The DOM (Document Object Model) isn’t “loaded all at once”; it’s built incrementally as the HTML is parsed.

1. HTML bytes received → converted to characters
2. Tokenizer: characters → tokens
  - Converts raw text into tokens like <html>, <div>, </p>.
3. Tree Constructor: tokens → DOM nodes
  - The tokens are converted into nodes and linked hierarchically into the DOM tree.
4. External resources
  - link and script>tags trigger resource fetching in parallel.
5. CSS Parsing
  - CSS is parsed into the CSSOM (CSS Object Model).
6. Render Tree
  - DOM + CSSOM → Render Tree, excluding non-visual nodes (like <head>, display: none).
7. Layout + Paint + Composite
  - Layout computes geometry, Paint fills pixels, and Composite merges layers into what you see.

IMP : 
  - A synchronous script tag halts parsing.
  - Use defer to execute after parsing or async to execute when downloaded.

### 🧩 3. CSR vs SSR — HTML Structures and Rendering Pipeline

- Client Side Rendering

Who renders HTML? The browser, using JavaScript (usually React/Vue).

1. Browser gets a minimal HTML skeleton:

```html
<body>
  <div id="root"></div>
  <script src="/bundle.js"></script>
</body>

```

2. JS executes, builds virtual DOM, and injects full UI dynamically. 
3. Initial load = blank screen → JS fetch → UI render.


Pros:

Great interactivity after load.

Easy routing and state management.

Efficient after first render.

Cons:

Slow first paint (FCP/TTI) — blank screen until JS runs.

Poor SEO if bots can’t execute JS (though Google can handle it now).

Large JS bundles hurt slow networks.

- Server Side Rendering

- Who renders HTML? The server.
  - Server generates fully rendered HTML string.


```html
<body>
  <div id="root">
    <h1>Welcome, Alice</h1>
    <p>Server rendered content</p>
  </div>
  <script src="/bundle.js"></script>
</body>

```
  
  - Browser displays meaningful content immediately.
  - JS “hydrates” the page — attaching event listeners and making it interactive.

Pros:

Fast initial render and SEO-friendly.

Better perceived performance.

Cons : 

Higher server load.

Slight delay during hydration (HTML → React).

Hybrid Models

SSR + Hydration (Next.js) → Pre-render + make interactive.

SSG (Static Site Generation) → Build once, serve static HTML (e.g., blogs).

ISR (Incremental Static Regeneration) → Update pages periodically without rebuilding all.

# 🎨 CSS — Layout, Architecture, and Optimization (Deep Dive)

## 🧱 Core Concepts

### 1. CSS Box Model
Every element in CSS is a rectangular box consisting of:
- **Content box** → where your content (text, image) lives.
- **Padding** → space between content and border.
- **Border** → surrounds the padding.
- **Margin** → space outside the border (separates elements).

**Box sizing:**
```css
/* Default */
box-sizing: content-box;

/* Includes padding & border in width/height */
box-sizing: border-box;
```
Using `border-box` avoids unexpected element size expansion when padding/border are added.

**Margin collapsing:**  
Adjacent vertical margins between block-level elements collapse into one — the largest of the two.

---

### 2. Flexbox
A one-dimensional layout system for **aligning items in a row or column**.

**Main properties:**
```css
display: flex;
flex-direction: row | column;
justify-content: flex-start | center | space-between;
align-items: stretch | center | flex-start;
gap: 10px;
```
- Great for navigation bars, aligning content vertically/horizontally, or equal-width columns.
- Flex items can grow/shrink using:
  ```css
  flex: grow shrink basis;
  ```

---

### 3. CSS Grid
Two-dimensional layout system (rows + columns).

**Example:**
```css
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: auto;
gap: 1rem;
```
Use `grid-area` for template-based layouts.  
Grid is preferred for page-level layouts, while Flexbox is for alignment within components.

---

### 4. Positioning
Defines how elements are placed in the document.

| Type | Description |
|------|--------------|
| `static` | Default; element follows normal flow |
| `relative` | Positioned relative to its normal position |
| `absolute` | Positioned relative to the nearest positioned ancestor |
| `fixed` | Positioned relative to viewport; stays fixed during scroll |
| `sticky` | Switches between `relative` and `fixed` based on scroll position |

`z-index` works **only** on positioned elements (`relative`, `absolute`, `fixed`, or `sticky`).

---

### 5. Specificity, Inheritance, Cascade Layers
**Specificity order:**
Inline styles > IDs > Classes > Elements  
`!important` overrides everything (use sparingly).

**Cascade layers (`@layer`)** (new CSS feature):
```css
@layer base, components, utilities;

@layer base {
  p { font-size: 16px; }
}
@layer components {
  .btn { color: white; }
}
```
Helps organize styles and manage specificity.

---

### 6. Pseudo-elements
Used to style parts of an element.

```css
p::before { content: "→ "; }
p::after { content: " ✓"; }
```
Common uses:
- Decorative icons
- Tooltips
- Custom list markers
- Skeleton loaders

---

### 7. Responsive Design & Media Queries
Designs adapt to screen size and device capabilities.

**Example:**
```css
@media (max-width: 768px) {
  .container { flex-direction: column; }
}
```
Use **mobile-first** approach:
- Start with small screens → scale up.

---

### 8. CSS Units
| Unit | Description |
|------|--------------|
| `px` | Absolute pixel |
| `%` | Relative to parent |
| `em` | Relative to element’s font size |
| `rem` | Relative to root (`html`) font size |
| `vh`, `vw` | Viewport height/width |
| `vmin`, `vmax` | Relative to smaller/larger viewport dimension |

`rem` is preferred for predictable scaling in responsive typography.

---

### 9. Transitions & Animations

**Transitions:**
```css
.element {
  transition: all 0.3s ease-in-out;
}
```
Smoothly animate property changes (e.g., hover effects).

**Keyframes:**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.loader { animation: spin 2s linear infinite; }
```
Use `transform` and `opacity` for smooth GPU-accelerated animations.

---

### 10. CSS Architecture & Methodologies

#### BEM (Block Element Modifier)
Improves readability and maintainability.
```css
.card {}
.card__title {}
.card--highlighted {}
```

#### CSS Modules
Scoped CSS per component (no naming collisions):
```css
.button { color: blue; }
```
Imported as:
```js
import styles from './button.module.css';
```

#### Styled Components (React)
CSS-in-JS approach:
```js
const Button = styled.button`
  background: blue;
  color: white;
`;
```

#### Tailwind CSS
Utility-first CSS framework:
```html
<div class="flex items-center justify-between p-4 bg-gray-800 text-white"></div>
```
Highly composable and eliminates the need for custom class naming.

---

### 11. Repaint vs Reflow (Render Performance)
**Reflow:** Layout recalculation when geometry changes (e.g., size, position).  
**Repaint:** Visual updates without layout changes (e.g., color, visibility).

- Reflows are more expensive than repaints.
- Avoid frequent DOM manipulations or layout-triggering properties (`offsetHeight`, `clientWidth`).
- Batch DOM changes using `requestAnimationFrame`.

---

## 🎯 Tricky Topics

### 1. `visibility: hidden` vs `opacity: 0` vs `display: none`

| Property | Element in Layout? | Clickable? | Triggers Reflow? |
|-----------|--------------------|-------------|------------------|
| `display: none` | ❌ No | ❌ No | ✅ Yes |
| `visibility: hidden` | ✅ Yes | ❌ No | ❌ No |
| `opacity: 0` | ✅ Yes | ✅ Yes | ❌ No |

Use `opacity: 0` for animations, `display: none` to completely remove element.

---

### 2. Why Avoid Inline Styles
- **No reusability** (cannot be shared across elements)
- **No media queries or pseudo-selectors**
- **Harder to override**
- **Bypasses CSS architecture systems (BEM, modules)**

Inline styles should only be used for dynamic JS-calculated values.

---

### 3. GPU Acceleration
Use transforms to offload rendering to GPU:
```css
will-change: transform, opacity;
transform: translateZ(0);
```
This promotes an element to its own GPU layer — smoother animations, especially for:
- Transforms (translate, rotate, scale)
- Opacity transitions

Be careful: overusing `will-change` or `translateZ(0)` increases memory usage.

---

## ⚙️ Optimization Tips

- Use **CSS variables** for consistent theming.
- Minimize CSS file size via **minification** and **unused CSS removal** (PurgeCSS).
- Prefer **composite properties** (`transform` + `opacity`) for animations.
- Load critical CSS inline (`<style>` in `<head>`), defer rest.
- Use **`content-visibility: auto;`** for lazy rendering off-screen content.

---

### 💡 Final Thought
CSS isn’t just about colors and fonts — it’s about controlling rendering, layout flow, and performance at the pixel level. Mastery comes when you understand *how browsers think* about your styles.



# HTML Basics

## Topic: HTML Basics  
### Sub Topic: Doctype, HTML Tree, Semantic Tags, Attributes, Comments

---

## 1. Doctype  
The **DOCTYPE** tells the browser which version of HTML the document uses.  
In modern HTML5, we simply use:

```html
<!DOCTYPE html>
```

It ensures the browser uses **standards mode**, not quirks mode.

---

## 2. HTML Tree (DOM Tree)  
When the browser reads HTML, it converts it into a **Document Object Model (DOM)** — a hierarchical tree-like structure.

Example structure:
```
html
 ├── head
 │     └── title
 └── body
       ├── header
       ├── main
       │      └── section
       └── footer
```

This tree allows JavaScript and CSS to access, modify, and style elements.

---

## 3. Semantic Tags  
Semantic tags describe **meaning**, not presentation.  
They help search engines, screen readers, and developers.

Common tags:

- `<header>` — top section of a page  
- `<nav>` — navigation links  
- `<main>` — primary content  
- `<section>` — grouped content  
- `<article>` — independent, self-contained content  
- `<aside>` — sidebar content  
- `<footer>` — bottom section  
- `<figure>` + `<figcaption>` — images with captions  

Semantic HTML improves accessibility (A11y) and SEO.

---

## 4. Attributes  
Attributes give extra information to an HTML element.

Examples:

```html
<img src="image.png" alt="Profile photo" width="200">
```

Common attributes:
- `id` — unique identifier  
- `class` — for styling and JS  
- `src` — source for media  
- `href` — link target  
- `alt` — alternative text  
- `type`, `value`, `name` — form attributes  

Attributes always appear in the **opening tag**.

---

## 5. Comments  
Comments help document your code. They are ignored by browsers.

```html
<!-- This is a comment -->
```

Useful for:
- Explanations  
- Debugging  
- Marking sections  

---

## Interview Questions (Theory)

1. **Why is the DOCTYPE needed?**  
   It tells the browser to use HTML5 standards mode for rendering.

2. **What is the DOM tree?**  
   A hierarchical structure created from HTML that browsers use to render and manipulate the page.

3. **Why use semantic tags?**  
   Better readability, SEO enhancements, accessibility improvements.

4. **Difference between `<div>` and semantic tags?**  
   `<div>` has no meaning; semantic tags convey structure and intent.

5. **Why is the `alt` attribute important?**  
   Helps screen readers and improves SEO; shows alternative text if the image fails.

6. **Can attributes be custom-defined?**  
   Yes, using `data-*` attributes for storing custom data.

7. **Are comments visible to users?**  
   No, only visible in source code; browsers ignore them.

8. **Difference between global and element-specific attributes?**  
   Global attributes (e.g., id, class) apply to all HTML tags; specific attributes apply only to certain tags.

---

## Coding Questions (Application Based)

### 1. Build a semantic layout:
```html
<!DOCTYPE html>
<html>
  <body>
    <header>My Website</header>
    <nav>Menu</nav>
    <main>
      <section>
        <article>
          <h1>Blog Title</h1>
        </article>
      </section>
    </main>
    <footer>Copyright 2025</footer>
  </body>
</html>
```

### 2. Create an accessible image tag:
```html
<img src="cat.png" alt="A small orange cat sitting on a laptop">
```

### 3. Example showing attributes + comments:
```html
<!-- Login form -->
<form action="/login" method="POST">
  <input type="text" name="email" placeholder="Enter email">
  <input type="password" name="password" placeholder="Password">
  <button type="submit">Login</button>
</form>
```

---

All necessary concepts are now covered comprehensively.


# Topic : Forms
## Sub Topic : `<form>`, input types, validation, accessibility, autocomplete, FormData

---

## 1. Quick Overview — What a web form is
A form is the HTML surface for collecting structured user input and sending it to a server or processing it client-side. Good forms are **usable**, **accessible**, and **robust** (works with JS off, validated server-side).

---

## 2. `<form>` element essentials
- `action` — URL to submit to. If omitted or empty (`""`) submits to current URL.
- `method` — `GET` (query string) or `POST` (request body). Use `POST` for mutations and file uploads.
- `enctype` — important for file uploads: `multipart/form-data`.
- `novalidate` — disable browser validation when you want custom handling.
- `target` — `_self`, `_blank`, iframe target.
- `autocomplete` — can be set on the form or individual inputs.

Example:
```html
<form action="/signup" method="post" enctype="multipart/form-data" autocomplete="on">
  ...
</form>
```

---

## 3. Common input types & their intended uses
- `text` — plain single-line text.
- `password` — obscured input.
- `email` — single email; browser can validate and show specialized keyboard on mobile.
- `tel` — phone numbers (no validation enforced).
- `url` — URL format check.
- `number` — numeric input; use `min`, `max`, `step`.
- `range` — slider for numeric ranges.
- `date`, `time`, `datetime-local`, `month`, `week` — date/time pickers (browser support variable).
- `checkbox` / `radio` — binary / mutually exclusive choices.
- `file` — file uploads; supports `multiple`.
- `textarea` — multi-line text.
- `select` — single/multiple choice lists.
- `hidden` — values not shown to user (be careful: modifiable client-side).

Example:
```html
<input type="email" name="email" required autocomplete="email" />
<input type="password" name="pwd" required minlength="8" />
<input type="file" name="resume" accept=".pdf,.docx" />
```

---

## 4. Client-side validation (HTML5 + JS)
### Native HTML5 attributes (first line of defense)
- `required`
- `min`, `max`, `step` (for numeric)
- `minlength`, `maxlength`, `pattern` (regex)
- `type` (email, url, number) triggers built-in checks
- `accept` (for file inputs)
- Constraint validation API: `input.checkValidity()`, `form.checkValidity()`, `input.setCustomValidity(msg)`, and `reportValidity()`.

### Custom JS validation
- Use `input.addEventListener('input', ...)` or `form.addEventListener('submit', e => { ... })`.
- Prevent submission with `e.preventDefault()` and show accessible error messages.
- Debounce expensive validations (e.g., network checks like username availability).

Example:
```js
form.addEventListener('submit', (e) => {
  if (!emailInput.checkValidity()) {
    e.preventDefault();
    emailInput.reportValidity(); // shows built-in message
  }
});
```

**Security note:** Client-side validation is for UX only — always validate server-side.

---

## 5. Accessibility (a11y) — make forms usable for everyone
- Always tie inputs to labels:
  ```html
  <label for="email">Email</label>
  <input id="email" name="email" />
  ```
  or wrap the input in the label:
  ```html
  <label>Email <input name="email"/></label>
  ```
- Group related controls with `<fieldset>` + `<legend>` (especially for radio groups).
- Provide clear error messages and link them to inputs with `aria-describedby`:
  ```html
  <input id="age" aria-describedby="age-err" />
  <div id="age-err" role="alert">Age must be &gt;= 18</div>
  ```
- Use `aria-invalid="true"` on invalid inputs.
- Ensure keyboard focus order and visible focus styles.
- For dynamic error updates, use `role="alert"` or `aria-live="polite"` regions.
- Avoid placeholders as substitutes for labels (placeholders are not persistent and harm accessibility).

---

## 6. Autocomplete — make forms faster and safer
- `autocomplete` attribute hints to browsers and password managers.
- Use standard tokens: `name`, `honorific-prefix`, `given-name`, `family-name`, `email`, `street-address`, `postal-code`, `cc-number`, `cc-exp` etc.
- Scoped example:
  ```html
  <input autocomplete="given-name" name="firstName" />
  <input autocomplete="family-name" name="lastName" />
  <input autocomplete="email" name="email" />
  ```
- For sensitive inputs you can set `autocomplete="off"` but browsers may ignore it for login fields.

---

## 7. FormData API & programmatic submission
- Construct `FormData` from form element: `const fd = new FormData(form)`.
- Works well with `fetch` for AJAX:
  ```js
  fetch('/upload', { method: 'POST', body: fd });
  ```
- Reading values:
  - `fd.get('name')`, `fd.getAll('tags')`, `fd.entries()` (iterate).
- For JSON APIs: build a plain object from entries then `JSON.stringify`.
- For files: `FormData` preserves `File` objects; do not convert files to base64 unless needed.

---

## 8. Progressive enhancement & server-side validation
- Provide working `<form>` with server endpoint — JS should enhance UX but not be required.
- Always re-validate and sanitize on server side.
- Rate-limit endpoints and verify file types & sizes server-side.

---

## 9. Patterns and best practices
- Keep inline validation helpful, not intrusive.
- Place labels above inputs for better scanning.
- Use explicit success/error states, and clear affordances for required fields (e.g., `* required`).
- Provide contextual help (tooltips) but not as the only source of critical info.
- For long forms, break into steps (save progress) and maintain accessibility.

---

## 10. Example: Accessible form with validation
```html
<form id="signup" action="/signup" method="post" novalidate>
  <label for="fn">First name</label>
  <input id="fn" name="firstName" autocomplete="given-name" required />

  <label for="em">Email</label>
  <input id="em" name="email" type="email" autocomplete="email" required />

  <fieldset>
    <legend>Subscription</legend>
    <label><input type="radio" name="plan" value="free" checked /> Free</label>
    <label><input type="radio" name="plan" value="pro" /> Pro</label>
  </fieldset>

  <div id="err" aria-live="polite"></div>

  <button type="submit">Sign up</button>
</form>

<script>
const form = document.getElementById('signup');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }
  const fd = new FormData(form);
  fetch(form.action, { method: form.method, body: fd })
    .then(r => /* handle */)
    .catch(err => console.error(err));
});
</script>
```

---

## 11. Interview-style Theory Questions (concise answers)
1. **Why use `enctype="multipart/form-data"`?**  
   Required when uploading files; it encodes files in the request body so servers can parse binary data.

2. **Difference between `GET` and `POST` in forms?**  
   `GET` encodes data in URL (limited length, bookmarkable), `POST` sends in body (suitable for sensitive or large data).

3. **What is `FormData` and when to use it?**  
   Browser API that serializes form fields and files for network submission; use when sending files or multipart data via `fetch`/XHR.

4. **What is the Constraint Validation API?**  
   Browser API (`checkValidity`, `setCustomValidity`, `reportValidity`) for programmatic control over native validation.

5. **How do you make forms accessible for screen readers?**  
   Use `<label>` for inputs, `<fieldset>`/`<legend>` for groups, `aria-describedby` for errors, `role="alert"` or `aria-live` for dynamic messages, and ensure keyboard operability.

6. **Why is server-side validation required if we have client-side validation?**  
   Client-side checks can be bypassed; server-side ensures data integrity and security.

7. **How does `autocomplete` improve or harm security?**  
   It improves UX by autofilling; it can expose sensitive data if a device is shared. Use tokens and `autocomplete="off"` selectively.

8. **What is the best pattern for showing field-level errors?**  
   Show concise inline message, attach to input with `aria-describedby`, mark `aria-invalid="true"`, and place `role="alert"`/`aria-live` for announcements.

---

## 12. Related coding / practical interview questions
1. **Implement custom password-strength meter in JS (explain events, debouncing, and accessibility).**  
2. **Write a function that converts a FormData instance to a JSON object, handling multiple values.**  
3. **Create an accessible custom radio-group component in React (keyboard navigation + ARIA).**  
4. **Handle file uploads in a form with client-side preview and size/type validation.**  
5. **Implement server-side validation sketch for common form inputs (email, username uniqueness, file validation).**

_Short sample: FormData -> JSON_
```js
function formDataToJson(fd) {
  const obj = {};
  for (const [key, val] of fd.entries()) {
    if (obj.hasOwnProperty(key)) {
      if (!Array.isArray(obj[key])) obj[key] = [obj[key]];
      obj[key].push(val);
    } else {
      obj[key] = val;
    }
  }
  return obj;
}
```

---

## 13. Quick checklist for production-ready forms
- [ ] Labels for all inputs
- [ ] Server-side validation
- [ ] Accessible error states
- [ ] Proper `enctype` for file uploads
- [ ] Use `autocomplete` tokens
- [ ] Rate limits on submit endpoint
- [ ] Tests for edge cases (empty values, large files)
- [ ] Mobile-friendly layout & keyboard usability

---

_End of cheat sheet_



# Topic : HTML5 APIs
## Sub Topic : LocalStorage, SessionStorage, Web Storage, IndexedDB, Web Workers

---

## Quick overview (what & when)
- **Web Storage (LocalStorage & SessionStorage)**: simple key-value string storage built on `window`.  
  - `localStorage`: persists across browser sessions (until explicitly cleared).  
  - `sessionStorage`: persists only for the current tab/window session.  
  - Best for small amounts of simple data (tokens, UI prefs). Not suitable for large binary blobs or complex queries.

- **IndexedDB**: a transactional, NoSQL-like object store in the browser for structured data (objects, indexes, large values).  
  - Good for offline apps, large datasets, binary objects (Blobs), and indexed queries.

- **Web Workers**: background threads for running JavaScript off the main UI thread.  
  - Use to offload expensive CPU work (parsing, compression, heavy loops) to keep UI responsive.
  - Communicate via `postMessage`. Supports transferable objects (ArrayBuffer) and SharedArrayBuffer (with constraints).

---

## API details & examples

### 1) localStorage / sessionStorage (Web Storage)
- Synchronous, string-only key → value store.
- Size limits vary by browser (~5-10MB typical).

**Basic usage**
```js
// localStorage
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme'); // "dark"
localStorage.removeItem('theme');
localStorage.clear(); // clear all keys

// sessionStorage
sessionStorage.setItem('draft', JSON.stringify({text:'hi'}));
```

**Storing non-strings**
```js
const obj = { name: 'Alice', age: 30 };
localStorage.setItem('user', JSON.stringify(obj));
const user = JSON.parse(localStorage.getItem('user'));
```

**Cross-tab sync (storage event)**
```js
window.addEventListener('storage', (e) => {
  if (e.key === 'someKey') {
    console.log('Updated in another tab:', e.newValue);
  }
});
```

**Caveats**
- Synchronous API can block the main thread if overused.
- Not secure for sensitive data (e.g., raw auth tokens) without additional protections.
- No indexing/querying, only exact key lookups.

---

### 2) IndexedDB (modern usage pattern)
- Asynchronous and transactional. Use Promises or wrappers (idb, dexie) for ergonomics.
- Data stored as structured clones (no functions; works with Objects, Arrays, Blobs).

**Open DB and create object store**
```js
function openDB(name='app-db', version=1) {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(name, version);
    req.onupgradeneeded = (e) => {
      const db = e.target.result;
      if (!db.objectStoreNames.contains('notes')) {
        const store = db.createObjectStore('notes', { keyPath: 'id', autoIncrement: true });
        store.createIndex('by_date', 'updatedAt');
      }
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}
```

**Add / get / query example**
```js
async function addNote(db, note) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('notes', 'readwrite');
    const store = tx.objectStore('notes');
    const req = store.add({...note, updatedAt: Date.now()});
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

async function getAllNotes(db) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('notes', 'readonly');
    const store = tx.objectStore('notes');
    const req = store.getAll();
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}
```

**When to use IndexedDB**
- Storing offline data for PWAs.
- Caching large assets (Blobs), images, search indexes.
- When you need queries, indexes, and transactions.

---

### 3) Web Workers (Dedicated worker)
**worker.js**
```js
// heavy compute (e.g., fibonacci)
self.onmessage = function(e) {
  const n = e.data;
  // naive example (CPU heavy)
  function fib(k) {
    if (k <= 1) return k;
    return fib(k-1) + fib(k-2);
  }
  const result = fib(n);
  postMessage(result);
};
```
**main thread**
```js
const worker = new Worker('worker.js');
worker.postMessage(40);
worker.onmessage = (e) => console.log('fib result', e.data);
```

**Transferable objects** (avoid copying)
```js
const buffer = new ArrayBuffer(1024*1024);
worker.postMessage(buffer, [buffer]); // buffer is transferred (neutered in main thread)
```

**SharedArrayBuffer**
- Allows shared memory between worker & main thread; requires COOP/COEP headers on your server and secure contexts.
- Use atomics for safe synchronization.

**Caveats**
- Workers have their own global scope (no `window`; `self` is global).
- DOM access is not available inside workers.
- Worker creation cost; reuse workers (worker pool) for repeated tasks.

---

## Theory-based interview questions (concise answers)
1. **What is the difference between localStorage and sessionStorage?**  
   localStorage persists across browser sessions; sessionStorage is per-tab and cleared on tab close. Both are string-only and synchronous.

2. **Is localStorage shared between tabs?**  
   Yes — same-origin tabs share localStorage. `storage` events notify other tabs (not the originator).

3. **Why is IndexedDB preferred over localStorage for large datasets?**  
   IndexedDB is asynchronous, supports structured objects, indexes, transactions and large binary objects. localStorage is synchronous and string-only.

4. **What is the structured clone algorithm?**  
   The algorithm used by postMessage, IndexedDB, and other APIs to duplicate objects across contexts. It supports objects, arrays, Blobs, typed arrays, Maps, Sets (with some limitations), but not functions or DOM nodes.

5. **Can you access the DOM from a Web Worker?**  
   No. Workers run in separate threads and cannot access DOM APIs. They communicate via `postMessage`.

6. **How do you store binary data in IndexedDB?**  
   Store `Blob` or `ArrayBuffer` objects directly; IndexedDB stores them via structured cloning.

7. **What are transferable objects and why use them?**  
   Transferable objects (like ArrayBuffer) move ownership to another context without copying, which is faster for large buffers.

8. **What’s a Service Worker vs Web Worker?**  
   Service Worker is a special worker that intercepts network requests and enables offline caching and background sync; it lives outside pages and can respond to fetch events. Web Workers are for general-purpose background computation tied to a page.

9. **How to avoid blocking the UI using Web Storage?**  
   Keep writes small and infrequent; for heavy data use IndexedDB (async) instead of synchronous Web Storage.

10. **How do you implement cross-tab locking (mutex) in the browser?**  
    Use BroadcastChannel or `localStorage` with atomic `storage` events and unique tokens (careful with race conditions). More robust: use IndexedDB with transactions to coordinate locks.

11. **How does IndexedDB versioning work?**  
    `indexedDB.open(name, version)` triggers `onupgradeneeded` when version increases, allowing schema migrations. Transactions in upgrade are versionchange transactions.

12. **What are quotas and how do browsers enforce storage limits?**  
    Browsers implement per-origin quotas (varies by engine). They may evict least-recently-used data or prompt users for permission for large storage. Exact policies differ by browser.

---

## Coding-based interview tasks & hints + sample solutions

### Task A — Sync theme between tabs using localStorage
**Spec:** Save `theme` to localStorage; when changed in one tab, update UI in others.
**Hint:** use `storage` event.
```js
// set theme
function setTheme(theme) {
  localStorage.setItem('theme', theme);
  applyTheme(theme);
}

// react to remote updates
window.addEventListener('storage', (e) => {
  if (e.key === 'theme') applyTheme(e.newValue);
});
```

### Task B — Save large number of notes offline using IndexedDB
**Spec:** Store notes with fields `{id, title, body, updatedAt}` and fetch latest 20 ordered by updatedAt.
**Hint:** create index on `updatedAt` and use a cursor in reverse order.
(Sample snippets in the main section above.)

### Task C — Offload image processing to a Web Worker
**Spec:** Resize an image in a worker using OffscreenCanvas (if available).
**Hint:** Transfer `ImageBitmap` or `ArrayBuffer` to worker; use `OffscreenCanvas` within worker to manipulate pixels.

### Task D — Implement simple cache with IndexedDB
**Spec:** Cache API responses (url → response blob). Check DB first, then network.
**Hint:** Use fetch, store response.clone().blob() in IndexedDB.

---

## Best practices & tips
- Prefer **IndexedDB** for large or complex data. Use wrappers (idb, dexie) to avoid callback hell.
- Avoid storing secrets in localStorage. Use httpOnly cookies for sensitive auth tokens.
- Keep writes to localStorage minimal (it's synchronous).
- Reuse workers; create worker pools for recurring tasks.
- Use `storage` and `BroadcastChannel` for cross-tab communication; `BroadcastChannel` is simpler for structured messages.
- Test storage limits and behavior across Chromium, Firefox, and Safari (Safari quotas differ).

---

## Further reading & libraries
- MDN Web Docs: localStorage, IndexedDB, Web Workers (search on MDN).  
- Libraries: `idb` (tiny promise wrapper for IndexedDB), `dexie.js` (full-featured wrapper).

---

## Quick interview checklist (one-liners you can say)
- LocalStorage/sessionStorage synchronous, string-only.  
- IndexedDB async, transactional, supports blobs and indexes.  
- Web Workers = no DOM, use postMessage and transferable objects.  
- Use Service Workers for request caching & offline strategies.  
- Use BroadcastChannel for cross-tab structured messaging.

---

*Prepared for interview revision — concise, with examples and coding tasks.*

# Media Tags in HTML5  
## Topic: Media Tags  
## Sub Topic: `<video>`, `<audio>`, `<picture>`, `<source>`, Attributes like `controls` / `autoplay`

---

## 1. Detailed Explanation

### `<video>`
The `<video>` tag embeds video content in a webpage.  
It supports multiple formats like MP4, WebM, Ogg.

**Common attributes:**
- **controls** — shows play/pause UI.
- **autoplay** — video plays automatically.
- **muted** — required for autoplay in modern browsers.
- **loop** — repeats video.
- **poster** — image shown before video loads.
- **width/height** — size of video.

**Example:**
```html
<video src="movie.mp4" controls autoplay muted width="400"></video>
```

---

### `<audio>`
Used to embed audio files (MP3, WAV, Ogg).

**Attributes:**
- controls  
- autoplay  
- loop  
- muted  

**Example:**
```html
<audio controls>
  <source src="song.mp3" type="audio/mpeg" />
</audio>
```

---

### `<picture>`
Responsive image tag: loads different images depending on screen size or resolution.

Useful for:
- mobile vs desktop  
- retina images  
- art direction  

**Example:**
```html
<picture>
  <source srcset="large.jpg" media="(min-width: 800px)">
  <source srcset="small.jpg" media="(max-width: 799px)">
  <img src="fallback.jpg" alt="Example image">
</picture>
```

---

### `<source>`
Defines alternative media sources for `<video>`, `<audio>`, or `<picture>`.

**Example inside `<video>`:**
```html
<video controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.webm" type="video/webm">
</video>
```

---

### Common Media Attributes

| Attribute | Meaning |
|----------|---------|
| controls | Shows default UI |
| autoplay | Starts playing automatically |
| muted | Mutes media (required for autoplay) |
| loop | Replays automatically |
| preload | `none`, `metadata`, `auto` |
| poster | Video placeholder image |

---

## 2. Theory-Based Interview Questions + Concise Answers

**1. Why do we use multiple `<source>` tags inside `<video>` or `<audio>`?**  
Browsers support different codecs. Multiple sources ensure maximum compatibility.

**2. Why is muted required for autoplay?**  
Browsers block autoplay with sound to avoid bad UX. Muted autoplay is permitted.

**3. What is the purpose of the `<picture>` element?**  
For responsive images and art direction—serves different images depending on screen conditions.

**4. Difference between `<img>` and `<picture>`?**  
`<img>` loads a single image; `<picture>` can load conditionally different images.

**5. What is `preload` and when is it used?**  
Tells browser how much data to load before playback. Good for performance tuning.

**6. Does `<audio>` support a poster attribute?**  
No, only `<video>` supports poster.

**7. Why use `<source type="">`?**  
Helps browser pick the correct file based on MIME type.

---

## 3. Coding-Based Questions

### Q1: Create a responsive image setup where mobile loads `small.jpg` and desktop loads `large.jpg`.
```html
<picture>
  <source srcset="large.jpg" media="(min-width: 768px)">
  <img src="small.jpg" alt="Device responsive image">
</picture>
```

### Q2: Build a media player with fallback text.
```html
<video controls width="500">
  <source src="trailer.mp4" type="video/mp4">
  <source src="trailer.webm" type="video/webm">
  Your browser does not support HTML5 video.
</video>
```

### Q3: Audio player with autoplay + loop (muted required for autoplay).
```html
<audio autoplay loop muted>
  <source src="bgtrack.mp3" type="audio/mpeg">
</audio>
```

---

This cheat sheet covers all essential interview-ready concepts of HTML5 media tags and attributes.


# Semantic HTML Cheat Sheet

## Topic: Semantic HTML  
## Sub Topic: header, main, footer, article, section, nav, aside

Semantic HTML gives meaningful structure to a webpage. Browsers, search engines, and assistive technologies understand pages better when semantic tags are used correctly.

---

## 1. Semantic Tags Explained

### `<header>`
Defines introductory content for a page or section.  
Often contains logo, navigation, page title.

### `<main>`
Represents the primary content of the document.  
Only one `<main>` per page.

### `<footer>`
Contains ending information like copyright, links, author info, or contact details.

### `<article>`
Represents a self-contained piece of content that can stand on its own.  
Examples: blog posts, comments, news cards.

### `<section>`
Groups related content within a page.  
A section usually has a heading.

### `<nav>`
Contains navigation links—site menus, table of contents, pagination.

### `<aside>`
Represents content indirectly related to the main content.  
Examples: sidebars, ads, related links.

---

## 2. Interview‑Style Theory Questions (With Short Answers)

**1. What is semantic HTML?**  
Semantic HTML uses descriptive tags that convey meaning about the content structure.

**2. Why use semantic HTML?**  
Improves accessibility, SEO, maintainability, and helps browsers understand content.

**3. Difference between `<section>` and `<article>`?**  
`<article>` is independent content; `<section>` groups related content but isn’t standalone.

**4. Can a page have multiple `<header>` tags?**  
Yes, each section or article can have its own header.

**5. Can `<main>` be nested?**  
No. There must be exactly one `<main>` and it cannot be nested inside other elements like header or footer.

**6. What goes inside `<nav>`?**  
Major navigation links such as menus, tables of contents, pagination.

**7. When to use `<aside>`?**  
For supplementary or tangential content like sidebars or ads.

**8. Is semantic HTML important for SEO?**  
Yes. Search engines understand page hierarchy better.

**9. Does `<div>` lose meaning compared to semantic tags?**  
`<div>` has no semantic meaning; semantic elements improve clarity.

**10. Are semantic tags important for screen readers?**  
Yes. Assistive tools rely on semantic structure for navigation.

---

## 3. Coding Questions Related to Semantic HTML

### **Q1. Create a webpage layout using semantic HTML.**
```html
<body>
  <header>
    <h1>My Blog</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/posts">Posts</a>
    </nav>
  </header>

  <main>
    <article>
      <h2>Post Title</h2>
      <p>This is an article.</p>
    </article>

    <aside>
      <h3>Related Links</h3>
      <ul>
        <li><a href="#">Another post</a></li>
      </ul>
    </aside>
  </main>

  <footer>© 2025 Harshith</footer>
</body>
```

### **Q2. Build multiple articles with sections inside.**
```html
<article>
  <header><h2>HTML Basics</h2></header>
  <section>
    <h3>Elements</h3>
    <p>Everything is an element.</p>
  </section>
  <section>
    <h3>Attributes</h3>
    <p>Attributes modify elements.</p>
  </section>
</article>
```

### **Q3. Create a navigation menu using `<nav>`.**
```html
<nav>
  <ul>
    <li><a href="#intro">Intro</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
```

---

This completes the cheat sheet for Semantic HTML.


# Meta Tags Cheat Sheet

## 1. Meta Charset
Defines the character encoding of the document.

```html
<meta charset="UTF-8">
```

## 2. Viewport Meta Tag
Controls layout on mobile browsers.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## 3. SEO Meta Tags
Used for search engine optimization.

```html
<meta name="description" content="This is a sample description for SEO.">
<meta name="keywords" content="HTML, Meta Tags, SEO">
<meta name="author" content="Your Name">
```

### Common SEO Tags
- **description** → summary of the page (very important for ranking & CTR)
- **keywords** → mostly ignored by modern search engines, but still used sometimes
- **robots** → control indexing  
```html
<meta name="robots" content="index, follow">
```

## 4. Open Graph (OG) Tags
Used for social media previews (Facebook, LinkedIn, Twitter/X uses them too).

```html
<meta property="og:title" content="Website Title">
<meta property="og:description" content="Short preview description">
<meta property="og:image" content="https://example.com/image.png">
<meta property="og:url" content="https://example.com">
<meta property="og:type" content="website">
```

## 5. Favicons
Icons shown in browser tabs, bookmarks, and devices.

```html
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

### Multiple Sizes Example
```html
<link rel="icon" sizes="32x32" href="/favicon-32.png">
<link rel="icon" sizes="16x16" href="/favicon-16.png">
```

---

# Interview Theory Questions (with concise answers)

### 1. Why do we use the viewport meta tag?
It ensures responsive design by making the layout fit the device width and prevents zooming issues on mobile screens.

### 2. What is the purpose of `<meta charset="UTF-8">`?
It sets the character encoding, allowing the page to correctly display most languages and symbols.

### 3. What are Open Graph tags?
They provide rich social media previews with title, description, image, and URL.

### 4. What is the `description` meta tag used for?
It gives search engines a summary of the page and influences click-through rates.

### 5. Do keywords meta tag impact SEO today?
Search engines mostly ignore them; they are rarely used now.

### 6. What does robots meta tag do?
Controls whether search engines index the page or follow links.

### 7. Why are favicons important?
They improve branding and user experience by showing your icon on tabs, bookmarks, and mobile screens.

---

# Coding Examples

## Adding all essential meta tags in a single HTML boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="A complete meta tags example page.">
  <meta name="robots" content="index, follow">

  <!-- Open Graph -->
  <meta property="og:title" content="My Website">
  <meta property="og:description" content="This is a preview description.">
  <meta property="og:image" content="https://example.com/preview.png">
  <meta property="og:url" content="https://example.com">

  <!-- Favicons -->
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">

  <title>Meta Tags Example</title>
</head>
<body>
  <h1>Meta Tags Demo Page</h1>
</body>
</html>
```

Topic : Accessibility
Sub Topic : ARIA roles, alt text, tabindex, screen readers

---

# Accessibility Cheat Sheet — ARIA roles, alt text, tabindex, screen readers
A compact interview-ready cheat sheet covering practical guidance, common pitfalls, quick examples, theory Q&A, and coding tasks (with short solutions). Designed to be copy-pasteable into notes or an interview repo.

---

## 1. Core concepts (quick overview)
- **Accessibility (a11y)**: designing so people with disabilities can perceive, understand, navigate, and interact with the web.
- **Semantic HTML**: always prefer native elements (`<button>`, `<a>`, `<form>`, `<header>`, etc.). They have built-in accessibility.
- **WAI-ARIA**: provides roles, states, and properties for communicating UI semantics when native HTML is insufficient.
- **Assistive technologies (AT)**: screen readers (NVDA, VoiceOver, JAWS), screen magnifiers, switch devices, etc.

---

## 2. ARIA roles — when & how to use
- **Rule of thumb**: Use ARIA only when semantic HTML can't express the intent.
- **Common roles**:
  - `role="button"`, `role="link"`, `role="navigation"`, `role="main"`, `role="dialog"`, `role="alert"`, `role="status"`.
  - Landmark roles: `banner`, `navigation`, `main`, `complementary`, `contentinfo`.
- **Examples**:

```html
<!-- Prefer native element -->
<button>Save</button>

<!-- Only use role when using non-semantic element (avoid if possible) -->
<div role="button" tabindex="0" aria-pressed="false">Toggle</div>
```

- **Accessible widgets**: If you implement custom widgets (tabs, accordions, comboboxes), mirror ARIA patterns from WAI-ARIA Authoring Practices, including keyboard behavior.

---

## 3. `alt` text — short, useful guidance
- **Purpose**: convey the content/meaning of an image to users who cannot see it.
- **Guidelines**:
  - If image is **decorative**, use `alt=""` (empty) and consider `role="presentation"` (or CSS background-image for purely decorative cases).
  - If image conveys content, describe its **meaning** succinctly. Focus on purpose, not pixel details.
  - For complex images (charts), provide a longer description nearby or via `aria-describedby`/`longdesc` (or a visible caption).

**Examples**:
```html
<img src="logo.png" alt="ACME financial services logo">
<img src="hero.jpg" alt="Smiling people in front of a product display at a conference">
<img src="pattern.png" alt=""> <!-- decorative -->
```

---

## 4. `tabindex` and keyboard focus
- **`tabindex="0"`**: element becomes focusable in natural tab order.
- **`tabindex="-1"`**: element is programmatically focusable (via `.focus()`), but not in tab order.
- **`tabindex="N>0"`**: DO NOT USE in most cases — it creates confusing focus orders.
- **Prefer** native focusable elements. Only add `tabindex` to non-focusable elements when you must.

**Best practices**:
- Keep a logical document order so tab traversal makes sense.
- For single-page apps, manage focus on route/dialog changes: move focus to the page heading or dialog container.
- Use `:focus-visible` for visible focus styles (when supported) and provide clear focus outlines.

Example — moving focus to a modal:
```js
const modal = document.getElementById('modal');
modal.setAttribute('aria-hidden', 'false');
modal.focus(); // make sure modal has tabindex="-1" or is focusable
```

---

## 5. Screen readers — practical tips
- **Common screen readers**: NVDA (Windows, free), VoiceOver (macOS/iOS), JAWS (Windows, paid).
- **Testing advice**:
  - Use keyboard-only navigation daily while developing.
  - Test with NVDA + Firefox (Windows) and VoiceOver + Safari (mac/macOS/iOS).
  - Test dynamic updates: use `role="status"`, `aria-live="polite"/"assertive"` for announcements.
- **VoiceOver quick check**: Turn VoiceOver on and try navigating headings (`H`), links (`L`), forms (`Form` rotor), and reading order.

---

## 6. Common mistakes and how to fix them
- Using `role` that conflicts with native element (e.g., `<button role="link">`) — avoid.
- Missing keyboard event handlers on `div role="button"` — must implement `Enter` and `Space` key handling.
- Overusing ARIA instead of semantic HTML.
- Not managing focus when opening/closing modals or navigating client-side routes.
- Not providing `alt` or providing redundant `alt` like `"image of logo"`.

---

## 7. Quick ARIA attributes cheat
- `aria-hidden="true"` — hide from AT (use carefully).
- `aria-live="polite|assertive"` — announce dynamic content.
- `aria-checked`, `aria-pressed`, `aria-expanded` — reflect widget state.
- `aria-describedby` — reference explanatory text.
- `aria-labelledby` — label an element by another element's text.

---

## 8. Interview-style theory questions (concise answers)
1. **What is the difference between semantic HTML and ARIA?**
   - Semantic HTML provides native semantics and keyboard support; ARIA supplements semantics when native HTML is insufficient.

2. **When should you use `aria-hidden`?**
   - Use to hide purely decorative or duplicate content from AT; avoid hiding interactive elements unless you also disable interaction.

3. **Explain `tabindex` values and their use-cases.**
   - `0`: include in tab order; `-1`: programmatically focusable only; positive: avoid. Prefer native elements.

4. **What is `aria-live` and when to use it?**
   - Tells AT to announce content changes in that region. Use for notifications, error summaries, dynamic content updates.

5. **How do you make a non-semantic element act like a button?**
   - Add `role="button"`, `tabindex="0"`, and keyboard handlers for `Enter` and `Space`, and manage `aria-pressed`/`aria-expanded` if applicable. Still prefer `<button>`.

6. **What should `alt` text contain?**
   - A succinct description of the image's meaning or function. Empty `alt` for decorative images.

7. **How to make accessible modals?**
   - Trap focus inside modal, restore focus on close, set `aria-modal="true"`, provide an accessible label (`aria-labelledby`) and `role="dialog"`.

8. **Difference between `aria-labelledby` and `aria-label`?**
   - `aria-labelledby` references visible element(s) by id for the label; `aria-label` provides a string label not visible on-screen.

9. **What are live regions and types?**
   - `aria-live` regions; `polite` waits for natural pause, `assertive` interrupts. Use sparingly.

10. **How to test accessibility in CI?**
   - Use automated linters (axe-core, eslint-plugin-jsx-a11y), static checks, and include sample axe runs in end-to-end tests (Playwright, Cypress with axe).

11. **Why avoid `tabindex` with positive integers?**
   - It creates an unnatural and hard-to-maintain focus order that differs from DOM order.

12. **What does `role="presentation"` do?**
   - Removes semantic meaning from an element for AT; used for decorative constructs where semantics would confuse.

---

## 9. Coding-style questions & short solutions (React + plain JS)

### Q1 — Make an accessible toggle button in React
**Prompt**: Implement a toggle that is keyboard accessible and announces state.

```jsx
// AccessibleToggle.jsx
import React, { useState } from 'react';
export default function AccessibleToggle() {
  const [on, setOn] = useState(false);
  return (
    <button
      aria-pressed={on}
      onClick={() => setOn(!on)}
    >
      {on ? 'On' : 'Off'}
    </button>
  );
}
```

Notes: Use native `<button>`; `aria-pressed` exposes state to AT.

---

### Q2 — Accessible image with long description
**Prompt**: Image that needs a verbose description.

```html
<figure>
  <img src="chart.png" alt="Quarterly sales chart, text summary below" />
  <figcaption id="chart-desc">Q1: 10k, Q2: 12k, Q3: 9k, Q4: 15k — overall growth 25% year-over-year.</figcaption>
</figure>
```

Or use `aria-describedby="chart-desc"` on the `<img>`.

---

### Q3 — Custom keyboard-focus trap (modal) plain JS
```js
function trapFocus(modal) {
  const focusable = modal.querySelectorAll('a[href], button, textarea, input, select, [tabindex]:not([tabindex="-1"])');
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  });
}
```

---

### Q4 — Linting & automated checks (example command)
- Add `axe-core` or `eslint-plugin-jsx-a11y` in CI.

Example (npm script):
```json
"scripts": {
  "test:a11y": "node ./scripts/run-axe.js"
}
```

---

### Q5 — Accessible custom dropdown basics (React sketch)
- Use `role="listbox"` + `role="option"`, manage `aria-activedescendant`, keyboard handlers (Up/Down/Enter/Escape), and ensure focus is on a combobox/button.

---

## 10. Tools & resources
- WAI-ARIA Authoring Practices — patterns for accessible widgets.
- MDN Accessibility docs.
- axe (Deque) — runtime accessibility testing.
- Lighthouse accessibility audits — quick checks but not comprehensive.
- NVDA (Windows), VoiceOver (macOS/iOS) — manual testing.

---

## 11. Quick checklist for PR reviews
- Are native elements used where possible?
- Do images have meaningful `alt` or empty `alt` if decorative?
- Are interactive elements keyboard accessible and focusable?
- Is focus managed for modals and route changes?
- Any ARIA roles/properties used — are they necessary and correct?
- Are dynamic updates announced (if needed)?
- Do color choices meet contrast requirements?

---

## 12. Short actionable tips — one-liners
- Use a real `<button>` instead of `div role="button"` 99% of the time.
- Empty `alt` overrides are valid and important for decorative images.
- Do not rely on automated tools alone — manual testing is essential.

---

# HTML Rendering: How Browsers Parse HTML into DOM, Reflow, Repaint

## Topic: HTML Rendering  
## Sub Topic: Browser Parsing → DOM, Reflow, Repaint

---

## 1. How Browsers Parse HTML into the DOM

Browsers read HTML as a stream of characters. This stream goes through several stages:

### Tokenization  
The HTML text is chopped into meaningful units: tags, attributes, text nodes.  
The tokenizing algorithm is strictly defined by the HTML spec.

### Tree Construction  
Tokens become **nodes**, and nodes form the **DOM Tree** (Document Object Model).  
DOM is a live, in‑memory representation of the HTML document.

Example:  
```html
<div id="root">
  <p>Hello</p>
</div>
```
Becomes a node tree:
- Document  
  └─ HTML  
     └─ Body  
        └─ Div#root  
           └─ P → "Hello"

### CSS Parsing → CSSOM  
CSS is parsed separately into its own tree: **CSSOM (CSS Object Model)**.

### Render Tree  
The browser combines DOM + CSSOM to create the **Render Tree**, which contains only *visible* nodes.  
Nodes like `<head>` or `display: none` elements don't appear in this tree.

### Layout (Reflow)  
The browser determines the geometry of each visible node:  
size, position, box model.

### Painting  
Pixels are filled: colors, borders, text, shadows.

### Compositing  
Layers (like those with transforms, opacity, etc.) are merged on the GPU.

---

## 2. Reflow (Layout)

Reflow happens when layout information must be recalculated.

Triggers include:
- Changing DOM structure (adding/removing nodes)
- Changing CSS layout properties (width, height, margin)
- Resizing window
- Changing font size
- Getting layout measurements (`offsetHeight`, `getBoundingClientRect`, etc.)

Reflow is expensive because layout changes can cascade across the entire document.

---

## 3. Repaint

Repaint happens when *visual appearance* changes but geometry is unaffected:
- background-color
- color
- visibility changes
- outline

Repaint is cheaper than reflow because it doesn’t recalc layout—just redraws.

---

## 4. Rendering Pipeline Summary

HTML → Tokens → DOM  
CSS → CSSOM  
DOM + CSSOM → Render Tree  
Render Tree → Layout (Reflow)  
Layout → Paint  
Paint → Compositing → Screen

---

## 5. Theory Interview Questions (Concise Answers)

### 1. What is DOM?
A tree representation of the HTML document where each element is a node.

### 2. What is CSSOM?
A tree representation of parsed CSS used for styling.

### 3. What is the Render Tree?
A combination of DOM + CSSOM containing only visible nodes.

### 4. What causes reflow?
Changes to layout—DOM insertions, size changes, reading layout properties, window resize.

### 5. What causes repaint?
Changes to visual style without affecting layout—color, background, border changes.

### 6. Why is reflow more expensive?
Because it can force recalculation of layout for large parts of the page.

### 7. What is compositing?
The GPU assembles layers (e.g., position: fixed, transforms) into the final screen output.

### 8. What operations are layout‑thrashing?
Repeatedly reading layout (`offsetTop`) and writing layout (changing style) in a loop.

### 9. How to avoid unnecessary reflows?
Batch DOM changes, use DocumentFragment, avoid forced synchronous layout reads, prefer CSS transforms.

### 10. What is critical rendering path?
The sequence of steps needed to convert HTML/CSS/JS into pixels on screen.

---

## 6. Related Coding Questions

### Q1: Example – Triggering Reflow in JavaScript  
```js
const box = document.getElementById("box");

// Reflow is forced here because we read layout
const height = box.offsetHeight;

// Then we write layout → costly
box.style.height = (height + 10) + "px";
```

### Q2: How to batch DOM writes to avoid layout thrashing?  
```js
const box = document.getElementById("box");

requestAnimationFrame(() => {
  box.style.width = "200px";
  box.style.height = "200px";
});
```

### Q3: Using DocumentFragment to avoid multiple reflows  
```js
const frag = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  const item = document.createElement("div");
  item.textContent = "Node " + i;
  frag.appendChild(item);
}
document.body.appendChild(frag); // Only one reflow
```

### Q4: CSS that avoids reflow but triggers repaint (safe optimization)
```css
.box:hover {
  background-color: blue;
}
```

---

## End


# Script Tags Cheat Sheet  
## Topic: Scripting  
## Sub Topic: `<script>` attributes (async, defer), module scripts, noscript  

---

## 1. Detailed Explanation

### 1. `<script>` Attributes: `async`, `defer`
Browsers normally stop parsing HTML to download and execute scripts. These attributes change that behavior.

**async**  
The script is downloaded in parallel with HTML parsing and executed immediately when ready. Parsing pauses only at execution time.  
Useful for: independent scripts like ads, analytics.

**defer**  
The script is downloaded in parallel but executed only after the entire HTML is parsed, in the order they appear.  
Useful for: DOM-dependent scripts and when maintaining execution order.

Comparison table:

| Attribute | Download | Execution | Order Guaranteed? | Use Case |
|----------|----------|-----------|--------------------|----------|
| None     | Blocking | Immediately | Yes | Legacy scripts |
| async    | Parallel | Immediately when ready | No | Independent scripts |
| defer    | Parallel | After HTML parsing | Yes | DOM-driven scripts |

---

### 2. Module Scripts: `type="module"`
Adds ES modules to HTML.

Key features:
- Supports `import` and `export`.
- Automatically deferred (executed after parsing).
- Loaded in strict mode.
- Separate execution scope (variables don’t pollute global namespace).
- Can load other modules dynamically.

Example:
```html
<script type="module">
  import { greet } from "./utils.js";
  greet();
</script>
```

---

### 3. `<noscript>`
Displayed only when:
- JavaScript is disabled.
- Browser doesn’t support scripting.

Useful for:
- Fallback UI.
- SEO crawl-friendly content.

Example:
```html
<noscript>
  JavaScript is disabled. Please enable it for full functionality.
</noscript>
```

---

## 4. Theory-Based Interview Questions (with concise answers)

### 1. What is the difference between `async` and `defer`?
Async executes the moment the script is ready, defer waits until HTML is parsed and preserves order.

### 2. Why do module scripts load in strict mode?
ES modules enforce strict mode to avoid silent errors and provide cleaner semantics.

### 3. When would you use `<noscript>`?
To show fallback content or messaging when JavaScript is disabled or unsupported.

### 4. Can `async` scripts maintain execution order?
No. Execution order depends on download completion.

### 5. Do module scripts block HTML parsing?
No, they behave like `defer` and execute after parsing.

---

## 5. Coding-Based Questions

### 1. Load two scripts where the first must run before the second.
```html
<script defer src="a.js"></script>
<script defer src="b.js"></script>
```

### 2. Example of dynamically importing a module.
```js
import('./math.js').then(mod => {
  console.log(mod.add(2, 3));
});
```

### 3. A script that must not block but must run after DOM is ready.
```html
<script defer src="main.js"></script>
```

---

# Shadow DOM / Web Components — Interview Cheat Sheet

## Topic: Shadow DOM / Web Components  
## Sub Topic: custom elements, shadowRoot, template tag, slot

---

## 1. Shadow DOM & Web Components (Detailed Explanation)

Web Components are browser-native building blocks for creating reusable, encapsulated UI elements without frameworks. Three main pieces team up here: **Custom Elements**, **Shadow DOM**, and **HTML Templates**.

### Custom Elements  
These let you define your own HTML tags like `<user-card>` or `<emoji-toggle>`.  
A custom element extends `HTMLElement` and implements lifecycle callbacks such as `connectedCallback()` and `attributeChangedCallback()`.

Example:  
```js
class MyCard extends HTMLElement {
  connectedCallback() {
    this.innerHTML = "Hello from custom element!";
  }
}
customElements.define("my-card", MyCard);
```

### Shadow DOM  
Shadow DOM creates an isolated subtree—essentially a private DOM island that lives inside a component. Styles and structure inside the shadow root do not leak outside, and external styles don’t bleed in.

Creation:  
```js
this.attachShadow({ mode: "open" });
```

Two modes:  
- **open** → shadowRoot accessible via `.shadowRoot`  
- **closed** → shadowRoot is hidden from outside access

Encapsulation is the star here. It keeps your component predictable regardless of global CSS chaos.

### Template Tag  
`<template>` is inert HTML—browser parses it but doesn’t render it until you clone and insert it. Useful for structuring UI for components.

Example:  
```html
<template id="card-template">
  <style>
    .box { padding: 10px; border: 1px solid #ccc; }
  </style>
  <div class="box">
    <slot></slot>
  </div>
</template>
```

### Slot  
Slots let users project their own content into your Web Component.

Example in custom element:  
```html
<my-card>
  <p>This gets slotted inside!</p>
</my-card>
```

---

## 2. Theory-Based Interview Questions (Concise Answers)

**1. What is Shadow DOM?**  
A scoped DOM tree inside a component, providing style & structure encapsulation.

**2. Why do we need Custom Elements?**  
To define reusable, self-contained, framework-agnostic UI components.

**3. Difference between open and closed shadow DOM?**  
Open: shadowRoot accessible via JS. Closed: hidden from outside, truly private.

**4. What is the purpose of the template tag?**  
Defines inert markup that can be cloned and inserted later.

**5. What are slots?**  
Content placeholders inside Shadow DOM enabling content projection.

**6. Do styles inside shadow DOM leak out?**  
No. Styles are scoped and encapsulated.

**7. What is the lifecycle of a custom element?**  
`constructor`, `connectedCallback`, `disconnectedCallback`, `attributeChangedCallback`.

**8. Can Shadow DOM contain its own styles?**  
Yes—styles inside shadowRoot apply only within it.

---

## 3. Coding-Based Questions & Examples

### Q1. Create a simple Web Component with Shadow DOM and slot.
```js
class SimpleCard extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: "open" });

    shadow.innerHTML = `
      <style>
        .card { padding: 12px; background: #f7f7f7; border-radius: 8px; }
      </style>
      <div class="card">
        <slot></slot>
      </div>
    `;
  }
}

customElements.define("simple-card", SimpleCard);
```

Usage:
```html
<simple-card>Content inside the card</simple-card>
```

---

### Q2. Create a component using `<template>` cloning.
```html
<template id="btn-template">
  <style>
    button { padding: 8px 12px; cursor: pointer; }
  </style>
  <button><slot></slot></button>
</template>

<script>
class MyButton extends HTMLElement {
  constructor() {
    super();
    const template = document.getElementById("btn-template");
    const clone = template.content.cloneNode(true);
    const shadow = this.attachShadow({ mode: "open" });
    shadow.appendChild(clone);
  }
}
customElements.define("my-button", MyButton);
</script>
```

---

### Q3. Shadow DOM styling test: internal styles vs global styles.
```js
shadow.innerHTML = `
  <style>
    p { color: red; }
  </style>
  <p>This is always red, global CSS won't override it.</p>
`;
```

---

### Q4. Custom element with observed attributes.
```js
class RatingStar extends HTMLElement {
  static get observedAttributes() { return ["count"]; }

  attributeChangedCallback(name, oldVal, newVal) {
    this.shadowRoot.querySelector(".stars").textContent = "⭐".repeat(newVal);
  }

  connectedCallback() {
    this.attachShadow({ mode: "open" });
    this.shadowRoot.innerHTML = `<div class="stars"></div>`;
  }
}
customElements.define("rating-star", RatingStar);
```

---

Need more sections added to the Web Components sheet? You can extend this foundation into design patterns, accessibility rules, or performance tuning for large UI libraries.


# CSS Fundamentals Cheat Sheet
## Selectors, Combinators, Specificity, Inheritance, Cascade

### 1. Selectors
Selectors tell the browser *which* elements to style.

- **Type selector**: `div`, `p`, `span`
- **Class selector**: `.box`
- **ID selector**: `#main`
- **Attribute selector**: `input[type="text"]`
- **Universal selector**: `*`
- **Pseudo-class**: `a:hover`, `input:focus`
- **Pseudo-element**: `p::before`, `::marker`

### 2. Combinators
Combinators define relationships between selectors.

- **Descendant (`A B`)**: Selects B *inside* A  
  Example: `div p`
- **Child (`A > B`)**: Selects B directly inside A  
  Example: `ul > li`
- **Adjacent sibling (`A + B`)**: Selects B immediately after A  
  Example: `h1 + p`
- **General sibling (`A ~ B`)**: Selects all B after A at same level  
  Example: `h1 ~ p`

### 3. Specificity
Specificity determines which rule wins when multiple rules match.

Order (low → high):  
`Universal < Type < Class/Attribute/Pseudo-class < ID < Inline Style`

Numeric format (a,b,c,d):
- Inline style → `1,0,0,0`
- ID selector → `0,1,0,0`
- Class/attribute/pseudo-class → `0,0,1,0`
- Type/pseudo-element → `0,0,0,1`

Example:
```css
#id { }          /* 0100 */
.container { }   /* 0010 */
p { }            /* 0001 */
```

### 4. Inheritance
Some CSS properties *inherit automatically* (e.g., `font-size`, `color`).  
Others *do not inherit* (e.g., `margin`, `padding`, `border`).

Control inheritance:
- `inherit` → force inheritance  
- `initial` → reset to default  
- `unset` → inherit if natural; else initial

### 5. Cascade
Cascade decides the final applied style using:
1. **Origin** (author > user > browser)
2. **Specificity**
3. **Importance** (`!important`)
4. **Order of appearance** (later wins)

### Interview Theory Questions (Short Answers)

**Q1: What is CSS specificity?**  
Specificity is a scoring mechanism that determines which selector’s styles apply when multiple rules target the same element.

**Q2: How does the CSS cascade work?**  
The cascade uses rule origin, specificity, importance, and order to decide the final applied style.

**Q3: Which CSS properties are inherited?**  
Text-related properties like `font-family`, `color`, `line-height` generally inherit; box-model properties do not.

**Q4: Difference between `A B` and `A > B`?**  
`A B` selects *any descendant*.  
`A > B` selects *only direct children*.

**Q5: What does `!important` do?**  
It overrides normal specificity rules but is overridden by another `!important` with higher specificity.

### Coding-Based Questions

**1. Style all `<p>` inside `.card` but not nested deeper than 1 level.**
```css
.card > p {
  color: blue;
}
```

**2. Highlight input fields with errors (using attribute selector).**
```css
input[aria-invalid="true"] {
  border: 2px solid red;
}
```

**3. Style only the first paragraph after an `<h2>`.**
```css
h2 + p {
  font-weight: bold;
}
```

**4. Add an icon before every list item using pseudo-element.**
```css
li::before {
  content: "• ";
  color: orange;
}
```

---

This cheat sheet covers selectors, combinators, specificity, inheritance, and cascade with interview prep sections and coding examples.

