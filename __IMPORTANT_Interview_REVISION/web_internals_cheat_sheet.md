# Browser Rendering Pipeline

## Parsing → DOM/CSSOM → Render Tree → Layout → Paint → Composite

### Topic: Browser Rendering Pipeline  
### Sub Topic: Parsing → DOM/CSSOM → Render Tree → Layout → Paint → Composite

---

## 1. Detailed Explanation

### Parsing  
The browser reads raw HTML characters and converts them into tokens, then into nodes, forming the DOM.  
CSS is parsed into the CSSOM.

### DOM & CSSOM  
DOM = structure  
CSSOM = styles  
Both required before layout.

### Render Tree  
DOM + CSSOM → Render Tree (only visible nodes).

### Layout (Reflow)  
Browser computes geometry and positions.

### Paint  
Browser fills pixels: colors, borders, shadows, text.

### Composite  
Browser merges layers via GPU.

---

## 2. Theory-Based Interview Questions

**1. What is the DOM?**  
Tree representation of HTML.

**2. DOM vs Render Tree?**  
DOM has all nodes; Render Tree has only visible styled nodes.

**3. Triggers layout?**  
Geometry changes.

**4. Triggers paint?**  
Visual changes.

**5. Composite-only updates?**  
transform, opacity.

---

## 3. Coding Examples

### Avoid layout thrashing
```js
const h = el.offsetHeight;
requestAnimationFrame(() => el.style.width = h + "px");
```

### Force reflow
```js
const force = element.offsetTop;
```

### Avoid layout via transform
```css
.box { transform: translateX(50px); }
```

# Topic : Event Loop & Task Queue

## Sub Topic : microtasks vs macrotasks, rendering frames, requestAnimationFrame

---

## Overview (short)

The JavaScript runtime is single-threaded for JS execution. The **event loop** is the mechanism that coordinates: the call stack (where JS runs), task queues (where callbacks wait), microtask queue (higher-priority tasks), and browser rendering steps (layout, paint, composite). Understanding how these pieces interleave explains tricky ordering behaviours, animation smoothness, and performance pitfalls.

---

## Key pieces and definitions

- **Call stack**: where functions execute. When it's empty the event loop can pick the next task.

- **Macrotasks (task queue / callback queue)**: tasks scheduled to run later. Examples:
  - `setTimeout`, `setInterval` callbacks
  - DOM events (click, keydown)
  - I/O callbacks (Node), `setImmediate` (Node)
  - `requestAnimationFrame` *schedules a callback but runs it in a special phase tied to rendering* — it's treated separately (see Rendering frames).

- **Microtasks (microtask queue)**: run immediately after the currently executing task finishes and before the next macrotask. Examples:
  - Promise reactions (`.then`, `catch`, `finally`)
  - `queueMicrotask`
  - `MutationObserver`
  - `process.nextTick` (Node — actually even higher priority in Node)

- **Rendering pipeline (browser)**: after a macrotask completes and microtasks drain, the browser may perform rendering: style calculations, layout, paint, composite — but only if something changed or a frame is due.

- **Frame budget**: for 60 FPS, the browser has ~16.66ms per frame to do JS + style/layout/paint/composite. If JS blocks longer than that, frames drop (jank).

- **requestAnimationFrame (rAF)**: schedules a callback to run right before the next repaint. Use it for smooth animations tied to display refresh. rAF callbacks run in a frame-phase distinct from ordinary macrotasks and after microtasks for that frame (details below).

---

## Order of execution (typical browser event loop simplified)

1. Run one macrotask from the macrotask queue (e.g., a `click` handler or `setTimeout` callback).
2. While the call stack is empty, drain the microtask queue completely (run all microtasks added during that macrotask; each microtask may enqueue more microtasks — keep draining until empty).
3. If a repaint is needed and the next frame is due, run `requestAnimationFrame` callbacks for that frame.
4. Browser performs painting/compositing if required.
5. Move to the next macrotask.

> Important subtlety: microtasks always run *before* rAF callbacks for the upcoming frame. So promise resolution inside a macrotask can affect what rAF sees.

---

## Example: ordering demonstration

```js
console.log('script start');

setTimeout(() => console.log('timeout macrotask'), 0);

Promise.resolve().then(() => console.log('promise microtask'));

requestAnimationFrame(() => console.log('rAF callback'));

console.log('script end');
// Typical output order:
// script start
// script end
// promise microtask
// rAF callback   <-- runs in frame phase before paint
// timeout macrotask
```

Notes:
- The microtask runs immediately after the current macrotask (the script) finishes.
- The rAF callback runs on the next frame and after microtasks for the script have drained.
- The `setTimeout` macrotask runs later.

---

## Practical implications & best practices

- **Use microtasks for fast, immediate follow-ups** (e.g., chaining async results via Promises). But avoid long-running microtasks — they block rAF and macrotasks because the microtask queue must drain first.

- **Avoid microtask starvation**: continuously scheduling microtasks (e.g., a loop that keeps `Promise.then` chaining) prevents the browser from running rAF or processing user events — the UI may freeze.

- **Prefer `requestAnimationFrame` for visual updates/animations**. It aligns JS with the browser repaint and avoids unnecessary layout thrashing.

- **Batch DOM writes**: read then write — repeated alternating reads and writes cause layout thrash. When inside rAF, batch DOM reads first, then writes.

- **Don't use `setTimeout(..., 0)` for animation** because it's unsynchronized with the refresh rate and may introduce jitter. Use rAF.

- **Heavy work** should move off the main thread (Web Worker) or be chunked into multiple macrotasks so the UI can remain responsive.

---

## Common pitfalls and gotchas

- **Promises vs setTimeout**: Promise callbacks (microtasks) execute before `setTimeout` callbacks even with 0ms.

- **Sequential microtasks blocking rAF**: if a microtask enqueues itself repeatedly, rAF and macrotasks never get a chance.

- **MutationObserver runs as microtasks** so tiny DOM changes observed immediately after the task can be processed before rAF.

- **Node differences**: Node has `process.nextTick` (even higher priority than Promises in practice) and `setImmediate` (macrotask-like). Event loop phases differ slightly from browsers — check Node docs when writing server-side code.

---

## Useful patterns (code)

### Use rAF for smooth throttling

```js
// Throttle costly handler using rAF
let scheduled = false;
function onScroll() {
  if (scheduled) return;
  scheduled = true;
  requestAnimationFrame(() => {
    // do work: batch reads then writes
    // e.g., measure scroll position, then update transforms
    scheduled = false;
  });
}
window.addEventListener('scroll', onScroll);
```

### Chunk heavy computation into macrotasks to keep UI responsive

```js
function doHeavy(items) {
  let i = 0;
  function chunk() {
    const start = performance.now();
    while (i < items.length && performance.now() - start < 8) {
      process(items[i++]);
    }
    if (i < items.length) setTimeout(chunk, 0); // yield to event loop
  }
  chunk();
}
```

### Promise microtask starvation example

```js
function runawayMicrotasks() {
  Promise.resolve().then(function loop() {
    // re-queue another microtask forever — UI will hang
    Promise.resolve().then(loop);
  });
}
```

---

## Interview theory questions (concise answers)

1. **Q:** What's the difference between macrotasks and microtasks?
   **A:** Macrotasks are scheduled callbacks (e.g., `setTimeout`, events) processed one per tick. Microtasks (Promises, `queueMicrotask`, `MutationObserver`) run immediately after the current macrotask finishes and before the next macrotask; they fully drain first.

2. **Q:** When do `requestAnimationFrame` callbacks run relative to microtasks and macrotasks?
   **A:** rAF callbacks run during the rendering phase for the next frame. Microtasks always drain before rAF callbacks for that frame. Macrotasks run before microtasks (one macrotask), then microtasks drained, then rAF if a frame is scheduled.

3. **Q:** Why should animations use rAF instead of `setTimeout`?
   **A:** rAF synchronizes with the browser's refresh cycle for smoother timing, and allows the browser to coalesce updates and avoid unnecessary paints, reducing jank.

