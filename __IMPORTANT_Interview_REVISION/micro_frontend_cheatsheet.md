# Micro Frontends — Cheat Sheet

**Topic:** Micro Frontends

**Sub Topic:** Concept — what is MFE, advantages, when to use

---

## 1. Quick definition

**Micro Frontend (MFE)** is an architectural style where a single web application is composed from multiple **independently developed, tested, and deployable frontend applications**. Each MFE owns its own UI, business logic, and deployment lifecycle while the host/container composes them into a unified experience.

---

## 2. Core ideas (short)

- **Team-per-feature**: each remote team owns an independently deployable slice of the UI.
- **Independent deployability**: MFEs are built and released separately; runtime composition stitches them together.
- **Tech-agnosticism**: teams may choose different frameworks or versions where needed.
- **Clear contracts**: well-defined UI/behavior contracts (routing points, events, shared styles) reduce coupling.

---

## 3. How MFEs are composed (patterns)

1. **Build-time integration (static composition)**
   - Microapps are compiled together into a single bundle at build-time.
   - Simpler runtime but couples deploys and builds.

2. **Server-side composition**
   - The server assembles HTML fragments from independently built MFEs and returns a composed page.
   - Good for SEO and initial-load performance.

3. **Client-side composition (runtime)**
   - The shell dynamically loads MFE bundles (via script tags, module federation, iframe-less runtime loaders).
   - Maximizes independence and deploy speed.

4. **Iframes**
   - Strong isolation; heavy and awkward for UX/communication; good when isolation/security is paramount.

---

## 4. Advantages / Benefits

- **Scalability for teams**: independent code ownership improves workflow for many teams.
- **Faster releases**: teams can ship independently without coordinating monolithic releases.
- **Technology freedom**: migration strategies and experimentation with new frameworks become easier.
- **Failure isolation**: a buggy MFE can be degraded without taking down the entire site.
- **Incremental refactor/migration**: replace parts of a large app progressively.

---

## 5. Trade-offs / Challenges

- **Complex runtime**: composition, shared dependencies, and boot order require careful design.
- **Bundle duplication**: risk of shipping multiple copies of libraries (React, utilities) unless deduped.
- **Cross-MFE communication**: requires agreed-upon patterns (events, shared stores, or minimal APIs).
- **UX consistency**: consistent look & feel across teams needs governance (design system, tokens).
- **Operational overhead**: CI/CD, monitoring, and debugging across many deployments increases complexity.

---

## 6. When to use MFEs (guidelines)

Use Micro Frontends when:

- You have a **large product** with multiple independent teams** working on distinct product areas.
- You need **independent deployment** velocity** and reduced coordination costs.
- You plan to **migrate** a monolithic frontend gradually to new stacks.
- You need **strong isolation** between features for security or ownership reasons.

Avoid MFEs when:

- You have a **small team** or small app — added complexity likely outweighs benefits.
- You need extreme performance on first load and can’t accept runtime complexity.

---

## 7. Practical patterns & best practices

- **Shared runtime / dependency strategy**: choose between shared dependency injection, CDN-hosted vendor bundles, or Module Federation with version policies.
- **Design system / tokens**: central repository for styles, tokens, and components to maintain consistent UX.
- **Contract-first communication**: use events or well-documented APIs (avoid tight coupling via global state).
- **CI/CD per MFE**: automated tests, linting, and Canary deployments per MFE to maintain quality.
- **Performance budgets**: set per-MFE budgets to avoid bloat.
- **Observability**: distributed tracing, per-MFE metrics, and centralized error reporting.

---

## 8. Interview — Theory questions (concise answers)

**Q1: What is a micro frontend?**
A1: An architectural approach that splits a frontend app into smaller, independently developed and deployable pieces that are composed at runtime or build time into a single user experience.

**Q2: Name three composition strategies for MFEs.**
A2: Build-time composition, server-side composition (HTML fragments), and client-side runtime composition (dynamic script/module loading); iframes as a fourth option.

**Q3: How would you avoid duplicate vendor libraries across MFEs?**
A3: Use shared dependency strategies — CDN-hosted vendor bundles, Module Federation shared modules with strict versioning, or a single shared runtime package.

**Q4: How do MFEs communicate between each other?**
A4: Prefer event-driven messaging (custom events, postMessage for iframes), a shared minimal pub/sub library, or agreed APIs; avoid sharing mutable global state.

**Q5: When would you not choose MFEs?**
A5: For small apps, single-team projects, or when the added complexity and performance cost outweigh benefits.

