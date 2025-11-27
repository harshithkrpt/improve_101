
# Node.js — V8 Internals (Cheatsheet)

## Preview & Download
Use the previewable + downloadable link in the top-right to export this cheatsheet.

---

# I. 💡 Basic Details of V8 Internals
V8 is the high-performance JavaScript engine used by Node.js. It compiles JavaScript into efficient machine code using just-in-time (JIT) compilation. V8 manages memory, optimizes code paths, performs garbage collection, and executes JS within isolated heaps.

Its relevance lies in performance tuning, debugging memory leaks, understanding GC pauses, and optimizing large Node.js backend systems.

---

# II. 🧠 Important Concepts to Remember
1. **Stack vs Heap** — The stack stores function frames and primitive values (fast, fixed-size). The heap stores objects, closures, and dynamically sized data. Analogy: stack is a clipboard; heap is a warehouse.

2. **V8 Memory Spaces** — V8 divides the heap into specialized regions:
   - *New Space*: small, short-lived objects.
   - *Old Space*: long-lived objects after surviving multiple GCs.
   - *Code Space*: JIT-compiled machine code.
   - *Large Object Space*: large buffers/arrays.
   - *Map/Read-only Spaces*: structural metadata.

3. **Generational GC** — Young generation (New Space) is collected frequently via minor GC; objects surviving GC get promoted to Old Space for major GC cycles.

4. **Minor (Scavenge) GC** — Fast copy-and-swap algorithm between two semi-spaces. Ideal for short-lived objects.

5. **Major (Mark-Sweep, Mark-Compact) GC** — Handles Old Space; slower but important to free long-lived memory. V8 uses incremental and concurrent marking to minimize pauses.

6. **Optimization Pipeline** — V8 uses Ignition (interpreter) and Turbofan (optimized compiler). Hot code is optimized; deoptimizations occur when assumptions break.

7. **Heap Snapshots & Memory Profiling** — Vital for diagnosing leaks. Snapshots show retained objects, closures, DOM-like structures, buffers, and memory references.

8. **Event-loop impact** — GC pauses can block JS execution; bad allocation patterns increase GC pressure.

---

# III. 📝 Theory — Most Asked Interview Questions (with concise model answers)

**Q1: What is the difference between stack and heap in V8?**
**A:** Stack holds function calls and primitive values with fixed lifetime; heap stores dynamic objects and closures. Stack is fast and contiguous; heap is larger and garbage-collected.

**Q2: How does the V8 garbage collector work?**
**A:** V8 uses generational GC: minor GC for young generation (copying/scavenge), and major GC for old generation (mark-sweep and mark-compact). It runs incremental and concurrent phases to reduce pauses.

**Q3: What triggers a minor GC vs major GC?**
**A:** Minor GC is triggered when the New Space fills up. Major GC occurs when Old Space grows too large or when the young generation promotes many objects.

**Q4: What is object promotion?**
**A:** When an object survives multiple minor GCs, it is moved from New Space to Old Space because it is considered long-lived.

**Q5: What causes memory leaks in Node.js?**
**A:** Retained references (closures, global variables), event listeners not removed, cache growth, never-ending timers, or large buffers remaining in Old Space.

**Q6: What is a heap snapshot and why is it useful?**
**A:** A heap snapshot is a captured view of V8's heap showing objects, references, and retained sizes. It helps find leaks by comparing snapshots over time.

**Q7: What is the role of Ignition and Turbofan?**
**A:** Ignition interprets bytecode; Turbofan compiles hot code to optimized machine code. Deoptimizations occur when assumptions change.

---

# IV. 💻 Coding / Practical — Most Asked Questions (with approaches)

**P1: Measure memory usage of a Node process.**
- *Approach*: Use `process.memoryUsage()` to get heapUsed, heapTotal, rss. Combine with OS-level tools.

**P2: Perform a heap snapshot programmatically.**
- *Approach*: Use the `inspector` module to trigger `HeapProfiler.takeHeapSnapshot()` and save it to disk.

**P3: Detect a memory leak by comparing snapshots.**
- *Approach*: Capture snapshots at intervals, inspect retained objects and reference chains. Identify growing classes or closures.

**P4: Profile CPU & GC behavior.**
- *Approach*: Use `node --prof`, Chrome DevTools Inspector, or `clinic.js` to profile JIT behavior and GC pauses.

**P5: Force a GC in development mode.**
- *Approach*: Run Node with `--expose-gc` then call `global.gc()`. This is only for debugging.

**P6: Reduce GC pressure in high-throughput servers.**
- *Approach*: Reuse objects, avoid large temporary arrays, use streams instead of full buffering, avoid unnecessary closures.

**P7: Tune memory limits.**
- *Approach*: Use `--max-old-space-size` to increase heap size when dealing with heavy in-memory processing.

---

# V. 🚀 Follow-Up Topics to Learn
1. **Node.js Worker Threads** — Offload CPU-heavy tasks without stressing the main thread.
2. **V8 JIT Optimizations** — Learn hidden classes, inline caches, and common deopt patterns.
3. **Advanced Profiling Tools (Clinic.js, DevTools)** — Deep dive into Flamegraphs and GC timeline.
4. **Memory-safe design patterns** — Streaming, resource pooling, backpressure handling.
5. **Native addons (N-API, Rust Neon)** — Build high-performance modules where JS overhead is too costly.

---

## Quick Practical Checklist
- Avoid unnecessary object creation.
- Monitor heap usage in production.
- Use heap snapshots for leaks.
- Stream large data.
- Watch out for long-lived closures.

---

*End of cheatsheet.*

# Node.js — Performance Tuning (Cheatsheet)

## I. 💡 Basic Details of Node.js Performance Tuning
**Definition & purpose:** Performance tuning in Node.js is the practice of measuring, diagnosing, and improving runtime characteristics (latency, throughput, memory, CPU) of Node.js applications so they serve more users, handle higher load, and use fewer resources.

**Brief history & relevance:** Node.js popularized event-driven, non-blocking I/O for server-side JavaScript. As adoption grew from prototypes to large-scale services, tuning became essential — from optimizing the event loop to using native profilers and flamegraphs to find hotspots. Today it’s critical for backend services, real-time apps, and microservices where latency, cost and reliability matter.


## II. 🧠 Important Concepts to Remember
1. **Event loop latency vs throughput** — *Latency* is per-request responsiveness; *throughput* is work completed per time. Optimizations that lower latency (e.g., offloading heavy tasks) may or may not increase throughput.
   *Analogy:* Event loop = a single cashier; latency = how long one customer waits, throughput = how many customers served per hour.

2. **CPU-bound vs I/O-bound** — Node.js excels at I/O-bound workloads (non-blocking syscalls). CPU-heavy work blocks the event loop and increases latency.
   *Tip:* Offload CPU-heavy tasks to worker_threads, child processes, or native addons.

3. **Backpressure & Streams** — Properly apply backpressure on streams to avoid buffering large data in memory. Use piping and `highWaterMark` tuning.

4. **Garbage Collection (GC) behavior** — V8 GC pauses can cause latency spikes. Monitor heap usage and tune `--max-old-space-size`, reduce allocations, and prefer object reuse when possible.

5. **Profiling & observability** — Use `node --prof`, `--inspect`, `clinic` (Doctor/Flame), `0x`, or `perf` to collect CPU profiles and flamegraphs. Metrics (event-loop lag, CPU, heap) + traces (distributed tracing) are key.

6. **Concurrency patterns** — Use clustering (multiple Node processes) for multi-core utilization; use sticky sessions or a stateless approach with a load balancer for horizontal scaling.

7. **Latency sources** — synchronous blocking APIs, JSON stringify/parse hot spots, large library initializations, uncontrolled timers, network waits, and GC.


## III. 📝 Theory — Most Asked Interview Questions (and model answers)

**Q1: Why is Node.js single-threaded, and how does it handle concurrency?**
**A:** Node.js has a single-threaded JavaScript execution model backed by libuv’s thread pool for asynchronous I/O. Concurrency is achieved via non-blocking I/O and callbacks/promises — the event loop schedules tasks while libuv handles blocking operations in worker threads.

**Q2: What causes event loop lag and how do you measure it?**
**A:** Causes include CPU-bound synchronous code, heavy microtasks, long GC pauses, and expensive synchronous I/O. Measure with `perf_hooks.monitorEventLoopDelay()`, `clinic doctor`, or app metrics (histograms of response times) and synthetic probes.

**Q3: When should you use worker_threads vs cluster?**
**A:** `cluster` (multiple processes) provides isolation and full-process memory; good for scaling across cores with independent heaps. `worker_threads` share memory and are lighter-weight, suitable for CPU-bound tasks that benefit from SharedArrayBuffer or passing ArrayBuffers.

**Q4: How do you reduce GC-related latency spikes?**
**A:** Reduce allocation churn, reuse buffers/objects, decrease retained heap growth, tune `--max-old-space-size`, and upgrade V8/Node.js for GC improvements. For extreme cases, move long-lived large allocations to worker processes.

**Q5: Explain backpressure and why it matters in Node.js streams.**
**A:** Backpressure prevents producers from overwhelming consumers by signaling when to pause/resume. Without it, memory spikes occur. Use `stream.pipe()` and listen for `drain`/`pause`/`resume` events; tune `highWaterMark`.


## IV. 💻 Coding / Practical — Most Asked Questions (and approaches)

**P1: How would you profile a live Node.js service with high latency? (steps)**
**Approach:**
1. Add lightweight metrics: event-loop delay, CPU, heap, and response time histograms.
2. Capture a CPU profile using `0x` or `clinic flame` or `node --inspect` + `pprof` on a staging-like load.
3. Generate flamegraphs and look for heavy JS functions or C++ calls.
4. Identify hotspots: synchronous loops, crypto, JSON serialization, DB client sync calls.
5. Patch with either algorithmic fixes, moving work to worker_threads, or caching.

**P2: Write a pattern to offload a CPU-heavy function to a worker thread (short example)**
**Approach / Snippet:**
```js
// main.js
const { Worker } = require('worker_threads');
function runTask(data) {
  return new Promise((res, rej) => {
    const w = new Worker('./cpu-task.js', { workerData: data });
    w.once('message', res);
    w.once('error', rej);
    w.once('exit', code => { if (code !== 0) rej(new Error('Worker failed')); });
  });
}

// usage
runTask({ n: 1e7 }).then(result => console.log(result));
```

**P3: How to measure event-loop latency programmatically?**
**Approach:** Use Node’s `perf_hooks`:
```js
const { monitorEventLoopDelay } = require('perf_hooks');
const h = monitorEventLoopDelay({ resolution: 10 });
h.enable();
setInterval(() => {
  console.log('min', h.min, 'mean', h.mean, 'max', h.max);
  h.reset();
}, 1000);
```

**P4: Tuning HTTP server for throughput — what would you change?**
**Approach:**
- Use keep-alive and tune `server.keepAliveTimeout` and `headersTimeout`.
- Tune connection backlog and OS TCP settings (somaxconn, tcp_tw_reuse) where applicable.
- Enable gzip/deflate carefully — prefer streaming compression for large responses.
- Use clustering or multiple instances behind a load balancer for multi-core utilization.

**P5: Preventing memory leaks — checklist**
**Approach:**
- Use heap snapshots (Chrome DevTools, `clinic memory`) and compare over time.
- Look for long-lived closures, global caches, event emitter leaks (`emitter.setMaxListeners`).
- Avoid accidental retention: large arrays, references in timers, or circular references in caches.


## V. 🚀 Follow-Up Topics to Learn
1. **Observability & Distributed Tracing (OpenTelemetry)** — Important to correlate latency across services and identify root causes beyond your Node process.
2. **Advanced V8 & GC internals** — Learn how V8 generational GC works; helps tune allocations and understand pause behavior.
3. **Kernel & Network Tuning for High Throughput** — TCP tuning, epoll behavior, and load balancer strategies that impact Node performance.
4. **Native Addons & N-API** — When performance needs C/C++ speed; write safe native modules with `node-gyp`/N-API.
5. **Performance Testing Tools & Chaos Engineering** — `wrk`, `k6`, `vegeta` for load tests; inject faults to validate resilience.


---
*Compact checklist*: measure → profile → isolate → fix → validate. Start with metrics and small synthetic tests before changing production.

*Credits & tools to try:* `clinic` (Doctor/Flame/Heap), `0x`, `node --prof` + `tick-processor`, `perf_hooks`, `pprof`, `wrk`/`k6`.


*Format note:* This document is written as a one-page cheatsheet for interview prep and quick on-call reference.

# Node.js Memory Management — Cheatsheet

## I. 💡 Basic Details of Node.js Memory Management

**Definition & purpose.** Node.js memory management is how the V8 engine and Node runtime allocate, use, and free memory for JavaScript objects, buffers, native allocations, and I/O structures. The goal: keep memory usage predictable, avoid leaks, and ensure GC (garbage collection) pauses are acceptable for your workload.

**Brief history & relevance.** V8 has evolved from simple mark-sweep collectors to generational and concurrent collectors. As Node apps grew long-running (servers, microservices), understanding leaks and heap behavior became essential for reliability and cost control.

**When this matters.** Long-lived processes, high-throughput services, background workers, or apps that manipulate large buffers or native addons.

---

## II. 🧠 Important Concepts to Remember (5–7 fundamentals)

1. **Heap vs External Memory** — The JS heap (objects/closures) is managed by V8. External memory includes Buffers, native addon allocations, and C++ structures. External allocations can cause OOM even if heap looks small.
   - *Analogy:* Heap == the pantry where you store jars (JS objects). External memory == heavy appliances sitting in the kitchen that the pantry inventory view doesn’t show.

2. **Generational GC & Minor/Major collections** — Young generation (new objects) is collected frequently (fast); old generation collection is more expensive. Long-lived objects get promoted to the old generation where they cost more to collect.
   - *Tip:* High allocation churn with many surviving objects leads to old-gen growth and costly GCs.

3. **Retained Size vs Shallow Size** — *Shallow size* is the memory for the object itself; *retained size* is the total memory that would be freed if that object were collected (its dominator subgraph). Retained size is the key metric for finding roots of leaks.

4. **Roots and Reachability** — Objects reachable from GC roots (globals, closures, active scopes, timers, event listeners) are kept alive. Leaks happen when path to a root remains even after the object is logically unused.

5. **Closures & Captured Variables** — Closures keep variables alive as long as the closure (function object or its call frame) is reachable. Capturing large structures by accident retains memory.
   - *Analogy:* A closure is a postcard that keeps a picture of a whole album — keeping the postcard keeps the album.