4. **Q:** What causes layout thrashing and how does it relate to event loop ordering?
   **A:** Layout thrashing happens when code repeatedly reads layout (like `offsetHeight`) and writes styles in alternating steps; interleaving reads and writes forces repeated style/layout calcs, often triggered within macrotasks/rAF. Batch reads and writes to avoid it.

5. **Q:** Can microtasks starve rendering? How?
   **A:** Yes. The microtask queue must drain before rAF and macrotasks proceed; if microtasks continuously enqueue more microtasks, rendering and event processing are blocked.

6. **Q:** Difference in Node: `process.nextTick` vs `setImmediate` vs Promises?
   **A:** `process.nextTick` runs before other microtasks — it runs immediately after the current operation, even before Promises in some Node versions. Promises (microtasks) run next. `setImmediate` queues a callback to run on the check phase (after I/O), functioning like a macrotask.

---

## Related coding-based interview questions

1. **Implement a microtask scheduler simulation** — given arrays of macrotasks and microtasks, simulate order of execution. (Answer expects you to drain microtasks after every macrotask.)

2. **Implement a throttle using `requestAnimationFrame`** — ensure a handler runs at most once per frame. (See rAF example above.)

3. **Chunk large array processing** — split work into chunks using `setTimeout(..., 0)` or `requestIdleCallback` (if available) to keep the UI responsive. Expect to discuss trade-offs (`requestIdleCallback` availability & behavior).

4. **Detect layout thrash in a code snippet** — given code that toggles a class and reads `offsetHeight` repeatedly, explain and fix it by batching reads/writes.

5. **Polyfill `setImmediate` (browser)** — implement a `setImmediate`-like function using `postMessage` or `MessageChannel` for near-macrotask behavior (interview-level exercise).


---

## Quick cheatsheet (commands & priority)

Priority order during one tick (simplified):

1. Run one macrotask from macrotask queue (e.g., current script or event callback).
2. Drain microtask queue completely (Promises, `queueMicrotask`, `MutationObserver`).
3. Run `requestAnimationFrame` callbacks (if frame is due).
4. Browser performs paint/composite if needed.
5. Repeat with next macrotask.

---

## Further reading / keywords to search

- "HTML standard event loop" (detailed spec)
- "Microtask checkpoint" and "task checkpoints"
- Node.js event loop phases
- requestAnimationFrame and frame timing

---

*Generated as an interview-focused cheat sheet. Save or download this file as Markdown for study and reference.*

# Reflow vs Repaint — Browser Rendering Cheat Sheet

## Topic: Reflow vs Repaint  
## Sub Topic: What Triggers Layout, Style Recalculation, Compositing Layers

---

## 1. Full Explanation

### Reflow (Layout)
Reflow is the browser’s quest to solve a geometry puzzle: it recalculates **where every element lives** and **how big it is**.  
Any change that affects an element’s size, position, or the layout of its neighbors triggers layout work.

Typical triggers:
- Adding/removing DOM nodes  
- Changing layout properties (width, height, margin, padding, border, display, position…)  
- Changing text content  
- Resizing the window  
- Changing fonts  
- Querying layout information (`offsetWidth`, `getBoundingClientRect`, etc.)—these force the browser to sync the layout first  

Reflow is the most expensive operation because it may cascade through the tree.

---

### Repaint
Repaint occurs when **visual appearance** changes but **layout stays the same**.  
The geometry doesn’t move; only pixels need to be redrawn.

Triggers:
- Changing color, background-color  
- Changing visibility (not display)  
- Outline, box-shadow  
- Opacity changes *may* only be a composite, not repaint  

Repaint is cheaper than reflow because geometry is untouched.

---

### Style Recalculation
Before layout or paint, the browser must determine **which CSS rules apply**.

Triggers:
- Adding/removing classes  
- Changing inline styles  
- Changing pseudo-classes (`:hover`, `:focus`)  
- DOM changes that alter which selectors match  

Style recalculation can cascade across the document depending on selector complexity.

---

### Compositing Layers
Modern browsers split a page into layers, each rendered separately and then composited by the GPU.

GPU-friendly properties:
- transform  
- opacity  
- filter  
- will-change  

Changes to these **avoid layout and paint**, triggering only compositing if the element already has its own layer.

When a layer is updated:
- No layout  
- No paint  
- Only GPU re-composition  

This is why `transform: translateZ(0)` or `will-change: transform` improves animation smoothness.

---

## 2. Theory-Based Interview Questions

**Q1. What is reflow?**  
Reflow is layout recalculation where the browser computes the size and position of elements.

**Q2. How does repaint differ from reflow?**  
Repaint updates visual styling without changing layout geometry.

**Q3. What triggers style recalculation?**  
Changes in classes, inline styles, DOM structure, or selector-dependent states.

**Q4. Why is reflow expensive?**  
Because layout changes can propagate through ancestors, siblings, and children.

**Q5. How do compositing layers improve performance?**  
They isolate parts of the page so transitions and transforms avoid layout and paint.

**Q6. Which CSS properties trigger only compositing?**  
transform, opacity, filter, and properties indicated via will-change.

**Q7. What causes forced synchronous layout?**  
Reading layout metrics immediately after writing DOM or style changes.

---

## 3. Related Coding-Based Questions

### Question 1  
Optimize an animation of a moving box so it avoids layout and paint.

**Solution concept:**  
Use `transform: translateX()` instead of changing `left` or `margin`.

```css
.box {
  transform: translateX(0);
  transition: transform 0.3s;
}
```

### Question 2  
Given a JavaScript snippet that causes layout thrashing, fix it.

Bad:
```js
for (let i = 0; i < 100; i++) {
  box.style.width = i + 'px';
  console.log(box.offsetWidth); // forces layout every iteration
}
```

Good (batch writes + reads):
```js
let widths = [];
for (let i = 0; i < 100; i++) widths.push(i);

requestAnimationFrame(() => {
  box.style.width = widths[widths.length - 1] + 'px';
  console.log(box.offsetWidth);
});
```

### Question 3  
Create a GPU layer to smooth a fade+move animation.

```css
.card {
  will-change: transform, opacity;
}
```

---

## End

# Web Internals — Critical Rendering Path

**Topic:** Web Internals

**Sub Topic:** Critical Rendering Path — minimizing CSS/JS blocking, preload, prefetch, async/defer

---

## 1. Overview
The Critical Rendering Path (CRP) is the sequence of steps the browser performs to convert HTML/CSS/JS into pixels on the screen. Optimizing the CRP reduces time-to-first-paint (TTFP), first meaningful paint (FMP), and largest contentful paint (LCP).

Key stages: parse HTML → build **DOM** → parse CSS → build **CSSOM** → construct **Render Tree** → **Layout (reflow)** → **Paint** → **Composite**.

Blocking resources (external CSS and certain scripts) pause this pipeline. The goal: minimize blocking, prioritize critical resources, and defer non-critical work.

---

## 2. What blocks rendering
- **External CSS**: must be downloaded and parsed before constructing the Render Tree (blocking). Inline styles in the head affect critical rendering.
- **Synchronous scripts** (`<script src="..."></script>` without `async`/`defer`) block HTML parsing; if they call `document.write` or mutate DOM/CSS, the browser must execute them immediately.
- **Fonts** and large images: fonts can cause FOIT/FOUT; images don't block the *initial* render but can affect LCP.

---

## 3. Practical strategies to minimize blocking

### 3.1 Critical CSS (inline above-the-fold)
- Extract the minimal CSS needed to render the initial viewport and inline it in `<head>` inside a `<style>` block.
- Load the rest of the CSS asynchronously (e.g. via `rel="preload"` + swap to `rel="stylesheet"`, or a small JS loader).
- Tools: `critical` (node), `penthouse`, webpack plugins, or build-time extraction.

**Trade-offs:** inlining reduces additional requests and avoids a render-block, but increases HTML size and can harm cache efficiency for repeat views.

### 3.2 `rel="preload"` (priority fetch)
- Use `rel="preload"` to instruct the browser to fetch a resource (font, CSS, script) early without applying it immediately.
- Always include the correct `as` attribute (e.g., `as="style"`, `as="script"`, `as="font"`) and `crossorigin` when needed.