---

## 9. Interview — Coding / architecture questions

**Q1: Design a shell that loads MFEs at runtime using native ES modules (high level).**
- Steps: host page uses a manifest (JSON) listing MFE entry module URLs → dynamic `import()` each module → call exported mount functions into DOM containers → handle unload/cleanup.
- Focus points: error handling, timeouts, loading indicators, and fallback UI.

**Q2: Show a minimal example (pseudo-code) of an MFE exposing a mount function.**

```js
// mfe-root/index.js
export function mount(container) {
  const root = document.createElement('div')
  root.innerHTML = `<h3>Product MFE</h3>`
  container.appendChild(root)
  return () => container.removeChild(root) // cleanup
}
```

**Q3: How would you share React between applications using Module Federation? (conceptual)**
- Declare React as a shared singleton in the host and remotes.
- Use strict versioning policy to avoid multiple copies.
- Verify at runtime that a single instance is used and provide fallbacks.

**Q4: Build-time vs runtime composition — advantages of runtime?**
- Runtime gives independent deploys and faster team autonomy; build-time is simpler and smaller runtime surface.

---

## 10. Quick checklist to evaluate MFE fit

- Number of teams: >2 → consider MFEs.
- Independent release needs: high → MFEs help.
- Product size & complexity: large → MFEs fit.
- Strong UX consistency requirement: yes → need governance.
- Operational maturity (CI/CD, monitoring): present → proceed.

---

## 11. Further reading

- Martin Fowler — *Micro Frontends* article
- micro-frontends.org — community patterns and examples
- ThoughtWorks Radar — micro-frontends guidance

---

*This cheat sheet is optimized for interview prep: theory + quick coding prompts. Use it as a starting point and adapt patterns to your team’s constraints.*


# Micro Frontends — Architecture Approaches & Module Federation & Routing

**Topic:** Micro Frontends

**Sub Topics:**
- Architecture Approaches — iframe, Webpack Module Federation, single-spa
- Module Federation — federated modules, host/remote concepts
- Routing — independent routes, communication via events or props

---

## 1. Architecture Approaches

### 1.1 Iframe-based Micro Frontends
Iframes provide hard isolation. Each micro frontend runs in its own document context with isolated CSS, JS, network scope, and security boundaries.

**Pros:**
- Strong sandboxing and security isolation.
- No shared global scope → safe for legacy apps.

**Cons:**
- Expensive in performance; each iframe is a full document.
- Harder shared routing and seamless navigation.
- Poor SSR and SEO.

**Use Case:** When you need strong isolation or when integrating legacy / externally owned apps.

---

### 1.2 Webpack Module Federation (Runtime Composition)
This is the modern, popular technique where each micro frontend exposes certain JavaScript modules at runtime, and the host dynamically loads them without rebuilding.

**How it works (high level):**
- Each **remote** app exposes modules through `ModuleFederationPlugin`.
- A **host** app dynamically loads the exposed modules at runtime.
- Dependencies can be shared as singletons.

**Pros:**
- True independent deployments.
- No iframes; seamless UX.
- Efficient shared dependencies.

**Cons:**
- Requires Webpack.
- Some complexity in version negotiation and caching.

**Use Case:** Large SPA ecosystems using Webpack + React/Vue/Angular.

---

### 1.3 single-spa (Application Orchestration Framework)
single-spa provides a framework that lets multiple micro apps coexist in the same page via lifecycle methods (`bootstrap`, `mount`, `unmount`).

**Pros:**
- Framework-agnostic (React, Vue, Angular can co-exist).
- Flexible routing and orchestration.

**Cons:**
- Requires careful global management.
- Shared dependencies not automatic like Module Federation.

**Use Case:** When you need framework-agnostic orchestration with explicit lifecycle control.

---

## 2. Module Federation — Deep Dive

### 2.1 Federated Modules
A federated module is a file exposed from a remote build so that a host can load it dynamically.

Example (Remote):
```js
// webpack.config.js
new ModuleFederationPlugin({
  name: 'products',
  filename: 'remoteEntry.js',
  exposes: {
    './ProductsApp': './src/App',
  },
  shared: ['react', 'react-dom'],
})
```

Example (Host):
```js
new ModuleFederationPlugin({
  remotes: {
    products: 'products@https://domain.com/remoteEntry.js',
  },
  shared: ['react', 'react-dom'],
})
```

---

### 2.2 Host / Remote Concepts
**Host**
- Loads remote applications at runtime.
- Defines shell UI, global layout, global routing.