6. **Common leak patterns** — Timers, event listeners, caches, long-lived arrays/Maps, forgotten references in closures, Promise chains, native resource mismanagement.

7. **Tools + Workflow** — `--inspect`/Chrome DevTools, `heapdump` (.heapsnapshot), `node --inspect-brk`, `clinic doctor/flame/heap` (Clinic.js), `0x`, `llnode` for core dumps. Learn to take snapshots and compare them.

---

## III. 📝 Theory — Most Asked Questions (Interview Prep)

**Q1: What is a memory leak in Node.js?**
**A1:** A memory leak is when a program unintentionally retains references to objects so the garbage collector cannot reclaim them, causing memory to grow over time and possibly lead to OOM.

**Q2: Explain shallow size vs retained size and why retained size matters.**
**A2:** Shallow size is the memory of an object itself. Retained size includes everything that would become unreachable if that object was collected (its dominated subgraph). Retained size helps identify which object(s) are keeping large parts of memory alive.

**Q3: How do closures cause memory leaks?**
**A3:** Closures capture variables from their lexical environment. If a closure lives for long (e.g., stored on an event emitter), it keeps references to captured variables, preventing them from being GC'd even if they’re no longer needed.

**Q4: How would you find a leak in production?**
**A4:** Collect periodic heap snapshots or memory metrics, compare snapshots to find objects whose retained size grows, inspect dominator trees and paths to GC roots, review code for common leak patterns (listeners, timers, caches), and add instrumentation or sampling if needed.

**Q5: Difference between `Memory Leak` and `Memory Bloat`?**
**A5:** Leak = unintended retained references. Bloat = expected high memory use (e.g., large caches) — not a leak if growth is bounded and expected.

---

## IV. 💻 Coding / Practical — Most Asked Questions (Interview Prep)

### Common practical tasks & optimal approaches

1. **How to take a heap snapshot (manual quick recipe)**
   - Start Node with inspector: `node --inspect app.js` (or `--inspect-brk` to pause at start).
   - Open `chrome://inspect` → Open dedicated DevTools for Node.
   - In DevTools Memory tab: take a *Heap snapshot* (click *Take snapshot*). Save the `.heapsnapshot` file.
   - Alternatively, programmatic snapshot with `heapdump`:
     ```js
     // npm install heapdump
     const heapdump = require('heapdump');
     // trigger: heapdump.writeSnapshot('/tmp/heap-' + Date.now() + '.heapsnapshot');
     ```

2. **How to analyze snapshots (practical steps)**
   - Load snapshot into Chrome DevTools Memory tab.
   - Sort by *Retained Size* and inspect top dominators.
   - Use **‘Comparison’** view between two snapshots (before/after a suspected leak) to spot growing objects.
   - For a candidate object, view *Retainers* and *Paths to GC root* to discover what reference keeps it alive.

3. **Minimal reproducible leak example (closure + timer)**
   ```js
   const leaky = [];
   function createLeaker() {
     const big = new Array(1e5).fill('x');
     function keepAlive() { return big[0]; }
     leaky.push(keepAlive); // closure retains `big`
   }
   setInterval(() => createLeaker(), 1000);
   ```
   - *Fix:* avoid pushing closures that capture large objects; store only needed data or clear timers/arrays.

4. **Finding leaks with `clinic heap`**
   - Run: `clinic heap -- node server.js` then exercise the app and `clinic` will open an interactive report showing heap growth over time.

5. **Detecting external (Buffer) leaks**
   - Track Buffer usage with `process.memoryUsage()` (rss, heapTotal, heapUsed, external).
   - `external` shows memory used by C++ side (Buffers). A rising `external` suggests Buffer/native leak.

6. **Useful Node flags**
   - `--max-old-space-size=<MB>`: increase old generation limit (temporary mitigation).
   - `--trace_gc` / `--trace_gc_verbose`: verbose GC logs (diagnostics).
   - `--expose-gc` then call `global.gc()` (only in debug/testing; not recommended for production) to force a collection when comparing snapshots.

7. **Practical mitigation checklist**
   - Remove or limit long-lived references.
   - Remove unused event listeners (`emitter.removeListener` / `off`).
   - Clear or size-bounded caches (use LRU caches, size limits).
   - Null out big variables when done (`bigObj = null;`).
   - Use `WeakMap` / `WeakRef` when appropriate for cache-like semantics.
   - Profile native modules or external packages when `external` memory grows.

---

## V. 🚀 Follow-Up Topics to Learn

1. **V8 Garbage Collector internals (Scavenger, Mark-Sweep, Concurrent Mark, Incremental Marking)**
   - *Why:* helps tune allocation patterns and understand GC pause reasons.

2. **Advanced profiling tools: `llnode`, `gcore` + `lldb`, and `perf`**
   - *Why:* for native-level debugging and offline post-mortem analysis of core dumps.

3. **Clinic.js deep-dive (Doctor / Flame / Heap)**
   - *Why:* integrates multiple views (CPU, heap) and makes diagnosing production problems quicker.

4. **Memory behavior of Buffers & Streams, and zero-copy patterns**
   - *Why:* many Node memory problems result from unmanaged buffers or streaming logic.

5. **Writing safe native addons (N-API) & diagnosing native leaks**
   - *Why:* native code mistakes often bypass V8 GC and cause hard-to-find leaks.

---

### Quick references & commands (cheat-line)

- Start inspector: `node --inspect index.js`
- Programmatic heap snapshot: `heapdump.writeSnapshot(path)`
- GC flags: `--trace_gc`, `--trace_gc_verbose`, `--max-old-space-size=4096`
- Inspect memory from app: `process.memoryUsage()` (RSS, heapTotal, heapUsed, external)
- Tooling: Chrome DevTools, Clinic.js, heapdump, llnode, 0x

---

*End of cheatsheet — concise, practical, and interview-ready.*

Previewable + Downloadable Link in the top right corner.

# Node.js Security — Cheatsheet

## I. 💡 Basic Details of Node.js Security
**Definition & purpose:** Node.js security is the practice of designing, coding, and operating Node.js applications so they resist attacks, prevent data leakage, and behave correctly under malicious inputs or compromised dependencies. The goal is to reduce the attack surface, fail safely, and keep user data and infrastructure intact.

**Brief history & relevance:** As Node.js became a dominant platform for server-side JavaScript, new classes of vulnerabilities (prototype pollution, unsafe deserialization, insecure dependency chains) and operational threats (supply-chain attacks) emerged. Modern Node.js security blends secure coding patterns, dependency hygiene, runtime defenses (CSP, secure headers), and observability.

---

## II. 🧠 Important Concepts to Remember (Top 7)
1. **Principle of Least Privilege (PoLP)** — Run processes, services and containers with the minimum permissions required. Think of it as locking every door except the one you must use.

2. **Avoid dynamic code execution (`eval`, `new Function`)** — Dynamic evaluation widens attack surface and defeats static analysis. If you must evaluate, isolate it heavily (sandbox) and prefer structured formats like JSON or a safe expression language.

3. **Prototype pollution** — Unsafe merging or assignment from untrusted objects (e.g., `_.merge`, `Object.assign`) can mutate `__proto__` and break assumptions across code. Always whitelist keys and deep-validate user-provided objects.

4. **Dependency supply-chain hygiene** — Regularly scan and fix vulnerabilities (npm audit, `npm audit fix`, Snyk, Dependabot). Prefer pinned or locked versions (`package-lock.json` / `pnpm-lock.yaml`) and review critical transitive dependencies.

5. **Content Security Policy (CSP) for SSR** — Apply a strict CSP header to mitigate XSS even when rendering server-side. Use nonces for inline scripts and avoid `unsafe-inline`/`unsafe-eval` wherever possible.

6. **Input validation & output encoding** — Validate inputs by type/shape/length and encode outputs for their context (HTML, URL, SQL, shell). Treat input validation and output encoding as separate responsibilities.

7. **Secrets & configuration management** — Never store secrets in source control. Use vaults (AWS Secrets Manager, HashiCorp Vault), environment variables in orchestrators, and rotate keys frequently.

Analogies: prototype pollution is like sneaking a key into a building’s blueprints so every door now accepts that key; CSP is a security guard who checks the script’s badge (nonce) before allowing execution.

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1 — Why is `eval` dangerous and what are safe alternatives?**
*Model answer:* `eval` executes arbitrary strings as code, allowing an attacker to run injected code. Alternatives: parse structured data (JSON), use safe expression libraries (JEXL, mathjs sandbox), or implement explicit command handlers. If dynamic behavior is required, design a whitelist-driven interpreter.

**Q2 — What is prototype pollution and how can it be exploited?**
*Model answer:* Prototype pollution occurs when user-supplied data can mutate `Object.prototype` (or another prototype), e.g., via `obj['__proto__'] = { isAdmin: true }`. This can change behavior across the app, bypass checks, or cause denial-of-service. Prevent by sanitizing keys and disallowing `__proto__`, `constructor`, and `prototype` during deep merges.

**Q3 — How does Content Security Policy (CSP) improve security for SSR apps?**
*Model answer:* CSP tells browsers what sources are allowed for scripts, styles, images, etc. For SSR, it mitigates XSS by disallowing inline scripts unless paired with secure nonces/hashes. Implement strict CSP headers and use nonces for legitimate inline scripts.

**Q4 — How do you handle vulnerable npm packages in production?**
*Model answer:* Run automated scans (npm audit, Snyk), triage vulnerabilities by severity and exploitability, update or patch packages, use lockfiles and reproducible builds, and consider temporary mitigations (e.g., runtime checks, network controls). For critical supply-chain incidents, roll back and patch all affected environments.

**Q5 — What are secure defaults when creating an Express server?**
*Model answer:* Use `helmet` for headers, enable strict CSP, disable `x-powered-by`, limit body size and request rates, enable HTTPS and HSTS, use cookie flags (`HttpOnly`, `Secure`, `SameSite`), validate inputs, and log suspicious activity.

---

## IV. 💻 Coding / Practical — Most Asked Questions

**P1 — How do you set strict CSP with nonces in an SSR Express app?**
*Approach & snippet:* Generate a random nonce per response, include it in the CSP header and the script tags.

```js
// Example (Express)
const crypto = require('crypto');
app.use((req, res, next) => {
  const nonce = crypto.randomBytes(16).toString('base64');
  res.locals.cspNonce = nonce; // for template use
  res.setHeader(
    'Content-Security-Policy',
    `default-src 'self'; script-src 'self' 'nonce-${nonce}'; style-src 'self' 'unsafe-inline';`
  );
  next();
});

// In template (e.g., Pug/EJS):
// <script nonce="<%= cspNonce %>"> /* inline script */ </script>
```

**P2 — How to prevent prototype pollution when merging user objects?**
*Approach:* Use a safe merge that rejects prototype keys, or whitelist keys.

```js
function safeMerge(target, source, allowedKeys = null) {
  for (const key of Object.keys(source)) {
    if (key === '__proto__' || key === 'constructor' || key === 'prototype') continue;
    if (allowedKeys && !allowedKeys.includes(key)) continue;
    const val = source[key];
    if (val && typeof val === 'object' && !Array.isArray(val)) {
      target[key] = target[key] || {};
      safeMerge(target[key], val, allowedKeys);
    } else {
      target[key] = val;
    }
  }
  return target;
}
```

**P3 — How to scan and act on dependency vulnerabilities?**
*Approach:* Add automated scans in CI, fail builds on high-severity findings, run `npm audit --json` to triage, use Snyk/Dependabot for PRs, pin/lock versions, and test updates in staging.

**P4 — How to safely use user-provided templates or HTML content?**
*Approach:* Avoid rendering raw HTML. If you must, sanitize (DOMPurify on server or trusted sanitizer) and isolate rendering in a sandboxed iframe for clients. For server-side templating, escape output by default and only allow controlled whitelists for markup.

**P5 — Implement rate-limiting and body size limits in Express**
*Approach & snippet:*

```js
const rateLimit = require('express-rate-limit');
app.use(express.json({ limit: '100kb' }));
app.use(
  rateLimit({
    windowMs: 60 * 1000, // 1 minute
    max: 100, // limit each IP
    standardHeaders: true,
    legacyHeaders: false,
  })
);
```

---

## V. 🚀 Follow-Up Topics to Learn
1. **Runtime Application Self-Protection (RASP)** — Learn how apps can detect and block attacks at runtime.
2. **Secure Software Supply Chain** — Deep dive into SBOMs (Software Bill of Materials), signing artifacts, and reproducible builds.
3. **Threat Modeling & STRIDE** — Systematically analyze threats and design mitigations early.
4. **Advanced Web App Hardening (CORS, SameSite, CSP hashes, Subresource Integrity)** — For fine-grained control of resource loading and policy enforcement.
5. **Container & Orchestration Security (Docker, Kubernetes)** — Node apps rarely run alone; secure build images, runtime policies (PodSecurity, seccomp), and secrets handling.

---

### Quick Checklist (for your repo/deployments)
- Add `npm audit` + Snyk in CI.
- Use `helmet` and set strict CSP with nonces.
- Disallow `eval` and avoid `Function` constructor.
- Sanitize/whitelist object keys to avoid prototype pollution.
- Pin dependencies and use lockfiles; enable Dependabot.
- Enforce least privilege for processes and secrets vaults.
- Apply rate-limiting, body size caps, and logging/alerting.

---

*Prepared as a compact cheatsheet for interview prep and practical hardening.*

Previewable + Downloadable Link (top-right)

# Node.js — Logging Cheatsheet

## I. 💡 Basic Details of Node.js Logging
**Definition & purpose**
Logging is recording runtime events from your application — errors, state changes, performance metrics, and traces — to help debugging, monitoring, alerting and audits.

**History & relevance**
As Node.js apps moved from single-process prototypes to distributed microservices, logging evolved from simple console output to structured, high-throughput, correlated, and observability-friendly systems (JSON logs, correlation ids, central ingesters).


## II. 🧠 Important Concepts to Remember
1. **Log levels** — severity labels (trace/debug/info/warn/error/fatal). Use them consistently; they drive filtering, alerting, and storage policies.
   - Analogy: log levels are like traffic lights — debug = green (keep going), warn = yellow (slow down), error = red (stop & fix).

2. **Structured logging (JSON)** — emit machine-readable objects (timestamp, level, msg, metadata). Enables search, enrichment, and analytics.
   - Analogy: JSON logs are tables; plain text logs are sticky notes.

