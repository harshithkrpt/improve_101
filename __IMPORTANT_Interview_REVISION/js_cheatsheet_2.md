
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

