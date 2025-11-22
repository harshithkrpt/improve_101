
# Topic : DOM & Events
## Sub Topic : DOM Manipulation — `querySelector`, `createElement`, `cloneNode`, `DocumentFragment`, reflow cost

---

## Quick Summary
This cheat-sheet covers the core DOM APIs you'll use to find, create, clone, and batch-insert nodes, and explains how browsers recalculate layout (reflow) and how to avoid expensive operations.

---

## API reference & behaviour (short)

### `querySelector` / `querySelectorAll`
- `document.querySelector(cssSelector)` returns the **first** element matching the selector or `null`.  
- `element.querySelectorAll(cssSelector)` returns a static `NodeList` of all matches (not live).  
- Uses depth-first pre-order traversal; selectors are standard CSS selectors.  
**When to use:** quick lookups for single elements; prefer `getElementById` for ids when performance matters.  
(See MDN: `querySelector`.)  

### `document.createElement(tagName)`
- Creates an element node in memory (not attached to the document). No reflow happens **until** it is appended to the document. You can set attributes, classes, textContent, event listeners while it's detached.  
**When to use:** construct new elements programmatically.

### `node.cloneNode(deep=false)`
- Returns a copy of `node`. If `deep=true` clones the entire subtree; otherwise clones only the element itself (shallow). Event listeners are **not** copied.  
**When to use:** make templates or repeat UI blocks efficiently.

### `DocumentFragment` / `document.createDocumentFragment()`
- A lightweight container that can hold nodes off-DOM. Appending a `DocumentFragment` to the document inserts its children (not the fragment itself) in a single operation. This minimizes DOM operations and reduces reflows.  
**When to use:** batch multiple DOM insertions or rearrangements to avoid repeated reflows.

---

## Reflow / Layout / Repaint — costs & practical guidance
- **Reflow (layout):** browser recalculates positions and geometry of elements. Triggers: DOM mutations that change layout (insert/remove nodes, change classes affecting layout, inline style changes that modify size/position). citeturn0search3  
- **Repaint:** drawing pixels after layout; less expensive than full reflow but still work.  
- **Forced synchronous layout (forced reflow):** occurs when JS reads geometry (e.g., `offsetWidth`, `getComputedStyle`) after changing the DOM or styles, forcing the browser to flush layout immediately — this blocks the main thread and is expensive. Avoid querying layout properties between writes. citeturn0search6turn0search11

Practical tips:
- Batch DOM writes (use `DocumentFragment`, string `innerHTML`, or build elements detached from DOM then append once). citeturn0search4turn0search12  
- Avoid interleaving reads and writes — group all reads, then all writes to prevent layout thrashing. citeturn0search6  
- Avoid large, complex layouts during animations; animate transform/opacity where possible to leverage compositor-only updates. citeturn0search11

---

## Examples

### 1) Efficiently append many items — `DocumentFragment`
```js
const list = document.querySelector('#my-list');
const frag = document.createDocumentFragment();

for (let i = 0; i < 1000; i++) {
  const li = document.createElement('li');
  li.textContent = `Item ${i}`;
  frag.appendChild(li);
}

list.appendChild(frag); // single DOM insertion -> minimal reflows
```

### 2) Clone a template node (deep) and customize
```js
const template = document.querySelector('.card-template');
const clone = template.cloneNode(true); // deep clone of subtree
clone.querySelector('.title').textContent = 'New title';
// event listeners must be attached manually:
clone.querySelector('.btn').addEventListener('click', onClick);
document.body.appendChild(clone);
```

### 3) Avoid forced reflow (don't do this)
```js
// bad: forces layout repeatedly
elem.style.width = '100px';
const w = elem.offsetWidth; // forces layout
elem.style.height = (w / 2) + 'px';
```

### 4) Read all geometry first, then apply writes (good)
```js
// read pass
const rects = items.map(it => it.getBoundingClientRect());

// write pass
rects.forEach((r, i) => {
  items[i].style.transform = `translateY(${r.top}px)`;
});
```

---

## Interview-style theory questions (with concise answers)

1. **Q:** What's the difference between `querySelector` and `getElementById`?  
   **A:** `getElementById` is faster for ID lookups and returns a single element; `querySelector` accepts any CSS selector and returns the first match. Use `getElementById` when you have an id. citeturn0search10

2. **Q:** Does `createElement` cause a reflow?  
   **A:** Creating an element detached from the document does **not** cause a reflow. Reflows happen when the element is inserted or when changing computed styles that affect layout. citeturn0search16turn0search3

3. **Q:** Will `cloneNode(true)` copy event listeners?  
   **A:** No. `cloneNode` copies the DOM structure and attributes, but not JS event listeners or properties attached directly to the node. citeturn0search5

4. **Q:** What is layout thrashing and how to prevent it?  
   **A:** Layout thrashing is repeated cycles of DOM write then read (or vice-versa) that force many synchronous layouts. Prevent by batching reads and writes separately or using `DocumentFragment`/off-DOM construction. citeturn0search6turn0search8

5. **Q:** When is `DocumentFragment` better than `innerHTML`?  
   **A:** `innerHTML` can be faster for building large static HTML via string concatenation, but `DocumentFragment` is safer for complex node creation (preserving node references, templates, event wiring) and avoids parsing pitfalls. Benchmark for your use-case. citeturn0search9turn0search4

---

## Coding-based interview problems (with short solutions)

1. **Problem:** Insert 10,000 rows into a table without blocking the UI for too long.  
   **Solution approach:** Use `DocumentFragment` in chunks and `requestIdleCallback` / `setTimeout` chunking to yield to the main thread.
```js
function insertRows(table, rows) {
  const CHUNK = 500;
  let i = 0;
  function workChunk() {
    const frag = document.createDocumentFragment();
    for (let end = Math.min(i + CHUNK, rows.length); i < end; i++) {
      const tr = document.createElement('tr');
      tr.innerHTML = `<td>${rows[i].id}</td><td>${rows[i].name}</td>`;
      frag.appendChild(tr);
    }
    table.tBodies[0].appendChild(frag);
    if (i < rows.length) requestAnimationFrame(workChunk);
  }
  requestAnimationFrame(workChunk);
}
```

2. **Problem:** Implement a `delegate` helper to add an event listener on a parent for matching child selectors.
```js
function delegate(parent, selector, type, handler) {
  parent.addEventListener(type, function(ev) {
    const target = ev.target.closest(selector);
    if (target && parent.contains(target)) handler.call(target, ev);
  });
}
```

3. **Problem:** Create a function `createCard(data)` that returns a DOM node (not yet appended) with a title, description and a button wired to an action.
```js
function createCard({title, desc, onClick}) {
  const root = document.createElement('div');
  root.className = 'card';
  const h = document.createElement('h3'); h.textContent = title;
  const p = document.createElement('p'); p.textContent = desc;
  const btn = document.createElement('button'); btn.textContent = 'Action';
  btn.addEventListener('click', onClick);
  root.append(h, p, btn);
  return root; // append later
}
```

---

## Best practices cheat-sheet (one-liners)
- Build off-DOM, then append once.  
- Batch DOM writes; avoid read–write interleaving.  
- Prefer `textContent` over `innerHTML` when inserting plain text.  
- Use `closest()` for delegation-friendly matching.  
- Use `requestAnimationFrame` for visual updates and chunk large insertions.  
- Profile using DevTools' Performance and Layout instrumentation.

---

## Further reading (selected authoritative pages)
- MDN `querySelector` / `Element.querySelector()` / `Document.querySelector()` docs.  
- MDN `createDocumentFragment()` and `DocumentFragment` article.  
- MDN `cloneNode()` doc.  
- Chrome DevTools: Forced reflow and layout thrashing article.  
(References are included in the chat companion reply.)

---

*Cheat-sheet generated for quick interview prep and practical use. Save or modify as needed.*


# DOM & Events – Event Bubbling & Capturing (JavaScript)

## Event Propagation Phases
Event propagation in the DOM consists of three phases:
1. **Capturing phase** – event travels from document → target.
2. **Target phase** – event triggers on the target element.
3. **Bubbling phase** – event travels from target → document root.

## Bubbling vs Capturing
- **Bubbling (default)**: Handlers run from the target upward.
- **Capturing**: Handlers run from the root downward to the target.
Use capturing with:
```js
element.addEventListener('click', handler, true);
```

## Stopping Propagation
```js
event.stopPropagation();          // stops bubbling further
event.stopImmediatePropagation(); // stops bubbling AND other handlers on same element
```

## Event Delegation Pattern
Attach one listener to a parent instead of multiple children:
```js
document.querySelector('#list').addEventListener('click', (e) => {
  if (e.target.matches('li')) {
    console.log('Item clicked:', e.target.textContent);
  }
});
```
Advantages: fewer handlers, better performance, dynamic elements supported.

## Interview Q&A

**What are the phases of event propagation?**  
Capturing → Target → Bubbling.

**What is event bubbling?**  
Event moves upward from target to ancestors.

**What is event capturing?**  
Event moves downward from ancestors to target.

**How to listen in capturing mode?**  
`addEventListener(type, handler, true)`.

**How to stop propagation?**  
`event.stopPropagation()`.