3. **Correlation IDs / Tracing context** — attach a request/transaction id to every log so you can assemble the full story across services.
   - Best practice: generate at the edge (ingress) and propagate via headers (e.g., `x-request-id`).

4. **Log transport & sinks** — local files, stdout (container-friendly), log aggregators (Fluentd/Vector/Logstash), cloud services (CloudWatch, Stackdriver, Datadog).
   - Containers: prefer stdout/stderr and let the platform collect logs.

5. **Log rotation & retention** — avoid unbounded disk growth. Rotate files (size/time), compress old logs, and set retention policies in the aggregator.

6. **Performance & reliability** — non-blocking/async logging, pooling, and backpressure strategies. Avoid synchronous disk writes on hot paths.

7. **Sensitive data & compliance** — never log PII or secrets. Use redaction or structured scrubbers before export.


## III. 📝 Theory — Most Asked Interview Questions (Concise Model Answers)

**Q1: What log levels would you use in production and why?**
A: Common set: `trace`, `debug`, `info`, `warn`, `error`, `fatal`. Use `info` for normal operational events, `debug/trace` for verbose developer troubleshooting (off in prod by default), `warn` for recoverable issues, and `error/fatal` for failures needing attention. Keep level semantics consistent across services.

**Q2: Why prefer JSON/structured logging over plain text?**
A: Structured logs are machine-readable, easier to query, parse, enrich, and route to observability tooling. They support indexing and field-based search which plain-text lacks reliably.

**Q3: How do correlation ids work?**
A: A correlation id is generated at request ingress, propagated via headers across services and logged with each event. This allows reconstructing request flow across distributed components. Use deterministic propagation (context libraries or middleware).

**Q4: How would you handle log rotation in Node.js?**
A: Use the platform logging (stdout) in containers; if writing files, use log-rotation tools (logrotate) or libraries that support rotation (e.g., file transport with rotation). Ensure rotation criteria (size/time) and retention are configured to prevent disk exhaustion.

**Q5: How to prevent logging from impacting performance?**
A: Use non-blocking loggers, batch writes, sample high-volume events, and push heavy processing (formatting, shipping) to background workers or the logging pipeline. Avoid heavy synchronous operations on hot paths.


## IV. 💻 Practical / Coding — Most Asked Questions (with approaches)

### Common libraries
- **pino**: very fast, low-overhead, produces JSON. Good for high-throughput services.
- **winston**: flexible transports and formats; more features but heavier.


### Example: Minimal pino setup (recommended for production)
```js
// logger.js
const pino = require('pino');
const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  base: { pid: process.pid },
  timestamp: pino.stdTimeFunctions.isoTime
});
module.exports = logger;
```

Usage in app:
```js
const logger = require('./logger');
logger.info({ reqId, userId }, 'user login');
```

Run with a log processor (to pretty-print locally):
```
node app.js | pino-pretty
```


### Example: Winston with rotation
```js
const { createLogger, format, transports } = require('winston');
require('winston-daily-rotate-file');

const transport = new transports.DailyRotateFile({
  filename: 'logs/app-%DATE%.log',
  datePattern: 'YYYY-MM-DD',
  maxFiles: '14d'
});

const logger = createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: format.combine(format.timestamp(), format.json()),
  transports: [transport]
});

module.exports = logger;
```


### Adding correlation id middleware (Express example)
```js
const { v4: uuidv4 } = require('uuid');
const logger = require('./logger');

function reqIdMiddleware(req, res, next) {
  req.id = req.headers['x-request-id'] || uuidv4();
  res.setHeader('x-request-id', req.id);
  // attach to logger via child with bound request context
  req.logger = logger.child({ reqId: req.id });
  next();
}

app.use(reqIdMiddleware);
```


### Shipping logs reliably
- Emit to stdout/stderr in containers.
- Use sidecar or collector (Fluentd, Vector) to forward to storage.
- Prefer structured fields: `timestamp`, `level`, `service`, `env`, `reqId`, `spanId`, `traceId`, `message`, `err`.


### Example of redaction/scrubbing
- Implement a log sanitizer that strips or masks `password`, `ssn`, `token` fields before calling logger.


## V. 🚀 Follow-Up Topics to Learn
1. **Distributed Tracing (OpenTelemetry)** — links logs with traces and metrics for full observability. Essential for microservices.
2. **Centralized Logging Stack (Elastic/Fluentd/Vector/Graylog/Cloud)** — learn ingestion, indexing, and querying for large-scale logs.
3. **Log-Based Metrics & Alerting** — create KPIs from logs (error rate, latency buckets) and wire alerts.
4. **Security & Compliance in Logging** — PII handling, immutable audit logs, and regulatory retention rules.
5. **Sampling & Backpressure Strategies** — techniques for high-cardinality logs and protecting storage and pipelines.


---

### Quick Reference — Snippets & Tips
- Container -> stdout. Avoid local files unless required.
- Use `pino` for speed at scale; `winston` for flexibility.
- Always propagate `x-request-id` and include it in structured logs.
- Keep log messages short; put rich detail in structured fields.
- Mask secrets before logging.


*Document generated by Cheatsheet Interview — ready to preview/download.*

# Node.js Observability — Cheatsheet

> **Previewable + Downloadable Link:** Use the top-right corner to preview or download this cheatsheet.

---

## I. 💡 Basic Details of Node.js Observability
**Definition & purpose**
Observability is the practice of instrumenting a system so you can understand its internal state from external outputs (logs, metrics, traces). In Node.js, observability helps you detect, diagnose, and mitigate performance issues, errors, and reliability regressions in production.

**Brief history & relevance**
Observability evolved from classical monitoring (alerts + dashboards) into a richer discipline that emphasizes distributed tracing, high-cardinality metrics, and structured telemetry. With widespread microservices and serverless patterns, Node.js apps benefit greatly from Prometheus-style metrics, OpenTelemetry for tracing, and error trackers like Sentry.

---

## II. 🧠 Important Concepts to Remember
1. **Logs vs Metrics vs Traces** —
   - *Logs*: Event records (text/JSON) for debugging. High fidelity, high volume.
   - *Metrics*: Numeric time-series (counters, gauges, histograms) for trends/alerting.
   - *Traces*: End-to-end request timelines showing spans across services.
   *Analogy*: Logs are diary entries, metrics are your health vitals, traces are a CCTV timeline of a request.

2. **Cardinality & Dimensionality** —
   - Tag/label cardinality controls storage cost and query performance. Avoid unbounded labels (user IDs) on high-frequency metrics.

3. **Exposition & Formats** —
   - Prometheus expects an HTTP `/metrics` endpoint that exposes text-format metric families. Use client libraries to correctly register counters, gauges, histograms.

4. **Sampling & Head-based vs Tail-based Tracing** —
   - Traces can be sampled to reduce volume. Head-based sampling decides at span start; tail-based evaluates after full trace is buffered (more accurate but heavier).

5. **Context Propagation** —
   - Pass trace context (trace id, span id, baggage) across async boundaries, HTTP headers, and message queues to correlate spans.

6. **Instrumenting Node.js** —
   - Use OpenTelemetry SDKs for automatic + manual instrumentation. Hook into HTTP, Express, database clients, and message brokers.

7. **SLOs, SLIs, Alerts** —
   - Metrics are the source for Service Level Indicators (SLIs) and Objectives (SLOs). Alert on symptom metrics, not correlated debug logs.

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: What is the difference between metrics, logs, and traces?**
**A:** Metrics are numerical time-series used for dashboards and alerts (counters/gauges/histograms). Logs are timestamped event records for detailed debugging. Traces represent the causal execution path of requests across distributed components. Use metrics for monitoring trends, logs for investigating incidents, and traces for performance root-cause analysis.

**Q2: How does Prometheus scrape metrics from a Node.js app?**
**A:** Prometheus performs HTTP GET scrapes against an endpoint (commonly `/metrics`). A Node.js app exposes metrics via a client library (e.g., `prom-client`) which registers metric families and returns them in Prometheus text exposition format for Prometheus to pull.

**Q3: Explain histogram vs summary in Prometheus. When to use which?**
**A:** Histograms bucket observed values and allow calculating quantiles and aggregations across instances (useful for latency distributions). Summaries calculate quantiles client-side (per-instance) and are not easily aggregatable across instances. For distributed systems, histograms are usually preferred for aggregatable latency metrics.

**Q4: What is OpenTelemetry and how does it help Node.js apps?**
**A:** OpenTelemetry is a vendor-neutral observability SDK (tracing, metrics, logs) standardizing telemetry collection. In Node.js, it provides auto-instrumentation for HTTP, DB drivers, and manual APIs to create spans and attributes, enabling consistent traces and metrics shipping to backends like Jaeger, Zipkin, or vendor APMs.

**Q5: How do you avoid high-cardinality explosion in metrics?**
**A:** Limit label values to bounded sets, avoid user/session IDs in labels, pre-aggregate where possible, use histograms for distributions instead of many per-value counters, and sample or roll up high-cardinality streams.

**Q6: How would you instrument a Node.js Express app for tracing?**
**A:** Install OpenTelemetry Node SDK + auto-instrumentation packages, initialize an OTLP exporter, configure resource attributes/service name, enable instrumentations for HTTP/Express and DB clients, and ensure context propagation through async boundaries (using built-in context manager). Optionally add manual spans around expensive operations.

**Q7: What are common Sentry integration points for Node.js?**
**A:** Use `@sentry/node` for server runtimes and `@sentry/integrations` to capture uncaught exceptions, unhandled rejections, HTTP requests, and performance (transactions/traces). Enrich events with user/context breadcrumbs and set sampling rates for performance.

---

## IV. 💻 Coding / Practical — Most Asked Questions

**Q1: Create a `/metrics` endpoint using `prom-client` (Node.js + Express)**
- **Approach:** Install `prom-client`, register metrics (Counter, Gauge, Histogram), and expose `promClient.register.metrics()` at `GET /metrics` with `Content-Type: text/plain; version=0.0.4`.
- **Notes:** Use `collectDefaultMetrics()` for process metrics (CPU/memory/event loop). Ensure metrics export is lightweight and non-blocking.

**Q2: Basic OpenTelemetry setup (Node.js) with OTLP exporter**
- **Approach:** Install `@opentelemetry/sdk-node`, `@opentelemetry/auto-instrumentations-node`, and an OTLP exporter (HTTP/grpc). Initialize `NodeSDK` with instrumentations, configure Resource (service.name), and start SDK before app code. Use `trace.getTracer` for manual spans.

**Q3: Capture errors to Sentry in an Express route**
- **Approach:** Initialize `Sentry.init({ dsn, tracesSampleRate })`, add `Sentry.Handlers.requestHandler()` and `Sentry.Handlers.errorHandler()`. In routes, call `Sentry.captureException(err)` for caught errors. Attach user/context with `Sentry.setUser()` and `Sentry.setContext()`.

**Q4: Instrument a database call with a custom span**
- **Approach:** Use OpenTelemetry tracer: `const span = tracer.startSpan('db.query'); try { await db.query(sql); } finally { span.end(); }`. Add attributes like query, id (avoid full SQL or PII in attributes), and set status based on error.

**Q5: Implement request-duration histogram with labels**
- **Approach:** Use a Histogram with buckets (e.g., [0.005, 0.01, 0.025, 0.05, 0.1, 0.5, 1, 2.5, 5]). On each request, observe duration with labels `{ method, route, code }`. Use route templating (e.g., `/users/:id -> /users/:id`) to avoid high cardinality.

---

## V. 🚀 Follow-Up Topics to Learn
1. **Advanced OpenTelemetry Features** — tail-based sampling, custom exporters, metrics adaptation. (Deepens tracing accuracy and cost control.)
2. **Prometheus + Thanos/Cortex** — long-term storage and multi-cluster aggregation. (Needed for scalable production-grade metrics retention.)
3. **Service Level Objectives (SLO) Design** — translating product requirements into SLIs/SLOs and alerting policies. (Makes monitoring actionable.)
4. **eBPF-based Observability (e.g., Pixie)** — low-overhead, kernel-driven insights into Node processes. (Powerful for production troubleshooting without code changes.)
5. **Chaos Engineering + Observability** — validate that telemetry captures failures and that alerts map to real incidents. (Ensures observability maturity.)

---

### Quick References & Best Practices
- Use **pull-based** metrics (Prometheus) for easier aggregation, but export to push gateways for short-lived jobs.
- Prefer **histograms** for latency distributions in distributed systems.
- Establish **naming conventions** for metrics and trace spans (service_name.metric_name and span naming with verbs).
- Always **sanitize** telemetry to avoid leaking PII.

---

*End of cheatsheet.*

[Previewable + Downloadable Link]

# Node.js — Debugging Cheatsheet

## I. 💡 Basic Details of Node.js Debugging
**Definition & purpose**
Node.js debugging is the process of finding and fixing bugs in Node.js applications using tools like the built-in debugger (`node inspect`), Chrome DevTools remote debugging, logging, core dumps, and runtime diagnostics. The goal is to observe runtime behavior, inspect state, and identify root causes of crashes, performance issues, and logic errors.

**Brief history & relevance**
Early Node debugging relied on `console.log` and crude tools. Modern Node integrates V8 debugging protocols, enabling rich remote debugging with Chrome DevTools and IDE integrations (VS Code, WebStorm). With microservices, serverless, and production constraints, knowing both local interactive debugging and non-interactive techniques (core dumps, flamegraphs, heap snapshots) is essential.

---

## II. 🧠 Important Concepts to Remember
1. **Inspectors & Protocols** — Node exposes the V8 Inspector Protocol; tools like `--inspect` and `--inspect-brk` open a WebSocket endpoint that DevTools or IDEs can attach to. *Analogy:* the inspector is a window into the running process.

2. **Breakpoints & Stepping** — Breakpoints pause execution so you can inspect scope, call stacks, and variables. Conditional breakpoints and logpoints are non-intrusive alternatives. *Analogy:* stop signs to examine the road conditions.

3. **Async Call Stacks & Async Hooks** — Async code fragments stack traces across ticks; modern debuggers show async stack traces. `async_hooks` gives low-level lifecycle hooks for async resources. *Analogy:* breadcrumbs across asynchronous callbacks.

4. **Heap & CPU Profiling** — Heap snapshots reveal memory retention; CPU profiles and flamegraphs show hot paths. Use `--inspect` with DevTools, `clinic`, `0x`, or `perf` for deeper profiling.

5. **Core Dumps & Postmortem** — When processes crash, core dumps capture memory for offline debugging (use `coredumpctl`, `gdb`, `lldb`, or `node report`). Helpful when reproducing the issue interactively is impossible.