```html
<link rel="preload" href="/static/css/main.css" as="style">
<link rel="preload" href="/static/fonts/io.woff2" as="font" type="font/woff2" crossorigin>
```

For CSS you usually pair preload with a small onload handler to apply it:

```html
<link rel="preload" href="/styles/noncritical.css" as="style" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/styles/noncritical.css"></noscript>
```

### 3.3 `rel="prefetch"` (low priority, future navigations)
- Use `rel="prefetch"` for resources you **might** need for future navigations or later interactions. Browser fetches with low priority (idle time).

```html
<link rel="prefetch" href="/next-page.js" as="script">
```

### 3.4 `async` vs `defer` vs module scripts
- `<script async src="...">` — downloads the script asynchronously and executes **as soon as** it’s available, possibly before HTML parsing completes. Good for independent analytics or third-party widgets.
- `<script defer src="...">` — downloads asynchronously and defers execution **until after HTML parsing** finishes. Execution order preserved for multiple deferred scripts. Great for app scripts that manipulate DOM.
- `<script type="module" src="...">` — modules are deferred by default in modern browsers and support `import` statements; they execute after the document is parsed.

**Guideline:** prefer `defer` for application code, `async` only for independent scripts.

### 3.5 Dynamic script injection
- Create scripts with JS and append to body to avoid blocking parsing. This is similar to `async` behavior.

```js
const s = document.createElement('script');
s.src = '/widget.js';
s.async = true;
document.head.appendChild(s);
```

### 3.6 Font optimizations
- Use `font-display: swap` to avoid FOIT (flash of invisible text) and show fallback fonts until custom fonts load.
- Preload critical webfonts with `as="font"` + `crossorigin`.

### 3.7 Resource hints
- `rel="preconnect"` to warm TCP/TLS and DNS to external origins (CDNs, analytics).

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://example-cdn.com">
```

### 3.8 Lazy-loading and `loading="lazy"`
- Use `loading="lazy"` for offscreen images and iframes. This reduces network contention for critical resources (images don’t contend for bandwidth until visible).

```html
<img src="/large.jpg" loading="lazy" alt="...">
```

### 3.9 Server-level improvements
- Enable HTTP/2 or HTTP/3 to improve multiplexing of many small requests.
- Use proper caching headers (immutable, cache-control) to reduce repeated downloads.
- Use gzip/ Brotli compression.

### 3.10 Code splitting and tree shaking
- Bundle only what's needed for the initial page (entry chunk + critical libs). Use dynamic imports for non-critical features.
- Tree-shake unused exports to reduce bundle sizes.

### 3.11 Prioritize Critical Requests in the Network Layer
- Set `importance` attribute (Chrome) or `fetchpriority` for images/resources to hint to the browser.

```html
<img src="hero.jpg" fetchpriority="high" alt="">
```

### 3.12 Using Service Workers (advanced)
- Cache critical assets and serve them immediately. Use service worker precache (with care) to speed up repeat loads and offline UX.
- Use runtime caching and background prefetching for non-critical assets.

---

## 4. Examples & snippets

**Preload font + swap**

```html
<link rel="preload" href="/fonts/inter-regular.woff2" as="font" type="font/woff2" crossorigin>
<style>
  @font-face {
    font-family: 'Inter';
    src: url('/fonts/inter-regular.woff2') format('woff2');
    font-display: swap;
  }
</style>
```

**Defer app script, async analytics**

```html
<script defer src="/static/js/app.bundle.js"></script>
<script async src="https://example-analytics.com/analytics.js"></script>
```

**Inline critical CSS (simplified)**

```html
<head>
  <style>
    /* Critical styles for header and hero */
    body { margin:0; font-family: system-ui, -apple-system; }
    header { display:flex; align-items:center; height:56px }
    .hero { min-height: 60vh }
  </style>
  <link rel="preload" href="/styles/main.css" as="style" onload="this.rel='stylesheet'">
</head>
```

**Rel=preload for CSS with fallback**

```html
<link rel="preload" href="/styles/noncritical.css" as="style" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/styles/noncritical.css"></noscript>
```

---

## 5. Measuring & debugging
- Use **Lighthouse** (Chrome DevTools) for LCP, CLS, FCP metrics and recommendations.
- Use the **Network** panel to inspect which resources block the parser (look for scripts in the waterfall and CSS blocking).
- Use `Performance` tab (record) to see long tasks, layout thrashing, and paint times.
- `coverage` tab (DevTools) to find unused JS/CSS.

---

## 6. Interview — theory questions (with concise answers)

1. **Q:** What is the Critical Rendering Path?  
   **A:** Sequence browser follows to convert HTML/CSS/JS into pixels: parse HTML → DOM, parse CSS → CSSOM, create Render Tree, layout, paint, composite.

2. **Q:** Which resources block rendering and why?  
   **A:** External CSS blocks rendering because the browser must construct CSSOM before Render Tree. Synchronous scripts block HTML parsing/execution to preserve script ordering and DOM access.

3. **Q:** When should you use `async` vs `defer`?  
   **A:** Use `defer` for app scripts that depend on DOM; use `async` for independent third-party scripts where execution order relative to other scripts doesn't matter.

4. **Q:** What is `rel="preload"` vs `rel="prefetch"`?  
   **A:** `preload` is for high-priority fetches needed for the current page render; `prefetch` is low-priority for future navigations.

5. **Q:** How does inlining critical CSS help and what’s the downside?  
   **A:** Inlining avoids extra request and blocks less, improving initial render. Downside: larger HTML and poor cache efficiency.

6. **Q:** What is FOIT and how to mitigate it?  
   **A:** Flash of Invisible Text — mitigate with `font-display: swap`, preloading fonts, and providing good fallbacks.

7. **Q:** How can HTTP/2 improve CRP performance?  
   **A:** Multiplexing reduces head-of-line blocking, making many small requests cheaper and enabling finer-grained splitting of assets.

8. **Q:** What is `render-blocking CSS`?  
   **A:** CSS that must be fetched/parsed before Render Tree can be built; external stylesheets are render-blocking.

9. **Q:** Why is code-splitting important for CRP?  
   **A:** It ensures only the code needed for initial render is loaded, reducing JS parse/compile time and improving FCP/LCP.

10. **Q:** How to prioritize images for LCP?  
   **A:** Mark hero images with `fetchpriority="high"` or preload them; compress, use next-gen formats, ensure they're cached.

---

## 7. Interview — practical / coding questions

1. **Task:** Add a font preload and ensure it's applied correctly.  
   **Expected:** Use `<link rel="preload" as="font" crossorigin>` + `@font-face` with `font-display: swap`.

2. **Task:** Convert a blocking stylesheet to non-blocking while preserving no-FOUT behavior.  
   **Expected approach:** Inline critical CSS, `preload` the full CSS and swap onload; provide `noscript` fallback.

3. **Task:** Make your main app bundle non-blocking.  
   **Expected:** Use `defer` on the script or use module `type="module"` + dynamic imports for heavy parts.

4. **Task:** Lazy-load offscreen images and components.  
   **Expected:** Use `loading="lazy"` for images and dynamic `import()` for components.

5. **Task:** Implement a simple service worker strategy to precache the shell and prefetch data.  
   **Expected:** Use Workbox or a basic SW that caches critical assets on `install` and uses `fetch` handler to serve cache-first for core files.

6. **Task:** Measure and reduce unused CSS.  
   **Expected:** Use DevTools Coverage to find unused selectors and trim via build tooling.

7. **Task:** Demonstrate how to defer non-critical JS that manipulates the DOM only after DOMContentLoaded.  
   **Sample:**

```html
<script>
  window.addEventListener('DOMContentLoaded', function(){
    const s = document.createElement('script');
    s.src = '/noncritical.js';
    s.defer = true;
    document.body.appendChild(s);
  });