**Difference between `event.target` and `event.currentTarget`?**  
`target` = element that initiated event.  
`currentTarget` = element whose listener is running.

**What is event delegation?**  
Using a single parent listener to manage events of many child elements.

## Coding Exercises
1. Create nested divs and log event order with and without `stopPropagation()`.
2. Demonstrate capturing listener vs bubbling listener.
3. Implement click delegation on a `<ul>` for its `<li>` children.
4. Add/remove `<li>` dynamically and verify delegation still works.
5. Prevent form submission using `preventDefault()` and stop bubbling.


# DOM & Events — Event Delegation  
**Subtopic:** Performance Optimization, Attaching Listeners Efficiently  
**Language:** JavaScript

---

## 1. Event Delegation — Detailed Explanation

Event delegation is a design technique where one event listener is attached to a parent element, and interactions from its children are detected using **event bubbling**.  
Instead of binding listeners to every child, the parent inspects `event.target` to figure out which child triggered the event.

### Why Event Delegation Is Important

• Reduces the number of event listeners → lower memory usage.  
• Works automatically with dynamically inserted elements.  
• Ideal for large lists, tables, or UI components that change over time.  
• Simplifies code by centralizing logic.

### Basic Example

```js
document.querySelector("#menu").addEventListener("click", (e) => {
  if (e.target.matches(".item")) {
    console.log("Clicked:", e.target.textContent);
  }
});
```

### Events That Don’t Bubble

Some events cannot be delegated:

• `focus`  
• `blur`  
• `mouseenter`  
• `mouseleave`  

These require capturing or manually re-creating bubbling behavior.

---

## 2. Interview Q&A

**Q1. Define event delegation.**  
A pattern in which a parent element handles events that originate from its child elements using bubbling.

**Q2. How does event delegation improve performance?**  
It reduces the total number of listeners, lowering overhead and memory usage.

**Q3. Can all events be delegated?**  
Only events that bubble. Others like `focus` and `mouseenter` do not.

**Q4. How do you detect which element triggered the delegated event?**  
Using `event.target` or `event.target.closest()`.

**Q5. Why is delegation useful for dynamic DOM elements?**  
Because newly added children are automatically covered by the parent listener.

---

## 3. Coding Questions & Answers

### Example 1 — Delegated List Item Click

```js
document.getElementById("items").addEventListener("click", (e) => {
  const li = e.target.closest("li");
  if (!li) return;
  console.log("Selected item:", li.textContent);
});
```

### Example 2 — Delegated Delete Button Inside Cards

```js
document.querySelector(".cards").addEventListener("click", (e) => {
  if (e.target.matches(".delete")) {
    e.target.closest(".card").remove();
  }
});
```

### Example 3 — Build Your Own Delegation Utility

```js
function delegate(parent, selector, type, handler) {
  parent.addEventListener(type, (e) => {
    const target = e.target.closest(selector);
    if (target && parent.contains(target)) {
      handler.call(target, e);
    }
  });
}
```

---

## Summary

Event delegation is one of the most efficient ways to work with dynamic or large-scale DOM structures.  
It cuts down listeners, boosts performance, and provides elegant control over event handling.

---


# DOM & Events – Custom Events (JavaScript)

## Topic: DOM & Events  
## Sub Topic: Custom Events – Creating and Dispatching Custom Events

Custom Events in JavaScript let you create your own event types beyond the browser's built‑in set. They behave like normal DOM events—bubbling, cancelable, and able to carry custom data. They’re tremendously useful for decoupling UI components, building event-driven architectures, and making widgets talk to each other without creating tangled dependencies.

---

## Understanding Custom Events

A Custom Event is created using:

```js
const event = new CustomEvent("eventName", {
  detail: { /* custom data */ },
  bubbles: true,
  cancelable: true
});
```

`detail` is a special property that holds extra data you want to send with the event.

You dispatch it using:

```js
element.dispatchEvent(event);
```

You listen to it like any normal event:

```js
element.addEventListener("eventName", (e) => {
  console.log(e.detail);
});
```

---

## Deep Dive: Creating & Dispatching Custom Events

### 1. Creating a Custom Event

```js
const myEvent = new CustomEvent("userLogin", {
  detail: {
    username: "harshith",
    time: Date.now()
  }
});
```

If you want bubbling and cancelability:

```js
const myEvent = new CustomEvent("userLogin", {
  bubbles: true,
  cancelable: true,
  detail: { username: "harshith" }
});
```

### 2. Dispatching a Custom Event

```js
document.body.dispatchEvent(myEvent);
```

### 3. Listening for It

```js
document.body.addEventListener("userLogin", (e) => {
  console.log("User logged in:", e.detail.username);
});
```

### 4. Stopping Event Propagation

```js
target.addEventListener("userLogin", (e) => {
  e.stopPropagation();
});
```

### 5. Cancelable Events

```js
const ev = new CustomEvent("beforeDelete", { cancelable: true });

element.addEventListener("beforeDelete", (e) => {
  e.preventDefault(); // cancels action if allowed
});
```

Then check:

```js
const proceed = element.dispatchEvent(ev);
if (!proceed) console.log("Deletion prevented");
```

---

## When Custom Events Shine

• Component communication in UI libraries  
• Event-driven architecture  
• Complex DOM widgets  
• Making reusable JS modules  
• Communicating from low-level DOM logic to upper-level controllers  

---

## Interview‑Style Theory Questions with Concise Answers

**1. What is a CustomEvent in JavaScript?**  
A user‑defined event type allowing you to dispatch events with custom data using the `detail` property.

**2. How do you create a CustomEvent?**  
Using the `CustomEvent` constructor: `new CustomEvent("name", { detail, bubbles, cancelable })`.

**3. How do you dispatch a custom event?**  
Call `.dispatchEvent(event)` on any DOM element.

**4. Can Custom Events bubble?**  
Yes, if the `bubbles: true` option is provided.

**5. What is the purpose of the `detail` property?**  
It holds extra data passed along with the event.

**6. How do you prevent default behavior in a custom event?**  
Mark event as cancelable and use `event.preventDefault()` inside listeners.

**7. How are Custom Events different from EventEmitter (Node.js)?**  
Custom Events use DOM event architecture; EventEmitter is a Node-specific pattern.

**8. Are Custom Events synchronous or asynchronous?**  
They are synchronous—listeners run before `dispatchEvent` returns.

---

## Coding Questions (Application-Based)

### 1. Create a custom event called `cartUpdated` that sends item count.

```js
const ev = new CustomEvent("cartUpdated", {
  detail: { itemCount: 5 }
});

cartElement.dispatchEvent(ev);
```

### 2. Listen to `cartUpdated` and update UI.

```js
cartElement.addEventListener("cartUpdated", (e) => {
  document.querySelector("#count").textContent = e.detail.itemCount;
});
```

### 3. Build a reusable function to emit events from components.

```js
function emit(el, name, data) {
  const ev = new CustomEvent(name, { detail: data, bubbles: true });
  el.dispatchEvent(ev);
}
```

### 4. Write a cancelable confirmation event before deleting a record.

```js
function requestDelete(el) {
  const ev = new CustomEvent("beforeDelete", { cancelable: true });
  const allowed = el.dispatchEvent(ev);
  if (allowed) console.log("Delete record");
  else console.log("Deletion blocked");
}
```

---

This material works as a compact interview-ready reference while giving a practical grasp of Custom Events in the browser.


# DOM & Events — MutationObserver

## Topic: MutationObserver  
## Sub Topic: Detecting DOM Changes, Intersection Observer vs Mutation Observer

### MutationObserver — The Essential Watcher of DOM Mutations  
MutationObserver is like a vigilant little librarian who notices every time someone edits the DOM “book.”  
It tracks structural changes: added nodes, removed nodes, attribute edits, and text updates.  
It operates asynchronously and avoids blocking the main thread.

---

## What MutationObserver Detects  
MutationObserver can observe:  
- **Child list changes** — new DOM nodes inserted or removed.  
- **Attribute changes** — changes to element attributes.  
- **Text/content changes** — changes to text nodes.  
- **Subtree changes** — observation extended recursively into all descendants.