6. **Remote & Production Safety** — In production, avoid pausing the event loop; use non-blocking diagnostics (sampling profiles, logging, lightweight tracing, pprof-style sampling). Secure inspector endpoints (auth, firewall) to avoid remote code execution risk.

7. **Logging vs Interactive Debugging** — `console`/structured logs are for observability over time; interactive debugging for local development. Use correlation IDs to trace requests across services.

---

## III. 📝 Theory — Most Asked Questions (Interview Prep)
**Q1: How do you start Node with the debugger attached?**
**A:** `node --inspect index.js` opens the inspector on the default port (9229). Use `--inspect-brk` to pause on the first line. Connect via `chrome://inspect` or an IDE.

**Q2: What is the difference between `--inspect` and `--inspect-brk`?**
**A:** `--inspect` opens the debug port but lets the program run. `--inspect-brk` opens the port and pauses execution before user code runs, allowing you to set breakpoints before any code executes.

**Q3: How do you debug asynchronous code and view async stacks?**
**A:** Modern DevTools show async stack traces (Promise chains, event callbacks). Use `async/await` with try/catch for clearer stacks. For low-level tracking, use the `async_hooks` API or enable `--trace-async-hooks` for debugging hooks usage.

**Q4: When would you use a core dump and how do you generate one?**
**A:** Use core dumps for postmortem debugging after fatal crashes or memory corruption in production where interactive debugging is impossible. On Linux, enable core dumps (`ulimit -c unlimited`), then when Node crashes, a core file is produced. Analyze with `gdb`/`lldb`, `node report`, or tools that understand V8 internals.

**Q5: Explain heap snapshot vs CPU profile.**
**A:** Heap snapshot captures memory allocations and object retainers at a point in time—useful for leaks. CPU profile samples where the CPU spends time across JS and native code—useful for identifying slow functions and hot paths.

**Q6: How do you safely enable remote debugging in production?**
**A:** Use short-lived, securely exposed debug sessions behind firewall and auth, or use secure tunnels (SSH port forwarding), and avoid breakpoints that block the event loop. Prefer non-blocking sampling profilers and aggregated logging.

---

## IV. 💻 Coding / Practical — Most Asked Questions (Interview Prep)
**P1: How to set breakpoints in VS Code for Node?**
**Approach:** Create a `launch.json` with `"type": "node"`, `"request": "attach"` (or `launch`), and port `9229`. Start Node with `--inspect` and hit the VS Code debugger "Attach" configuration. Use conditional breakpoints and watch expressions.

**P2: Reproduce and debug an intermittent memory leak**
**Approach:**
- Reproduce the leak in a staging workload.
- Capture heap snapshots at intervals (DevTools or `node --inspect` + Heap snapshot).
- Compare snapshots to find growing retainers and root paths.
- Use `--trace-gc` or `v8.getHeapStatistics()` to monitor.
- Fix the root cause (closure keeping references, caching without eviction).

**P3: Find a CPU hot-path in production**
**Approach:**
- Collect sampling CPU profiles (pprof-style or `clinic flame`, `0x`, or `--cpu-prof` in Node 12+ with `--prof` converted via `node --prof-process`).
- Generate flamegraph and inspect long stacks and heavy native bindings.
- Optimize algorithmic complexity, move heavy work to worker threads or native addons, or cache results.

**P4: Debugging unhandled promise rejections**
**Approach:**
- Use `process.on('unhandledRejection', handler)` during development to log stack traces and contexts.
- Prefer explicit `try/catch` around `await` or return caught rejections to the caller. Use linters and Node options (`--unhandled-rejections=strict`) to fail fast.

**P5: Attach Chrome DevTools to a running containerized Node app**
**Approach:**
- Start Node with `--inspect=0.0.0.0:9229` inside the container.
- Map container port to host (`-p 9229:9229`) and secure access (localhost-only mapping, SSH port forwarding) to avoid exposing the inspector publicly.
- Open `chrome://inspect` and add the target.

---

## V. 🚀 Follow-Up Topics to Learn
1. **Node.js Diagnostics (`node --diagnostic-report` / `node report`)** — Useful for automated crash and performance reports; bridges the gap between live debugging and postmortem analysis.
2. **Profiling Tooling: Clinic.js / 0x / pprof** — Deep dive into flamegraphs, latency sources, and production-safe profiling patterns.
3. **Memory Management & V8 Internals** — Learn GC types (minor/major), generational heap, and how allocation patterns affect GC behavior.
4. **Observability: OpenTelemetry + Tracing** — Correlate traces with debug artifacts to find problematic requests and reproduce issues.
5. **Worker Threads & Offloading** — When and how to offload CPU-bound work to worker threads or external services safely.

---

### Quick commands & snippets
- Start with inspector: `node --inspect index.js`  
- Pause at start: `node --inspect-brk index.js`  
- Heap snapshot from DevTools: Open Memory panel → Take Heap Snapshot.  
- CPU profiling: DevTools Performance panel or `node --prof` → `node --prof-process`.
- Enable core dumps (Linux): `ulimit -c unlimited` then run Node; inspect with `gdb` or `node report`.

---

*Cheatsheet created for interview prep and quick debugging reference.*

# Node.js Testing — Unit & Integration — Cheatsheet

> **Previewable + Downloadable Link:** Use the top-right corner to preview or download this cheatsheet.

---

## I. 💡 Basic Details of Node.js Testing (Unit & Integration)
**Definition & purpose**
Unit testing verifies individual components (functions, classes) in isolation. Integration testing verifies that multiple components or layers (e.g., HTTP route → controller → DB) work together as expected. Together they increase confidence, prevent regressions, and provide executable documentation for expected behavior.

**Brief history & relevance**
Testing in Node.js started with simple assertion libraries and evolved into rich ecosystems (Mocha, Jest, Tap) that support mocking, snapshot testing, coverage, and parallel execution. As Node apps scale and adopt microservices, solid unit and integration tests reduce incident rates and speed up safe refactoring.

---

## II. 🧠 Important Concepts to Remember
1. **Unit vs Integration vs E2E** —
   - Unit: isolated function/class; fast and deterministic. Use mocks/stubs for dependencies.
   - Integration: multiple components together; may touch DB, file system, or external services (prefer test doubles for third-party systems).
   - End-to-end (E2E): full-system tests simulating user flows (usually slower).

2. **Test Doubles** —
   - *Mocks*: verify interactions (expectations).
   - *Stubs*: provide canned responses.
   - *Spies*: observe calls without replacing behavior.
   - *Fakes*: lightweight in-memory implementations (e.g., in-memory DB).
   *Analogy*: Unit test doubles are theatre props — they stand in so the actor can rehearse alone.

3. **Isolation & Determinism** —
   - Tests should not depend on external networks, time of day, or machine-specific state. Use dependency injection and test-specific fixtures.

4. **Dependency Injection (DI)** —
   - Inject dependencies (DB clients, HTTP clients) rather than `require`-ing singletons; makes unit testing and substitution trivial.

5. **Assertions & Matchers** —
   - Use expressive matchers (e.g., `toEqual`, `toMatchObject`, `toHaveBeenCalledWith`) for clear failure messages.

6. **Test Coverage** —
   - Measure which code paths are executed. 100% coverage is rarely necessary; focus on meaningful coverage (critical logic, error handling).

7. **Fast Feedback Loop** —
   - Keep unit tests fast (milliseconds) and integration tests slower but still CI-friendly. Run unit tests on every edit and integration tests on CI or pre-merge pipelines.

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: What is the difference between a mock, stub, and spy?**
**A:** A stub replaces a function to provide predetermined responses. A spy observes calls to a function (arguments, call count) without changing behaviour. A mock both replaces and sets expectations about how it will be called; a test fails if expectations aren’t met.

**Q2: Why use dependency injection in Node.js tests?**
**A:** DI allows passing in test doubles instead of real implementations, enabling isolation, deterministic behavior, and easier control over edge cases. Avoiding hard-coded imports reduces test fragility.

**Q3: When do you use integration tests instead of unit tests?**
**A:** Use integration tests when you need to verify interactions between modules or with infrastructure (DB, message brokers). They catch contract/serialization issues and configuration problems unit tests can miss.

**Q4: What pitfalls cause flaky tests and how to fix them?**
**A:** Flakiness arises from timing/race conditions, reliance on external services, shared global state, and test order dependency. Fix by isolating state, using proper async/await, using deterministic test data, and leveraging in-memory or mocked infrastructure.

**Q5: How to test asynchronous code in Node.js?**
**A:** Use frameworks’ async helpers: return a Promise from the test, use `async/await`, or use the `done` callback in callbacks-style tests. Always ensure the test waits for completion and throws on errors.

**Q6: How should secrets and configuration be handled in tests?**
**A:** Keep secrets out of test code. Use environment-specific config loaded from CI secrets or test environment variables. For local dev, provide sample `.env.test` with non-sensitive defaults.

---

## IV. 💻 Coding / Practical — Most Asked Questions (with approaches)

**Q1: Setup a basic unit test with Jest for a pure function**
- **Approach:** Install `jest`. Create `sum.js` and `sum.test.js`. Use `expect(sum(2,3)).toBe(5)`. Run with `npx jest --watch`.

**Q2: Mock an HTTP client (e.g., axios) in Jest**
- **Approach:** Use `jest.mock('axios')` and set `axios.get.mockResolvedValue({ data: { ... } })`. Assert that the module under test handles the response and that axios was called with expected args.

**Q3: Integration test an Express route hitting an in-memory DB**
- **Approach:** Use `supertest` to issue requests to the app. Spin up an in-memory DB (e.g., `sqlite3` in memory or testcontainers) or use a test instance. Seed required data, call endpoints, assert status codes and response bodies, then teardown DB.

**Q4: Use dependency injection to replace a database client in tests**
- **Approach:** Export a factory that accepts a `db` parameter (`createUserService(db)`). In production pass real client; in tests pass a fake with the needed methods (e.g., `findOne`, `insert`). This avoids global singletons.

**Q5: Measure test coverage with nyc / Jest**
- **Approach:** For `nyc`: run `nyc mocha`. For Jest: enable `--coverage`. Review the HTML report to identify untested branches and improve tests accordingly.

**Q6: Example: Testing error handling path**
- **Approach:** Force dependency to throw (mock `db.query` to reject), assert that the service returns the expected error shape and logs the error. Also assert that retries or compensating actions were attempted if applicable.

---

## V. 🚀 Follow-Up Topics to Learn
1. **Property-based Testing (fast-check)** —
   - Generates many inputs automatically, revealing edge cases you didn’t think to test.

2. **Contract Testing (Pact)** —
   - Ensures integrations between services follow agreed contracts without full E2E tests.

3. **Testcontainers / Docker-based Integration Tests** —
   - Run real DBs/queues in ephemeral containers in CI for higher-fidelity integration tests.

4. **Mutation Testing (Stryker)** —
   - Validates test quality by introducing code mutations and verifying tests catch them.

5. **CI Test Strategy & Parallelization** —
   - Learn to split test suites (unit vs integration vs E2E), run in parallel, and gate merges effectively.

---

### Quick Tips & Best Practices
- Prefer **Jest** for batteries-included runner, mocking, and snapshot support; **Mocha** for flexible, minimal setups; **Tap** for simplicity and deterministic output.
- Keep unit tests **fast** and isolated; run them locally and on PRs. Run integration tests in CI or nightly where they won’t slow dev feedback.
- Avoid test pollution by cleaning up global state and using unique test data.
- Use **fixtures** and **factories** for repeatable test data.
- Track flaky tests and fix or quarantine them promptly.

---

*End of cheatsheet.*

# Node.js Ecosystem — Popular Libraries — Cheatsheet

> **Previewable + Downloadable Link:** Use the top-right corner to preview or download this cheatsheet.

---

## I. 💡 Basic Details of the Node.js Ecosystem (Popular Libraries)
**Definition & purpose**
The Node.js ecosystem is a rich collection of open-source libraries (packages) that solve common problems: utility functions, HTTP clients, promise utilities, debugging helpers, and more. These libraries accelerate development, standardize patterns, and reduce the need to reinvent common functionality.

**Brief history & relevance**
Since Node's early days, the npm registry grew rapidly. Some libraries became de-facto standards (e.g., lodash for utilities, axios for HTTP). As the platform matured, Node core also added features (Promises, `util.promisify`), shifting some patterns from external libs to built-in APIs. Still, the ecosystem remains essential for productivity and interoperability.

---

## II. 🧠 Important Concepts to Remember
1. **When to use a library vs native API** —
   - Prefer core APIs for stability and smaller dependency surface (e.g., `fetch`/`http`, `util.promisify`). Use libraries when they offer significant ergonomics, cross-environment behavior, or battle-tested solutions.

2. **Utility libraries (lodash / underscore)** —
   - Provide helpers for arrays, objects, functions, and numbers. Lodash offers modular imports so you can ship only used functions to reduce bundle size.

3. **HTTP clients (axios / node-fetch / undici)** —
   - Axios: feature-rich, supports older Node versions, interceptors, and automatic JSON handling. node-fetch: lightweight `fetch`-compatible API for Node. undici: high-performance, Node core-backed HTTP client that focuses on throughput and modern features.

4. **Promise & async helpers (bluebird legacy, native Promises)** —
   - Bluebird provided advanced promise utilities (cancellation, concurrency helpers) before native Promises matured. Today, native Promises plus utilities (e.g., `Promise.allSettled`, `p-map`) satisfy most needs.

5. **Debugging helpers (`debug`)** —
   - `debug` provides namespaced, opt-in logging controlled via `DEBUG` env var—lightweight compared to structured loggers and ideal for libraries and conditional debug output.

6. **Interop & compatibility (transpilation, polyfills)** —
   - Be mindful of Node version targets. Newer APIs (global `fetch`, `AbortController`) may require polyfills or minimum Node engines. Choose libraries that match your runtime support matrix.

7. **Security & maintenance** —
   - Prefer well-maintained libraries with active maintainers, tests, and reasonable release cadence. Watch for vulnerabilities (npm audit, Snyk) and avoid abandoned packages.

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: When would you use `lodash` instead of native JS methods?**
**A:** Use `lodash` when you need concise, battle-tested helpers that handle edge cases (deep cloning, uniqueId, complex merges), or when you want consistent behavior across Node versions. For simple operations, prefer native `Array`/`Object` methods to reduce dependencies.