**Remote**
- Exposes components, functions, or full apps.
- Owns its own build & deployment pipeline.

**Shared Modules**
- Libraries shared as singletons (e.g., React) to prevent duplicates.

**Advantages:**
- Enables full runtime composition.
- Removes need for coordinated builds.

---

### 2.3 Deployment Strategy
- Each remote deploys independently.
- The host loads the latest remote entry file via URL.
- Remote version mismatches should be handled via version constraints.

---

## 3. Routing in Micro Frontends

### 3.1 Independent Routes
Each MFE owns its routes internally. The shell router decides which micro app to mount based on the URL.

Example (Host Routing Logic):
```js
if (location.pathname.startsWith('/products')) {
  mountProductsApp()
} else if (location.pathname.startsWith('/account')) {
  mountAccountApp()
}
```

Each remote might then use its own React Router instance internally:
```jsx
<Routes>
  <Route path="/products" element={<ProductList/>} />
  <Route path="/products/:id" element={<ProductDetail/>} />
</Routes>
```

---

### 3.2 Communication between MFEs
MFEs should avoid tight coupling. Use event-driven patterns or props passed during mount.

**Approaches:**
- Custom browser events: `window.dispatchEvent(new CustomEvent('cart:add', {detail: ...}))`
- Shared global event bus (lightweight pub/sub)
- Passing props to remote via host:
```js
mountProductsApp({ onProductClick: openDetails })
```
- URL as the contract (search params, hash)

Avoid: Sharing global mutable state directly across MFEs.

---

## 4. Interview Theory Questions (Concise Answers)

**Q1: What are the three main architecture approaches for micro frontends?**
A1: Iframes (hard isolation), Module Federation (runtime composition), and single-spa (orchestrated lifecycle-based integration).

**Q2: What problem does Module Federation solve?**
A2: It enables independent deployments by dynamically loading remote modules at runtime without rebuilding the host.

**Q3: What is a host and what is a remote?**
A3: Host loads micro apps. Remotes expose modules via Module Federation.

**Q4: How do you handle routing between multiple MFEs?**
A4: The shell controls top-level routing and mounts/unmounts MFEs. Each MFE manages internal routing.

**Q5: How should MFEs communicate without tight coupling?**
A5: Use custom browser events, a minimal pub/sub system, or props from the host.

---

## 5. Coding / Architecture Exercises

**Exercise 1:** Implement a Module Federation host that loads two remotes and mounts them based on the URL.
- Focus: remotes config, shared libraries, dynamic imports, mount APIs.

**Exercise 2:** Write a `mount()` function for a remote app that accepts properties (like callbacks) from the host.

```js
export function mount(container, props) {
  const root = createRoot(container)
  root.render(<App {...props} />)
  return () => root.unmount()
}
```

**Exercise 3:** Design an event-driven communication system using `window.dispatchEvent` and `addEventListener`.

---

*This document complements the previous Micro Frontends cheat sheet with deeper architectural and implementation-level detail covering composition approaches, Module Federation internals, and routing patterns.*

# Micro Frontends — State Sharing, Deployment Strategies & Integration Techniques

**Topic:** Micro Frontends

**Sub Topics:**
- State Sharing — cross-app store syncing, broadcast channels, custom events
- Deployment Strategies — independent deployment, version mismatches
- Integration Techniques — importing remoteEntry.js, dynamic module loading

---

## 1. State Sharing in Micro Frontends
State sharing becomes tricky because MFEs should be loosely coupled. A good strategy avoids global mutable state and instead relies on explicit communication channels.

### 1.1 Custom Events (Browser Native)
Custom DOM events are the simplest cross-app communication mechanism.

**Example:**
```js
// Sender
window.dispatchEvent(new CustomEvent('cart:add', { detail: { id: 42 } }))

// Listener
window.addEventListener('cart:add', e => {
  console.log('Item added:', e.detail)
})
```

**Pros:** Framework-agnostic, lightweight.
**Cons:** Only message passing, no shared store.

---

### 1.2 Broadcast Channel API
A browser-native channel for multi-tab and cross-MFE messaging.

```js
const channel = new BroadcastChannel('global-store')
channel.postMessage({ type: 'USER_LOGIN', payload: user })

channel.onmessage = (e) => {
  console.log('Received message', e.data)
}
```

**Pros:** Efficient, works across iframes and tabs.
**Cons:** No persistence; only event stream.

---

### 1.3 Cross-App Stores (Shared Library or Event Bus)
A lightweight pub/sub system can act as a centralized messaging hub.