</script>
```

8. **Task:** Use `fetchpriority` on a hero image in HTML.  
   **Sample:** `<img src="/hero.jpg" fetchpriority="high" alt="hero">`

---

## 8. Quick checklist for production
- Extract and inline critical CSS.
- Preload fonts and hero images.
- Defer application JS and async third-party widgets.
- Use `prefetch` for next-page assets.
- Use `loading="lazy"` for offscreen content.
- Enable HTTP/2, Brotli; set cache headers.
- Measure with Lighthouse and iterate.

---

## 9. Further reading / tools (suggested)
- Lighthouse (Chrome DevTools)
- `critical` / `penthouse` (critical CSS extraction)
- Workbox (service worker helpers)
- webpack / Rollup / Vite: code-splitting and tree-shaking

---

*End of document.*

# Web Internals – HTTP Basics  
## HTTP/1.1 vs HTTP/2 vs HTTP/3, Methods, Headers, Status Codes

---

## 1. HTTP/1.1  
HTTP/1.1 uses TCP and processes requests sequentially, creating bottlenecks.  
It allows persistent connections but can experience head‑of‑line blocking at the application layer.

---

## 2. HTTP/2  
HTTP/2 adds multiplexing and binary framing over TCP.  
Multiple streams share one connection, avoiding application-level blocking but still constrained by TCP’s ordered delivery.

---

## 3. HTTP/3 (QUIC)  
HTTP/3 runs on QUIC, a UDP-based protocol that avoids TCP’s ordering slowdown.  
It offers faster handshakes, connection migration, and no transport-level head‑of‑line blocking.

---

## 4. HTTP Methods  
GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, TRACE, CONNECT.

---

## 5. Headers  
Request headers: Host, Authorization, User-Agent, Accept.  
Response headers: Content-Type, Cache-Control, Set-Cookie, ETag, CORS headers.

---

## 6. Status Codes  
1xx Informational  
2xx Success (200 OK, 201 Created)  
3xx Redirects (301, 302, 304)  
4xx Client errors (400, 401, 403, 404, 429)  
5xx Server errors (500, 502, 503)

---

## Interview Questions (Concise)

Q: HTTP/1.1 vs HTTP/2 vs HTTP/3?  
A: 1.1 = text over TCP, sequential; 2 = multiplexed binary over TCP; 3 = QUIC/UDP, no HoL blocking, faster.

Q: Why is HTTP/2 still blocked sometimes?  
A: TCP enforces ordered delivery → transport-level head‑of‑line blocking.

Q: PUT vs PATCH?  
A: PUT replaces whole resource; PATCH updates part of it.

Q: Purpose of CORS?  
A: Controls cross-origin requests for security.

---

## Coding Tasks

### Parse headers
```javascript
function parseHeaders(raw) {
  const lines = raw.trim().split(/\r?\n/);
  const headers = {};
  for (const line of lines) {
    const [k, ...v] = line.split(':');
    headers[k.trim()] = v.join(':').trim();
  }
  return headers;
}
```

### Simple Node.js HTTPS GET
```javascript
const https = require("https");

function get(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = "";
      res.on("data", (chunk) => data += chunk);
      res.on("end", () => resolve({status: res.statusCode, headers: res.headers, body: data}));
    }).on("error", reject);
  });
}
```

### Express middleware
```javascript
app.use((req, res, next) => {
  console.log("User-Agent:", req.headers["user-agent"]);
  next();
});
```

# Web Internals – Caching Mechanisms  
## Topic: Caching Mechanisms  
## Sub Topic: Cache-Control, ETag, Service Worker Cache, CDN

### Cache-Control  
Cache-Control is an HTTP header that instructs browsers and intermediaries how to cache responses.  
Key directives:  
- **max-age**: how long the response can be cached.  
- **no-cache**: must revalidate before using cache.  
- **no-store**: caches must not store.  
- **public/private**: public allows shared caching; private restricts to browser.  
- **immutable**: asset won't change over its lifetime.

### ETag  
ETag (Entity Tag) is a unique fingerprint for a resource.  
When client sends `If-None-Match` with ETag, server checks:  
- If unchanged → responds `304 Not Modified`  
- If changed → sends full new resource

### Service Worker Cache  
Service workers can intercept network requests and provide cached responses.  
Useful for offline apps, custom caching strategies, background sync.  
Common patterns: cache-first, network-first, stale-while-revalidate.

### CDN  
CDNs serve content from geographically distributed edge servers.  
They reduce latency, improve speed, and offload traffic from origin.  
Use advanced caching rules, edge TTLs, smart invalidation.

---

## Interview Theory Questions  
1. **Difference between Cache-Control and ETag?**  
Cache-Control defines caching policy; ETag helps conditional validation. Both work together.

2. **Why use no-store vs no-cache?**  
no-store forbids any caching; no-cache allows caching but requires validation.

3. **What is stale-while-revalidate?**  
Serve cached version immediately while fetching an updated version in background.

4. **How does a Service Worker intercept requests?**  
Via `fetch` event, deciding whether to respond from cache, network, or custom logic.

5. **Why do CDNs improve performance?**  
They serve content closer to the user using edge servers.

---

## Coding Practice

### 1. Cache-Control Example (Express.js)
```javascript
app.get('/static', (req, res) => {
  res.set('Cache-Control', 'public, max-age=31536000, immutable');
  res.sendFile('/path/to/file');
});
```

### 2. ETag Example  
```javascript
app.set('etag', 'strong');
```

### 3. Basic Service Worker Cache  
```javascript
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open('v1').then(cache => cache.add('/index.html'))
  );
});
```

### 4. CDN Cache Invalidation (Example for Cloudflare API)
```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/<zone>/purge_cache" -H "Authorization: Bearer <token>" -d '{"purge_everything": true}'
```

# Web Internals – Security  
## Topic: Web Internals  
## Sub Topic: CORS, CSP, XSS, CSRF, HTTPS, SRI

---

## 1. **CORS (Cross-Origin Resource Sharing)**  
CORS is the browser’s gatekeeper for cross-origin requests. When a website on one origin (scheme + host + port) tries to fetch data from another, the browser checks headers to decide whether it should allow the request.  
It exists to prevent malicious sites from silently making authenticated requests to other domains on behalf of the user.

### How it works  
- Browser sends a **preflight OPTIONS** request for non‑simple requests.  
- Server must respond with:  
  - `Access-Control-Allow-Origin`  
  - `Access-Control-Allow-Methods`  
  - `Access-Control-Allow-Headers`  
- Without correct headers, browser blocks the response.

---

## 2. **CSP (Content Security Policy)**  
CSP is like a “diet plan” for the browser — it restricts what kinds of resources the page can load.  
It prevents script injection by allowing developers to specify:  
- Allowed domains for scripts, images, fonts  
- Inline script execution using nonces or hashes  
- Blocking unsafe-eval and unsafe-inline

### Example directive  
```http
Content-Security-Policy: script-src 'self' https://trusted.com; object-src 'none';
```

---

## 3. **XSS (Cross-Site Scripting)**  
XSS occurs when untrusted user input ends up in the DOM without sanitization. It lets attackers run JavaScript in a victim’s browser.

### Types  
- **Reflected XSS**: Payload in request, echoed by server.  
- **Stored XSS**: Payload stored persistently (DB, comments).  
- **DOM-based XSS**: Happens entirely in the browser via JS manipulating the DOM.

### Prevention  
- Escape output (`<`, `>`, `"`, `'`)  
- Use frameworks with auto-escaping  
- Use CSP  
- Avoid `innerHTML`

---

## 4. **CSRF (Cross-Site Request Forgery)**  
CSRF rides along on your existing authentication cookies and performs unwanted actions on sites where you're logged in.

### Prevention  
- CSRF tokens  
- SameSite cookies  
- Double-submit cookies  
- Use of non-GET requests for sensitive operations

---

## 5. **HTTPS**  
HTTPS is HTTP with TLS encryption. It defends against network sniffing, tampering, and man-in-the-middle attacks.  

### How it protects  
- **Confidentiality**: Encrypts data  
- **Integrity**: Detects tampering  
- **Authentication**: Certificates verify server identity

---