**Q2: Compare `axios` and `node-fetch`. Which should you pick?**
**A:** `axios` is feature-rich (automatic JSON parsing, interceptors, request cancellation via tokens) and convenient for many apps. `node-fetch` (or native `fetch` in modern Node) is lighter and matches browser `fetch` semantics. Choose `axios` for comfort and features, `fetch` for standards alignment and smaller footprint, and `undici` for high-performance server workloads.

**Q3: What is `util.promisify` and when is it useful?**
**A:** `util.promisify` converts Node-style callback functions `(err, result) => {}` into functions that return Promises, enabling `async/await` usage with older APIs. Use it when you need to modernize callback-based libraries without rewriting them.

**Q4: Is Bluebird still relevant?**
**A:** Bluebird offered advanced features before native Promise APIs matured. While many Bluebird-specific features became unnecessary, it still provides some handy utilities and performance in certain cases. For most projects, native Promises with small helper libs are sufficient; consider Bluebird only for legacy codebases or very specific performance or API needs.

**Q5: How does `debug` differ from console.log or structured logging?**
**A:** `debug` is namespaced and opt-in via `DEBUG` env var, producing lightweight debug output suitable for development and libraries. Structured logging (e.g., pino, bunyan) is aimed at production observability with JSON logs, levels, and integration with log collectors. Use `debug` for dev-time details and libraries; use structured loggers for production logs and telemetry.

**Q6: What should you consider when adding a new dependency?**
**A:** Check maintenance (recent commits, issues), popularity (downloads), licensing, bundle size (if frontend), security advisories, and whether native APIs now cover the need. Prefer small, focused, and well-maintained packages.

---

## IV. 💻 Coding / Practical — Most Asked Questions (with approaches)

**Q1: Importing only lodash functions to minimize bundle size**
- **Approach:** Use modular imports like `const merge = require('lodash/merge')` or `import merge from 'lodash/merge'`. For build systems, enable tree-shaking and use `lodash-es` in ESM builds.

**Q2: Using `util.promisify` to convert `fs.readFile`**
- **Approach:** `const { promisify } = require('util'); const readFile = promisify(require('fs').readFile);` Then use `await readFile(path, 'utf8')` in async functions.

**Q3: Basic axios request with error handling and cancellation**
- **Approach:** Create an `AbortController`, pass `signal` to axios (or use axios CancelToken for older versions), wrap request in try/catch, and inspect `error.response` vs `error.request`.

**Q4: Replace axios with native fetch (modern Node)**
- **Approach:** Use global `fetch` (Node 18+) or `node-fetch` polyfill. Convert axios-specific features (interceptors) to wrapper functions or middleware-style layers.

**Q5: Using `debug` in a module**
- **Approach:** `const debug = require('debug')('my-module:sub'); debug('starting with %o', config);` Then run with `DEBUG=my-module:* node app.js` to enable output.

**Q6: Switch from Bluebird.map to native alternatives with concurrency control**
- **Approach:** Use `p-map` or implement a small concurrency pool: `await Promise.all(chunked.map(chunk => Promise.all(chunk.map(fn))))` or prefer `p-map(tasks, mapper, { concurrency })` for readability.

---

## V. 🚀 Follow-Up Topics to Learn
1. **undici and HTTP performance** —
   - Learn the Node core-backed HTTP client (`undici`) for high-throughput services and compare performance vs axios/undici.

2. **Node.js core improvements (fetch, AbortController)** —
   - Track core platform improvements to know when to remove dependencies and rely on built-ins.

3. **Bundle optimization & tree-shaking (for isomorphic apps)** —
   - Learn how bundlers handle imports, how to reduce client-side bundle size, and alternatives like `lodash-es`.

4. **Security scanning & supply-chain hygiene** —
   - Tools and practices: `npm audit`, `snyk`, lockfile maintenance, and minimal dependency strategies.

5. **Micro-libraries vs full-stack libs** —
   - When to pick a focused micro-library (small surface area, single responsibility) vs a larger, opinionated library.

---

### Quick Tips & Best Practices
- Prefer the Node.js core when it suffices; add libraries when they provide clear, tested value.
- Keep third-party dependencies minimal and audited. Use modular imports to avoid shipping unnecessary code.
- Use `debug` for developer-focused tracing and structured loggers for production telemetry.
- Revisit dependencies when upgrading Node versions — newer cores often remove the need for older libs.

---

*End of cheatsheet.*

# Node.js — TypeScript & Tooling (Cheatsheet)

### Previewable + Downloadable Link in the top right corner.

---

# I. 💡 Basic Details of TypeScript with Node

**Definition & purpose**
TypeScript (TS) is a statically-typed superset of JavaScript that compiles to plain JavaScript. With Node.js, TS adds type safety, better editor DX (autocomplete/refactor), and earlier error detection while running on the same V8 runtime.

**Brief history & relevance**
TypeScript was released by Microsoft (2012) to address scaling issues in JS. Today it’s the dominant way to write large Node.js codebases: better maintainability, safer refactors, and smoother teamwork.

**Common usage patterns with Node**
- Compile ahead-of-time with `tsc` -> produce `dist/` JS files for Node to run.
- Use `ts-node` for fast prototyping / scripts (interprets TS at runtime).
- Use bundlers (esbuild/webpack/rollup) or transpilers (Babel) for advanced optimizations or ESM/CJS bridging.

---

# II. 🧠 Important Concepts to Remember

1. **tsconfig.json** — central config for `tsc`. Controls `target`, `module`, `moduleResolution`, `outDir`, `rootDir`, `strict` flags, `paths`/`baseUrl` for aliases.
   - Analogy: `tsconfig.json` is the map that tells tsc where to go and how to speak.

2. **Module formats (CJS vs ESM)** — Node historically used CommonJS (`require`/`module.exports`) and now supports ESM (`import`/`export`). The interplay affects `tsconfig` (`module`), package.json (`type`), and bundling.
   - Quick rule: pick ESM for new projects; use `"type":"module"` in package.json and set `module`/`target` in tsconfig accordingly.

3. **Declaration files (.d.ts)** — provide type information for JS libraries or compiled output. Generate via `tsc --declaration` or hand-write `.d.ts` for runtime JS packages.
   - Think of `.d.ts` as the contract that documents runtime behavior.

4. **ts-node vs compiled workflow** — `ts-node` runs TS in place (great DX), but production should use compiled output (`tsc` or bundler). Consider `ts-node` + `nodemon` for dev.

5. **Type-only imports / emit helpers** — `import type {X} from 'y'` prevents runtime imports; use `--importsNotUsedAsValues` or `tsc` options to avoid leftover emit.

6. **Path aliases & moduleResolution** — configure `paths` + `baseUrl` in tsconfig and ensure runtime resolver (tsconfig-paths, babel, or bundler) mirrors it.

7. **Tooling tradeoffs (esbuild / tsc / Babel)**
   - `tsc`: authoritative type checker, slower for large projects, emits `.d.ts`.
   - `esbuild`: extremely fast bundler/transpiler, minimal type-checking (use `tsc --noEmit` alongside for types).
   - `Babel`: flexible transforms and plugin ecosystem, needs `@babel/preset-typescript` (drops types — use `tsc` for types).
   - Analogy: `tsc` is the judge (types), `esbuild` is the sprinter (speed), `Babel` is the stylist (transform power).

---

# III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: What is the difference between `tsc` and `babel` when compiling TypeScript?**
**A:** `tsc` performs full type-checking and emits JS and optional `.d.ts` files. `Babel` with `@babel/preset-typescript` strips types and transpiles TS syntax to JS but does not perform type-checking — so many projects run `babel` for transforms plus `tsc --noEmit` (or `tsc` separately) for types.

**Q2: How do you make path aliases work at runtime and compile time?**
**A:** Configure `paths` and `baseUrl` in `tsconfig.json` for the compiler. At runtime, Node doesn’t read tsconfig, so use a resolver: either a bundler (esbuild/webpack/ts-loader) that respects aliases or runtime helpers like `tsconfig-paths/register` or adjust `NODE_PATH` or use `module-alias`.

**Q3: When should a project output declaration files (`.d.ts`)?**
**A:** Output `.d.ts` when publishing a package (so TypeScript consumers get types) or when splitting a monorepo with shared packages. Enable `declaration: true` and `declarationMap` for better DX.

**Q4: Pros/cons of ESM in Node for TypeScript projects?**
**A:** ESM provides a modern module system and better static analysis of imports. Challenges: interop with CJS packages, different `package.json` `type`, dynamic import differences, and configuring `tsc` to emit `module: "ESNext"` or `module: "NodeNext"`. Often simpler for new apps but requires careful bundler/runtime config.

**Q5: How to avoid type-only imports causing runtime errors?**
**A:** Use `import type { X } from 'y'` for purely type imports. Ensure `tsconfig` has `importsNotUsedAsValues` configured (e.g., `remove`) and enable `--preserveValueImports`/`--importsNotUsedAsValues` behavior according to your TS version to avoid accidental emits.

---

# IV. 💻 Coding / Practical Most Asked Questions

**P1: Setup a minimal Node + TypeScript project**
- `npm init -y`
- `npm i -D typescript ts-node @types/node` (plus `eslint`/`prettier` if desired)
- `npx tsc --init`
- `tsconfig` recommended bits: `target: "ES2020"`, `module: "CommonJS"` or `ESNext` (if ESM), `outDir: "dist"`, `rootDir: "src"`, `strict: true`, `esModuleInterop: true`.
- Add scripts: `build: tsc`, `dev: ts-node src/index.ts`, `start: node dist/index.js`.

**P2: Create a declaration file for a plain JS module**
- If `lib/foo.js` exists, add `lib/foo.d.ts` with `export function doThing(x: string): number;` or generate via `tsc` options for compiled TS.

**P3: Fast dev server with esbuild (example approach)**
- Use `esbuild`'s watch mode to transpile and bundle: run `esbuild src/index.ts --bundle --platform=node --outfile=dist/index.js --watch` and `node dist/index.js` (or use `nodemon` to restart). Run `tsc --noEmit --watch` in parallel for type checks.

**P4: Migrating a JS project to TypeScript**
- Start with `allowJs: true` and `checkJs: false`; rename files gradually to `.ts`/`.tsx`. Use `--noEmit` and `skipLibCheck` to ease migration. Add `@types/*` for dependencies.

**P5: Handling mixed ESM/CJS dependencies**
- Use `import pkg from 'pkg'` with `esModuleInterop: true` or `const pkg = require('pkg')` in CJS. For ESM packages in CJS projects, prefer dynamic `import()` or move to ESM.

**P6: Type-only utility — `ts-node` usage in scripts**
- Dev script: `"dev": "ts-node --transpile-only src/server.ts"` and run `tsc --noEmit` in CI to enforce types. `--transpile-only` skips type-check for speed.

---

# V. 🚀 Follow-Up Topics to Learn

1. **Advanced Module Resolution & Node's ESM Loader** — deep-dive into `exports`/`imports` fields in package.json, conditional exports, and `module`/`resolve` algorithms. (Important for publishing cross-target packages.)

2. **Monorepos & TypeScript Project References** — use project references (`composite` projects) for large codebases to speed up builds and incremental compile.

3. **Type System Mastery: Advanced Types & Generics** — mapped types, conditional types, distributive conditional types, `infer`, and template literal types for safer APIs.

4. **Build Systems: esbuild/Rollup/webpack and CI** — learn how to wire type-checking with fast bundlers and set up reproducible production builds in CI (cache, parallelization).

5. **Runtime Type Validation** — libraries like `zod`, `io-ts`, `runtypes` for runtime assertions and bridging static types with runtime guarantees (useful for APIs and boundary validation).

---

*Concise, practical reference you can paste into notes or use as onboarding material.*

# Node.js — Build & Bundling (Cheatsheet)

### Previewable + Downloadable Link in the top right corner.

---

# I. 💡 Basic Details of Build & Bundling for Node

**Definition & purpose**
Build and bundling tools take your source files, transform them (TypeScript/JS features), resolve dependencies, and produce optimized output that Node (or another runtime) executes. For server-side Node apps, bundlers can reduce cold-start time, package native ESM/CJS interop, and simplify deployment by producing a single artifact.

**Short history & relevance**
Historically Node ran raw JS files (CJS). As ecosystems grew and projects adopted TypeScript and modern syntax (ESM, top-level await), build tools evolved: webpack and Rollup pioneered module bundling, and esbuild introduced ultra-fast builds. Today, choice of tool affects DX, performance, and compatibility.

**When to bundle for Node**
- Serverless / single-file deployment (Lambda, Cloud Run) to reduce cold-starts and simplify packaging.
- Obfuscation or shipping a single binary-like artifact.
- When using TypeScript or non-standard syntax that Node doesn’t natively support (older Node versions).
- For production builds where deterministic output and tree-shaking matter.

---

# II. 🧠 Important Concepts to Remember

1. **Bundling vs Transpilation** — `bundling` merges modules into a package (often one file) plus transforms; `transpilation` converts syntax (TS→JS, modern→older JS) but keeps module boundaries.
   - Analogy: transpilation translates the book; bundling pastes every chapter into one book.

2. **Native ESM vs Transpiled Output** — modern Node supports ESM natively (when `type: "module"` or `.mjs`). Choosing native ESM avoids transforms but requires careful dependency and export config. Transpiling to CJS (or to ESM with different target syntax) can improve compatibility with older tools.

3. **Tree-shaking & dead-code elimination** — bundlers remove unused exports when modules are static ESM; CJS hampers tree-shaking. Use ESM-style exports to make tree-shaking effective.

4. **Platform target: node vs browser** — bundlers can target `platform: 'node'` to preserve Node built-ins and avoid polyfills. For server builds, avoid browser-targeted transforms that add unnecessary polyfills.

5. **Source maps & sourcemap strategy** — include inline or external source maps for better production debugging; some platforms support uploading source maps (e.g., Sentry).

6. **Externalizing dependencies** — for server bundles, you often `external` large native modules (e.g., `node_modules`, `pg`, `bcrypt`) or native binaries to avoid bundling heavy or incompatible code. Many bundlers provide `externals` config.

7. **Code-splitting & lazy-loading** — useful for large monoliths or cold-start sensitive serverless functions; split hot paths from rarely-used code and load dynamically.

---

# III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: When should you prefer esbuild over webpack for a Node project?**
**A:** Prefer esbuild when you need extremely fast build times (dev iteration, CI caching) and a simple configuration. Use webpack for complex needs (advanced plugin ecosystem, custom loaders, intricate asset handling). For Node server bundles, esbuild offers a simple, fast path with `platform: 'node'` and `bundle: true`.