```js
// eventBus.js
const listeners = {}
export function emit(event, data) {
  (listeners[event] || []).forEach(cb => cb(data))
}
export function on(event, cb) {
  listeners[event] = [...(listeners[event] || []), cb]
}
```

**Pros:** Simple, framework-neutral.
**Cons:** Needs care to avoid tight coupling.

---

### 1.4 Shared State via Module Federation
A shared dependency can export a store singleton.

```js
// shared-store/index.js
export const store = createStore()
```

The host and remotes share the same instance if configured as a singleton.

**Pros:** True shared store.
**Cons:** Version mismatches or accidental duplication may break the singleton.

---

## 2. Deployment Strategies

### 2.1 Independent Deployments
Each micro frontend deploys its assets separately — usually as a bundle served from its own domain or CDN.

**Key idea:** The host loads the remote's `remoteEntry.js` dynamically, so updates require no host rebuild.

---

### 2.2 Handling Version Mismatches
With many independent deployments, mismatches are common.

**Strategies:**
- Shared libs pinned to exact versions.
- Semantic version ranges for compatible releases.
- Fall back gracefully if remote can't load.
- Deploy host with a compatibility matrix (e.g., routing + API contracts).

**Runtime detection** can be implemented:
```js
try {
  await import('products/App')
} catch (err) {
  loadFallbackUI()
}
```

---

### 2.3 Atomic vs Non-Atomic Deployments
**Atomic:** Host + remotes always deployed together. Safer, less flexible.
**Non-atomic:** Each MFE deploys independently. More flexibility but requires strict contracts.

---

## 3. Integration Techniques

### 3.1 Importing `remoteEntry.js` at Runtime
A remote exposes its metadata through a generated manifest (`remoteEntry.js`). Load it dynamically:

```js
function loadRemote(url, scope) {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script')
    script.src = url
    script.onload = () => resolve(window[scope])
    script.onerror = reject
    document.head.appendChild(script)
  })
}
```

---

### 3.2 Dynamic Module Loading via Module Federation
Once the entry is loaded, you request modules from the remote:

```js
await __webpack_init_sharing__('default')
const container = window.products
await container.init(__webpack_share_scopes__.default)
const module = await container.get('./ProductsApp')
const ProductsApp = module()
```

This allows the host to mount any remote app without bundling it.

---

### 3.3 Integrating Without Module Federation
**ESM-based dynamic imports:**
```js
const ProductsApp = await import('https://domain.com/products-app/index.js')
ProductsApp.mount(document.querySelector('#app'))
```

**SystemJS:** Legacy-friendly runtime module loader widely used before Module Federation.

---

## 4. Interview Theory Questions (Concise Answers)

**Q1: How can state be shared across micro frontends?**
A1: Using custom events, Broadcast Channels, lightweight event buses, or shared singletons via Module Federation.

**Q2: What’s the main challenge with state sharing?**
A2: Avoiding tight coupling and ensuring independence between MFEs.

**Q3: How do independent deployments work in Module Federation?**
A3: Each remote deploys its own `remoteEntry.js`, which the host loads dynamically.

**Q4: How do you handle remote version mismatches?**
A4: Strict version constraints, semantic ranges, fallbacks, or compatibility matrices.

**Q5: What’s `remoteEntry.js`?**
A5: A manifest file generated by Module Federation that exposes runtime module metadata.

---

## 5. Coding / Architecture Exercises

**Exercise 1:** Implement a BroadcastChannel-based global event stream.

**Exercise 2:** Create a dynamic loader that downloads and mounts a remote module.

**Exercise 3:** Build a shared store using Module Federation that multiple MFEs consume.

---

*This document adds deep-dive specifics on state sharing, deployment patterns, and integration mechanisms commonly used in modern micro frontend architectures.*


# Micro Frontends — State Sharing, Deployment Strategies & Integration Techniques

**Topic:** Micro Frontends

**Sub Topics:**
- State Sharing — cross-app store syncing, broadcast channels, custom events
- Deployment Strategies — independent deployment, version mismatches
- Integration Techniques — importing remoteEntry.js, dynamic module loading

---

## 1. State Sharing in Micro Frontends
State sharing becomes tricky because MFEs should be loosely coupled. A good strategy avoids global mutable state and instead relies on explicit communication channels.

### 1.1 Custom Events (Browser Native)
Custom DOM events are the simplest cross-app communication mechanism.

**Example:**
```js
// Sender
window.dispatchEvent(new CustomEvent('cart:add', { detail: { id: 42 } }))

// Listener
window.addEventListener('cart:add', e => {
  console.log('Item added:', e.detail)
})
```