MutationObserver does *not* detect:  
- Element size changes  
- Visibility changes  
- Intersection changes  
- Scroll-based events  
(That's what IntersectionObserver is for.)

---

## MutationObserver Example

```js
const target = document.querySelector('#watch-me');

const observer = new MutationObserver(mutations => {
  mutations.forEach(mutation => {
    console.log(mutation.type, mutation);
  });
});

observer.observe(target, {
  childList: true,  
  attributes: true, 
  characterData: true,
  subtree: true
});

// To stop observing:
// observer.disconnect();
```

---

## MutationObserver vs IntersectionObserver

MutationObserver watches **DOM structural changes**, whereas IntersectionObserver watches **visibility changes relative to viewport or parent element**.

| Feature | MutationObserver | IntersectionObserver |
|--------|------------------|----------------------|
| Detects DOM additions/removals | Yes | No |
| Detects attribute changes | Yes | No |
| Detects text changes | Yes | No |
| Detects element visibility | No | Yes |
| Detects scroll-based visibility | No | Yes |
| Detects size changes | No | No* (ResizeObserver does this) |
| Use cases | UI updates, SPA reactivity, watching content changes | Lazy-loading, infinite scroll, view animations |

---

## Most Commonly Used DOM Observers in Modern JS

### 1. MutationObserver  
Watches DOM *structure* changes.

### 2. IntersectionObserver  
Watches element *visibility* relative to viewport.  
Use cases: lazy loading, infinite scroll, fade-in animations.

### 3. ResizeObserver  
Watches *element size* changes.  
Use cases: responsive components, graphs, virtualized lists.

### 4. PerformanceObserver  
Watches Web Performance events.  
Use cases: CLS, LCP, memory, resource timings.

These four form the “Core Observer Squad” of the modern web platform.

---

## Interview Preparation — Theory Questions

**1. What is MutationObserver?**  
A browser API that asynchronously observes DOM structural changes like child insertion, removal, attributes, and text updates.

**2. Difference between MutationObserver and DOMNodeInserted/Removed events?**  
Old mutation events were synchronous and slow; MutationObserver is asynchronous and more efficient.

**3. Can MutationObserver detect CSS changes?**  
No, only attribute or DOM structure changes.

**4. Why is MutationObserver asynchronous?**  
To batch DOM mutation records and avoid blocking the main thread.

**5. What is the difference between MutationObserver and IntersectionObserver?**  
MutationObserver observes DOM changes; IntersectionObserver observes visibility within viewport.

**6. What is the performance impact of using MutationObserver with subtree: true?**  
More nodes observed → more computation → use carefully.

---

## Coding Questions (Interview Style)

### Q1: Write a MutationObserver that logs every new DOM element added.
```js
const obs = new MutationObserver(muts => {
  muts.forEach(m => {
    if (m.addedNodes.length) {
      console.log('New node added:', m.addedNodes);
    }
  });
});

obs.observe(document.body, { childList: true, subtree: true });
```

### Q2: Detect when text content of an element changes.
```js
const target = document.querySelector('#msg');

const obs = new MutationObserver(muts => {
  muts.forEach(m => {
    if (m.type === 'characterData') {
      console.log('Text changed:', m.target.data);
    }
  });
});

obs.observe(target, { characterData: true, subtree: true });
```

### Q3: Stop observing after the first mutation.
```js
const obs = new MutationObserver((muts, observer) => {
  console.log(muts[0]);
  observer.disconnect();
});

obs.observe(document.body, { childList: true });
```

---

## Summary  
MutationObserver is the tool when you need to detect *what* changed in the DOM.  
IntersectionObserver is for detecting *when* something appears in viewport.  
ResizeObserver is for watching size changes.  
PerformanceObserver keeps an eye on browser performance events.

These four together form the backbone of reactive browser mechanics that don’t rely on expensive polling or event hacks.



# Topic : Async & Concurrency
## Sub Topic : Async JS Patterns — callbacks, promises, async/await, fetch

---

## 1. Overview (what & why)
JavaScript runs on a single main thread for executing JS code. To remain responsive while performing long-running tasks (network, timers, I/O), it uses asynchronous programming patterns that let operations run without blocking the main thread. This cheatsheet covers the main idioms: callbacks, promises, async/await, and the Fetch API — plus concurrency concepts (event loop, microtasks vs macrotasks).

---

## 2. Patterns & Concepts

### Callbacks
- A callback is a function passed into another function to be invoked later.
- Pros: simple for trivial tasks, universally supported.
- Cons: "callback hell" / pyramid of doom, harder error handling.

Example:
```js
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) { console.error(err); return; }
  console.log(data);
});
```

### Promises
- A `Promise` represents a value that may be available now, in the future, or never.
- Core methods: `then`, `catch`, `finally`.
- Composition utilities: `Promise.all`, `Promise.race`, `Promise.allSettled`, `Promise.any`.

Example:
```js
fetch(url)
  .then(resp => {
    if (!resp.ok) throw new Error('Network error');
    return resp.json();
  })
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

### async / await
- Syntactic sugar over promises. `async` functions return a promise. `await` pauses execution inside async function until the promise resolves (without blocking the main thread).
- Use try/catch around `await` for error handling.

Example:
```js
async function getUser() {
  try {
    const resp = await fetch('/user');
    if (!resp.ok) throw new Error('Fetch failed');
    const user = await resp.json();
    return user;
  } catch (err) {
    console.error(err);
    throw err;
  }
}
```

### Fetch API (modern network requests)
- `fetch()` returns a promise that resolves to a `Response` object. Replace `XMLHttpRequest` with `fetch`.
- You still need to check `response.ok` and parse response via `response.json()`, `response.text()`, `response.blob()`, etc.

Example:
```js
const resp = await fetch('/api/data', { method: 'POST', body: JSON.stringify(payload) });
if (!resp.ok) throw new Error(resp.statusText);
const data = await resp.json();
```

---

## 3. Concurrency fundamentals (event loop, microtasks vs macrotasks)
- **Event loop**: processes tasks (macrotasks) from a task queue and runs microtasks after each macrotask before rendering/next macrotask.
- **Macrotasks** include: `setTimeout`, `setInterval`, I/O callbacks, UI events.
- **Microtasks** include: promise callbacks (`.then/.catch`), `queueMicrotask`, `MutationObserver`.
- Microtasks run **before** the next macrotask and can starve rendering if abused.

Short example demonstrating order:
```js
console.log('script start');

setTimeout(() => console.log('timeout'), 0);

Promise.resolve().then(() => console.log('promise1')).then(() => console.log('promise2'));

console.log('script end');
// Expected order:
// script start
// script end
// promise1
// promise2
// timeout
```

---

## 4. Patterns for common async tasks

### Parallel requests
```js
const [a, b] = await Promise.all([fetch('/a'), fetch('/b')].map(p => p.then(r => r.json())));
```

### Sequential requests
```js
const r1 = await fetch('/1').then(r => r.json());
const r2 = await fetch(`/2?id=${r1.next}`).then(r => r.json());
```

### Retry with backoff (simplified)
```js
async function fetchWithRetry(url, attempts = 3) {
  for (let i = 0; i < attempts; i++) {
    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error('Bad response');
      return await res.json();
    } catch (err) {
      if (i === attempts - 1) throw err;
      await new Promise(r => setTimeout(r, 2 ** i * 100));
    }
  }
}
```

### Cancellation (AbortController)
```js
const controller = new AbortController();
fetch('/long', { signal: controller.signal }).catch(err => {
  if (err.name === 'AbortError') console.log('aborted');
});
controller.abort(); // triggers AbortError
```

---

## 5. Best practices & pitfalls
- Prefer promises / async-await for readability; avoid deep callback nesting.
- Don’t `await` if tasks are independent — use `Promise.all` to run in parallel.
- Always handle errors (`try/catch`, `.catch`) and check `response.ok`.
- Avoid long-running synchronous computation on the main thread; consider Web Workers for CPU-heavy work.
- Be careful with unbounded microtask creation (can starve rendering).
- Use `AbortController` to cancel fetch requests when appropriate.

---

## 6. Interview theory Qs (with concise answers)

1. **Q:** What is a promise?  
   **A:** An object representing eventual completion/failure of an async operation; has states pending/fulfilled/rejected and methods `then`, `catch`, `finally`.  

2. **Q:** Difference between callbacks and promises?  
   **A:** Callbacks are functions invoked later; promises provide an object-based API for async results enabling chaining and better error handling, reducing callback nesting.

3. **Q:** What does `async` do? What does `await` do?  
   **A:** `async` makes a function return a promise. `await` pauses execution of the async function until the awaited promise resolves or rejects (without blocking event loop).

4. **Q:** When to use `Promise.all` vs `Promise.race`?  
   **A:** `Promise.all` waits for all promises to fulfill (rejects if any reject). `Promise.race` resolves/rejects as soon as the first promise settles.

5. **Q:** Explain microtask vs macrotask.  
   **A:** Macrotasks are main tasks (timers, I/O); microtasks are processed immediately after the current task completes (promise `.then`, `queueMicrotask`). Microtasks run before the next macrotask and before rendering.

6. **Q:** How do you cancel a fetch request?  
   **A:** Use `AbortController` and pass its `signal` option to `fetch`. Calling `controller.abort()` rejects the fetch with `AbortError`.

7. **Q:** What problems can `async/await` introduce?  
   **A:** Excessive sequential `await` where parallel execution would be better, and forgetting to handle promise rejections. Also, unhandled rejected promises can crash Node (depending on settings).

8. **Q:** How can you handle multiple concurrent operations and limit concurrency?  
   **A:** Use a concurrency-limiter (pool) pattern, or implement a queue that runs N tasks at a time (e.g., p-limit library or custom worker pool).

---

## 7. Coding interview questions (practical)

1. **Implement `Promise.all` from scratch.**  
   - Requirements: accept iterable of promises/values, return a promise that resolves to array of resolved values or rejects on first rejection.

2. **Write a function that limits concurrent promises to N (concurrency pool).**  
   - Input: array of async functions, concurrency limit N. Output: results array preserving order.

3. **Fetch with timeout.**  
   - Use `AbortController` to abort a fetch if it exceeds given ms.

4. **Debounce and throttle using async-aware functions.**  
   - Implement debounce that cancels previous pending async action.

5. **Make N requests in parallel but stop early when K succeed (e.g., fastest K responses).**  
   - Variation of `Promise.race`/`Promise.any` behavior.

---

## 8. Quick reference snippets

### Basic promise creation
```js
const p = new Promise((resolve, reject) => {
  setTimeout(() => resolve('done'), 1000);
});
```

### Convert callback to promise (promisify)
```js
function promisify(fn) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      fn(...args, (err, res) => {
        if (err) reject(err); else resolve(res);
      });
    });
  };
}
```

---

## 9. Further reading (official docs)
- MDN: Promises, async functions, Fetch API, Event loop & microtasks.  
- javascript.info: in-depth event loop and fetch tutorials.

---

## 10. Footer
This file gives a focused interview-centered cheat-sheet for Async & Concurrency patterns in JavaScript. Practice implementing the coding exercises and explaining microtask/macrotask behavior with small console examples.

# Topic : Async & Concurrency

## Sub Topic : Promise Internals — states, thenable objects, resolving/rejecting

---

### Quick overview
A **Promise** is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. Internally it is a tiny state machine plus a microtask-scheduled reaction chain.

---

## 1) Promise states and transitions
- **Pending** — initial state. No value or reason yet.
- **Fulfilled (resolved)** — operation completed successfully; has a value.
- **Rejected** — operation failed; has a reason (usually an `Error`).

**Important rules:**
- A promise transitions **once**: pending → fulfilled **or** pending → rejected. After that it is immutable.
- Resolving with another promise causes *adoption* of that promise's state (the *thenable resolution procedure*).
- A promise cannot resolve to itself — that throws a `TypeError` (self-resolution guard).

---

## 2) Promise executor and resolve/reject
When you do `new Promise((resolve, reject) => { ... })`:
- `resolve(value)` will queue a microtask that fulfills the promise with `value`.
- `reject(reason)` will queue a microtask that rejects the promise with `reason`.
- If the executor throws synchronously, the promise is rejected with that thrown error.

**Note:** The `resolve` is not immediate synchronous fulfillment; it *schedules* fulfillment as a microtask. This ensures `.then` handlers that are attached immediately after construction will still run in correct order.

---

## 3) Microtasks, event loop, and ordering
- Promise reactions (`.then`, `.catch`, `.finally`) are queued as **microtasks** (also called job-queue tasks).
- Microtasks run **after** the current JS stack finishes but **before** the next macrotask (e.g., `setTimeout`) begins.
- This ordering guarantees deterministic behavior for promise chains and gives them higher scheduling priority than timers.

Example order: synchronous code → microtasks (Promise reactions) → macrotasks (setTimeout, I/O callbacks).

---

## 4) Thenables and the resolution procedure
A **thenable** is any object with a `.then` method. When resolving with a thenable, the Promise resolution procedure will:
1. If value is an object or function, check if it has a `then` property.
2. If `then` is a function, call it with `value` as `this`, providing `resolve` and `reject` callbacks.
3. Ensure `then` is called only once (protects against well-intentioned or malicious thenables).

`Promise.resolve(thenable)` therefore "assimilates" the thenable into a native Promise.

---

## 5) `.then`, chaining, and error propagation
- `.then(onFulfilled, onRejected)` returns a **new** promise (p2). The returned value from `onFulfilled`/`onRejected` determines p2's state:
  - If handler returns a value `x`, p2 is fulfilled with `x` (again running resolution steps if `x` is thenable).
  - If handler throws, p2 is rejected with that error.
  - If handler returns a promise, p2 adopts that promise's eventual state.
- If `onFulfilled` or `onRejected` is omitted, the corresponding value/error is propagated down the chain unchanged.

This makes promise chains conveniently composable and keeps synchronous exceptions within the asynchronous chain.

---

## 6) `finally` semantics
`promise.finally(cb)` runs `cb` regardless of fulfillment or rejection. It passes through the original value/reason. If `cb` returns a thenable, the original resolution is delayed until that thenable settles.

---

## 7) Common APIs and their semantics
- `Promise.resolve(x)` — returns a promise resolved with `x` (assimilates thenables).
- `Promise.reject(r)` — returns a promise rejected with `r`.
- `Promise.all(iterable)` — fulfills with an array of settled values if **all** fulfill; rejects immediately if any rejects.
- `Promise.race(iterable)` — settles as soon as any input promise settles (value or rejection).
- `Promise.allSettled(iterable)` — always fulfills with an array of outcome objects `{status: 'fulfilled'|'rejected', value|reason}`.
- `Promise.any(iterable)` — fulfills with first fulfilled value; rejects with an `AggregateError` if all reject.

---

## 8) Edge cases & gotchas
- **Synchronous then handler**: Even if a promise is already resolved, `.then` callbacks are run asynchronously (microtask), not synchronously.
- **Self-resolution**: `new Promise(res => res(promise))` where `promise` is the same promise leads to `TypeError`.
- **Multiple calls**: Well-formed implementation ensures `resolve`/`reject` are effective only once; malicious thenables may attempt multiple calls — spec protects you by ignoring subsequent calls.
- **Unhandled rejections**: If a promise rejects and no handler consumes it by the end of the microtask checkpoint, most environments emit an `unhandledrejection` event. Make sure to attach `.catch` or return the promise to the caller.

---

## 9) Minimal illustrative examples
### Promise adopting another promise (thenable behavior):
```js
const thenable = { then(onFulfill) { onFulfill(42); } };
Promise.resolve(thenable).then(v => console.log(v)); // logs 42 (as microtask)
```

### Microtask order example:
```js
console.log('sync start');
Promise.resolve().then(() => console.log('microtask'));
setTimeout(() => console.log('macrotask'), 0);
console.log('sync end');
// Output:
// sync start
// sync end
// microtask
// macrotask
```

---

## 10) Interview-style theory questions (concise answers)
1. **Q:** What are the three Promise states?  
   **A:** Pending, Fulfilled, Rejected.

2. **Q:** Are `.then` callbacks synchronous or asynchronous?  
   **A:** Asynchronous — scheduled as microtasks.

3. **Q:** What is a thenable?  
   **A:** Any object with a callable `.then` property; Promise resolution will "assimilate" it.

4. **Q:** What happens if a `.then` handler throws?  
   **A:** The returned promise is rejected with the thrown error.

5. **Q:** How does `Promise.all` behave on rejection?  
   **A:** It rejects immediately with the first rejection reason; remaining results are ignored.

6. **Q:** What's `finally` used for?  
   **A:** Run cleanup logic regardless of outcome; passes through original value or reason.

7. **Q:** Why does `Promise.resolve(promise)` not create an extra wrapper?  
   **A:** It returns the same promise if the input is already a native Promise (no extra wrapping).

8. **Q:** What is the self-resolution guard?  
   **A:** The runtime throws `TypeError` if a promise is resolved with itself to avoid infinite recursion.

9. **Q:** How do microtasks compare with macrotasks?  
   **A:** Microtasks run before the next macrotask; microtasks drain completely between macrotasks.

10. **Q:** How does `Promise.any` indicate failure when all promises reject?  
    **A:** It rejects with an `AggregateError` containing all individual rejection reasons.

---

## 11) Coding — common interview tasks + short solutions
### A. Implement a minimal `Promise`-like class (conceptual)
```js
class MiniPromise {
  constructor(executor) {
    this.state = 'pending';
    this.value = undefined;
    this.handlers = [];

    const resolve = (val) => {
      queueMicrotask(() => this._resolve(val));
    };
    const reject = (err) => {
      queueMicrotask(() => this._reject(err));
    };

    try { executor(resolve, reject); }
    catch (e) { reject(e); }
  }