**Q2: What is "external" in bundler configs and why use it?**
**A:** `external` tells the bundler not to include certain modules in the bundle; instead the runtime will `require` or `import` them. Use it for native modules, large vendor libs, or when the runtime environment provides the module.

**Q3: Why can CJS hurt tree-shaking compared to ESM?**
**A:** CJS exports are dynamic at runtime (`module.exports = { ... }`), so static analyzers can't reliably determine unused exports. ESM has static import/export syntax, enabling bundlers to remove unused code.

**Q4: How do you handle native node modules (e.g., bcrypt, sharp) in bundles?**
**A:** Mark them external and keep deployment steps that install native binaries on the target environment (e.g., postinstall `npm rebuild`, include prebuilt binaries, or use lambda layers). Alternatively use pure-JS alternatives if feasible.

**Q5: What are the tradeoffs of shipping a single-file server bundle?**
**A:** Pros: simple deploy, smaller cold-start overhead, deterministic artifact. Cons: larger build time, tricky native dependency handling, debugging complexity if source maps are missing, potentially larger memory footprint at startup.

---

# IV. 💻 Coding / Practical Most Asked Questions

**P1: Minimal esbuild server bundle config (CLI example)**

```
esbuild src/index.ts \
  --bundle \
  --platform=node \
  --target=node18 \
  --outfile=dist/index.js \
  --external:aws-sdk \
  --sourcemap
```

**P2: Example Rollup config for Node (rollup.config.js)**

```js
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import typescript from '@rollup/plugin-typescript';
import { terser } from 'rollup-plugin-terser';

export default {
  input: 'src/index.ts',
  output: { file: 'dist/index.js', format: 'cjs', sourcemap: true },
  external: ['pg', 'bcrypt'],
  plugins: [resolve({ preferBuiltins: true }), commonjs(), typescript(), terser()],
};
```

**P3: Webpack for server: key options**
- `target: 'node'`
- `externals: [nodeExternals()]` (use `webpack-node-externals` plugin)
- `output.libraryTarget: 'commonjs2'`
- Use `ts-loader` or `babel-loader` for TypeScript.

**P4: Handling ESM packages when bundling for Node (practical pattern)**
- Use `module: 'NodeNext'` or `module: 'ESNext'` in `tsconfig` when using native ESM.
- If bundling, ensure bundler resolves `package.json` `exports` and `type` fields correctly; esbuild and Rollup have options to preserve or prefer ESM.

**P5: CI pipeline sample steps for server bundling**
1. `npm ci`
2. `npm run build` (esbuild/webpack/rollup)
3. `npm prune --production` or install production deps separately for packaging if not bundled
4. Package artifact + `node_modules` (if externals used) or single bundle for deployment

---

# V. 🚀 Follow-Up Topics to Learn

1. **Serverless-specific optimizations** — cold start strategies, layering, minimal handler bootstrap, and using smaller runtimes.

2. **Native binaries & cross-compilation** — learn how to build and ship native modules for different target platforms (musl vs glibc, Alpine issues).

3. **Module graphs & dependency analysis** — tools to visualize and analyze bundle size (e.g., `source-map-explorer`, `esbuild` metafile analysis).

4. **V8 snapshots & packaging (pkg, ncc, nexe)** — techniques to create single executables or V8 startup snapshots to improve performance and simplify distribution.

5. **Advanced bundler internals** — plugin system design, rollup’s treeshaking algorithm, esbuild’s parser & codegen model, and how sourcemaps are generated.

---

*Compact reference aimed at server-side Node apps: quick commands, config patterns, and pitfalls to watch for.*

# Node.js CI/CD — Cheatsheet

> **Previewable + Downloadable Link:** Use the top-right corner to preview or download this cheatsheet.

---

## I. 💡 Basic Details of Node.js CI/CD
**Definition & purpose**
CI/CD (Continuous Integration / Continuous Delivery or Deployment) is the automation of building, testing, and releasing software. For Node.js projects, CI/CD ensures code quality, security, and reliable releases by running linters, tests, security scanners, building artifacts, and automating release tagging and publishing.

**Brief history & relevance**
CI practices began with automated builds and unit tests; CD evolved to automate deployments and release management. Modern Node.js development relies heavily on CI/CD to maintain fast iteration, shift-left security, and reproducible releases across environments.

---

## II. 🧠 Important Concepts to Remember
1. **Pipeline stages** —
   - Typical stages: install → lint → unit tests → integration tests → build → security scans → publish/release.

2. **Fail-fast vs fail-safe** —
   - Fail-fast: stop on first critical failure (lint/test). Fail-safe: continue non-critical steps (e.g., smoke tests) for diagnostics. Choose strategy per stage.

3. **Secrets & credentials** —
   - Store tokens and keys in CI secrets/vaults, not in source. Use short-lived tokens and least privilege for publish operations.

4. **Caching & performance** —
   - Cache `node_modules`, build artifacts, or package manager caches (npm, pnpm, yarn) to speed pipelines; invalidate caches on lockfile changes.

5. **Test matrix & parallelization** —
   - Run test matrices (Node versions, OS) and parallelize independent jobs to reduce wall-clock time. Prefer fast unit tests locally and full matrices in CI.

6. **Security scanning** —
   - Integrate `npm audit`, Snyk, Dependabot, and static analysis into the pipeline. Block merges for critical vulnerabilities when appropriate.

7. **Release automation & semantic-release** —
   - Automate versioning, changelogs, and publish via conventional commits with tools like `semantic-release`. Use commit message conventions to derive release types.

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: What is the difference between Continuous Delivery and Continuous Deployment?**
**A:** Continuous Delivery ensures every change is build-and-testable and can be deployed to production manually. Continuous Deployment goes further by automatically deploying every passing change to production without manual approval.

**Q2: How do you securely store and use credentials in CI?**
**A:** Use the CI platform’s secrets store (GitHub Secrets, GitLab CI variables), or a centralized secrets manager (HashiCorp Vault, AWS Secrets Manager). Grant minimal scopes, rotate regularly, and inject secrets at runtime — never commit them to source or logs.

**Q3: What is semantic-release and why use it?**
**A:** `semantic-release` automates versioning and changelog generation based on commit messages following Conventional Commits. It determines the next semantic version (patch/minor/major), creates release tags, publishes artifacts, and releases notes — removing human error in release steps.

**Q4: How would you structure tests across pipelines?**
**A:** Run fast unit tests in pre-commit hooks and PR checks; run integration and E2E tests in CI (possibly on a separate pipeline or environment); schedule heavy tests (e.g., load tests) nightly or as part of release gating.

**Q5: How to handle flaky tests in CI?**
**A:** Triage and fix root causes (timing, resource constraints). Use retries sparingly with careful logging. Quarantine flaky tests temporarily, annotate with flake dashboards, and block merges only if tests are stable.

**Q6: How to implement canary releases or feature flags in Node.js deployments?**
**A:** Use feature flag services (LaunchDarkly, Unleash) or traffic-splitting in load balancers. Deploy new versions to a subset of instances (canary) and monitor metrics/alerts before promoting globally. Automate rollback on SLO violations.

---

## IV. 💻 Coding / Practical — Most Asked Questions (with approaches and snippets)

**Q1: Minimal GitHub Actions workflow for Node.js tests + lint**
- **Approach:** Use `actions/checkout`, `actions/setup-node`, cache `~/.npm`, install, run `npm ci`, run `npm run lint` and `npm test`. Use matrix for Node versions and `--coverage` if needed.

**Q2: Add security scanning with npm audit and Dependabot**
- **Approach:** Run `npm audit --json` in CI and fail on critical vulnerabilities. Enable Dependabot to open PRs for dependency updates; configure auto-merge for vetted updates.

**Q3: Semantic-release with GitHub Actions**
- **Approach:** Configure `semantic-release` in CI with a job that runs on `push` to `main`. Provide a GitHub token with `repo` scope in secrets. Use plugins for `@semantic-release/changelog`, `@semantic-release/git`, and `@semantic-release/npm` as needed.

**Q4: Release tagging & changelog generation manually**
- **Approach:** Use `conventional-changelog` or `standard-version` to generate changelogs and bump versions locally; commit the changelog and tags, then push. Prefer automation to avoid human error.

**Q5: CI caching example (actions/cache)**
- **Approach:** Cache `~/.npm` or the package manager cache keyed by `package-lock.json` hash. Invalidate cache on lockfile changes to avoid stale deps.

**Q6: Example: Running integration tests with a test DB using Docker in CI**
- **Approach:** Use service containers (e.g., PostgreSQL) or `testcontainers` to spin up ephemeral DBs, wait-for readiness, run migrations/seed, execute tests with `supertest`, then teardown.

**Q7: Automating releases for monorepos**
- **Approach:** Use tools like `lerna` (classic) or `changesets` to manage package-level versioning and changelogs. Combine with `semantic-release` plugins that understand monorepos or use workspace-aware changelog tooling.

---

## V. 🚀 Follow-Up Topics to Learn
1. **Infrastructure as Code + GitOps (ArgoCD, Flux)** —
   - Shift deployment definitions into Git and automate reconciliations for reproducible deployments.

2. **Advanced Release Strategies (blue-green, canary, feature flags)** —
   - Reduce risk by controlling traffic and rollouts; instrument monitoring to automate promotion/rollback.

3. **Pipeline Observability & SLO-driven CI** —
   - Monitor CI pipeline health, flakiness, and lead times; optimize for developer feedback and reliability.

4. **Artifact Registries & SBOMs** —
   - Use private registries (GitHub Packages, Artifactory), sign artifacts, and publish SBOMs for supply-chain auditing.

5. **Policy-as-Code (OPA, Gatekeeper)** —
   - Enforce security and compliance policies in the CI/CD pipeline automatically.

---

### Quick Tips & Best Practices
- Keep pipelines **fast** and **deterministic**; fail early on fast checks (lint/tests) and run heavier checks in parallel or gated.
- Automate releases with **semantic-release** or similar to avoid human error; ensure tokens and permissions are limited.
- Use **Dependabot** + `npm audit` + Snyk for layered dependency security.
- Cache intelligently (lockfile-based keys) and purge caches on dependency updates.
- Version and tag releases consistently; prefer machine-readable changelogs for automation.

---

*End of cheatsheet.*


# Node.js Deployment — Cheatsheet

> **Previewable + Downloadable Link:** Use the top-right corner to preview or download this cheatsheet.

---

## I. 💡 Basic Details of Node.js Deployment
**Definition & purpose**
Deployment covers packaging, running, and operating Node.js applications in production. This includes containerization, process management, orchestration, observability hooks (health checks, metrics), and operational concerns like scaling, resilience, and rollout strategies.

**Brief history & relevance**
Node apps originally ran on bare servers or PaaS (Heroku). Today, containerization (Docker) and orchestrators (Kubernetes) dominate for portability, reproducibility, and scaling. Process managers like PM2 or systemd still matter for simple deployments and edge cases where orchestration isn't used.

---

## II. 🧠 Important Concepts to Remember
1. **Immutable artifacts** —
   - Build once, deploy the same artifact everywhere (container images, tarballs). Rebuilds should be rare and traceable.

2. **Container best practices** —
   - Use small base images, multi-stage builds, non-root user, pin dependency versions, and keep layers cache-friendly.

3. **12-factor app rules relevant to deployment** —
   - Treat backing services as attached resources, store config in env vars, and make processes stateless where possible to enable horizontal scaling.

4. **Process management (PM2 / systemd)** —
   - PM2 offers clustering, zero-downtime reloads, and process monitoring; systemd provides OS-level process supervision with native logging and restart policies.

5. **Orchestration (Kubernetes)** —
   - Pods, Deployments, Services, ConfigMaps, Secrets, Probes (readiness/liveness), and RBAC are core primitives. Understand resource requests/limits and autoscaling (HPA/VPA).

6. **Health checks & graceful shutdown** —
   - Implement liveness and readiness probes. On shutdown, stop accepting new requests, finish in-flight work, close DB connections, and exit within the orchestrator's terminationGracePeriod.

7. **Networking & service discovery** —
   - Understand cluster networking (CNI), service types (ClusterIP/NodePort/LoadBalancer), and ingress/controllers for external traffic. Use DNS-based discovery within clusters.

8. **Observability hooks** —
   - Expose metrics endpoints, structured logs, and tracing. Ensure probes and health endpoints are light and reliable.

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: Why use Docker for Node.js apps?**
**A:** Docker packages the app and its runtime into a portable, reproducible image, removing "works on my machine" issues. It provides layering for efficient builds, predictable environments, and easy rollout in orchestrators.

**Q2: What is the difference between readiness and liveness probes in Kubernetes?**
**A:** Readiness probes signal whether a pod is ready to receive traffic (used by Service load balancing). Liveness probes detect if a container is dead or stuck and should be restarted. Readiness affects routing; liveness affects lifecycle.

**Q3: How do you implement graceful shutdown in a Node.js HTTP server?**
**A:** On SIGTERM/SIGINT, stop accepting new connections (`server.close()`), wait for existing requests to finish (or set a maximum drain timeout), close DB connections, flush logs/metrics, then exit. In clusters, coordinate with the process manager/orchestrator to allow time for draining.

**Q4: When would you use PM2 instead of Kubernetes?**
**A:** Use PM2 for single-host deployments, simple clustering, or when full orchestration isn't needed. Kubernetes is appropriate for large-scale, multi-host, microservice architectures requiring advanced scheduling, scaling, and service discovery.

**Q5: What are common security practices for Node.js containers?**
**A:** Run as non-root, minimize installed packages, scan images for vulnerabilities, use base image pinning, mount secrets via orchestrator-managed secrets (not environment variables in plaintext if avoidable), limit network privileges, and apply network policies.

**Q6: How do you manage config and secrets across environments?**
**A:** Store non-sensitive config in ConfigMaps or environment variables; store secrets in orchestrator secrets stores (Kubernetes Secrets, Vault) and grant least-privilege access. Use injection mechanisms rather than baking secrets into images.

---

## IV. 💻 Coding / Practical — Most Asked Questions (with approaches & examples)

**Q1: Minimal Dockerfile for a Node.js app (multi-stage)**
- **Approach:** Use a builder stage to install dependencies and build artifacts, then copy only necessary files into a slim runtime image. Run as non-root and set `NODE_ENV=production`.

```dockerfile
# Builder
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Runtime
FROM node:18-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/index.js"]
```

**Q2: Graceful shutdown snippet for HTTP server**
- **Approach:** Track open connections, call `server.close()` on signal, await in-flight requests or use a drain timeout.