**Pros:** Framework-agnostic, lightweight.
**Cons:** Only message passing, no shared store.

---

### 1.2 Broadcast Channel API
A browser-native channel for multi-tab and cross-MFE messaging.

```js
const channel = new BroadcastChannel('global-store')
channel.postMessage({ type: 'USER_LOGIN', payload: user })

channel.onmessage = (e) => {
  console.log('Received message', e.data)
}
```

**Pros:** Efficient, works across iframes and tabs.
**Cons:** No persistence; only event stream.

---

### 1.3 Cross-App Stores (Shared Library or Event Bus)
A lightweight pub/sub system can act as a centralized messaging hub.

```js
// eventBus.js
const listeners = {}
export function emit(event, data) {
  (listeners[event] || []).forEach(cb => cb(data))
}
export function on(event, cb) {
  listeners[event] = [...(listeners[event] || []), cb]
}
```

**Pros:** Simple, framework-neutral.
**Cons:** Needs care to avoid tight coupling.

---

### 1.4 Shared State via Module Federation
A shared dependency can export a store singleton.

```js
// shared-store/index.js
export const store = createStore()
```

The host and remotes share the same instance if configured as a singleton.

**Pros:** True shared store.
**Cons:** Version mismatches or accidental duplication may break the singleton.

---

## 2. Deployment Strategies

### 2.1 Independent Deployments
Each micro frontend deploys its assets separately — usually as a bundle served from its own domain or CDN.

**Key idea:** The host loads the remote's `remoteEntry.js` dynamically, so updates require no host rebuild.

---

### 2.2 Handling Version Mismatches
With many independent deployments, mismatches are common.

**Strategies:**
- Shared libs pinned to exact versions.
- Semantic version ranges for compatible releases.
- Fall back gracefully if remote can't load.
- Deploy host with a compatibility matrix (e.g., routing + API contracts).

**Runtime detection** can be implemented:
```js
try {
  await import('products/App')
} catch (err) {
  loadFallbackUI()
}
```

---

### 2.3 Atomic vs Non-Atomic Deployments
**Atomic:** Host + remotes always deployed together. Safer, less flexible.
**Non-atomic:** Each MFE deploys independently. More flexibility but requires strict contracts.

---

## 3. Integration Techniques

### 3.1 Importing `remoteEntry.js` at Runtime
A remote exposes its metadata through a generated manifest (`remoteEntry.js`). Load it dynamically:

```js
function loadRemote(url, scope) {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script')
    script.src = url
    script.onload = () => resolve(window[scope])
    script.onerror = reject
    document.head.appendChild(script)
  })
}
```

---

### 3.2 Dynamic Module Loading via Module Federation
Once the entry is loaded, you request modules from the remote:

```js
await __webpack_init_sharing__('default')
const container = window.products
await container.init(__webpack_share_scopes__.default)
const module = await container.get('./ProductsApp')
const ProductsApp = module()
```

This allows the host to mount any remote app without bundling it.

---

### 3.3 Integrating Without Module Federation
**ESM-based dynamic imports:**
```js
const ProductsApp = await import('https://domain.com/products-app/index.js')
ProductsApp.mount(document.querySelector('#app'))
```

**SystemJS:** Legacy-friendly runtime module loader widely used before Module Federation.

---

## 4. Interview Theory Questions (Concise Answers)

**Q1: How can state be shared across micro frontends?**
A1: Using custom events, Broadcast Channels, lightweight event buses, or shared singletons via Module Federation.

**Q2: What’s the main challenge with state sharing?**
A2: Avoiding tight coupling and ensuring independence between MFEs.

**Q3: How do independent deployments work in Module Federation?**
A3: Each remote deploys its own `remoteEntry.js`, which the host loads dynamically.

**Q4: How do you handle remote version mismatches?**
A4: Strict version constraints, semantic ranges, fallbacks, or compatibility matrices.

**Q5: What’s `remoteEntry.js`?**
A5: A manifest file generated by Module Federation that exposes runtime module metadata.

---

## 5. Coding / Architecture Exercises

**Exercise 1:** Implement a BroadcastChannel-based global event stream.

**Exercise 2:** Create a dynamic loader that downloads and mounts a remote module.

**Exercise 3:** Build a shared store using Module Federation that multiple MFEs consume.

---

*This document adds deep-dive specifics on state sharing, deployment patterns, and integration mechanisms commonly used in modern micro frontend architectures.*