## 6. **SRI (Subresource Integrity)**  
SRI validates that an external script or stylesheet hasn’t been tampered with.

### Example  
```html
<script src="https://cdn.com/app.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GhYkrxF4gZ7OJbRRsE3z4LB3PjihjQ6V2P6fQ"
        crossorigin="anonymous"></script>
```

---

# Theory Interview Questions (Concise Answers)

### 1. What is CORS and why is it needed?  
It’s a browser security policy that controls how websites can make cross-origin requests to prevent unauthorized access to protected resources.

### 2. What’s the difference between simple and preflighted requests?  
Simple: GET/POST with certain headers. Preflighted: Browser sends OPTIONS first to verify permission.

### 3. How does CSP prevent attacks?  
By restricting allowed sources of scripts, styles, images, and by blocking inline scripts unless explicitly allowed.

### 4. What is XSS?  
An injection flaw where attackers run malicious JS in a victim’s browser.

### 5. Difference between Stored and Reflected XSS?  
Stored persists on the server; reflected is echoed immediately from the request.

### 6. How does CSRF work?  
Exploits automatic cookie sending to trigger unwanted authenticated actions.

### 7. How does HTTPS prevent man-in-the-middle attacks?  
It encrypts data and authenticates servers using certificates.

### 8. What is SRI?  
A mechanism for validating the integrity of externally loaded resources.

---

# Coding-Based Questions

### 1. Write an Express.js middleware that sets a secure CSP header.
```js
app.use((req, res, next) => {
  res.setHeader(
    "Content-Security-Policy",
    "default-src 'self'; script-src 'self' https://cdn.com"
  );
  next();
});
```

### 2. Validate CORS requests using an allowed origins whitelist.
```js
const allowed = ["https://example.com", "https://foo.com"];

app.use((req, res, next) => {
  const origin = req.headers.origin;
  if (allowed.includes(origin)) {
    res.setHeader("Access-Control-Allow-Origin", origin);
    res.setHeader("Access-Control-Allow-Credentials", "true");
  }
  next();
});
```

### 3. Sample CSRF token generation.
```js
const crypto = require("crypto");
function generateCSRF() {
  return crypto.randomBytes(32).toString("hex");
}
```

### 4. Escape user input to prevent XSS.
```js
function escapeHTML(str) {
  return str.replace(/[&<>"]/g, c => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;"
  }[c]));
}
```

---

# End

# Web Internals – DNS & TCP Handshake  
## Topic: DNS & TCP Handshake  
## Sub Topic: DNS lookup, TCP 3‑way handshake, TLS negotiation

---

# 1. DNS Lookup  
DNS (Domain Name System) is the internet’s phonebook. When you type a URL, your system resolves it into an IP address.

### How DNS Lookup Works  
1. **Browser Cache** – Checks if domain → IP is cached locally.  
2. **OS Cache** – If browser misses, OS resolver checks host cache.  
3. **Router Cache** – Your router might have entries cached.  
4. **DNS Recursive Resolver** – Usually provided by ISP or public DNS (Cloudflare 1.1.1.1, Google 8.8.8.8).  
5. **Root Servers** – Directs resolver to the correct TLD server.  
6. **TLD (Top Level Domain) Servers** – Example: `.com`, `.net`; provides authoritative NS.  
7. **Authoritative DNS Server** – Returns actual IP for the domain.  
8. **Response Cached** – Resolver caches for TTL, OS/browser caches too.

### Important DNS Records  
- `A` – IPv4 address  
- `AAAA` – IPv6 address  
- `CNAME` – Canonical name alias  
- `NS` – Nameserver record  
- `MX` – Mail server  
- `TXT` – Misc text (SPF, DKIM, verification)  

---

# 2. TCP 3‑Way Handshake  
TCP (Transmission Control Protocol) establishes a reliable connection using the classic 3‑step dance.

### Steps  
1. **SYN** – Client → Server: “Can we talk?”  
2. **SYN‑ACK** – Server → Client: “Yes, let's talk.”  
3. **ACK** – Client → Server: “Cool, starting now.”

### Result  
A full‑duplex, byte‑stream connection is established.  
After handshake, HTTP request can be sent.

---

# 3. TLS Negotiation  
Secure connections add a layer on top of TCP.

### Steps of TLS 1.2/1.3 (Simplified)
1. **ClientHello** – Client sends supported cipher suites, TLS versions, random nonce.  
2. **ServerHello** – Server picks cipher suite, sends certificate.  
3. **Key Exchange** – Using Diffie‑Hellman (ECDHE) for forward secrecy.  
4. **Session Keys Derived** – Both compute symmetric session key.  
5. **Secure Communication Begins** – All HTTP data now encrypted (HTTPS).

### Modern TLS Notes  
- TLS 1.3 is faster: only **1 round‑trip** instead of 2–3.  
- Uses forward‑secret ciphers only.  
- Supports 0‑RTT resumption for faster reconnects.

---

# 4. Interview Theory Questions (with concise answers)

### 1. What is DNS?  
A distributed system that resolves domain names to IP addresses.

### 2. What is a recursive resolver?  
A DNS server that performs all DNS steps on behalf of the client.

### 3. What is the difference between recursive and iterative DNS queries?  
Recursive: resolver handles entire resolution.  
Iterative: resolver asks step by step (root → TLD → authoritative).

### 4. What is the TCP 3‑way handshake?  
The SYN → SYN‑ACK → ACK process to establish a reliable connection.

### 5. Why is handshake needed?  
To synchronize sequence numbers and establish reliability.

### 6. What problem does TLS solve?  
Encrypts communication, ensures authenticity and integrity.

### 7. What is the difference between SSL and TLS?  
SSL is deprecated; TLS is the modern, secure version.

### 8. How does HTTPS differ from HTTP?  
HTTPS = HTTP + TLS; encrypted and tamper‑proof.

### 9. What is forward secrecy?  
Compromised long‑term keys cannot decrypt past traffic.

### 10. What is 0‑RTT in TLS 1.3?  
Allows sending encrypted data in the first round trip for returning clients.

---

# 5. Coding Questions Related to DNS, TCP, TLS

### 1. Resolve a domain programmatically (Node.js)
```js
const dns = require("dns");

dns.lookup("example.com", (err, address, family) => {
  console.log("IP:", address);
});
```

### 2. Perform an HTTPS request showing TLS details (Node.js)
```js
const https = require("https");

https.get("https://example.com", (res) => {
  console.log("Protocol:", res.socket.getProtocol());
});
```

### 3. Low‑level TCP connection example (Node.js `net`)
```js
const net = require("net");

const socket = net.createConnection(80, "example.com", () => {
  console.log("Connected via TCP");
  socket.write("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n");
});
```

---

This file covers DNS lookup, TCP handshake, TLS flow, theory questions, and coding examples.  
The next layer of exploration could dive into QUIC/HTTP‑3 where handshake overhead collapses into a single step.

# Web Internals – Compression & Optimization  
## Topic: Compression & Optimization  
## Sub Topic: Gzip/Brotli, Image Optimization, Lazy Loading

---

## 🔥 Detailed Explanation

### **Gzip & Brotli Compression**
Browsers and servers compress text-based assets (HTML, CSS, JS, JSON, SVG) before sending them over the network.

**Gzip**  
A widely-supported compression format that uses the DEFLATE algorithm. It offers solid compression ratios and works on all browsers.

**Brotli**  
A newer compression format developed by Google. It generally compresses 15–25% better than Gzip, especially for JS/CSS. Modern browsers support Brotli. It uses multiple compression modes with dictionary‑based optimizations.

**When the browser requests a resource**, it includes the header:  
`Accept-Encoding: gzip, br`  
The server responds with the best available:  
`Content-Encoding: br`

**When to use what?**  
- Use **Brotli** for static files because it compresses slower but serves faster.  
- Use **Gzip** as a fallback or for on‑the‑fly dynamic content.

---

### **Image Optimization**
Images are heavy and often dominate page weight.

**Key techniques**