  _resolve(val) {
    if (this.state !== 'pending') return;
    if (val === this) return this._reject(new TypeError('Self resolution'));
    if (val && (typeof val === 'object' || typeof val === 'function')) {
      let then;
      try { then = val.then; } catch (e) { return this._reject(e); }
      if (typeof then === 'function') {
        let called = false;
        try {
          then.call(val, y => { if (!called) { called = true; this._resolve(y); } }, r => { if (!called) { called = true; this._reject(r); } });
        } catch (e) { if (!called) this._reject(e); }
        return;
      }
    }
    this.state = 'fulfilled';
    this.value = val;
    this._runHandlers();
  }

  _reject(err) { if (this.state !== 'pending') return; this.state = 'rejected'; this.value = err; this._runHandlers(); }

  _runHandlers() {
    this.handlers.forEach(h => queueMicrotask(() => h(this.value)));
    this.handlers = [];
  }

  then(onFulfilled, onRejected) {
    return new MiniPromise((resolve, reject) => {
      const handle = (val) => {
        try {
          if (this.state === 'fulfilled') {
            if (typeof onFulfilled === 'function') resolve(onFulfilled(val));
            else resolve(val);
          } else if (this.state === 'rejected') {
            if (typeof onRejected === 'function') resolve(onRejected(val));
            else reject(val);
          }
        } catch (e) { reject(e); }
      };

      if (this.state === 'pending') this.handlers.push(handle);
      else queueMicrotask(() => handle(this.value));
    });
  }
}
```
(This is conceptual and omits many spec details — but demonstrates the state machine, microtasks, and thenable assimilation.)


### B. Implement `Promise.all` (concise)
```js
function promiseAll(iter) {
  return new Promise((resolve, reject) => {
    const items = Array.from(iter);
    const results = [];
    let remaining = items.length;
    if (remaining === 0) return resolve([]);

    items.forEach((p, i) => Promise.resolve(p).then(v => {
      results[i] = v;
      if (--remaining === 0) resolve(results);
    }, reject));
  });
}
```

### C. Create a thenable object that resolves asynchronously
```js
const thenable = {
  then(resolve, reject) {
    setTimeout(() => resolve('done'), 10);
  }
};