```js
const http = require('http');
const app = require('./app'); // express instance
const server = http.createServer(app);
let connections = new Set();
server.on('connection', (socket) => { connections.add(socket); socket.on('close', () => connections.delete(socket)); });

const shutdown = async () => {
  console.log('Shutting down...');
  server.close(() => console.log('Stopped accepting new connections'));
  // optionally wait for active requests
  setTimeout(() => connections.forEach((s) => s.destroy()), 30000); // force after 30s
  // close DB, flush logs...
};
process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);

server.listen(3000);
```

**Q3: Kubernetes Deployment with readiness and liveness probes**
- **Approach:** Add `readinessProbe` and `livenessProbe` that hit lightweight endpoints (e.g., `/health/readiness`, `/health/liveness`). Configure `terminationGracePeriodSeconds` to allow draining.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  template:
    spec:
      terminationGracePeriodSeconds: 60
      containers:
      - name: app
        image: my-app:latest
        ports:
        - containerPort: 3000
        readinessProbe:
          httpGet: { path: /health/readiness, port: 3000 }
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet: { path: /health/liveness, port: 3000 }
          initialDelaySeconds: 30
          periodSeconds: 20
```

**Q4: Using PM2 for zero-downtime reloads**
- **Approach:** Start app with `pm2 start dist/index.js -i max` to cluster across CPUs. Use `pm2 reload all` to perform graceful reloads without downtime. Configure `ecosystem.config.js` for env and restart policies.

**Q5: Health endpoint design**
- **Approach:** Keep health checks light (check process and critical dependencies minimally). Readiness should verify ability to serve traffic (DB reachable, caches warm). Liveness should be a quick self-check that the process isn't deadlocked.

**Q6: Rolling updates vs blue/green**
- **Approach:** Rolling updates progressively replace pods; blue/green deploys a separate environment and switches traffic when ready. Use rolling updates for simplicity, blue/green for safer, instant rollback and verification.

---

## V. 🚀 Follow-Up Topics to Learn
1. **Service Mesh (Istio/Linkerd)** —
   - Adds observability, fine-grained traffic control, and mTLS without changing application code.

2. **Cluster Autoscaling & Cost Optimization** —
   - Autoscaling nodes/pods, right-sizing resources, and leveraging spot instances for cost savings.

3. **Advanced SIGTERM handling & draining patterns** —
   - Understand platform-specific lifecycle hooks and integrate with load-balancers to ensure smooth rollouts.

4. **Image security (Notary/Trivy) & supply-chain hardening** —
   - Sign and scan images, maintain SBOMs, and enforce policies for trusted images.

5. **Edge deployment patterns (serverless, edge runtimes)** —
   - Learn when to deploy functions (AWS Lambda, Cloud Run) or edge workers for latency-sensitive workloads.

---

### Quick Tips & Best Practices
- Build immutable container images and deploy the same artifact across environments.
- Implement readiness and liveness probes and ensure graceful shutdown logic is reliable.
- Prefer stateless services and externalize state to managed stores.
- Run processes as a non-root user and minimize image attack surface.
- Instrument health endpoints, metrics, and logs to make deployments observable.

---

*End of cheatsheet.*

# Node.js — Databases & ORMs (Cheatsheet)

### Previewable + Downloadable Link in the top right corner.

---

# I. 💡 Basic Details: Databases & ORMs for Node

**Definition & purpose**
Database drivers provide a low-level API to talk to a database (SQL or NoSQL). ORMs/ODMs (Object‑Relational/Object‑Document Mappers) wrap drivers to provide higher-level abstractions: typed models, query builders, migrations, and relationship helpers.

**Short history & relevance**
As Node applications scaled, ecosystems produced both direct drivers (fast, explicit) and ORMs (convenience, productivity). Modern stacks often combine both: use ORM/query builder for app-level modeling and raw drivers for performance-critical paths.

**Common libraries**
- SQL drivers: `pg`/`pg-pool`, `mysql2`, `mssql`.
- NoSQL drivers: `mongodb` (native driver), `redis` (clients like `ioredis`/`redis`).
- ORMs/ODMs & query builders: Prisma (ORM + type-safe client), TypeORM, Sequelize, Objection.js (knex-based), Knex (query builder), Mongoose (MongoDB ODM).

---

# II. 🧠 Important Concepts to Remember

1. **Driver vs ORM** — Drivers = thin client to DB. ORMs = mapping to objects + convenience. Use drivers for raw performance and ORMs for developer productivity.

2. **Connection pooling** — reuse DB connections to avoid expensive TCP/handshake overhead. Pool size should match app concurrency and DB limits. In serverless contexts, avoid naive pooling (clients can explode connections) — use connection proxies (PgBouncer) or serverless-friendly pools.

3. **Transactions & ACID** — use transactions for multi-step consistent updates. Understand isolation levels and how your driver exposes transactions (e.g., `BEGIN`/`COMMIT`/`ROLLBACK` or client.transaction APIs).

4. **Query builders vs raw SQL** — query builders (Knex, Prisma) balance safety and readability; raw SQL offers full control and sometimes superior performance. Prefer parameterized queries to avoid SQL injection.

5. **Migrations & schema management** — keep schema changes versioned (migrations). Tools: Prisma Migrate, Knex migrations, TypeORM migrations, Sequelize CLI.

6. **Connection ergonomics in long-running servers vs serverless** — long-lived servers keep a pool open; serverless needs pooled connection strategies, single-connection proxies, or connection pooling services.

7. **Type safety & generated clients** — Prisma generates a typed client based on schema; reduces runtime errors and improves DX. ORMs vary in type support.

---

# III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: When would you choose a driver over an ORM?**
**A:** Choose a driver when performance predictability and fine-grained control over SQL is required, when working with complex queries not well-expressed in an ORM, or to avoid ORM overhead in microservices. Use an ORM when fast development, maintainable models, and migration tooling matter.

**Q2: How does connection pooling work and why is it important?**
**A:** A pool maintains a set of open DB connections and hands them to requesting code. It reduces connection setup cost and manages concurrent usage. Configure pool size to avoid exhausting DB resources; in shared/cloud DBs keep conservative values.

**Q3: What problems occur when using a pooled DB client in serverless platforms (e.g., AWS Lambda)?**
**A:** Each function invocation can create new pools, exploding total connections and hitting DB limits. Solutions: use a connection proxy (PgBouncer/ProxySQL), a serverless-friendly pooling library, or a central pool service.

**Q4: Compare Prisma and Sequelize.**
**A:** Prisma emphasizes a schema-first approach, generates a type-safe client, and focuses on developer DX. Sequelize is an active Record-style ORM with mature ecosystem and runtime model objects. Prisma usually gives better TypeScript ergonomics; Sequelize offers more direct model instances and lifecycle hooks.

**Q5: How to ensure safe queries against SQL injection?**
**A:** Always use parameterized queries or ORM query bindings instead of string concatenation. Avoid manual interpolation of user inputs into SQL.

---

# IV. 💻 Coding / Practical Most Asked Questions

**P1: Minimal PostgreSQL usage with `pg` and pooling**

```js
const { Pool } = require('pg');
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 20, // pool size
  idleTimeoutMillis: 30000,
});