1. **Modern formats**  
   - **WebP**: 25–35% smaller than JPEG/PNG, supports transparency.  
   - **AVIF**: Even smaller and better quality; supports HDR, but slower to encode.

2. **Responsive images**  
   HTML attributes like `srcset`, `sizes` allow the browser to pick the right image size.

3. **Compression (Lossy/Lossless)**  
   - Lossy reduces file size aggressively but may reduce quality.  
   - Lossless preserves pixels but reduces size moderately.

4. **Serving appropriately sized images**  
   Don’t serve a 2000px image to a 400px container.

---

### **Lazy Loading**
Lazy loading defers loading images (or components/scripts) until they are required.

Native HTML:  
`<img src="img.jpg" loading="lazy" />`

**How it works**  
The browser calculates whether an element is near the viewport. If not, it avoids network calls and decoding tasks. This is especially useful for long pages or news feeds.

For custom logic, developers use **IntersectionObserver**, allowing precise control over when to load off-screen components.

Lazy loading improves:  
- Time to First Paint (FP)  
- Time to Interactive (TTI)  
- Reduces bandwidth usage

---

## 💼 Theory-Based Interview Questions (With Concise Answers)

**1. What is Gzip compression?**  
A DEFLATE-based compression algorithm used by servers to reduce transfer size of text-based resources.

**2. How is Brotli different from Gzip?**  
Brotli offers better compression ratios and uses a dictionary-based algorithm, but is slower to compress.

**3. What resources benefit most from compression?**  
HTML, CSS, JS, JSON, SVG—basically all text-based assets.

**4. Why are images not compressed with Gzip/Brotli?**  
Images are already compressed (JPEG, PNG, WebP); compressing again offers no benefit.

**5. What is WebP?**  
A modern image format offering 25–35% smaller files compared to JPEG/PNG.

**6. What is lazy loading?**  
A mechanism to defer fetching resources until they enter or approach the viewport.

**7. How does IntersectionObserver help with lazy loading?**  
It notifies when elements enter a viewport threshold, allowing controlled resource loading.

---

## 🧪 Coding-Based Questions

### **1. Lazy Loading an Image Using IntersectionObserver (JS)**
```javascript
const images = document.querySelectorAll("img[data-src]");

const observer = new IntersectionObserver((entries, obs) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      obs.unobserve(img);
    }
  });
}, { threshold: 0.1 });

images.forEach(img => observer.observe(img));
```

### **2. Serving Different Image Sizes with `srcset`**
```html
<img
  src="image-400.jpg"
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 900px) 800px, 1200px"
  alt="Sample"
/>
```

### **3. Express.js Example – Enable Gzip & Brotli**
```javascript
const express = require("express");
const compression = require("compression");
const shrinkRay = require("shrink-ray-current"); // Brotli support

const app = express();
app.use(shrinkRay()); // Brotli + gzip
app.use(compression());

app.listen(3000);
```

---

## 📝 End Note
Compression, image optimization, and lazy loading are the trifecta of front-end performance tuning. Together, they make pages feel lighter, faster, and friendlier. Exploring these three areas opens doors to deeper web-performance techniques like adaptive loading and resource prioritization.


# Web Internals – Rendering Engines  
## Topic: Rendering Engines  
## Sub Topic: Blink, WebKit, Gecko & Layout Differences

---

## 1. Rendering Engines Overview

Rendering engines are the browser subsystems that parse HTML/CSS, build the DOM/CSSOM, construct the render tree, compute layout, and paint to the screen. Each engine follows web standards but interprets implementation details slightly differently, leading to subtle layout variations.

---

## 2. Blink

Blink is the rendering engine used by Chromium-based browsers: Chrome, Edge, Opera, Brave, Samsung Internet.

### Key Traits
- Forked from WebKit in 2013 by Google.
- Multi-threaded architecture; heavy use of parallelization.
- LayoutNG (new layout engine) improves precision and reduces quirks.
- Strong support for modern standards: CSS Grid, Flexbox, Houdini APIs, display-locking, container queries.
- Predictable performance due to aggressive optimization and V8 integration.

### Layout Behavior
- LayoutNG reduces float inconsistencies.
- Very strict about invalid markup.
- Flexbox behavior is highly compliant with W3C spec.
- Some subtle differences in baseline alignment compared to Firefox.

---

## 3. WebKit

WebKit powers Safari on macOS/iOS and several embedded systems.

### Key Traits
- Very strict about privacy/security; throttles background tasks.
- Uses JavaScriptCore engine for JS.
- Less aggressive multi-threading compared to Blink.
- Slower adoption of new CSS/JS APIs due to Apple’s cautious release cycle.

### Layout Behavior
- More conservative layout engine; sometimes diverges in handling:
  - Flexbox min-content sizing rules
  - `position: sticky` behaviors
  - `aspect-ratio` handling (historically delayed)
- Viewport units on iOS behave differently due to browser UI chrome.

---

## 4. Gecko

Gecko powers Firefox and emphasizes standards purity.

### Key Traits
- Extremely standards-faithful implementation.
- Uses SpiderMonkey for JS execution.
- High focus on security, privacy, and accessibility.
- Independent implementation of many features, leading to unique strengths (e.g., superior Grid debugging tools).

### Layout Behavior
- Flexbox spec implemented very precisely, but some differences in auto/min-content calculations.
- Sub-grid first implemented by Firefox.
- More predictable line-height behavior vs. Blink.

---

## 5. Layout Differences Summary

### Flexbox
- Safari sometimes misinterprets `flex-basis` and prefers content size unless explicitly overridden.
- Firefox uses more accurate min-content sizing than Chrome.
- Chrome/Blink sometimes differ in baseline alignment for nested flex containers.

### Grid
- Firefox leads in spec-complete grid features.
- Safari had long-standing issues with `min-height: 0` inside grid children.

### Positioning & Scrolling
- Safari’s `position: sticky` historically breaks if ancestors overflow.
- Chrome/Blink scroll anchoring is more aggressive, occasionally causing unintended jumps.
- Firefox’s scroll-snap follows spec more strictly.

### Viewport Units
- iOS Safari has special dynamic units (`svh`, `lvh`, `dvh`) due to mobile UI chrome.
- Chrome/Firefox mobile follow standard `vh`, but implement dynamic viewport separately.

---

## 6. Interview Questions (Theory-Based)

**Q: Why did Google fork Blink from WebKit?**  
A: To gain independence for rapid development, multi-process improvements, and deep V8 integration.

**Q: Which engine is most standards-faithful?**  
A: Gecko, because Mozilla implements specs without shortcuts or proprietary deviations.

**Q: Why does Safari often lag in new web APIs?**  
A: Apple prioritizes stability, battery life, and security on iOS/macOS, making them conservative with new APIs.

**Q: What causes layout differences between rendering engines?**  
A: Interpretation of ambiguous specs, prioritizing performance vs. correctness, historical implementations, and platform-specific constraints.

**Q: How does layout differ in mobile Safari vs desktop browsers?**  
A: Unique viewport units, aggressive memory limits, and UI chrome interference (address bar shrinking).

---

## 7. Coding / Practical Questions

**1. Why does this Flexbox layout behave differently in Safari?**

```css
.container {
  display: flex;
}
.item {
  flex: 1;
  min-width: 0; /* Required for Safari to prevent overflow */
}
```

Safari defaults to content-based sizes unless `min-width: 0` is set.

---

**2. Why does sticky positioning not work in Safari?**

```css
.parent {
  overflow: hidden; /* breaks sticky in Safari */
}
.child {
  position: sticky;
  top: 0;
}
```

Safari requires no ancestor with `overflow` other than `visible`.

---

**3. Grid overflow differences**

Firefox: follows min-content size more strictly.  
Chrome: sometimes allows overflow unless constrained explicitly.

```css
.grid > div {
  min-height: 0; /* fixes scrolling inside grid child */
}
```

---

## Closing Thought

Rendering engines are like three different musicians playing the same sheet music. The melody is the same—the web standards—but each brings its own interpretation, quirks, and improvisations. Understanding these subtleties makes you a more resilient developer.