Promise.resolve(thenable).then(console.log); // "done"
```

---

## 12) Practical tips & debugging
- Attach `.catch` to long-living promise chains or return the chain to callers.
- Use `Promise.allSettled` when you want results of all operations regardless of failure.
- Use `queueMicrotask` to schedule work in the microtask queue when integrating with Promises.
- When debugging ordering issues, sprinkle `console.log` before and inside `.then` handlers — remember they run in microtasks.
- Prefer `async/await` for readability, but remember `await` is syntactic sugar over `Promise` (it pauses in async function and resumes as a microtask).

---

## 13) Further reading (keywords)
Promise specification (Promise/A+ and ECMAScript spec), microtask queue, event loop, AggregateError, unhandledrejection.

---

*End of cheat-sheet.*


# Topic : Async & Concurrency
## Sub Topic : Event Loop Deep Dive — task ordering, requestAnimationFrame, queueMicrotask

## 1. High-level overview
The JavaScript runtime is single-threaded (per agent/window) and uses an **event loop** to coordinate execution of synchronous code, asynchronous callbacks, rendering, and microtasks. The loop repeatedly takes one *task* (macrotask) from the task queue, runs it to completion, then processes all pending microtasks, then performs rendering/layout/paint steps before moving to the next iteration. This ordering is what gives microtasks (promises/queueMicrotask/mutation observers) higher priority than macrotasks (setTimeout, I/O callbacks, DOM events).  

## 2. Key queues and steps (simplified)
- **Call stack** — where functions run.
- **Task (macrotask) queue(s)** — host callbacks such as `setTimeout`, `setInterval`, network events, user event callbacks, some API callbacks.
- **Microtask queue** — promise reactions (`.then/.catch`), `queueMicrotask()`, `MutationObserver` callbacks. Processed after each macrotask and paused only when empty.
- **Rendering step** — includes style/layout/paint and `requestAnimationFrame` callbacks are invoked ahead of the next repaint.

## 3. Practical ordering examples (what actually runs when)
1. Synchronous script runs and finishes.
2. Event loop takes at most one macrotask and runs it.
3. After the macrotask returns, **run all microtasks** (and any microtasks they enqueue) until the microtask queue is empty.
4. Perform rendering (if needed) and call `requestAnimationFrame` callbacks before the paint.
5. Repeat.

This means: microtasks run *before* rendering and before the next macrotask. `requestAnimationFrame` callbacks run during the rendering phase (before the paint), so they will execute after microtasks but before the visual frame appears.

## 4. `queueMicrotask()` specifics
- `queueMicrotask()` enqueues a microtask that will run at the next microtask checkpoint — that is, after the current macrotask finishes but before rendering and before the next macrotask.  
- Microtasks can enqueue other microtasks; the event loop will keep draining microtasks until the microtask queue is empty — be careful to avoid infinite microtask loops.

## 5. `requestAnimationFrame()` specifics
- `requestAnimationFrame(callback)` schedules `callback` to run right before the next repaint. The browser will call your callback in the rendering phase after microtasks for that frame have finished. It's the correct place to read/write layout-affecting DOM values for animations and to avoid layout thrashing.
- `requestAnimationFrame` callbacks are throttled in background tabs and can be aligned with display refresh for smoother animations.

## 6. Common pitfalls and gotchas
- Expectation mismatch: `setTimeout(fn, 0)` does **not** run immediately after the current function; it goes to the macrotask queue and will run after microtasks and rendering for the current loop iteration complete.
- Starvation: a continuously refilled microtask queue can starve macrotasks and block rendering.
- `requestAnimationFrame` vs `setTimeout(..., 16)` — the latter can drift and is not synced to paint cycles; prefer `rAF` for visual updates.

## 7. Small annotated examples

### Example A — microtasks before macrotasks and rAF
```js
console.log('script start');

setTimeout(() => console.log('macrotask: setTimeout'), 0);

Promise.resolve().then(() => {
  console.log('microtask: promise.then');
  queueMicrotask(() => console.log('microtask: queued via queueMicrotask'));
});

requestAnimationFrame(() => console.log('rAF: before paint'));

console.log('script end');
```
Likely order:
```
script start
script end
microtask: promise.then
microtask: queued via queueMicrotask
rAF: before paint
macrotask: setTimeout
```

### Example B — microtask causing starvation (avoid)
```js
function spin() {
  queueMicrotask(spin);
}
spin();
// This will keep the microtask queue non-empty and block rendering and macrotasks.
```

## 8. Interview-style theory questions (concise answers)

**Q1: What is the difference between microtasks and macrotasks?**  
A: Microtasks (promises, `queueMicrotask`, `MutationObserver`) are processed after each macrotask and before rendering/next macrotask; macrotasks (e.g., `setTimeout`, I/O, events) are processed one-per-event-loop-turn. Microtasks have higher scheduling priority.  

**Q2: When is `requestAnimationFrame` callback executed relative to microtasks and macrotasks?**  
A: `requestAnimationFrame` callbacks run in the rendering phase, after the current macrotask finishes and microtasks drain, but before the actual paint.  

**Q3: Why can a long chain of microtasks be dangerous?**  
A: Because microtasks are drained completely before the event loop proceeds to the next macrotask or rendering, an endlessly added microtask chain can starve macrotasks and block rendering, freezing the UI.

**Q4: Does `setTimeout(fn, 0)` run immediately after current synchronous code?**  
A: No. It schedules a macrotask; microtasks and rendering happen before it executes.

**Q5: How to force work to run after rendering?**  
A: Use `requestAnimationFrame` to schedule work before the next paint; to run after paint, you can `requestAnimationFrame(() => requestAnimationFrame(afterPaint))` (double rAF) or use other browser-specific APIs.

## 9. Coding/practical interview problems

1. **Problem:** Implement a basic scheduler that batches DOM writes and reads to avoid layout thrashing using `requestAnimationFrame` and a microtask queue.  
   **Answer sketch:** Collect reads and writes in arrays; schedule a single rAF to run all reads first, then perform writes — ensure reads happen before writes; use microtasks to allow synchronous enqueuing of reads/writes within the same tick.

2. **Problem:** Given interleaving promises, setTimeouts and rAFs, predict output order (typical whiteboard question).  
   **Practice:** Walk through the code: label each statement as sync / macrotask / microtask / rAF, then simulate event loop: run sync → macrotask → drain microtasks → rAF/render → next macrotask.

3. **Problem:** Prevent UI freeze when processing many items (e.g., rendering thousands of DOM nodes).  
   **Answer sketch:** Process in chunks using `requestIdleCallback` (if available), `setTimeout` with yielding, or `queueMicrotask` for small micro-batches — prefer chunking across macrotasks so the browser can render between chunks.

## 10. Quick reference cheatsheet (one-line bullets)
- After every macrotask: drain microtasks. citeturn0search10  
- `Promise.then`, `queueMicrotask`, `MutationObserver` → microtasks. citeturn0search3turn0search10  
- `setTimeout`, `setInterval`, user events, I/O → macrotasks. citeturn0search0  
- `requestAnimationFrame` runs in the render phase before paint. citeturn0search6turn0search8  
- Avoid infinite microtask chains (starvation + no painting). citeturn0search1

---

## References
- MDN: Microtask guide and queueMicrotask().  
- MDN: requestAnimationFrame() docs.  
- Jake Archibald: Tasks, microtasks, queues, and schedules.  
- javascript.info: Event loop description.  

# Topic : Async & Concurrency

## Sub Topic : Web APIs — setTimeout, fetch, Web Workers, Service Workers

---

> This cheat-sheet covers: how each API works, concrete code examples, gotchas and best practices, short interview-style theory questions with concise answers, and related coding problems you can practice. Downloadable as a single Markdown file.

---

# 1) Overview — what these APIs solve

- **setTimeout**: schedules a one-shot callback after a delay (or 0 ms to queue a macrotask). Useful for short deferred work, throttling UI updates, avoiding long synchronous blocks.
- **fetch**: modern promise-based network API for HTTP requests. Replaces `XMLHttpRequest` in almost every use-case, integrates with streams and Service Worker caching models.
- **Web Workers**: background threads for running CPU-bound or blocking tasks off the main UI thread. They communicate via message passing and have limited access to browser globals (no DOM).
- **Service Workers**: scriptable network proxy that runs separate from pages; intercepts network requests, enables offline-first caching strategies, push notifications and background sync.


---

# 2) API details + examples

## setTimeout

**What it does**
- Schedules callback execution after at least `delay` milliseconds. The browser uses task queues (macrotasks/microtasks) for scheduling; `setTimeout(fn, 0)` queues a macrotask.

**Example**
```js
const id = setTimeout(() => {
  console.log('runs later');
}, 1000);
// cancel
clearTimeout(id);
```

**Worker vs Window**
- `setTimeout` exists on both `Window` and `WorkerGlobalScope` (so workers can use it).

**Pitfalls & tips**
- Minimum delay clamping in inactive tabs / background throttling may increase delay.
- Long-running callbacks still block the thread they run on (use a worker for CPU tasks).
- Prefer `requestAnimationFrame` for DOM painting/updating synced with screen refresh.


## fetch

**What it does**
- Returns a `Promise` that resolves to a `Response` object. Supports streaming, request/response objects, credentials modes, and many cache modes.

**Example**
```js
async function loadJson(url) {
  const res = await fetch(url, { cache: 'no-cache' });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```

**Advanced**
- Use `AbortController` to cancel requests.
- Use response streams (`res.body.getReader()`) for progressive processing.
- Cache-control is handled by the browser and influenced by `Cache` mode and server headers.

**Pitfalls & tips**
- `fetch` only rejects on network errors — 4xx/5xx still resolve the Promise (check `res.ok`).
- Beware CORS: server must include correct headers to allow cross-origin access.


## Web Workers

**What they are**
- Dedicated scripts that run on a background thread. Communicate with main thread via `postMessage` and `message` events.

**Creating a worker**
```js
// main.js
const w = new Worker('worker.js');
w.postMessage({ cmd: 'start', payload: 42 });
w.onmessage = e => console.log('from worker', e.data);

// worker.js
onmessage = e => {
  // do CPU work
  const result = heavyCalc(e.data.payload);
  postMessage({ result });
};
```

**Capabilities & limits**
- No DOM access. Can use `fetch`, WebSockets (in some environments), IndexedDB, and other worker-friendly APIs.
- Can spawn other workers (subject to same-origin policies).

**Pitfalls & tips**
- Message passing copies or uses structured clone; avoid sending huge objects unless using `Transferable` (e.g., `ArrayBuffer`).
- Workers introduce serialization/deserialization overhead — best for heavier, long-running tasks.


## Service Workers

**What they are**
- Event-driven workers that act as a programmable network proxy for pages under their scope. Persist beyond page lifecycle (they can wake to handle `fetch`, `push`, `sync`, etc.).

**Registration**
```js
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js', { scope: '/' })
    .then(reg => console.log('registered', reg.scope))
    .catch(err => console.error('sw reg failed', err));
}
```

**Basic sw.js skeleton**
```js
self.addEventListener('install', e => {
  // pre-cache assets
});