// query
const res = await pool.query('SELECT id, name FROM users WHERE id = $1', [id]);
```

**P2: Basic Prisma setup and usage**

1. `npm install prisma @prisma/client`
2. `npx prisma init` → edit `schema.prisma`
3. `npx prisma migrate dev --name init`
4. Usage:

```ts
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();
await prisma.user.create({ data: { name: 'Ana' } });
```

**P3: Transaction example (using `pg` client)**

```js
const client = await pool.connect();
try {
  await client.query('BEGIN');
  await client.query('UPDATE accounts SET balance = balance - $1 WHERE id = $2', [amt, fromId]);
  await client.query('UPDATE accounts SET balance = balance + $1 WHERE id = $2', [amt, toId]);
  await client.query('COMMIT');
} catch (err) {
  await client.query('ROLLBACK');
  throw err;
} finally {
  client.release();
}
```

**P4: Handling migrations in CI**
- Run migrations in a dedicated migration job: `npx prisma migrate deploy` or `knex migrate:latest` before running the app or deploying. Avoid running automatic migrations in every app startup in production.

**P5: Serverless pattern for PostgreSQL connections**
- Use a connection proxy (PgBouncer) or a managed pooler (Amazon RDS Proxy). If not available, reduce pool size to 1 per lambda and use pooling via an external service or reuse global client in warm containers (e.g., store pool on global object to be reused across invocations).

---

# V. 🚀 Follow-Up Topics to Learn

1. **Distributed transactions & sagas** — for multi-service consistency when traditional DB transactions don't span services.
2. **Change data capture (CDC)** — Debezium or cloud provider tools to react to DB changes for event-driven architectures.
3. **CQRS & Read-replica strategies** — using separate read/write databases and replication lag considerations.
4. **Indexing & query performance tuning** — EXPLAIN plans, indexes, partitioning strategies for large tables.
5. **Observability for DBs** — tracing slow queries, instrumentation (pg tracing, query logs), and integrating DB metrics into monitoring.

---

*Compact, practical reference for Node apps: drivers, ORMs, pooling strategies, and common pitfalls.*


# Node.js — Caching Cheatsheet

## I. 💡 Basic Details of Node.js Caching
**Definition & purpose:** Caching stores computed or fetched data (responses, DB rows, computed results) in a faster-access layer so subsequent requests are quicker and cheaper. In Node.js apps caching improves latency, throughput, and reduces load on slow/backend systems.

**History & relevance:** Caching is a fundamental performance technique dating back to CPU/memory hierarchies. In web apps it became essential with REST/HTTP, microservices, and cloud-native architectures. Redis is the most common external cache used with Node.js because of its speed, rich data types, and features like TTL and persistence.


## II. 🧠 Important Concepts to Remember
1. **In-memory cache (process-local):** e.g., a Map, LRU cache. Fast (no network) but scoped to a single process—lost on restart and not shared across instances. Good for per-process memoization.
   - *Analogy:* a sticky note on your desk — instant but only you can see it.

2. **External cache (Redis, Memcached):** shared across processes/hosts, survives multiple app instances, optional persistence/configurable eviction.
   - *Analogy:* a bulletin board in the hallway everyone can read.

3. **TTL (time-to-live):** automatic expiration. Controls staleness and memory usage. Use TTL to bound inconsistency windows.

4. **Cache invalidation strategies:**
   - **Time-based expiry (TTL):** simple, eventual freshness.
   - **Explicit invalidation / write-through / write-back:** when data changes, proactively update or delete cached entries.
   - **Cache-aside (lazy loading):** application reads cache first, on miss fetches DB then populates cache.
   - **Read-through / write-through:** cache layer handles fetching/writing automatically (common in some libraries).
   - **Versioned keys / cache-busting:** include a version or timestamp in keys to cheaply invalidate groups.

5. **Consistency tradeoffs:** caching introduces stale reads. Decide acceptable staleness, and design for eventual consistency if necessary.

6. **Eviction policies & memory limits:** LRU (least recently used), LFU, TTL, or custom policies — choose based on access patterns.

7. **Cache stampede / thundering herd:** many requests on an expired key can overload backend. Mitigations: request coalescing, lock (mutex) per-key, early recompute, randomized TTL jitter.


## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: What is cache-aside and how does it work?**
**A:** Cache-aside (lazy caching) means the application checks the cache on read; if a miss, it fetches from the authoritative store (DB), then writes the result back to the cache and returns it. Writes go to DB, and then the cache is invalidated or updated by the application.

**Q2: Compare in-memory caching vs Redis.**
**A:** In-memory cache is fastest and simplest but only available to a single process and lost on crash. Redis is networked (slower than local memory but still very fast), sharable across instances, supports TTL, persistence, and complex data structures. Use in-memory for cheap per-process memoization; use Redis for cross-instance caching, coordination, and larger datasets.

**Q3: How would you prevent a cache stampede?**
**A:** Options include (1) request locking/coalescing so only one request regenerates the cache while others wait or serve stale, (2) use stale-while-revalidate: serve stale value while background refresh occurs, (3) add randomized TTL jitter to avoid synchronized expirations, (4) use probabilistic early recompute (e.g., refresh when remaining TTL < random threshold).

**Q4: When would you use write-through vs write-back vs cache-aside?**
**A:** Write-through writes both cache and DB synchronously—simpler consistency but higher write latency. Write-back writes to cache then asynchronously flushes to DB—faster writes but riskier for durability. Cache-aside gives the application control: reads populate cache lazily; writes go to DB and then invalidate/update cache—good balance and commonly used in web apps.

**Q5: What are the downsides of caching?**
**A:** Complexity (invalidations), stale reads, memory/cost, risk of inconsistencies, operational overhead (monitoring eviction, heat), and potential security concerns if sensitive data is cached incorrectly.


## IV. 💻 Coding / Practical — Most Asked Questions

**P1: Implement cache-aside using Node.js and Redis (pseudo / concise approach)**
- On read request:
  1. Try `GET key` from Redis.
  2. If hit, return parsed value.
  3. If miss, fetch from DB, `SET key value EX ttl`, return value.
- On write/update:
  1. Update DB.
  2. Delete/`DEL key` from Redis or `SET` new value.

**Notes:** handle serialization (JSON), errors (fallback to DB), and TTL choice.

**P2: Preventing cache stampede (approach)**
- Use a lightweight distributed lock per key (Redis `SET key lock ... NX PX ...`) so only one worker regenerates.
- Alternatively implement `stale-while-revalidate`: store `{value, expiresAt, refreshInProgress}`; if expired but present, return stale and start background refresh with lock.

**P3: Choosing TTL values (practical rules)**
- Short TTL for rapidly changing data; long TTL for infrequently changing or expensive-to-compute data.
- Add jitter: `ttl = baseTTL + random(-delta, +delta)` to spread expirations.
- Consider user experience: slightly stale data may be acceptable for speed.

**P4: Example Node.js snippets (conceptual)**
- Use `ioredis` or `redis` client. Keep Redis client as a singleton across the app. Use `JSON.stringify`/`parse` for complex objects. Use `EX` or `PEX` for TTL when setting.

**P5: Caching strategies for paginated queries / lists**
- Avoid caching raw DB pagination offsets. Prefer cursor-based pagination caches or cache canonical resources (by id) and assemble pages from cached IDs. Use small TTLs or cache per-user views carefully.


## V. 🚀 Follow-Up Topics to Learn
1. **Distributed locking & consensus patterns (Redlock):** practical when coordinating cache rebuilds. Learn tradeoffs around safety and correctness.
2. **Cache design for microservices (CQRS + read models):** separating read/write models helps scale caches and prevent invalidation complexity.
3. **Advanced Redis features:** streams, Lua scripting, RedisJSON, Redis modules — powerful for specialized caching or de-normalized data.
4. **Content Delivery Networks (CDNs) & edge caching:** for static assets and API edge caching (e.g., CloudFront, Fastly, Cloudflare Workers).
5. **Observability for caches:** metrics (hit/miss ratio, latency), alerting on sudden miss spikes, and tracing cache impact on end-to-end latency.

---
*Quick tip:* measure before optimizing. A good cache strategy is guided by real metrics: what’s hot, what’s expensive, and acceptable staleness.


# Node.js — Message Queues (RabbitMQ & Kafka) Cheatsheet

**Previewable + Downloadable Link:** Use the canvas preview in the top-right to download or export this document.

---

## I. 💡 Basic Details of Message Queues
**Definition & purpose**
Message queues are middleware systems that allow asynchronous, decoupled communication between services by sending messages to a broker which stores and forwards them to consumers. They improve reliability, scalability, and resilience in distributed systems.

**Brief history & relevance**
Message queuing dates back to early enterprise middleware (JMS, MSMQ) and evolved into modern systems like RabbitMQ (AMQP-based, long history in enterprise) and Kafka (log-based, built for high-throughput streaming). Today they are essential for event-driven architectures, microservices, stream processing, and backpressure handling.

**Where Node.js fits**
Node.js commonly acts as a producer/consumer for I/O-bound workloads: webhooks, background jobs, stream processing. Popular client libraries: `amqplib` / `rhea` (RabbitMQ), `kafkajs` / `node-rdkafka` (Kafka).

---

## II. 🧠 Important Concepts to Remember
1. **Broker vs Client** — *Broker* stores/forwards messages; *Client* produces/consumes. Think of the broker as the post office and clients as mail senders/receivers.
2. **Queue vs Topic (Pub/Sub)** — *Queue* (work queue): one consumer handles a message. *Topic* (pub/sub): multiple subscribers each receive a copy.
3. **Delivery semantics** — *At-least-once*: message may be delivered multiple times (idempotency required). *At-most-once*: message delivered <=1 (possible loss). *Exactly-once*: very hard; typically achieved via idempotence + transactions or deduplication.
4. **Acknowledgements (ACKs)** — Consumer ACKs tell broker a message was processed; NACK/requeue for retries. Unacked messages may be redelivered.
5. **Durability & Persistence** — Durable queues/topics + persistent messages survive broker restarts; ephemeral/in-memory ones do not. Use durability for important work.
6. **Ordering & Partitions** — Kafka preserves order within a partition; RabbitMQ ordering is queue-dependent and can be affected by consumers/acks. When ordering matters, partitioning/keying matters.
7. **Backpressure & Flow control** — Brokers and clients support prefetch/consumer window settings to avoid overwhelming consumers.

---

## III. 📝 Theory — Most Asked Interview Questions (and model answers)

**Q1: What are the main differences between RabbitMQ and Kafka?**
**A:** RabbitMQ is an AMQP-based broker optimized for flexible routing (exchanges, routing keys), lower latency for small messages, and supports complex topologies (direct, fanout, topic, headers). Kafka is a distributed commit log optimized for high-throughput, long-term storage, stream processing and ordered delivery within partitions. Kafka scales via partitions and encourages immutable logs; RabbitMQ focuses on message routing and transient work queues.

**Q2: Explain "at-least-once" vs "exactly-once" semantics and practical ways to approach them.**
**A:** *At-least-once* ensures messages are delivered at least once; duplicates possible — handle with idempotency or dedup keys. *Exactly-once* means consumer side effect occurs once — achievable through transactional producers/consumers with broker support or external deduplication/state stores. In practice, aim for idempotent consumers and dedup keys; use Kafka exactly-once semantics (EOS) features where supported.

**Q3: How do you ensure ordering of messages?**
**A:** Use a single consumer per queue/partition to preserve order. In Kafka, write messages with the same partition key so they go to the same partition. In RabbitMQ, avoid parallel consumers that ACK out-of-order and set prefetch to 1 if strict ordering is required.

**Q4: When would you choose RabbitMQ over Kafka (and vice versa)?**
**A:** Choose RabbitMQ for task queues, RPC-style messaging, flexible routing, and scenarios with varied consumers and complex routing. Choose Kafka for high-throughput event streaming, event sourcing, retaining large amounts of message history, and stream processing use-cases.

**Q5: What is a dead-letter queue (DLQ) and when to use it?**
**A:** A DLQ stores messages that could not be processed after retries (due to poison messages, schema errors, etc.). Use DLQs to separate problematic messages for inspection and prevent blocking normal processing.

---

## IV. 💻 Coding / Practical — Most Asked Questions (with approaches)

**Q1: Implement a reliable worker in Node.js that pulls jobs from RabbitMQ and gracefully handles crashes.**
**Approach:** Use `amqplib`.
- Connect and create a durable queue.
- Use `channel.prefetch(1)` for fair dispatch.
- Consume with `noAck: false`, process job, then `channel.ack(msg)` on success; on failure `channel.nack(msg, false, false)` to drop or `true` to requeue depending on policy.
- On process shutdown, close channel and connection after waiting for current job.

**Q2: Produce and consume events to Kafka with ordering and idempotence.**
**Approach:** Use `kafkajs`.
- Configure a producer with `idempotent: true` (if available) and send messages with the same `key` to ensure ordering to a partition.
- Consumer group reads from partitions; ensure processing is idempotent or use an external transactional sink.

**Q3: Design a retry strategy for failed messages.**
**Approach:** Use exponential backoff with a retry count stored in message headers and DLQ for terminal failures. RabbitMQ supports delayed retries via separate delay/exchange or the `rabbitmq_delayed_message_exchange` plugin. Kafka often uses a retry topic pattern (retry-topic → backoff processor → original-topic) or external scheduler.

**Q4: How to handle schema evolution for messages?**
**Approach:** Use a schema registry (Avro/Protobuf/JSON Schema) to enforce compatibility (backwards/forwards). Kafka integrates well with Confluent Schema Registry; for RabbitMQ adopt versioning in message metadata and write backwards compatible consumers.

**Q5: Implement consumer idempotency with dedup keys.**
**Approach:** Each message includes a unique `messageId`. Consumer checks a durable store (Redis, DB) for that `messageId`. If seen, skip processing; if not, record it atomically and proceed. Use TTL to limit dedup store size depending on retention window.

---

## V. 🚀 Follow-Up Topics to Learn
1. **Event-driven architecture & Event Sourcing** — Good next step to design systems where events are the source of truth; Kafka is a natural fit.
2. **Stream processing (Kafka Streams / ksqlDB / Flink)** — Learn to transform and aggregate streams in-flight for analytics and ETL.
3. **Distributed systems guarantees (exactly-once, transactions, idempotence)** — Deepen understanding of distributed transactions, idempotency patterns, and their tradeoffs.
4. **Observability for message systems** — Monitoring lag, consumer group offsets, broker health, and tracing (OpenTelemetry) is critical for production.
5. **Security & multi-tenant design for brokers** — TLS, SASL, ACLs, and tenant isolation patterns.

---

*Quick reference libraries for Node.js*
- RabbitMQ: `amqplib`, `rhea`, `amqp-connection-manager`
- Kafka: `kafkajs`, `node-rdkafka`, `kafka-node`

---

If you want, I can: provide runnable example code snippets (RabbitMQ worker + Kafka producer/consumer), export this as markdown or PDF, or add a small diagram. The canvas preview in the top-right has download/export options.


# Node.js — APIs & Protocols Cheatsheet

**Previewable + Downloadable Link:** Use the canvas preview in the top-right to download or export this document.

---

## I. 💡 Basic Details of APIs & Protocols
**Definition & purpose**
APIs (Application Programming Interfaces) define how software components talk to each other. Protocols are the rules/standards that carry those messages (HTTP/2, gRPC over HTTP/2, WebSocket). In Node.js, building APIs means designing request/response contracts, choosing serialization formats (JSON, Protobuf), and picking the right transport for constraints (latency, throughput, streaming).

**Brief history & relevance**
REST emerged from HTTP’s ubiquity and simplicity; GraphQL offered flexible client-driven queries and reduced over/under-fetching; gRPC embraced Protobuf and binary streaming for high-performance inter-service RPCs; Webhooks enable event-driven callbacks between systems. Each has tradeoffs in complexity, performance, and operational requirements.

**Where Node.js fits**
Node.js is used widely to implement HTTP servers (Express, Fastify), GraphQL servers (Apollo, graphql-js), gRPC services (`@grpc/grpc-js`), and webhook receivers. Choose Node when you need fast I/O, JSON-first APIs, and an ecosystem of adapters and middleware.

---

## II. 🧠 Important Concepts to Remember
1. **Resources vs RPC** — REST models resources (nouns, stateless), RPC focuses on actions/commands. Use REST for CRUD-like resources; RPC/gRPC for low-latency RPCs and streaming. Analogy: REST is a library catalog; RPC is a phone call asking someone to do something.
2. **Idempotency** — Safe retries require idempotent operations (PUT, idempotency keys for POST). Critical for retries and network failures.
3. **Versioning** — Options: URL versioning (`/v1`), header versioning, content negotiation. Pick a strategy and keep compatibility rules clear.
4. **Error handling & status codes** — Use standard HTTP status codes; for GraphQL, surface errors in the `errors` field and use extensions for codes. For RPC/gRPC, use well-defined status codes (gRPC status codes) and structured error metadata.
5. **Authentication & Authorization** — Common patterns: OAuth2, JWT, API keys. Use HTTPS/TLS, rotate keys, and enforce least privilege.
6. **Schema & Contracts** — OpenAPI/Swagger for REST, GraphQL schema for GraphQL, Protobuf for gRPC. Schema-first design enables validation, client generation, and documentation.
7. **Streaming & Backpressure** — gRPC and HTTP/2 support streaming; GraphQL has subscriptions (WebSocket); Webhooks are push-only and need retry/backoff logic. Handle backpressure with windowing and flow control.

---

## III. 📝 Theory — Most Asked Interview Questions (and model answers)

**Q1: What's the difference between REST and GraphQL?**
**A:** REST exposes multiple endpoints representing resources and relies on server-defined responses; GraphQL exposes a single endpoint where clients specify exactly what fields they need, reducing over/under-fetching. GraphQL adds complexity (query cost, caching challenges) but gives clients flexibility.

**Q2: When should you use gRPC instead of REST?**
**A:** Use gRPC for low-latency RPC calls, binary serialization (Protobuf), bidirectional streaming, or when you need strongly-typed contracts and client/server code generation. REST is better for public HTTP APIs consumed by third-parties and for human-readability.

**Q3: How do you secure webhooks?**
**A:** Validate signatures using a shared secret (HMAC), enforce TLS, rate-limit endpoints, verify payloads, and use replay protection (timestamp + nonce). Treat webhooks as untrusted input and validate strictly.

**Q4: Explain idempotency and how to implement it for POST requests.**
**A:** Idempotency ensures repeated requests have the same effect. For POST, require an `Idempotency-Key` header; store processed key + result server-side and return cached result for retries until TTL expires.

**Q5: How do you handle versioning of APIs with minimal client disruption?**
**A:** Prefer backwards-compatible changes (additive fields) and deprecate fields with clear timelines. Use minor versioning or feature toggles. For breaking changes, use a new version endpoint (`/v2`) while supporting `/v1` during transition.

---

## IV. 💻 Coding / Practical — Most Asked Questions (with approaches)

**Q1: Create a minimal REST API in Node.js with Express and input validation.**
**Approach:**
- Use `express` and `express.json()`.
- Validate request bodies with `ajv` (JSON Schema) or `zod`.
- Return proper HTTP status codes and structured error responses.
- Add middleware for logging, rate-limiting (`express-rate-limit`), and auth.

**Q2: Build a GraphQL server using Apollo Server and schema-first design.**
**Approach:**
- Define schema with SDL, implement resolvers separately.
- Use data loader pattern (`dataloader`) to batch DB calls and avoid N+1 queries.
- Implement depth/complexity limiting and query cost analysis to prevent expensive queries.
- Use persisted queries or persisted documents in production for caching.

**Q3: Implement a gRPC service in Node.js.**
**Approach:**
- Define service and messages in `.proto` files.
- Use `@grpc/grpc-js` and `@grpc/proto-loader` to load protos.
- Generate client code or use dynamic loading; handle unary and streaming RPCs.
- Run gRPC over HTTP/2 and secure with TLS; integrate with service mesh if needed.

**Q4: Reliable webhook receiver implementation.**
**Approach:**
- Verify signature (HMAC) against shared secret.
- Respond `2xx` only after validating the payload; enqueue processing to a background job to avoid timeouts.
- Implement retries with exponential backoff for outgoing webhooks; use idempotency keys to avoid duplicate processing.

**Q5: Caching and performance for GraphQL and REST.**
**Approach:**
- REST: use HTTP caching headers (`ETag`, `Cache-Control`) and CDN for public resources.
- GraphQL: cache at field level using a persisted cache (Redis), or use persisted queries and CDN for query results. Use CDN + edge caching when queries are predictable.

---

## V. 🚀 Follow-Up Topics to Learn
1. **API Gateways & Service Mesh (Envoy, Istio, Kong)** — For routing, auth, rate-limiting, observability at the edge or service level.
2. **OpenAPI and Code Generation** — Generate clients, validators, and mock servers from OpenAPI specs to improve contract reliability.
3. **Advanced gRPC: Streaming Patterns & Load Balancing** — Explore client/server streaming, bidi streaming, and how to scale gRPC across multiple instances.
4. **GraphQL Federation & Schema Stitching** — Decompose monolithic schemas into federated subgraphs for large teams.
5. **Observability for APIs** — Distributed tracing (OpenTelemetry), structured logging, and API metrics (latency, error rates, saturation).

---

*Quick reference libraries for Node.js*
- REST: `express`, `fastify`, `koa`.
- GraphQL: `apollo-server`, `graphql-js`, `graphql-tools`, `dataloader`.
- gRPC: `@grpc/grpc-js`, `@grpc/proto-loader`.
- Webhooks & Security: `crypto` (HMAC), `express-rate-limit`, `helmet`.

---

If you'd like I can now:
- Add runnable example code (Express API + Apollo GraphQL schema + gRPC server).
- Export this as Markdown or PDF.
- Add diagrams (sequence for webhook verification, gRPC streaming flow).

The canvas preview in the top-right has download/export options.