# Web Internals — Service Workers  
## Topic: Service Workers  
## Subtopic: PWA Caching, Offline, Background Sync

---

## 1. Service Workers Explained

A service worker is a programmable network proxy that sits between your web app and the network. It runs in its own thread, survives page reloads, and gives web apps superpowers: offline capability, background sync, caching strategies, and push notifications.

It cannot access the DOM directly but communicates through postMessage.

The essential life cycle is:  
**register → install → activate → idle → fetch/intercept → terminate (and restart when needed).**

---

## 2. PWA Caching

Caching in service workers relies on the Cache Storage API. This lets you store request–response pairs and serve them later without hitting the network.

### Common Cache Strategies (Brain‑Friendly Summary)

**Cache First**  
Serve from cache; go to network only if missing. Useful for images, icons, static assets.

**Network First**  
Try network; fall back to cache if offline. Good for dynamic content like user dashboards.

**Stale While Revalidate**  
Serve cached response immediately; update cache in background. Smooth and fast.

**Network Only**  
Always fetch from network. Rare, used for authenticated APIs where caching isn’t desired.

**Cache Only**  
Serve only cached resources. Not common, but good for fully offline bundles.

---

## 3. Offline Support

Offline support happens because service workers intercept fetch events. When the network fails, the worker can choose a cached response.

Typical flow:  
1. User visits site → service worker installs → caches essential assets (app shell).  
2. When offline → service worker intercepts fetch → responds from cache.  
3. App feels native‑like.

Offline-first experiences often use the **App Shell Model**: HTML, CSS, JS, icons, and minimal layout cached on install.

---

## 4. Background Sync

Background Sync lets the browser retry operations even after connectivity returns.

Two flavors:

### One‑off Sync ("sync")
Used to send queued actions (e.g., pending form submissions).  
Workflow:  
- App queues data in IndexedDB.  
- Service worker listens for `"sync"` event.  
- When connectivity returns → sync event triggers → data is sent reliably.

### Periodic Background Sync  
Allows periodic data refresh (like a news feed).  
Browser-controlled, requires user permission.  
Triggered only when device has battery, network, and permission.

---

## 5. Interview Theory Questions (Concise Answers)

**What is a service worker?**  
A background script that intercepts network requests, enables offline capability, caching, and background tasks.

**Why can’t service workers access the DOM?**  
They run in a separate worker thread for safety and performance; they communicate via postMessage.

**What is the service worker lifecycle?**  
Install → Activate → Fetch/Events. These phases manage setup, cleanup, and runtime behavior.

**How is a PWA offline?**  
Service workers intercept fetch events and serve cached assets when the network fails.

**What is the App Shell Model?**  
Caching the minimal UI structure so the app loads instantly even offline.

**Difference between sync and periodicSync?**  
Sync is one‑time retry on reconnection; periodicSync refreshes data on a schedule.

**Why version your caches?**  
To safely update cached assets and delete old caches during activation.

**What is stale‑while‑revalidate?**  
Return cached response instantly and update cache in the background.

---

## 6. Coding Questions + Examples

### Q: Write a basic service worker that caches assets on install.
```js
const CACHE_NAME = 'v1';
const ASSETS = ['/', '/index.html', '/styles.css', '/app.js'];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
});
```

### Q: Intercept fetch and implement “cache first” strategy.
```js
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cached =>
      cached || fetch(event.request)
    )
  );
});
```

### Q: Implement a “network first” strategy for API requests.
```js
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(res => {
        const clone = res.clone();
        caches.open('dynamic').then(cache => cache.put(event.request, clone));
        return res;
      })
      .catch(() => caches.match(event.request))
  );
});
```

### Q: Basic one‑off background sync registration (in main thread).
```js
navigator.serviceWorker.ready.then(reg => {
  return reg.sync.register('send-pending-data');
});
```

### Q: Service worker handling of sync event.
```js
self.addEventListener('sync', async event => {
  if (event.tag === 'send-pending-data') {
    event.waitUntil(sendQueuedItems());
  }
});
```

---

## 7. Summary

Service workers transform ordinary sites into resilient, offline‑ready applications. Caching strategies give fine‑grained control over performance, and background sync ensures reliability even with unstable networks. These ideas form the backbone of modern Progressive Web Apps.

# WebSockets & Server-Sent Events (SSE) — Cheat Sheet

## Topic: Web Internals  
## Sub Topic: WebSockets & SSE  
Realtime communication basics, differences, and use‑cases.

---

## 1. Understanding Realtime Communication

Realtime communication means the server can push updates to the client without waiting for the client to request them. This avoids the old pattern of *polling*, where the client repeatedly asks, “Any updates yet?”

Modern browsers support two primary realtime mechanisms:
- **WebSockets** — full-duplex communication.
- **Server-Sent Events (SSE)** — unidirectional server→client stream.

---

## 2. WebSockets — Deep Dive

WebSockets upgrade a regular HTTP connection into a persistent, bidirectional channel.  
This is done through the **WebSocket handshake**, where the client sends an `Upgrade: websocket` header and switches protocol.

### Core Characteristics
- Full-duplex communication (both client and server can send anytime).
- Low latency due to persistent TCP connection.
- Works over port 80/443.
- Supports binary and text data.
- Great for chat apps, games, financial tickers.

### Lifecycle
1. HTTP → WebSocket handshake.
2. Connection open.
3. Message exchange (frames).
4. Close handshake or abrupt termination.

### Code Example (JavaScript)
```js
const ws = new WebSocket("wss://example.com/socket");

ws.onopen = () => ws.send("Hello");
ws.onmessage = (msg) => console.log(msg.data);
ws.onclose = () => console.log("Closed");
```

---

## 3. Server-Sent Events (SSE) — Deep Dive

SSE uses a persistent HTTP connection where the server streams events to the client.  
Client cannot send data back over the same channel — it's one‑way.

### Core Characteristics
- Unidirectional: server → client only.
- Automatic reconnection built in.
- Lightweight text-based streaming format.
- Ideal for notifications, logs, and live feed updates.
- Uses `EventSource` API.

### Format
```
data: hello
id: 1
event: message
```

### Code Example
```js
const es = new EventSource("/events");

es.onmessage = (e) => console.log(e.data);
es.onerror = () => console.log("Connection lost");
```

---

## 4. WebSockets vs SSE — Key Differences

| Feature | WebSockets | SSE |
|--------|------------|-----|
| Direction | Bidirectional | Server → Client |
| Reconnect | Manual | Automatic |
| Binary Support | Yes | No (text only) |
| Overhead | Low | Very Low |
| Use in HTTP/2 | Not natively multiplexed | Works great |
| Ideal Use | Chat, multiplayer, trading | Notifications, feeds, metrics |

---

## 5. Interview Theory Questions with Concise Answers

**1. How is WebSocket different from HTTP?**  
HTTP is request‑response. WebSocket is a persistent bidirectional channel.

**2. When would you prefer SSE over WebSocket?**  
When updates flow one way (server→client), like notifications or logs.

**3. Can SSE send binary data?**  
No. Only UTF‑8 text.

**4. Why do WebSockets need a handshake?**  
To switch from HTTP protocol to WebSocket protocol securely.

**5. Do SSE connections automatically reconnect?**  
Yes, with configurable retry intervals.

**6. Do WebSockets work over HTTP/2?**  
Not natively; they require an HTTP/1.1 upgrade.

---

## 6. Coding Questions (Realtime Communication)

**1. Implement a WebSocket echo server (Node.js).**
```js
import { WebSocketServer } from 'ws';

const server = new WebSocketServer({ port: 8080 });

server.on("connection", socket => {
  socket.on("message", msg => socket.send("Echo: " + msg));
});
```

**2. SSE Node.js stream endpoint.**
```js
app.get("/events", (req, res) => {
  res.set({
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  });

  setInterval(() => {
    res.write(`data: ${Date.now()}

`);
  }, 1000);
});
```

**3. Build a client that falls back from WebSocket → SSE → Polling.**
(Demonstrates hybrid realtime strategy.)

---

## End of Cheat Sheet

# Web Internals – Core Web Vitals