self.addEventListener('activate', e => {
  // cleanup old caches
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cached => cached || fetch(event.request))
  );
});
```

**Capabilities & limits**
- Can intercept/modify network requests, access Cache Storage API, respond offline, and receive push messages.
- Must be served over HTTPS (except `localhost`).

**Pitfalls & tips**
- Scope rules: registration `scope` controls which pages the worker controls.
- Lifecycle: `install` → `activate`; updates are controlled by `skipWaiting()` and `clients.claim()` optionally.
- Cache invalidation strategies matter (stale-while-revalidate, network-first, cache-first, etc.).


---

# 3) Performance considerations & best practices

- Offload expensive CPU work to Web Workers to keep main thread responsive.
- Use `AbortController` + timeouts for network requests.
- For UI updates tied to frame rates, use `requestAnimationFrame` instead of `setTimeout(…, 16)`.
- Use Service Worker caching strategies tailored to your app: e.g., network-first for dynamic data, cache-first for static assets.
- Keep Service Worker install fast: pre-cache essential assets; lazy-cache large resources.


---

# 4) Interview-style theory questions (concise answers)

1. **Q:** How does `setTimeout(fn, 0)` differ from `Promise.resolve().then(fn)`?  
   **A:** `setTimeout(...,0)` queues a macrotask; `.then(...)` schedules a microtask that runs earlier in the event loop (after current stack, before next macrotask).

2. **Q:** When does `fetch` reject its Promise?  
   **A:** Only on network-level errors (DNS failure, aborted fetch). HTTP error responses (4xx/5xx) resolve the Promise — check `response.ok`.

3. **Q:** Can a Web Worker access `document` or `window`?  
   **A:** No. Workers run in an isolated global scope (`WorkerGlobalScope`) without DOM access.

4. **Q:** Why are Service Workers served over HTTPS only?  
   **A:** They can intercept network requests and run arbitrary code — to avoid MITM and ensure security, browsers require HTTPS (localhost exception for dev).

5. **Q:** What is `postMessage` structured clone?  
   **A:** It's the algorithm used to copy data between contexts (main thread ↔ worker). It supports many types but not functions; use Transferables to avoid copying.


---

# 5) Concise answers to common follow-up theory micro-topics

- **Event loop order (simplified):** current script → microtasks (Promises, queueMicrotask) → next macrotask (setTimeout, I/O callbacks) → rendering.
- **Service worker lifecycle:** register → install (cache assets) → activate (cleanup) → controlled → update flow requires redeploying and new SW installing; clients must be claimed to take control.
- **Fetch streaming:** `Response.body` gives a readable stream; you can `.getReader()` to process chunks progressively.


---

# 6) Coding interview practice questions (application)

1. **Implement a debounce function using `setTimeout`.**  
   *Goal:* Avoid calling a function more than once in a short time window.

2. **Use `fetch` with `AbortController` to implement a timeout wrapper that rejects after X ms.**  
   *Goal:* Combine cancelation and network request handling.

3. **Offload JSON parsing of a very large payload to a Web Worker and send progress messages back.**  
   *Goal:* Practice message passing and transfer of `ArrayBuffer`.

4. **Build a simple Service Worker that implements `stale-while-revalidate` caching for static assets.**  
   *Goal:* Practice cache strategies, install/activate events.

5. **Create a pool of Web Workers to parallelize CPU-heavy tasks and collect results with Promise.all.**  
   *Goal:* Worker lifecycle, load balancing, and structured cloning vs Transferables.


---

# 7) Quick code snippets (answers to the tasks above)

### Debounce
```js
function debounce(fn, wait) {
  let t;
  return function (...args) {
    clearTimeout(t);
    t = setTimeout(() => fn.apply(this, args), wait);
  };
}
```

### fetch timeout with AbortController
```js
async function fetchWithTimeout(url, options = {}, ms = 5000) {
  const ac = new AbortController();
  const id = setTimeout(() => ac.abort(), ms);
  try {
    const res = await fetch(url, { ...options, signal: ac.signal });
    clearTimeout(id);
    return res;
  } catch (e) {
    clearTimeout(id);
    throw e;
  }
}
```

### Worker JSON parse (main thread)
```js
const worker = new Worker('parseWorker.js');
worker.postMessage({ buf: myArrayBuffer }, [myArrayBuffer]); // transfer
worker.onmessage = e => console.log('done', e.data);
```

### Service Worker stale-while-revalidate (simplified)
```js
// sw.js
const CACHE = 'v1';
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(CACHE).then(async cache => {
      const cached = await cache.match(event.request);
      const network = fetch(event.request).then(res => {
        cache.put(event.request, res.clone());
        return res;
      }).catch(() => null);
      return cached || network;
    })
  );
});
```


---

# 8) Further reading & references

- MDN — setTimeout, fetch, Web Workers, Service Worker guides.
- WHATWG Fetch Standard for in-depth fetch behaviors.
- web.dev PWA and service worker tutorials for real-world patterns.


---

# 9) How to use this file

- Use the theory questions as quick interview flashcards.
- Use the coding tasks to create small repo examples and unit tests.
- Copy snippets into small sandboxes (CodePen / JSFiddle / stackblitz) to experiment.


---

*End of cheat-sheet.*


# Async & Concurrency — Debounce & Throttle

**Topic:** Async & Concurrency  
**Sub Topic:** Debounce & Throttle — implementation, differences, performance use cases

---

## At-a-glance summary

- **Debounce**: Group rapid-fire calls and run the function **once** after the events stop for a given delay. Great for *"wait until user stops typing/resizing"* scenarios.
- **Throttle**: Limit a function to run at most once every `interval` milliseconds. Great for *"run at a steady rate during continuous activity"* scenarios.

---

## Implementations (Vanilla JS)

### Simple debounce (trailing)
```js
function debounce(fn, wait) {
  let timer = null;
  return function(...args) {
    const ctx = this;
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(ctx, args), wait);
  };
}
```

### Debounce with `immediate` (leading) option and `cancel`
```js
function debounce(fn, wait, immediate = false) {
  let timer = null;
  const debounced = function(...args) {
    const ctx = this;
    const callNow = immediate && !timer;
    clearTimeout(timer);
    timer = setTimeout(() => {
      timer = null;
      if (!immediate) fn.apply(ctx, args);
    }, wait);
    if (callNow) fn.apply(ctx, args);
  };
  debounced.cancel = () => { clearTimeout(timer); timer = null; };
  return debounced;
}
```

### Simple throttle (timestamp approach, leading)
```js
function throttle(fn, interval) {
  let last = 0;
  return function(...args) {
    const now = Date.now();
    if (now - last >= interval) {
      last = now;
      fn.apply(this, args);
    }
  };
}
```

### Throttle with trailing invocation (timer approach)
```js
function throttle(fn, interval) {
  let last = 0;
  let timer = null;
  return function(...args) {
    const ctx = this;
    const now = Date.now();
    const remaining = interval - (now - last);
    if (remaining <= 0) {
      clearTimeout(timer);
      timer = null;
      last = now;
      fn.apply(ctx, args);
    } else if (!timer) {
      timer = setTimeout(() => {
        last = Date.now();
        timer = null;
        fn.apply(ctx, args);
      }, remaining);
    }
  };
}
```

---

## Differences (concise)

- **When they fire**
  - Debounce: fires *after* events stop for `wait` ms.
  - Throttle: fires at most once every `interval` ms (regularly during activity).
- **Guarantees**
  - Debounce: may never fire if events never stop (unless `immediate`/leading).
  - Throttle: guarantees periodic execution.
- **Best for**
  - Debounce: search inputs, form validation, resize debounce, API call after typing.
  - Throttle: scroll listeners, mousemove, window resize updates while resizing, progress indicators.

---

## Performance considerations & tradeoffs

- Debounce reduces **number of calls** drastically; useful when you only need a final result (fewer network requests).
- Throttle controls **rate of calls** and provides smoother periodic updates; reduces burstiness while retaining responsiveness.
- Both reduce main-thread work and paint/layout thrashing when attached to high-frequency DOM events.
- Prefer using battle-tested libraries (e.g., `lodash.debounce` / `lodash.throttle`) when you need robust, edge-case-handled implementations.

---

## Real-world use-cases

- **Debounce**
  - Autocomplete / search-as-you-type (delay API calls until typing stops).
  - Form validation after user stops typing.
  - Resize handler that recalculates layout once when resizing stops.
- **Throttle**
  - Infinite-scroll load triggering while scrolling (check position periodically).
  - Animations or position updates on `scroll` / `mousemove`.
  - Polling UI updates limited to once per X ms.

---

## Interview theory questions (short answers)

1. **Q: What is debounce?**  
   A: A technique that delays function execution until calls stop for a specified delay; it collapses many calls into one.

2. **Q: What is throttle?**  
   A: A technique that ensures a function runs at most once per specified interval; it spaces out repeated calls.

3. **Q: When would you choose debounce over throttle?**  
   A: When you only need the final action after rapid events end (e.g., search input, final resize).

4. **Q: When is throttle better?**  
   A: When you need periodic updates during continuous events (e.g., scroll-based position updates).

5. **Q: What issues do you watch for with debounced event handlers?**  
   A: Missed final call if your debounce is cancelled or if you rely on immediate/leading behaviour; also UX delay if wait is too long.

6. **Q: How does leading/trailing options change behavior?**  
   A: Leading causes immediate invocation at start of burst; trailing calls at the end. Combining both needs careful implementation to avoid double calls.

---

## Coding interview questions (application + quick hints)

1. **Implement `debounce` with `cancel()` and `flush()` methods.**  
   - Hint: store timer, track last args/context, `flush()` should invoke pending call immediately.

2. **Implement `throttle` that supports `leading` and `trailing` options.**  
   - Hint: combine timestamp + timer approach; guard against double-invocation.

3. **Given a search input, implement client-side debounced API calls with React hooks.**  
   - Hint: use `useRef` to keep timer and `useEffect` to clean on unmount; consider `useCallback` memoization or `use-debounce` hook.

4. **Optimize a heavy `scroll` handler to update only every 100ms and ensure final update runs when scrolling stops.**  
   - Hint: use throttle for periodic updates and a debounced finalizer (combo pattern).

5. **Find bugs in a broken debounce implementation (candidate's code).**  
   - Hint: look for incorrect `this` binding, missing `clearTimeout`, improper handling of immediate/leading, and memory leaks.

---

## Example: React hook (debounced value)
```js
import { useState, useEffect } from 'react';