## Topic: Web Internals  
## Sub Topic: Core Web Vitals (How measured, optimization, thresholds)

---

# 1. Core Web Vitals Explained

Core Web Vitals are a set of user-centric performance metrics Google uses to assess real‑world page experience. They focus on loading, interactivity, and visual stability.

They are measured in the field using:
- **Real User Monitoring (RUM)** via Chrome User Experience Report (CrUX)
- **In‑browser JavaScript APIs** like PerformanceObserver
- **Lab tools** such as Lighthouse, WebPageTest, and Chrome DevTools (helpful, but not used for ranking)

---

# 2. Core Metrics

## **1. LCP — Largest Contentful Paint**
Represents the loading performance of the most meaningful element (image, hero text, video poster frame).

### Thresholds:
- Good: **≤ 2.5s**
- Needs Improvement: 2.5–4.0s
- Poor: **> 4.0s**

### How measured:
Browser detects the largest visible element and measures time until it’s rendered.

### How to Optimize:
- Use optimized images (`<img>`), responsive formats, lazy loading below the fold
- Serve assets via CDN
- Preload hero image or key CSS
- Reduce main-thread blocking JS

---

## **2. INP — Interaction to Next Paint**
Replaces FID in 2024. Measures the responsiveness delay between user interaction (tap, click, keypress) and the next visual update.

### Thresholds:
- Good: **≤ 200ms**
- Needs Improvement: 200–500ms
- Poor: **> 500ms**

### How measured:
Observes all page interactions, picks the worst (or close to worst) event.

### How to Optimize:
- Avoid heavy JS on interaction paths
- Break long tasks (`requestIdleCallback`, `setTimeout`, Web Workers)
- Reduce render-blocking code
- Use passive event listeners
- Avoid large layout shifts triggered by JS

---

## **3. CLS — Cumulative Layout Shift**
Measures visual stability — how much the layout jumps unexpectedly.

### Thresholds:
- Good: **≤ 0.1**
- Needs Improvement: 0.1–0.25
- Poor: **> 0.25**

### How measured:
Tracks changes in layout shift score during page lifecycle.

### How to Optimize:
- Always set explicit width/height for images, ads, iframes
- Reserve space for dynamic content
- Avoid injecting content above existing content
- Use CSS `transform` instead of forcing layout changes

---

# 3. Additional Metrics (Supporting Web Vitals)

These don’t affect ranking directly but matter:

### **TTFB — Time to First Byte**
Server response speed.

### **FCP — First Contentful Paint**
First piece of visible content.

### **TBT — Total Blocking Time**
Proxy for INP in lab conditions.

### **Speed Index**
Visual completeness of the page.

---

# 4. Mini Interview Questions + Answers (Concise)

### Q1. What are Core Web Vitals?
A set of performance metrics measuring loading (LCP), interactivity (INP), and stability (CLS).

### Q2. Why is INP replacing FID?
FID measured only the first interaction; INP covers *all* interactions and better reflects responsiveness.

### Q3. How does the browser determine LCP?
It looks at render timings of the largest visible element (images, background images, text blocks).

### Q4. Causes of poor CLS?
Missing dimensions on images/ads, injected elements, dynamically loaded fonts.

### Q5. How do you measure Core Web Vitals in real users?
Using CrUX, PerformanceObserver, and RUM analytics.

### Q6. What impacts INP the most?
Long JavaScript tasks delaying event processing.

---

# 5. Coding‑Style Questions Related to Performance

### 1. Debounce a search input (reduce INP delay)
```js
function debounce(fn, delay) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), delay);
  };
}
```

### 2. Split a long task to avoid blocking INP
```js
function chunkWork(items, process) {
  let i = 0;
  function work() {
    const end = Math.min(i + 100, items.length);
    for (; i < end; i++) process(items[i]);
    if (i < items.length) requestIdleCallback(work);
  }
  requestIdleCallback(work);
}
```

### 3. Reserve image space to avoid CLS
```html
<img src="hero.jpg" width="1200" height="600" alt="hero">
```

### 4. Preload hero image to improve LCP
```html
<link rel="preload" as="image" href="/hero.png">
```

---

# 6. Summary
Core Web Vitals drive real‑world performance. Improving them means optimizing server speed, reducing JavaScript cost, and stabilizing layout. The journey often leads deeper into browser internals, revealing just how much engineering goes into a single smooth click.

# Web Internals Cheat Sheet  
## Topic: DevTools  
## Sub Topic: Debugging Layout, Network, Performance, Memory

---

## 🌐 DevTools – Debugging Layout, Network, Performance & Memory

Modern browsers ship with DevTools, a kind of digital X-ray machine for the web. It helps you peek into layout calculations, network requests, rendering timelines, memory leaks, and general page gremlins.

---

# 1. Layout Debugging (Elements + Layout Tools)

### **What Happens During Layout**
Browsers calculate where every element should sit. DevTools lets you visualize:
- Box model (margin, border, padding, size)
- CSS grid & flex overlays
- Repaints & reflows triggered by scripts
- Auto layout decisions (gap, alignment, basis)

### **How to Debug Layout**
- Use *Inspect Element → Box Model Panel* to understand spacing.
- Toggle CSS properties to isolate layout shifts.
- Use *Grid/ Flexbox Overlay* to see track lines and sizing behavior.
- Use *Rendering → Layout Shift Regions* to track CLS issues.

---

# 2. Network Debugging

### **What You See**
- Request waterfall
- DNS/TCP/SSL timings
- Caching headers
- Payload size, compression
- H2/H3 multiplexing efficiency

### **Common Tasks**
- Filter by resource type (JS/CSS/XHR/WS)
- Replay XHR requests
- See cache status (200, 304, disk-cache, memory-cache)
- Throttle network to simulate slow 3G
- Inspect request/response headers

---

# 3. Performance Debugging

### **Performance Panel Shows**
- Main-thread tasks
- Scripting + rendering + painting breakdown
- FPS graph
- Long tasks > 50ms
- Web vitals timeline (LCP, CLS, FID)

### **How to Debug**
- Record a performance profile
- Identify expensive JS functions
- Look for layout thrashing (forced reflows)
- Detect heavy paints (big layer changes)
- Use *Coverage Tab* to detect unused CSS/JS

---

# 4. Memory Debugging

### **Memory Tools**
- Heap snapshots
- Allocation timeline
- Garbage collection tracking
- Detached DOM nodes

### **Finding Memory Leaks**
- Increasing heap after forced GC
- Event listeners stuck on removed nodes
- Global references preventing cleanup
- Leaking closures in long-running components

---

# 🎯 Interview Theory Questions & Concise Answers

### 1. **What causes layout thrashing?**  
Frequent reads from layout properties mixed with writes (like changing style), forcing recalculation repeatedly.

### 2. **How do you detect unused JS/CSS?**  
Use Coverage tab; it marks executed vs non-executed bytes.

### 3. **What is a heap snapshot?**  
A capture of in-memory objects and references to analyze memory leaks.

### 4. **How does DevTools show Web Vitals?**  
Performance panel marks key events like LCP, FCP, CLS with timestamps.

### 5. **Why do network requests show `memory cache` or `disk cache`?**  
Indicates whether the response was served from RAM or disk according to caching headers.

---

# 🎯 Coding-Oriented Questions

### **1. Detect Layout Thrashing**
```js
function bad() {
  for (let i = 0; i < 1000; i++) {
    const h = element.offsetHeight; // layout read
    element.style.height = h + 1 + "px"; // layout write
  }
}
```
**Fix:** Cache reads, batch writes.

---

### **2. Memory Leak Example**
```js
let store = [];
document.getElementById("btn").addEventListener("click", () => {
  store.push(new Array(100000).fill("x"));
});
```
DevTools helps reveal growing heap across interactions.

---

### **3. Network Debugging Test**
```js
fetch("/api/data")
  .then(r => r.json())
  .then(console.log);
```
You can inspect this request in the Network tab (headers, timings, caching).

---

# Done.  
Use this sheet as your debugging north star—your browser is a laboratory, and DevTools is the microscope.