export function useDebouncedValue(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);

  return debounced;
}
```

---

## Combination pattern
Sometimes you want both behaviors: e.g., throttle updates while user scrolls, but run a debounced finalizer after the scroll stops (updateSnapshot + saveState).

---

## Further reading
- MDN Glossary: *Debounce* / *Throttle* – succinct definitions and guidance.  
- Lodash docs for robust `_.debounce` / `_.throttle` implementations.  
- Visual guides and blog posts (CSS-Tricks, Kettanaito) for intuition.

---

## Short checklist for choosing
- Need final-only action → **Debounce**.  
- Need periodic updates during activity → **Throttle**.  
- Need both periodic + final → **Throttle + Debounce (combined)**.  
- Need robust behavior across environments → **Use lodash**.


# Memory & Performance — Garbage Collection (JavaScript)

## Topic
**Garbage Collection** — mark-and-sweep, reference cycles, WeakMap / WeakRef / FinalizationRegistry

---

## 1) Core concepts (short, sharp)
### What is garbage collection?
Automatic reclamation of memory that is no longer reachable from program "roots" (globals, stack frames, closures). Modern JS engines run GC to free unreachable objects so developers don't manually `free` memory.

### Mark-and-sweep (the base algorithm)
1. **Mark phase**: Start from roots, recursively mark reachable objects.
2. **Sweep phase**: Walk heap; collect/unallocate objects not marked as reachable.  
This is the conceptual algorithm used by most JS engines. citeturn0search0turn0search4

### Generational GC
- Heap split into **young** and **old** generations.
- Short-lived objects are collected frequently in the young gen (fast, copying/Scavenge).
- Long-lived objects are tenured/moved to old gen and collected less often (mark-compact/sweep).  
V8 and other engines heavily optimize with generational strategies. citeturn0search6turn0search11

### Incremental / concurrent strategies
To reduce pause times, modern collectors perform marking incrementally or concurrently with program execution (e.g., incremental marking, parallel sweeping). These are engine-specific optimizations (V8, SpiderMonkey, JavaScriptCore). citeturn0search13turn0search11

---

## 2) Reference cycles — are they a problem?
Classic myth: *circular references cause leaks in JS.* Reality: JS mark-and-sweep collectors detect reachability from roots; if an entire cycle is unreachable it will be collected — **cycles are not inherently leaked**. Reference-counting-only collectors (rare in modern JS) would leak cycles, but major engines use tracing GCs which handle cycles. citeturn0search1turn0search12

However, leaks still happen when references from **roots** (globals, DOM, closures, timers, event listeners) keep objects alive — cycles that are reachable won't be collected.

---

## 3) Weak references: WeakMap, WeakSet, WeakRef, FinalizationRegistry
- **WeakMap / WeakSet**: keys are held *weakly* — presence as a key does not keep the key object alive. Useful for attaching metadata to objects without preventing GC (caching, private metadata for DOM nodes). You can't iterate over WeakMap because entries can disappear asynchronously. citeturn0search2turn0search10
- **WeakRef**: holds a weak reference to an object; can be used to access an object if still alive. Must be used carefully; object may be collected at any time. Use `FinalizationRegistry` to run cleanup when an object is collected (but timing and ordering are implementation-dependent). citeturn0search8

---

## 4) Common memory leak sources & how to fix them
1. **Forgotten timers / intervals** (`setInterval`, `setTimeout` callbacks referencing large objects).  
   *Fix*: clear timers when not needed.
2. **Detached DOM nodes**: removing nodes from DOM but still keeping references in JS (closures, caches).  
   *Fix*: null references, avoid long-lived caches referencing node trees, prefer WeakMap for node metadata.
3. **Global variables / singletons** that accumulate data.  
   *Fix*: limit lifetime, purge caches periodically, use scoped storage.
4. **Closures capturing large objects** (event handlers that close over big structures).  
   *Fix*: avoid capturing whole structures; store only what's necessary.
5. **Event listeners not removed** (especially on long-lived DOM elements).  
   *Fix*: remove listeners or use delegated listeners tied to lifecycles.

Practical debugging: use Chrome DevTools Memory tab (Heap snapshots, allocation instrumentation, allocation timelines) to find retained dominators and leaking roots. citeturn0search4turn0search20

---

## 5) Quick interview-style theory Qs (concise answers)

**Q1: Explain mark-and-sweep in 2–3 sentences.**  
A: Start from roots and mark all reachable objects; then sweep the heap and reclaim objects not marked. This collects unreachable objects including cycles, unlike naive reference counting. citeturn0search0

**Q2: What is generational GC and why is it useful?**  
A: Heap split into young/old generations; most objects die young so frequent, fast collections in young gen reduce overall GC cost and improve throughput. citeturn0search6

**Q3: Do circular references cause memory leaks in JS?**  
A: No—tracing GCs (mark-and-sweep) can collect unreachable cycles. Leaks occur when cycles are reachable from roots (globals, closures, DOM). citeturn0search1

**Q4: When should you use WeakMap vs Map?**  
A: Use WeakMap when keys are objects you don’t want to keep alive solely for the mapping (e.g., DOM node metadata). Use Map when you need iteration or stable entries. citeturn0search2

**Q5: What is FinalizationRegistry for? Should you rely on it?**  
A: It lets you register a cleanup callback when an object is GC'd, but timing is non-deterministic and should not be used for critical program logic (use for opportunistic cleanup). citeturn0search8

---

## 6) Practical code examples (small, focused)

### Example: a memory leak via closed-over variable
```js
// Leaky: handler holds ref to 'big'
function register() {
  const big = new Array(1e6).fill("x");
  window.addEventListener('resize', () => {
    console.log(big[0]); // closure keeps 'big' alive
  });
}
register();
// big will stay reachable while the handler exists
```

**Fix**: remove listener or avoid capturing `big`:
```js
function register() {
  const big = new Array(1e6).fill("x");
  const handler = () => { /* do minimal work */ };
  window.addEventListener('resize', handler);
  // when done:
  // window.removeEventListener('resize', handler);
}
```

### Example: using WeakMap for node metadata
```js
const meta = new WeakMap();

function attach(node, info) {
  meta.set(node, info);
}

// when node is removed and no other refs exist, it can be GC'd
```

### WeakRef + FinalizationRegistry (advanced, use carefully)
```js
const registry = new FinalizationRegistry(token => {
  console.log('clean up for', token);
});

(function() {
  let obj = {name: 'temp'};
  const ref = new WeakRef(obj);
  registry.register(obj, 'objToken');
  obj = null; // object eligible for GC; registry may call cleanup later
})();
```

---

## 7) Coding interview-style problems (with brief hints)
1. **Detect memory growth in a long-running server** — write an endpoint that reports process memory (Node: `process.memoryUsage()`), and set up automated heap snapshots when RSS or heapUsed crosses thresholds. *Hint*: use heap snapshots + diff to locate retained dominators.  
2. **Implement a cache that doesn't prevent GC** — implement a memoization cache using `WeakMap` for object keys; for primitive keys use a regular Map. *Hint*: separate caches by key-type.  
3. **Find leak in DOM app** — given a single-page app that slowly grows in memory on route changes, locate detached nodes by taking two heap snapshots before and after route change and compare retained sizes. *Hint*: look for detached DOM trees and large retained sizes.

---

## 8) Quick checklist to prevent leaks
- Remove event listeners and timers when components unmount.
- Avoid storing DOM nodes on long-lived globals.
- Use WeakMap for metadata tied to object lifetime.
- Null large references if no longer needed (rarely necessary but explicit).
- Profile regularly in DevTools.

---

## 9) Further reading (short list)
- MDN: Memory management in JavaScript. citeturn0search4  
- javascript.info: Garbage collection. citeturn0search0  
- V8 blog / Orinoco posts: deep implementation details. citeturn0search11turn0search6

---

## 10) Save & use
This cheat-sheet is designed as a compact interview + reference guide. Use the code snippets in Node or browser consoles to experiment and use DevTools for concrete profiling.

---

*Generated by your Interview Cheat Sheet assistant — concise, practical, and runnable.*

# Memory & Performance — Memory Leaks in JavaScript

## Topic: Memory & Performance  
## Sub Topic: Memory Leaks (Common Causes: Closures, Event Listeners, Global Variables)

---

## 1. Detailed Explanation

JavaScript runs in a garbage-collected environment. The collector frees memory when values are no longer reachable. A **memory leak** happens when references to unused objects persist, preventing cleanup. These leaks creep into JS apps through subtle patterns—especially closures, listeners, and broad-scoped variables.

### Closures
A closure keeps a function’s external variables alive. This is useful, but trouble arrives when closures retain references to objects no longer needed.

Example issue:
```js
function makeLeaker() {
  const heavyObj = { big: new Array(100000).fill("x") };
  return function() {
    console.log("Using only a tiny part");
  };
}
```
Even though the inner function doesn't need `heavyObj`, the outer scope keeps it alive.

### Event Listeners
Event listeners attach functions to elements. If you forget to remove them when elements are removed, the listener still holds references to the node, preventing collection.

Example leak:
```js
const el = document.getElementById("btn");
function handler() {}
el.addEventListener("click", handler);

el.remove(); // Listener still alive → memory leak
```

### Global Variables
Variables kept in the global scope essentially remain reachable for the entire lifetime of the page. If they hold large objects or collections that grow over time, memory usage climbs.

Example:
```js
window.cache = {};
```
This cache will stay alive as long as the page lives.

---

## 2. Theory Questions for Interviews (With Compact Answers)

**1. What is a memory leak in JavaScript?**  
A memory leak occurs when memory that’s no longer needed remains reachable, preventing the garbage collector from freeing it.

**2. How do closures cause memory leaks?**  
Closures keep references to outer scope variables. If a closure persists longer than needed, it retains memory for unused variables.

**3. How do event listeners cause memory leaks?**  
When a DOM node with listeners is removed without removing the listener, the listener retains references to the node.

**4. Why are global variables a common source of leaks?**  
They remain reachable for the lifetime of the application, so anything referenced by them can’t be freed.

**5. How does the garbage collector decide what to free?**  
It frees objects that are *not reachable* from roots like global objects or current execution contexts.

**6. How does a detached DOM node cause leaks?**  
JS references to removed DOM nodes keep them from being garbage-collected even if they're not in the DOM.

---

## 3. Coding Questions Related to Memory Leaks

### Q1: Detecting a Memory Leak in a Web App
Write code that tracks allocations over time to detect potential leaks.

```js
let arr = [];
setInterval(() => {
  arr.push(new Array(10000).fill("data"));
  console.log("size", arr.length);
}, 1000);
```
This intentionally leaks memory; useful for profiling in Chrome DevTools.

### Q2: Fix an Event Listener Leak
Problem code:
```js
function init() {
  const el = document.getElementById("btn");
  el.addEventListener("click", () => console.log("clicked"));
}
```
Fix:
```js
function init() {
  const el = document.getElementById("btn");
  function handler() {
    console.log("clicked");
  }
  el.addEventListener("click", handler);

  return () => el.removeEventListener("click", handler);
}
```

### Q3: Prevent Closure-Based Leak
```js
function setup() {
  let huge = new Array(500000).fill("XX");
  document.getElementById("ready").onclick = function () {
    console.log("ready");
  };
  huge = null; // release reference
}
```

---

## Downloadable Cheat Sheet Ready
This file summarizes memory leaks, their causes, questions, and related coding patterns.


# Memory & Performance Cheat Sheet

## Topic: Performance Profiling  
### Sub Topic: Chrome DevTools, Flame Charts, Optimizing Reflows

Modern browsers give you x‑ray goggles for JavaScript execution. Chrome DevTools' Performance tab lets you record a page’s activity and inspect where time evaporates. A flame chart visualizes your call stack over time: wide bars mean long-running functions. Anything repeatedly expanding like a fractal fern is a hotspot.  

Reflows happen when the browser recalculates layout because your code touched style-affecting properties. Excessive reflows slow down rendering. Minimizing layout thrashing—toggling between JS writes and reads of layout-dependent values—keeps the engine calm.

### Common Theory Questions with Concise Answers
Q: What does a flame chart show?  
A: A timeline of function calls where width represents execution time, helping identify slow or repeated tasks.

Q: What triggers reflows?  
A: DOM mutations that change geometry (size, position) or computed styles.

Q: How do you avoid layout thrashing?  
A: Batch DOM reads together and DOM writes together.

### Coding-Based Interview Examples
Example: Identify layout thrashing.
```js
// Bad
for (let el of list) {
  let h = el.offsetHeight; // layout read
  el.style.height = h + 10 + "px"; // write
}
```

Optimized:
```js
const heights = list.map(el => el.offsetHeight);
list.forEach((el, i) => el.style.height = heights[i] + 10 + "px");
```

---

## Topic: Object & Array Optimizations  
### Sub Topic: Shallow vs Deep Copy, Immutability Patterns

A shallow copy duplicates only top-level references. A deep copy recreates nested structures. Immutable patterns avoid in-place mutation, enabling predictable state updates—core to libraries like React.

### Concise Theory Answers
Q: Why avoid deep copying large structures frequently?  
A: Deep copies are expensive; they recreate entire object graphs.

Q: How to create a shallow copy?  
A: Using spread (`{...obj}`) or `Object.assign`.

Q: Why prefer immutability?  
A: It simplifies debugging and allows structural sharing for performance.

### Coding Examples
Shallow copy:
```js
const newObj = { ...oldObj };
```

Deep copy (simple):
```js
const deep = JSON.parse(JSON.stringify(obj));
```

Immutable update:
```js
const updated = { ...state, count: state.count + 1 };
```

---

## Topic: Defer & Async Scripts  
### Sub Topic: Render Blocking, Preloading, Prefetching

A browser blocks parsing when it hits a normal `<script>` tag. `async` loads scripts in parallel but executes immediately once ready. `defer` waits to execute scripts until HTML parsing is done.

Preloading tells the browser to fetch a resource early. Prefetching prepares for future navigation, whispering hints about what's needed soon.

### Concise Theory Answers
Q: What is render-blocking?  
A: When script loading pauses HTML parsing.

Q: Difference between async and defer?  
A: `async` executes ASAP; `defer` waits until DOM is parsed.

Q: What is preload used for?  
A: High‑priority early fetching of critical resources.

### Coding Examples
Async vs Defer:
```html
<script src="script.js" async></script>
<script src="script.js" defer></script>
```

Preload critical CSS:
```html
<link rel="preload" href="styles.css" as="style">
```

Prefetch next‑page assets:
```html
<link rel="prefetch" href="/next-page.js">
```

