# Node.js Basics Cheatsheet

## I. Basic Details of Node.js
Node.js is a JavaScript runtime built on the V8 engine, designed for executing JavaScript outside the browser. It uses an event‑driven, non‑blocking I/O model, making it efficient for scalable network applications. Created by Ryan Dahl in 2009, it became popular for backend services, APIs, real‑time apps, and tooling ecosystems.

## II. Important Concepts to Remember

### 1. Node Process Model  
Node runs inside a single OS process. Unlike multithreaded servers, it handles concurrency using an event loop and async I/O.

### 2. Node vs Browser  
Browsers run JS for UI, handle DOM APIs, and sandbox execution.  
Node runs JS for backend logic, provides filesystem, networking APIs, and no DOM.

### 3. Single‑Threaded Event Loop  
Node executes JS on a single thread, while async tasks (I/O) are delegated to underlying system threads via libuv.

### 4. V8 Engine  
V8 is Google’s high‑performance JS engine. It compiles JavaScript into native machine code using just‑in‑time (JIT) compilation.

### 5. libuv  
libuv is a C library providing the event loop, thread pool, filesystem I/O, timers, and cross‑platform abstractions.

### 6. Non‑Blocking I/O  
Node never blocks the thread for I/O. Instead, it registers callbacks/promises that fire when data is ready.

### 7. Module System  
Node originally used CommonJS (`require`), now supports ES Modules (`import`) as well.

## III. Theory Interview Questions

**Q1: Why is Node.js single‑threaded?**  
A: The JS execution environment is single‑threaded for simplicity, but Node achieves concurrency via the event loop and libuv thread pool.

**Q2: What is the event loop?**  
A: A mechanism that processes asynchronous callbacks in phases, allowing Node to perform non‑blocking operations.

**Q3: How is Node different from the browser?**  
A: Browsers provide DOM, window, and UI APIs; Node provides filesystem, networking, buffers, streams, and no DOM.

**Q4: What is libuv?**  
A: A C library giving Node a consistent event loop, thread pool, and async I/O across platforms.

**Q5: What role does the V8 engine play?**  
A: V8 parses, optimizes, and executes JavaScript with JIT compilation.

**Q6: What is non‑blocking I/O?**  
A: Operations return immediately while the actual work is done asynchronously, improving throughput.

## IV. Coding/Practical Interview Problems

**Q1: Demonstrate the event loop ordering.**
```js
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");
```
Explanation: Microtasks (promises) run before timers, so output: A, D, C, B.

**Q2: Read a file asynchronously.**
```js
const fs = require("fs");

fs.readFile("data.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
});
```
Explanation: Delegates to libuv thread pool.

**Q3: Create a simple HTTP server.**
```js
const http = require("http");

http.createServer((req, res) => {
  res.end("Hello!");
}).listen(3000);
```
Explanation: Event‑driven request handling.

**Q4: Demonstrate CommonJS modules.**
```js
// math.js
module.exports.add = (a, b) => a + b;

// app.js
const { add } = require("./math");
console.log(add(2, 3));
```
Explanation: Node’s synchronous module loading for local files.

## V. Follow‑Up Topics to Learn

1. **Node Streams** – Efficient data pipelines and backpressure handling.  
2. **Cluster & Worker Threads** – Scaling Node across cores.  
3. **Async Patterns** – Promises, async/await, event emitters.  
4. **Performance Tuning** – Profiling, memory leaks, V8 optimizations.  
5. **Express/Koa Frameworks** – Building robust backend APIs.


# Node.js — Installation & Versioning Cheatsheet

## I. 💡 Basic Details of Node.js Installation & Versioning
**Definition & purpose**
Node.js is a JavaScript runtime built on Chrome's V8 engine. This cheatsheet covers how to install Node.js, manage multiple Node versions, differences between LTS and Current releases, and the relationship between npm (the package manager) and the Node runtime (core).

**Brief history & relevance**
Node.js emerged in 2009 to run JavaScript on the server. Since then it's become the de facto runtime for backend JavaScript, developer tooling, and build systems. Correct installation and version management is crucial for reproducible builds, compatibility with native modules, and team workflows.


## II. 🧠 Important Concepts to Remember (5–7)
1. **nvm (Node Version Manager)** — a shell tool to install/switch Node versions per-shell or per-directory. Analogy: nvm is like a language wardrobe; pick the Node outfit you need for the job.
2. **System installers vs. version managers** — Installing via OS package managers or installers gives a single global Node; version managers let you have many versions side-by-side.
3. **LTS vs Current (Stable vs Cutting-edge)** — LTS (Long-Term Support) prioritizes stability and bug/security fixes for production; Current contains latest features but may introduce breaking changes. Analogy: LTS = pickup truck you trust for work; Current = sports car for new features and experiments.
4. **npm vs node core** — `node` is the runtime; `npm` is the package manager shipped with Node (but can be updated independently). `npm` installs packages, `node` runs them.
5. **Global vs local packages** — local (per-project) packages live in `node_modules` and are preferred for project reproducibility; globals are for CLI tools you want available everywhere.
6. **Native modules & ABI compatibility** — some packages use native bindings and must be rebuilt when switching Node major versions; keeping consistent Node versions avoids rebuild headaches.
7. **Lockfiles and reproducibility** — `package-lock.json` (npm) pins dependency trees; combine with a fixed Node version (via `.nvmrc` or engines) for deterministic installs.


## III. 📝 Theory — Most Asked Questions (Interview Prep)
**Q1: What is nvm and why use it?**
**A:** `nvm` is a bash/zsh/fish script that installs & switches Node versions per-shell. Use it to test projects across Node versions, match CI versions, and avoid system-level conflicts.

**Q2: Difference between Node LTS and Current? Which to choose?**
**A:** LTS receives maintenance and security updates and is recommended for production. Current contains new features and faster release cadence — use it for trying new APIs or upgrading when you can test dependencies.

**Q3: How does npm relate to Node? Can npm and node have different versions?**
**A:** npm is bundled with Node but can be upgraded separately. `node --version` shows runtime; `npm --version` shows package manager. You can upgrade npm without reinstalling Node.

**Q4: How to ensure all developers use the same Node version?**
**A:** Commit an `.nvmrc` (or `.node-version`) file with the exact version (e.g., `18.17.1`), add CI step to `nvm use`, and optionally add an `engines` field in `package.json` plus an install check script.

**Q5: What problems arise from using OS package managers?**
**A:** OS packages may lag behind, install a single global version, and cause permission issues for global npm packages. Version managers avoid elevated permission problems and support multiple versions.


## IV. 💻 Coding / Practical — Most Asked Questions (Interview Prep)
**P1: How do you install nvm and install Node 18 LTS?**
**Answer / approach:**
1. Install nvm (curl): `curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.6/install.sh | bash` (verify latest nvm release first).
2. Restart shell or source `~/.nvm/nvm.sh`.
3. `nvm install --lts` or `nvm install 18` and then `nvm use 18`.
4. Optionally, `nvm alias default 18` to default to that version.

**P2: How to set project Node version so CI and teammates pick it automatically?**
**Answer / approach:**
- Create `.nvmrc` with the version string (`18` or `18.17.1`).
- Add to README: `nvm use` or use `corepack`/`volta` as alternative.
- Configure CI to read `.nvmrc` (e.g., `nvm install $(cat .nvmrc)` or `setup-node` action).

**P3: Resolving `npm` permission errors when installing global packages**
**Answer / approach:**
- Avoid `sudo npm install -g`.
- Reconfigure npm global folder: `mkdir ~/.npm-global && npm config set prefix '~/.npm-global'` then add `~/.npm-global/bin` to `PATH`.
- Alternatively use nvm or a containerized environment so you never need sudo.

**P4: How to handle native modules after switching Node versions (e.g., `node-gyp` errors)?**
**Answer / approach:**
- Rebuild native modules: `npm rebuild` or remove `node_modules` and reinstall.
- Ensure build toolchain (Python, make, C/C++ compiler) matches required versions.
- Use consistent Node versions between dev, CI, and deployment.

**P5: When to use `n` vs `nvm` vs `volta` vs `asdf`?**
**Answer / approach:**
- `nvm`: shell-based, popular for per-shell switching; works well on macOS/Linux.
- `n`: simple Node version manager; uses sudo sometimes.
- `volta`: fast, per-project pinning, auto-installs version on `package.json`/`volta` config — good for teams and CI.
- `asdf`: multi-language manager with plugins — useful if you already use it for other runtimes.
Choose based on OS, team preferences, and CI integrations.


## V. 🚀 Follow-Up Topics to Learn
1. **Volta** — a modern tool for pinning Node & package managers per-project (zero shell setup and faster). Good next step for team reliability.
2. **Corepack (pnpm / yarn)** — package manager shims that help tie package manager versions to projects.
3. **Native module troubleshooting & `node-gyp`** — deep-dive into binary builds, prebuilds, and ABI compatibility.
4. **Containerizing Node apps (Docker)** — enforce runtime version reproducibility and simplify deployment.
5. **Node release schedule & LTS strategy** — learn Node's release cadence to plan upgrades safely.


---
*Extras included in the document:*
- Quick command clipboard with common nvm/node/npm commands
- Minimal `.nvmrc` + `package.json` `engines` snippet


*End of cheatsheet.*


# Node.js Runtime Environment Cheatsheet

## I.  Basic Details of Node.js Runtime Environment
Node.js provides a JavaScript runtime outside the browser, powered by the V8 engine. Its runtime environment includes APIs for interacting with the OS process, environment variables, command-line arguments, system signals, and exit mechanisms. This makes Node.js suitable for scripting, servers, CLIs, and automation.

## II.  Important Concepts to Remember
**1. `process` Object**  
The global `process` object gives metadata and controls the current Node.js process. You can read info like PID, platform, versions, and resource usage.

**2. Environment Variables (`process.env`)**  
Environment variables configure behavior without changing source code—like telling your app the port or API keys.

**3. Command-Line Arguments (`process.argv`)**  
An array containing the Node.js executable path, script path, and any user‑supplied CLI arguments.

**4. Signals (e.g., `SIGINT`, `SIGTERM`)**  
Signals let the OS notify your running process of events—like Ctrl+C, shutdown requests, or kill commands.

**5. Exit Codes (`process.exitCode`)**  
A process exits with a numeric code. Zero means success; non-zero means failure.

**6. Event-driven Lifecycle**  
The Node.js runtime stays alive while there are pending tasks or event listeners. Signals and exit codes interact with this lifecycle.

**7. Process Streams**  
`process.stdin`, `stdout`, and `stderr` are standard I/O streams commonly used in CLI tools.

## III.  Theory Most Asked Questions (Interview Prep)
**1. What is the `process` object in Node.js?**  
It’s a global object providing control and information about the currently running Node.js process.

**2. Why do we use environment variables?**  
To configure applications without embedding sensitive or environment‑specific values in code.

**3. What does `process.argv` contain?**  
An array where index 0 is Node path, index 1 is script path, and the rest are user arguments.

**4. What are signals in Node.js?**  
Notifications from the OS to the process—like `SIGINT` for keyboard interrupt or `SIGTERM` for graceful shutdown.

**5. What is exit code 0 vs non-zero?**  
0 indicates successful execution; non‑zero indicates some error or custom exit state.

**6. How does Node.js handle process termination?**  
It exits when the event loop is empty or when explicitly told to exit via signals or `process.exit()`.

## IV.  Coding/Practical Most Asked Questions
**1. Read command- line arguments**  
```js
console.log(process.argv.slice(2));
```
Extracts only user arguments.

**2. Access environment variables**  
```js
console.log(process.env.NODE_ENV);
```
Used for configuration.

**3. Graceful shutdown on `SIGINT`**  
```js
process.on('SIGINT', () => {
  console.log('Cleaning up...');
  process.exit(0);
});
```
Allows cleanup before process termination.

**4. Setting exit code without terminating**  
```js
process.exitCode = 1;
```
Indicates failure after current tasks finish.

**5. Using `stdin` and `stdout`**  
```js
process.stdin.on('data', d => {
  process.stdout.write(`Echo: ${d}`);
});
```
Basic CLI interaction.

## V.  Follow-Up Topics to Learn
**1. Node.js Event Loop** — Understanding how tasks, microtasks, and I/O scheduling affect process lifetime.

**2. Child Processes** — Enables running external commands, spawning workers, and scaling apps.

**3. Cluster Module** — Helps utilize multi-core systems for Node.js servers.

**4. Node.js Streams** — Efficient data processing with backpressure handling.

**5. OS Module (`os`)** — Provides system-level details to complement process metadata.


# Node.js Modules — Cheatsheet Interview

> **Previewable + Downloadable Link in the top right corner.**

---

## I. 💡 Basic Details of Node.js Modules

**Definition & purpose**
Node.js modules are the building blocks for organizing JavaScript code into reusable, encapsulated units. Modules expose interfaces (functions/objects) that other modules can import. They help manage scope, dependencies, and reuse across applications.

**History & relevance**
- **CommonJS** (CJS) emerged early in Node.js to provide a synchronous `require()`-based module system suited to server-side I/O.
- **ES Modules** (ESM) are the standardized JavaScript module system introduced to browsers and later adopted by Node.js to unify module syntax across environments using `import`/`export`.
- Today both systems coexist; understanding interoperability, resolution, and `package.json` `type` is essential for modern full-stack and backend engineering.

---

## II. 🧠 Important Concepts to Remember (5–7)

1. **CommonJS vs ES Modules — Syntax & semantics**
   - CJS: `const x = require('x')`, `module.exports = value`. Synchronous and uses a module wrapper. Evaluated on first `require` and cached.
   - ESM: `import x from 'x'`, `export default value` / `export const y`. Static structure (imports are statically analyzable), supports top-level `await`, and has live bindings for named exports.
   - *Analogy*: CJS is a handwritten letter you open when you call `require`; ESM is a blueprint that a build tool can inspect before construction.

2. **Module resolution algorithm**
   - Node resolves specifiers (relative `./foo`, absolute `/abs`, or package names like `express`) using a defined algorithm: file lookup (.js, .json, .node), package `exports`/`main`, `node_modules` traversal up the directory tree, and folder `index` resolution.
   - `exports` and `imports` fields in `package.json` can override resolution and create safer package boundaries.

3. **`package.json` `type` field**
   - `"type": "module"` treats `.js` files as ESM by default; `"type": "commonjs"` (or absent) treats `.js` as CommonJS. Use `.mjs`/`.cjs` extensions to force module interpretation when needed.

4. **Interoperability pitfalls**
   - Default export vs `module.exports`: CJS modules export a single value that becomes the `default` when importing from ESM only in certain interop behaviors. Named exports from ESM are not automatically available as CJS named properties.
   - Synchronous `require` vs asynchronous ESM loading and top-level `await` — runtime behavior differs.

5. **Caching & singletons**
   - Modules are cached on first load. Requiring/importing the same module yields the same instance (useful for singletons, but watch mutation side-effects).

6. **Conditional exports & subpath exports**
   - `exports` in `package.json` can expose specific entry points depending on environment (`node`, `import`, `require`) and disallow deep imports. This helps package authors maintain stable public APIs.

7. **Native addons & `.node`**
   - Native binaries use the `.node` extension and are loaded via the same resolution algorithm; they require build steps and ABI compatibility consideration.

---

## III. 📝 Theory — Most Asked Questions (Interview Prep)

### Q1: What are the main differences between CommonJS and ES Modules?
**Model answer (concise):**
CommonJS uses synchronous `require()` calls and `module.exports` to export values; it's dynamic and evaluated at runtime. ES Modules use `import`/`export` with static structure enabling tree-shaking and compile-time analysis, supports top-level `await`, and has live bindings for named exports. Node.js supports both with differences in file extension handling and loader behavior.

### Q2: How does Node.js resolve `require('pkg')` or `import pkg from 'pkg'`?
**Model answer (concise):**
Node uses a resolution algorithm: if specifier is relative/absolute, it resolves to a file by trying extensions and index files; for bare specifiers it searches `node_modules` in the current directory and then parent directories up to the filesystem root. `package.json` `exports` and `main` fields can control which file is exposed.

### Q3: What effect does `"type": "module"` in `package.json` have?
**Model answer (concise):**
It makes `.js` files be parsed as ESM by default within that package. To force CJS in this mode use `.cjs`. Conversely, without it (or with `"type":"commonjs"`), `.js` is CommonJS and `.mjs` is ESM.

### Q4: How to import a CommonJS module from an ES Module and vice versa?
**Model answer (concise):**
- From ESM -> CJS: `import pkg from './cjs-module.cjs'` may yield a namespace where `pkg.default` is the CJS `module.exports`. Alternatively use `createRequire` from `module` to `require()` inside ESM.
- From CJS -> ESM: Use dynamic `import()` which returns a promise resolving to the ESM namespace. Direct `require()` of ESM is not supported.

### Q5: What are `exports` and `imports` fields in `package.json` used for?
**Model answer (concise):**
They define precise entry points and subpath mappings for package consumers. `exports` restricts and maps package subpaths and can provide different files for `require` vs `import`. `imports` allows internal aliasing within a package.

---

## IV. 💻 Coding / Practical — Most Asked Questions (Interview Prep)

### P1: Convert a small project from CommonJS to ESM. What changes are needed?
**Optimal approach:**
- Add `"type": "module"` to `package.json` or rename files to `.mjs`/`.cjs` when mixing.
- Replace `require()`/`module.exports` with `import`/`export` (or use `export default` / named exports).
- Update dynamic `require()` usage to dynamic `import()` or `createRequire` when necessary.
- Update tooling (Babel, Jest, bundlers) configuration to support ESM (or use interop shims).

### P2: How to import JSON or CommonJS-style configs in ESM?
**Optimal approach:**
- For JSON: Node supports `import config from './config.json'` behind a flag in older Node; in modern Node you can `import` JSON using the `assert { type: 'json' }` syntax: `import cfg from './config.json' assert { type: 'json' }` (supported in current Node versions). Alternatively use `fs.readFile` or `createRequire`.
- For CJS configs: use `createRequire(import.meta.url)` then `const cfg = require('./cjs-config.js')`.

### P3: Troubleshoot `ERR_MODULE_NOT_FOUND` when importing a package
**Optimal approach:**
- Check if path is correct (relative vs bare). Ensure extension or directory index exists.
- If using ESM, ensure package `exports` maps the requested subpath; try the package's documented entrypoint.
- Inspect `package.json` `type` and file extensions. Use `node --trace-resolve` for debugging.

### P4: Implement a small plugin architecture where plugins are loaded at runtime (mix of ESM/CJS)
**Optimal approach:**
- Use dynamic `import()` to load ESM plugins (async). For CJS plugins, in ESM host use `createRequire` to `require()` them.
- Define a standard plugin interface (e.g., export `setup(app)` or default export) and validate at load time.
- Consider isolating plugins in child processes if you need process-level isolation.

---

## V. 🚀 Follow-Up Topics to Learn

1. **Bundlers & Tree-shaking (esbuild, Rollup, Webpack)**
   - Why: ESM static structure enables tree-shaking; learn how bundlers treat modules, polyfills, and interop.

2. **Node.js Loader Hooks & Custom Loaders**
   - Why: Understand how to customize ESM resolution, transform code at load-time (useful for transpilers, TypeScript runtime support).

3. **Package Exports, Conditional Exports & Distribution Best-Practices**
   - Why: Writing robust public packages requires understanding `exports`, `types`, `module`, and how to provide both ESM and CJS consumers.

4. **Native Addons (N-API) & Binary Modules**
   - Why: Learn how native extensions are packaged and resolved, and the compatibility concerns across Node versions.

5. **Monorepos & Workspaces (pnpm, Yarn, npm workspaces)**
   - Why: Large projects often mix module formats across packages; workspace tooling affects resolution and hoisting.

---

## Quick Reference (cheat-sheet)
- **CJS:** `require()`, `module.exports` — synchronous, `.cjs`/`.js` (default)
- **ESM:** `import`/`export` — static, supports top-level `await`, `.mjs`/`.js` (with `type: "module"`)
- **File ext tips:** Use `.mjs` to force ESM, `.cjs` to force CJS.
- **Interop:** Use `createRequire(import.meta.url)` in ESM, and dynamic `import()` in CJS.
- **Package fields:** `main` (legacy), `exports` (modern entry points), `type` (module interpretation).

---

_End of cheatsheet._


# Node.js Package Management — Cheatsheet

## I. 💡 Basic Details of Node.js Package Management
**Definition & purpose**
Package management in Node.js is the system that handles installing, updating, configuring, and distributing JavaScript libraries (packages) and apps. It ensures reproducible builds, dependency resolution, and version control for project dependencies.

**Brief history & relevance**
- **npm** launched in 2010 as the default registry+CLI for Node.js and quickly became the de facto ecosystem.
- **Yarn** (2016) introduced faster installs and deterministic installs via its lockfile, responding to npm pain points at the time.
- **pnpm** (2016+) focused on disk efficiency and strict node_modules layout using hard links and a global store.

Today package management is essential for developer productivity, security (vulnerability scanning), reproducibility (lockfiles), monorepo tooling, and multi-registry enterprise workflows.

---

## II. 🧠 Important Concepts to Remember
1. **package.json (manifest)**
   - The authoritative metadata file for a Node project. Contains `name`, `version`, `main`, `scripts`, `dependencies`, `devDependencies`, `peerDependencies`, `optionalDependencies`, `engines`, and `license`.
   - Analogy: package.json is the recipe card that tells the package manager what ingredients (dependencies) and steps (scripts) the project needs.

2. **Semantic Versioning (semver)**
   - Format: `MAJOR.MINOR.PATCH` (e.g., `2.4.1`).
   - Rules: increment MAJOR for breaking changes, MINOR for backward-compatible features, PATCH for bug fixes.
   - Ranges: `^1.2.3` (caret) allows non-breaking updates; `~1.2.3` (tilde) allows patch updates; `1.2.3` pins exact.
   - Analogy: semver is a promise label on packages — how much the author promises not to break.

3. **Lockfiles (package-lock.json / yarn.lock / pnpm-lock.yaml)**
   - Capture the *exact* dependency tree (including transitive deps) used when installing.
   - Ensure repeatable installs across machines and CI.
   - Commit lockfiles to VCS for apps; libraries typically do not commit lockfiles.

4. **Shrinkwrap vs Lockfiles**
   - `npm shrinkwrap` produces `npm-shrinkwrap.json` and is similar to `package-lock.json` but intended for published packages to lock down production installs.
   - Today `package-lock.json` is the default for npm; shrinkwrap still exists for explicit locking of published packages.

5. **Different package managers**
   - **npm**: default, broadest compatibility, continuously improved (lockfile, workspaces).
   - **Yarn**: originally faster and deterministic; Yarn v2+ (berry) introduced plugin architecture and slightly different workflows.
   - **pnpm**: enforces a strict node_modules structure, uses a global content-addressable store to save disk space and speed installs.
   - Choice depends on team, monorepo needs, disk/CI constraints, and tooling compatibility.

6. **Private registries & scopes**
   - Companies use private npm registries (e.g., Nexus, Artifactory, GitHub Packages, npm Enterprise) to host internal packages.
   - Scoped packages (`@org/name`) make it easy to separate and control access.

7. **Dependency types & semantics**
   - `dependencies`: required at runtime (production).
   - `devDependencies`: only needed for development (tests, build tools).
   - `peerDependencies`: used by plugins that expect the host project to provide a dependency (e.g., React plugins stating React as a peer dep).
   - `optionalDependencies`: failures to install are tolerated — used for OS-specific or non-critical packages.

---

## III. 📝 Theory — Most Asked Questions (Interview Prep)
**Q1: What does `npm install --save-dev` do?**
**A:** Adds a package to `devDependencies` in package.json and installs it locally. Used for build tools, test runners, and other development-only dependencies.

**Q2: Explain semantic versioning and how `^` and `~` differ.**
**A:** Semver is MAJOR.MINOR.PATCH. `^1.2.3` allows updates that don’t change MAJOR (e.g., `1.x.x`), enabling MINOR and PATCH updates. `~1.2.3` allows patch updates only (e.g., `1.2.x`).

**Q3: Why commit a lockfile?**
**A:** To ensure deterministic installs across environments/CI by freezing the complete dependency tree, preventing unexpected differences caused by transitive updates.

**Q4: When should you use peerDependencies?**
**A:** For plugins or libraries that depend on a host framework provided by the app (e.g., a React component library should declare React as a peerDependency to avoid duplicate React copies).

**Q5: What problems does pnpm solve compared to npm?**
**A:** pnpm saves disk space with a global content-addressable store and enforces a strict node_modules layout that avoids phantom dependencies and improves determinism.

---

## IV. 💻 Coding / Practical — Most Asked Questions (Interview Prep)
**Q1: How to create a minimal package.json and publish a package?**
- `npm init -y` → edit `package.json` (name, version, main, license)
- `npm publish` (ensure unique name or use scope/private registry)
- For scoped public packages, use `npm publish --access public`.

**Q2: Convert npm project to use pnpm**
- Install pnpm globally: `npm install -g pnpm`
- Run `pnpm import` to generate `pnpm-lock.yaml` from existing lockfile
- Use `pnpm install` moving forward; update CI to call `pnpm install`.

**Q3: Add a workspace/monorepo with npm/pnpm**
- `package.json` (root) sample for workspaces:
```json
{"name":"monorepo","private":true,"workspaces":["packages/*"]}
```
- Put packages under `packages/` with their own package.json; use `pnpm` or npm workspaces for hoisting

**Q4: Resolve a dependency conflict between two packages requiring different versions**
- Try upgrading/downgrading the direct dependency to a compatible version
- Use resolutions (Yarn) or overrides (npm v8+, pnpm) to force a single version
- Consider isolating via separate packages or plugins if incompatible

**Q5: Lockfile CI strategy**
- Always run installs from lockfile in CI (e.g., `npm ci` for npm)
- Fail the build if lockfile & package.json drift (verify `npm ci` exit code)

---

## V. 🚀 Follow-Up Topics to Learn
1. **Monorepo tooling & patterns (Nx, Turborepo, pnpm workspaces)** — scales packages and build/test caching.
2. **Supply-chain security for JS (Snyk, npm audit, Dependabot, sigstore)** — protects from vulnerabilities and supply-chain attacks.
3. **Module formats & interoperability (CommonJS vs ESM)** — affects packaging, exports, and bundling strategies.
4. **Advanced npm features: overrides, package exports, conditional exports** — useful for compatibility and tree-shaking.
5. **Publishing pipelines & private registries (GitHub Packages, Verdaccio, Artifactory)** — enterprise package governance and automation.

---

*Cheatsheet created for quick interview prep and practical reference. Tweak examples to match your team’s package manager and CI workflows.*

# Node.js Event Loop — Detailed Cheatsheet

**Previewable + Downloadable Link:** (Use the top-right preview / download controls in this canvas.)

---

## I. 💡 Basic Details of Node.js Event Loop

**Definition & Purpose**
The Node.js Event Loop is a single-threaded loop that schedules and dispatches asynchronous operations. It allows Node.js to handle I/O-bound concurrency efficiently by delegating work (I/O, timers, callbacks) and processing completion events in phases.

**History & Relevance**
Built on libuv, the event loop abstracted cross-platform asynchronous I/O for Node.js. Understanding it is essential for writing correct, high-performance Node apps and for debugging subtle timing and concurrency bugs.

---

## II. 🧠 Important Concepts to Remember (5–7 core concepts)

1. **Phases of the Event Loop (high level)**
   - The loop repeatedly cycles through well-defined phases: **timers**, **pending callbacks**, **idle/prepare**, **poll**, **check**, and **close**. Each phase has a FIFO queue of callbacks.
   - Analogy: imagine a round-robin arena where each gate (phase) opens in turn and lets queued players (callbacks) through.

2. **Timers phase (setTimeout / setInterval)**
   - Timers callbacks are scheduled after their threshold has elapsed _and_ when the loop enters the timers phase. Timers are *not* exact — they are earliest-possible times, subject to scheduling.
   - Short delays (0 ms) still wait until the next timers phase.

3. **Poll phase**
   - The poll phase retrieves new I/O events and executes their callbacks. If the poll queue is empty, the loop may block waiting for I/O or proceed to the `check` phase depending on timers and other conditions.
   - This is the phase where most I/O callbacks run.

4. **check phase (setImmediate)**
   - `setImmediate` callbacks run in the `check` phase, which happens after the poll phase completes. `setImmediate` is useful for running code after I/O callbacks in the same tick.

5. **Microtasks vs Macrotasks**
   - **Microtasks**: Promise `.then()` callbacks, `process.nextTick()`. They run *immediately after the current JavaScript stack finishes*, before the event loop continues to the next phase.
   - **Macrotasks**: timers, I/O callbacks, `setImmediate`, etc. They are scheduled in event loop phases.
   - Key rule: microtasks always drain fully before the event loop proceeds; `process.nextTick()` is even prioritized above Promise microtasks.

6. **Starvation & Priority traps**
   - Excessive microtasks (or tight `process.nextTick()` loops) can starve the event loop — macrotasks (I/O, timers) get delayed. This can freeze I/O and timers.

7. **Timers semantics & clock drift**
   - Node uses system timers; delays can be longer due to blocking JS, heavy CPU, or OS scheduling. `setInterval` can accumulate drift; prefer recursive `setTimeout` when you need stable spacing.

---

## III. 📝 Theory — Most Asked Questions (Interview Prep)

**Q1 — Explain the phases of the Node.js event loop and where timers, I/O, setImmediate, and close callbacks run.**
**Model answer (concise):** The loop cycles through: `timers` (expired `setTimeout`/`setInterval`), `pending callbacks` (some system callbacks), `idle/prepare` (internal), `poll` (retrieves I/O events and runs callbacks), `check` (runs `setImmediate` callbacks), and `close` (e.g., socket `close` events). Microtasks (Promises, `process.nextTick`) drain between ticks and before moving to the next phase.

**Q2 — What’s the difference between `setImmediate` and `setTimeout(fn, 0)`?**
**Model answer:** `setTimeout(fn, 0)` schedules `fn` in the timers phase after a minimum delay; `setImmediate(fn)` schedules `fn` in the check phase, which runs after the current poll phase. `setImmediate` is generally more predictable after I/O.

**Q3 — Where do Promise callbacks run relative to the event loop?**
**Model answer:** Promise `.then`/`.catch` handlers are microtasks that run right after the current call stack clears, before the event loop moves to the next phase. `process.nextTick()` runs even before Promise microtasks.

**Q4 — How can microtasks cause starvation?**
**Model answer:** If microtasks repeatedly schedule more microtasks (`process.nextTick()` or chained Promises`), the microtask queue never empties, preventing the event loop from moving on to macrotasks — delaying I/O and timers.

**Q5 — Why might a `setTimeout(fn, 1000)` fire significantly later than 1s?**
**Model answer:** Because timers are scheduled to run in the timers phase and are delayed by CPU-bound JS, blocking operations, long-running callbacks, or system scheduling; timers provide a minimum delay, not an exact guarantee.

---

## IV. 💻 Coding / Practical — Most Asked Questions (Interview Prep)

### Practical question 1 — Predict the output ordering
**Q:** What is the order of logs for this snippet?

```js
console.log('start');
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));
Promise.resolve().then(() => console.log('promise'));
process.nextTick(() => console.log('nextTick'));
console.log('end');
```

**Optimal approach / answer (explain):** Execution order: `start`, `end`, `nextTick`, `promise`, and then either `timeout` or `immediate` depends on environment timing — after an I/O cycle `setImmediate` typically runs before `setTimeout(0)`, but ordering between them is not strictly guaranteed. In a plain script `setTimeout(0)` may run before `setImmediate` because timers phase can run first.

---

### Practical question 2 — Avoiding timer drift
**Q:** How to implement a recurring task that minimizes drift?

**Approach:** Use recursive `setTimeout` which measures the next run time relative to the intended schedule, or compute drift compensation by subtracting elapsed time and scheduling the next `setTimeout` accordingly. Avoid `setInterval` for precise scheduling.

---

### Practical question 3 — Demonstrate starvation and fix it
**Q:** Show how `process.nextTick()` can starve the loop and how to fix it.

**Approach/Answer:** A loop using `process.nextTick()` that re-queues itself will prevent the event loop from running I/O. Fix by using `setImmediate()` or `setTimeout` to yield to the event loop, or limit `process.nextTick()` usage.

---

### Practical question 4 — When to use `setImmediate` vs `setTimeout` vs `process.nextTick` vs Promises
**Quick guidance:**
- Use `process.nextTick()` for micro-queueing something that must run immediately after the current call stack (careful — can starve). 
- Use Promise microtasks for asynchronous continuation semantics. 
- Use `setImmediate()` to run after I/O callbacks in the same tick. 
- Use `setTimeout(..., 0)` if you want to schedule on the timers phase (not time-critical).

---

## V. 🚀 Follow-Up Topics to Learn

1. **libuv internals** — learn how libuv implements the loop, handles threadpool and platform differences. (Why: deepens understanding of cross-platform behavior and perf.)
2. **Worker Threads & cluster** — moving CPU-bound work off the event loop. (Why: prevents blocking the loop.)
3. **Streams & backpressure** — patterns for efficient I/O handling and preventing memory blowups. (Why: real-world I/O performance.)
4. **Observability & diagnosing event-loop lag** — using `clinic`, `0x`, `perf_hooks` (`monitorEventLoopDelay`) to profile delays. (Why: practical debugging of latency.)
5. **Concurrency patterns in Node (async iterators, queues)** — design patterns to coordinate async work safely. (Why: production-ready concurrency control.)

---

### Appendix: Quick cheat reminders
- `process.nextTick()` > Promise microtasks > macrotasks (timers, I/O, setImmediate).
- `setImmediate()` runs in `check` phase; `setTimeout(..., 0)` runs in `timers` phase.
- Avoid busy microtask loops; yield periodically via `setImmediate`.

---

*End of cheatsheet.*

(You can preview or download this document using the canvas controls in the top-right. If you want this exported to markdown, PDF, or a code-friendly variant, tell me which format and I'll produce it.)

# Node.js — Async Patterns (Callbacks, Promises, async/await, error propagation)

> **Previewable + Downloadable Link:** Use the top-right corner of this canvas to preview or download the cheatsheet.

---

## I. 💡 Basic Details of Node.js Async Patterns
**What it is (concise):** Asynchronous patterns in Node.js are the techniques and language features used to handle operations that take time (I/O, timers, network, file system) without blocking the single-threaded JavaScript runtime.

**Purpose & relevance:** Keep the event loop responsive while performing long-running tasks. Proper async patterns improve performance, reliability, and developer ergonomics in servers, CLIs, and tools.

**A short history:** Node originally used callbacks (error-first callbacks) because JavaScript had no built-in concurrency primitives. Promises were standardized (ES6/ES2015) to improve composability. `async`/`await` (ES2017) added syntactic sugar for promises, making asynchronous flows look synchronous and easier to reason about.

---

## II. 🧠 Important Concepts to Remember
1. **Event loop, call stack, task queues**
   *Analogy:* Think of the event loop as a dispatcher at a busy post office: the call stack is the active worker, tasks (timers, I/O callbacks) are packages waiting in queues. The dispatcher picks the next package when the worker is free.

2. **Macro‑tasks vs Micro‑tasks**
   - Macro‑tasks: timers, I/O callbacks, setImmediate, setTimeout.
   - Micro‑tasks: Promise `.then`/`.catch`/`.finally` callbacks and `process.nextTick` (Node-specific). Micro‑tasks run *between* macrotasks and can starve macrotasks if abused.

3. **Error‑first callbacks pattern (`(err, result) => {}`)**
   - Convention used by core Node APIs. Always check `err` first. Mistakes: forgetting to return after calling callback, or double-calling it.

4. **Promises — composition over inversion**
   - Promises represent a future value and support chaining and error bubbling. Use them to compose async flows instead of deeply nested callbacks.

5. **`async` / `await` — syntactic clarity**
   - `await` unwraps promises and lets you write linear code. Always `try/catch` around awaits when you need to handle errors.

6. **Error propagation and handling strategies**
   - Errors can be handled locally, bubbled up, or converted into domain errors. Always handle edge cases for uncaught rejections (`'unhandledRejection'`) and uncaught exceptions.

7. **Cancellation & backpressure**
   - Promises don't have built-in cancellation. Use AbortController, streams, or libraries that support cancellation for long-running ops. For heavy I/O, use streams to apply backpressure.

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: What's the difference between callbacks, promises, and async/await?**
**Answer (concise):** Callbacks pass a function to execute later; they can cause nested code (callback hell). Promises represent eventual results and support chaining and error propagation. `async`/`await` is syntax on top of promises giving linear, try/catch-compatible code.

**Q2: What are microtasks and why do they matter?**
**Answer:** Microtasks (Promise reactions, `process.nextTick`) run immediately after the current task finishes and *before* the next macrotask. They matter because heavy microtask chains can delay timers and I/O handlers.

**Q3: How does error propagation differ between callbacks and promises?**
**Answer:** With callbacks, errors must be explicitly passed to the callback (error-first). With promises, throwing or rejecting inside a `.then` automatically rejects the promise and can be caught downstream with `.catch` or `try/catch` for `await`.

**Q4: How do you prevent callback hell?**
**Answer:** Modularize callbacks into named functions, use Promises to flatten chains, or use `async`/`await`. Also use control-flow helpers (e.g., `Promise.all`, `p-map`) for concurrency management.

**Q5: When would you use `Promise.allSettled` vs `Promise.all`?**
**Answer:** Use `Promise.all` when you need all promises to succeed (it rejects on the first rejection). Use `Promise.allSettled` when you want results for every promise regardless of rejection.

**Q6: How to handle long-running CPU-bound tasks in Node?**
**Answer:** Offload to worker threads (or external services) to avoid blocking the event loop. For streaming I/O, use Node streams that apply backpressure.

---

## IV. 💻 Coding / Practical — Most Asked Questions (with approaches & snippets)

### 1) Convert an error‑first callback to a Promise
**Why:** Makes APIs composable.

```js
// callback-style
function readFileCb(path, cb) {
  fs.readFile(path, 'utf8', cb); // cb(err, data)
}

// promisified
const { promisify } = require('util');
const readFile = promisify(fs.readFile);

// usage with async/await
async function load() {
  try {
    const text = await readFile('./file.txt', 'utf8');
    console.log(text);
  } catch (err) {
    console.error('failed:', err);
  }
}
```

### 2) Run concurrent tasks with limited concurrency
**Question:** How to run 100 async tasks but only 10 at a time.
**Approach:** Use a concurrency pool (manual queue, `p-limit` library, or `Promise.all` on batches).

_Pattern (simple batch example):_
```js
async function runInBatches(tasks, batchSize = 10) {
  for (let i = 0; i < tasks.length; i += batchSize) {
    const batch = tasks.slice(i, i + batchSize).map(t => t());
    await Promise.all(batch);
  }
}
```

### 3) Retry with exponential backoff
**Approach:** Wrap the operation in a loop with delay doubling and jitter.

```js
async function retry(fn, retries = 5) {
  let attempt = 0;
  while (true) {
    try { return await fn(); }
    catch (err) {
      if (++attempt > retries) throw err;
      const delay = Math.pow(2, attempt) * 100 + Math.random() * 100;
      await new Promise(r => setTimeout(r, delay));
    }
  }
}
```

### 4) Avoiding unhandled rejections
**Approach:** Always return/await promises and add a global handler in apps for visibility.

```js
process.on('unhandledRejection', (reason, promise) => {
  console.error('unhandledRejection', reason);
  // decide: log, alert, or shut down gracefully
});
```

### 5) Proper error handling with async/await
**Pattern:** Use `try/catch` inside the async function when you need to handle; otherwise let errors bubble and handle them at a higher level.

```js
async function handler(req, res) {
  try {
    const user = await getUser(req.params.id);
    res.send(user);
  } catch (err) {
    res.status(500).send({ error: err.message });
  }
}
```

### 6) Using streams to handle large data and apply backpressure
**Why:** Streams process data piece-by-piece and avoid loading entire payloads into memory.

_Basic pipeline:_
```js
const fs = require('fs');
const zlib = require('zlib');

fs.createReadStream('big.log')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('big.log.gz'))
  .on('finish', () => console.log('done'));
```

---

## V. 🚀 Follow-Up Topics to Learn
1. **Node Streams (advanced)** — essential for efficient I/O and backpressure.
2. **Worker Threads & Child Processes** — for CPU-bound concurrency and isolation.
3. **AbortController & Cancellation patterns** — modern cancellation techniques for fetch/IO and long tasks.
4. **Concurrency control libraries (p-limit, p-map, bottleneck)** — for production-grade concurrency strategies.
5. **Reactive programming (RxJS)** — when you need rich event composition and cancellation semantics.

---

### Quick reference (cheat lines):
- `process.nextTick()` & `Promise.then()` run before next macrotask.
- `Promise.all` rejects fast, `Promise.allSettled` returns everything.
- `async` functions always return a Promise.
- Use `util.promisify()` to wrap node style callbacks.

---

*Created for quick interview prep and practical use. Tweak examples for your Node version and coding style.*

# Node.js Streams — Cheatsheet

> **Previewable + Downloadable Link:** Use the document viewer controls in the top-right of this page to preview or download this cheatsheet.

---

## I. 💡 Basic Details of Node.js Streams

**Definition & purpose**
Node.js Streams are abstract interfaces for working with streaming data — reading from a source or writing to a destination in a continuous, incremental fashion instead of loading the entire dataset into memory. They allow processing of large data efficiently (e.g., files, network sockets, process stdio) and enable composition (piping/transforms).

**Brief history & relevance**
Streams were introduced in Node.js early on to address I/O-bound workloads and memory constraints for server-side JavaScript. They remain central in modern Node apps for file processing, HTTP request/response handling, real-time systems, CLI utilities, and large-data ETL.

**When to use**
- Large files or datasets (avoid buffering whole file).
- Low-latency processing (process chunks as they arrive).
- Composable pipelines (pipe read → transform → write).
- Backpressure-sensitive systems (prevent producer overwhelm).

---

## II. 🧠 Important Concepts to Remember (5–7 core concepts)

1. **Stream types**
   - **Readable**: emits data (e.g., `fs.createReadStream`).
   - **Writable**: accepts data to write (e.g., `fs.createWriteStream`).
   - **Duplex**: both readable and writable (e.g., sockets).
   - **Transform**: duplex that modifies data passing through (e.g., gzip).

   *Analogy*: Think of pipes in plumbing — read = faucet, write = drain, duplex = bidirectional pipe, transform = filter inside the pipe.

2. **Modes: flowing vs paused**
   - *Flowing*: data is read automatically and emitted via `'data'` events.
   - *Paused*: data is read only when `.read()` is called or when a consumer pulls it.

   *Tip*: `stream.on('data', ...)` switches to flowing mode.

3. **Backpressure**
   - Mechanism for preventing a fast producer from overwhelming a slow consumer.
   - For `Writable`, `stream.write(chunk)` returns `false` when internal buffer is full — producer should stop and wait for `'drain'`.

   *Analogy*: A conveyor belt where workers slow down when the next station is full.

4. **Piping & chaining**
   - `readable.pipe(writable)` connects streams and manages backpressure automatically.
   - You can chain transforms: `rs.pipe(transform1).pipe(transform2).pipe(ws)`.

5. **Encoding & objectMode**
   - By default streams handle `Buffer`/string chunks. `setEncoding()` converts to strings. `objectMode: true` allows arbitrary JS objects as chunks (useful for streams of records).

6. **HighWaterMark & buffering**
   - `highWaterMark` controls internal buffer size (bytes for binary streams, number of objects in `objectMode`). Tuning it affects latency and memory use.

7. **Error handling & cleanup**
   - Always handle `'error'` on each stream; use `stream.pipeline()` (Node 10+) for safer composition and automatic cleanup.

---

## III. 📝 Theory Most Asked Questions (Interview Prep)

**Q1: What are Node.js stream types and when to use each?**
**Answer:** Readable for data sources (files, HTTP responses), Writable for sinks (files, HTTP requests), Duplex for bidirectional channels (sockets), Transform for data modification (compression, encryption). Use Transform when you need on-the-fly processing without buffering entire payload.

**Q2: How does backpressure work in Node streams?**
**Answer:** When a writable stream’s internal buffer reaches `highWaterMark`, `write()` returns `false`. Producers should pause writing and listen for `'drain'` to resume. `.pipe()` automatically manages this for you.

**Q3: Difference between piping and manually handling 'data' events?**
**Answer:** `.pipe()` connects streams and manages flow/backpressure automatically. Using `'data'` often forces flowing mode and requires manual pause/resume/backpressure handling.

**Q4: What is objectMode and when is it useful?**
**Answer:** `objectMode: true` allows streams to transport JavaScript objects (one per chunk) instead of buffers/strings. Useful for streaming parsed records or messages.

**Q5: How does `stream.pipeline()` help compared to manual pipe chaining?**
**Answer:** `pipeline()` handles errors across all streams, ensures proper cleanup (closing streams), and returns a callback/promise on completion or failure.

---

## IV. 💻 Coding / Practical Most Asked Questions (Interview Prep)

**Q1: Copy a large file without buffering whole file — show code**
**Approach:** Use `fs.createReadStream()` piped to `fs.createWriteStream()`.

```js
const fs = require('fs');
const rs = fs.createReadStream('big.iso');
const ws = fs.createWriteStream('copy.iso');
rs.pipe(ws);
// handle errors
rs.on('error', console.error);
ws.on('error', console.error);
ws.on('finish', () => console.log('done'));
```

**Q2: Build a transform stream that uppercases text**
**Approach:** Extend `stream.Transform` and implement `_transform`.

```js
const { Transform } = require('stream');
class Uppercase extends Transform {
  _transform(chunk, enc, cb) {
    cb(null, chunk.toString().toUpperCase());
  }
}
```

**Q3: Use pipeline with async/await and Promises**
**Approach:** Use `stream/promises` pipeline.

```js
const { pipeline } = require('stream/promises');
await pipeline(fs.createReadStream('in'), new Uppercase(), fs.createWriteStream('out'));
```

**Q4: Handle backpressure manually when writing to a slow writable**
**Approach:** Check `write()` return value and wait for `'drain'`.

```js
function writeChunks(ws, chunks) {
  for (const chunk of chunks) {
    if (!ws.write(chunk)) {
      await once(ws, 'drain');
    }
  }
  ws.end();
}
```

**Q5: Stream JSON array items without loading full JSON**
**Approach:** Use a streaming JSON parser (e.g., `JSONStream` or `stream-json`) in objectMode and pipe into processing stream.

---

## V. 🚀 Follow-Up Topics to Learn

1. **`stream.pipeline()` & `stream.finished()`** — Robust composition and lifecycle management; essential for production reliability.
2. **Backpressure tuning (highWaterMark) & performance tradeoffs** — Learn how buffer sizing impacts throughput and latency.
3. **Binary protocols & framing (net sockets, TLS)** — Real-world applications of duplex streams with framing/parsing.
4. **Streaming parsers (CSV, JSON, XML)** — Techniques for record-level processing without buffering entire files.
5. **Workers & streams (streams + threads / child processes)** — Offload CPU-heavy transforms while retaining streaming benefits.

---

### Quick reference & tips
- Prefer `pipeline()` for chaining; it prevents resource leaks.
- Use `objectMode` for non-binary chunks.
- Tune `highWaterMark` to balance memory vs throughput.
- Always handle `'error'` on each stream or use `pipeline()`.

---

*End of cheatsheet.*

# Node.js — **Buffers & Binary** (Cheatsheet)

---

## I. 💡 Basic Details of Node.js Buffers & Binary

**Definition & purpose**

A *Buffer* in Node.js is a raw binary data container — a fixed-length sequence of bytes — used to handle binary protocols, files, cryptography, and interop with native code. Buffers avoid JavaScript string/Unicode complications and let you work at the byte level.

**History & relevance**

Buffers were introduced early in Node to support network and file IO in a server environment where binary formats matter. They remain central when handling binary protocols (HTTP bodies, TCP frames), performance-sensitive code, and binary encoding/decoding.

---

## II. 🧠 Important Concepts to Remember

1. **Buffer vs TypedArray vs ArrayBuffer**
   - `Buffer` is Node-specific and extends `Uint8Array`. Internally it wraps an `ArrayBuffer` or a native memory region. Use `Buffer` for most Node IO; use `TypedArray` for numeric computations or Web APIs.
   - Analogy: *ArrayBuffer* is the raw memory slab, *TypedArray* is the tool that views it (like goggles), and *Buffer* is Node's comfy wrapper with helper methods.

2. **Byte order (Endianness)**
   - Use `readUInt32BE/LE`, `writeInt16BE/LE`, etc. BE = big-endian, LE = little-endian. Always agree on endianness for protocols.

3. **Encodings**
   - Common encodings: `utf8`, `utf16le`, `latin1` (a.k.a. binary), `base64`, `hex`. `utf8` encodes Unicode, variable bytes per char. `latin1` maps bytes to codepoints 0–255.

4. **Buffer allocation & memory**
   - `Buffer.alloc(size)` (zero-filled) — safe.
   - `Buffer.allocUnsafe(size)` — faster but may contain old memory; safe only if you immediately overwrite.
   - Avoid frequent small allocations in hot loops; reuse slices when possible.

5. **Slicing & copying**
   - `buf.slice()` creates a view (no copy) that shares underlying memory. `Buffer.from(buf)` or `buf.copy()` creates a copy.
   - Be careful: modifying a slice modifies the original.

6. **Binary parsing patterns**
   - Keep a read offset, parse fixed-size fields with `read*`, for variable-length fields read a length then slice.
   - For streaming data, buffer incomplete frames across `data` events — don't assume one event == one message.

7. **Interoperability**
   - Convert between Buffer and TypedArray / ArrayBuffer: `Buffer.from(typedArray)`, `buf.buffer` (careful: may include full underlying ArrayBuffer), `buf.slice().buffer`.

---

## III. 📝 Theory — Most Asked Questions (Interview Prep)

**Q1: What is a Buffer and why is it needed in Node?**
**A:** Buffer is a fixed-length binary data container used for raw bytes. It's needed because JavaScript strings are for text, not arbitrary binary data; buffers enable network I/O, file handling, crypto, and efficient binary protocol handling.

**Q2: Difference between `Buffer.alloc`, `Buffer.allocUnsafe`, and `Buffer.from`?**
**A:** `alloc` zeros memory (safe, slower). `allocUnsafe` returns uninitialized memory (faster, must overwrite). `from` creates a Buffer from array, string, or existing ArrayBuffer/TypedArray (copies where necessary).

**Q3: How do you read/write integer values at offsets?**
**A:** Use methods like `buf.readUInt8(offset)`, `buf.readUInt16BE(offset)`, `buf.readInt32LE(offset)`, and symmetric `write*` methods. Track offsets to parse sequential fields.

**Q4: How does `buf.slice()` differ from `buf.copy()`?**
**A:** `slice()` returns a view sharing the same underlying memory (no copy). `copy()` or `Buffer.from()` creates a new independent Buffer with its own memory.

**Q5: How to handle partial frames when receiving streaming binary data?**
**A:** Keep a temporary buffer for leftover bytes. Append incoming chunks, attempt to parse complete frames (using length prefix or delimiter). After parsing, keep the remaining bytes for next chunk.

---

## IV. 💻 Coding / Practical — Most Asked Questions (Interview Prep)

### Problem 1 — Parse a length-prefixed frame stream
**Question:** Implement parsing for messages where each frame: `[4-byte BE length][payload]`, arriving in arbitrary chunk boundaries.

**Optimal approach (algorithm outline):**
1. Maintain `buffered` (Buffer) and `offset = 0`.
2. On new chunk: `buffered = Buffer.concat([buffered.slice(offset), chunk]); offset = 0`.
3. While `buffered.length - offset >= 4`: read length `len = buffered.readUInt32BE(offset)`.
4. If `buffered.length - offset >= 4 + len`: extract `payload = buffered.slice(offset + 4, offset + 4 + len)`, process payload, `offset += 4 + len`.
5. Else break; after loop set `buffered = buffered.slice(offset)` and `offset = 0`.

**Pitfalls:** avoid unbounded `Buffer.concat` by trimming processed bytes.

---

### Problem 2 — Convert a UTF-8 string to hex and back
**Question:** Encode string → hex Buffer → string roundtrip.

**Approach:**
```js
const s = 'こんにちは';
const buf = Buffer.from(s, 'utf8');
const hex = buf.toString('hex');
const buf2 = Buffer.from(hex, 'hex');
const s2 = buf2.toString('utf8');
```
This preserves the original string if encoding chosen consistently.

---

### Problem 3 — Implement a simple checksum (e.g., CRC or XOR) for a packet
**Question:** Append a single-byte XOR checksum to a Buffer and verify on receive.

**Approach:**
```js
function appendXorChecksum(buf){
  const out = Buffer.alloc(buf.length + 1);
  buf.copy(out, 0);
  let xor = 0;
  for (let i = 0; i < buf.length; i++) xor ^= buf[i];
  out[buf.length] = xor;
  return out;
}
function verifyXorChecksum(bufWithChecksum){
  let xor = 0;
  for (let i = 0; i < bufWithChecksum.length; i++) xor ^= bufWithChecksum[i];
  return xor === 0; // true if checksum ok
}
```

---

### Problem 4 — Efficiently build a binary message from fields
**Question:** Pack `{id:uint32, flag:uint8, payload:Buffer}` into a Buffer.

**Approach:**
```js
function pack(id, flag, payload){
  const out = Buffer.alloc(4 + 1 + payload.length);
  out.writeUInt32BE(id, 0);
  out.writeUInt8(flag, 4);
  payload.copy(out, 5);
  return out;
}
```
Use `write*` and `copy` to avoid intermediate allocations.

---

### Problem 5 — TypedArray interop and performance
**Question:** Convert `Float32Array` to a Buffer and back without extra copies where possible.

**Approach:**
```js
const ta = new Float32Array([1.23, 4.56]);
const buf = Buffer.from(ta.buffer); // shares underlying ArrayBuffer (no copy) if typed array owns it
// careful: buf.byteOffset/length may reflect full ArrayBuffer; to copy exact bytes:
const exact = Buffer.from(ta.buffer, ta.byteOffset, ta.byteLength);
```
For heavy numeric work prefer `TypedArray` views and avoid copying into Buffer until IO is necessary.

---

## V. 🚀 Follow-Up Topics to Learn

1. **Node.js Streams & Backpressure** — Binary frames are commonly streamed; learn `Readable/Transform/Writable` and how buffering/backpressure affects memory and latency.
   - *Why:* Essential for scalable network services.

2. **Protocol Buffers / FlatBuffers / MessagePack** — Efficient binary serialization formats with schema support.
   - *Why:* Replaces ad-hoc binary formats with versioned, compact, cross-language structures.

3. **WebAssembly (Wasm) + Binary Interop** — Work with linear memory and shared buffers when calling Wasm from Node.
   - *Why:* High-performance numeric and crypto workloads often move to Wasm.

4. **N-API / Native Addons (C/C++)** — When you need zero-copy native buffers, learn N-API and how Node shares memory with native code.
   - *Why:* Sometimes required for highest throughput or platform integration.

5. **Binary Protocol Design & Security** — Framing, authentication, replay protection, and safely parsing untrusted binary inputs.
   - *Why:* Binary formats often expose subtle parsing bugs and security issues.

---

### Quick Reference — Common Buffer Methods

- `Buffer.alloc(size)`, `Buffer.allocUnsafe(size)`, `Buffer.from(...)`
- `buf.toString([encoding])`, `buf.toJSON()`
- `buf.copy(target, targetStart=0, sourceStart=0, sourceEnd=buf.length)`
- `buf.slice(start, end)` (shares memory)
- `buf.readUInt8(offset)`, `readUInt16BE/LE`, `readInt32BE/LE`, `readFloatLE/BE`, etc.
- `buf.writeUInt32BE(value, offset)`, symmetric `write*` methods

---

*Document created as a compact interview & practical cheatsheet. Use it as a quick reference, interview prep, or a basis to expand into protocol docs or internal wiki.*


# Node.js — File System (Cheatsheet)

## Preview & Download
Top-right: [Download the cheatsheet](sandbox:/mnt/data/nodejs_fs_cheatsheet.md)

---

## I. 💡 Basic Details
**What it is:** Node's `fs` module provides file and directory operations (read/write/rename/watch/permissions). It offers both callback-based, Promise-based (`fs/promises`), and synchronous versions of many APIs. The Promise APIs run work on Node's libuv threadpool, keeping the event loop responsive.  
**Why it matters:** Choosing the right fs API (sync vs async), using streams for large files, and ensuring atomic writes/watcher reliability are crucial for performant, correct server-side apps. citeturn0search17turn0search12

---

## II. 🧠 Important Concepts to Remember (5–7 keys)

1. **Sync vs Async**
   - *Sync* blocks the event loop — use only for short, startup, or CLI tasks. *Async* is non-blocking and should be default in servers. Prefer `fs/promises` + `async/await`. citeturn0search17turn0search6
   - Analogy: sync = pausing the whole restaurant to make one order; async = kitchen handles many orders concurrently.

2. **Streams & Backpressure**
   - Use `fs.createReadStream()` / `fs.createWriteStream()` for large files to avoid OOM and leverage built-in backpressure. Prefer `.pipe()` for standard copy flows. Tune `highWaterMark` for performance tuning. citeturn0search12turn0search20
   - Analogy: streams are an assembly line with a conveyor belt that slows down when the packer can't keep up.

3. **File Watchers**
   - `fs.watch()` is lightweight and delegates to OS notifications but behavior varies across platforms; `fs.watchFile()` polls (high CPU). `chokidar` is a robust cross-platform wrapper that adds stability and higher-level features. Evaluate needs: for simple, low-scale watchers `fs.watch` may suffice; for robust tooling use `chokidar`. citeturn0search17turn0search18turn0search7

4. **Atomic Writes / Safe Replacements**
   - To avoid data corruption when writing files, write to a temp file then `fs.rename()` (atomic on most OSes). Use proven libraries like `write-file-atomic` (or `fast-write-atomic`) instead of ad-hoc sequences. Be mindful of permissions and cross-device rename failures. citeturn0search2turn0search8turn0search5

5. **Locking & Concurrent Access**
   - Node itself doesn't provide strict file-locking across processes. Coordinate with advisory locks, database/IPC, or careful write-rename strategies when multiple processes may update the same file. citeturn0search19

6. **Edge Cases**
   - Watchers: debounce/coalesce events, handle duplicate events, and consider polling on unreliable filesystems or network mounts.  
   - Streams: always handle `error` events and close streams (`destroy()`/`close`) on errors. citeturn0search4turn0search12

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

1. **Q:** Why prefer async fs calls over sync on a server?  
   **A:** Async avoids blocking the event loop, enabling Node to handle other requests concurrently. Synchronous I/O blocks the single-threaded event loop and degrades throughput. Use sync only for startup scripts or short CLI tasks. citeturn0search17

2. **Q:** What is backpressure in streams and why does it matter?  
   **A:** Backpressure is the flow-control mechanism preventing a fast readable stream from overwhelming a slower writable consumer. Node streams expose `readable.pause()` / `resume()` and `write()`'s return boolean; `.pipe()` handles this automatically. Ignoring backpressure can cause increased memory usage and crashes. citeturn0search12

3. **Q:** How do you implement an atomic file write?  
   **A:** Write to a temporary file in the same directory (to ensure rename is atomic), fsync the temporary file, then `fs.rename()` to the target name. Use battle-tested packages like `write-file-atomic` to avoid pitfalls (e.g., cross-device rename). citeturn0search5turn0search2

4. **Q:** When would you use `chokidar` instead of `fs.watch`?  
   **A:** Use `chokidar` for cross-platform reliability, handling complex globs, recursive watching, and normalizing inconsistent OS events. For simple, low-scale needs, `fs.watch` may be enough and avoids an extra dependency. Test behavior on your target OSes. citeturn0search18turn0search7

5. **Q:** What are pitfalls of using `fs.watch`?  
   **A:** Platform differences (ignored events on network filesystems), duplicated events, missing rename semantics, and resource limits when watching many files. Consider polling or a library if you need robust behavior. citeturn0search17turn0search7

---

## IV. 💻 Coding / Practical — Most Asked Problems & Solutions

1. **Copy a large file efficiently**
   - Approach: use streams and pipe with error handling.
   ```js
   const fs = require('fs');
   const src = fs.createReadStream('big.bin');
   const dest = fs.createWriteStream('big.copy.bin');

   src.on('error', err => { dest.destroy(err); });
   dest.on('error', err => { src.destroy(err); });
   dest.on('close', () => console.log('done'));
   src.pipe(dest);
   ```
   Notes: `.pipe()` manages backpressure. Tune `highWaterMark` if you need throughput tuning. citeturn0search12turn0search20

2. **Atomic write helper (pattern)**
   - Approach: write to temp file, fsync, rename.
   ```js
   const fs = require('fs').promises;
   const path = require('path');
   async function atomicWrite(filePath, data) {
     const dir = path.dirname(filePath);
     const tmp = path.join(dir, '.' + path.basename(filePath) + '.tmp-' + Date.now());
     await fs.writeFile(tmp, data);
     // optional: await fs.fsync on file descriptor if using low-level APIs
     await fs.rename(tmp, filePath);
   }
   ```
   Recommendation: use `write-file-atomic` to handle edge cases (cross-device, permissions). citeturn0search5turn0search2

3. **Robust watcher with chokidar**
   ```js
   const chokidar = require('chokidar');

   const watcher = chokidar.watch('src/**/*.js', {
     persistent: true,
     ignoreInitial: true,
     awaitWriteFinish: { stabilityThreshold: 200, pollInterval: 100 }
   });

   watcher.on('add', path => console.log(`Added: ${path}`))
          .on('change', path => console.log(`Changed: ${path}`))
          .on('unlink', path => console.log(`Removed: ${path}`));
   ```
   Tips: `awaitWriteFinish` helps with editors that write temp files; debounce events if you need a single reaction per logical change. citeturn0search18

4. **Reading JSON config safely (avoid partial writes)**
   - Use atomic write for updates; when reading, validate JSON and optionally retry/backoff if parsing fails (could be reading mid-write). Consider keeping backups/versions. citeturn0search5

---

## V. 🚀 Follow-Up Topics to Learn
1. **Streams2 internals & custom Transform streams** — to build efficient pipelines (e.g., compression, CSV parsing). Reason: mastery lets you process large datasets without swapping to external tools. citeturn0search20
2. **File locking strategies & advisory locks** — when multiple processes modify shared files. Reason: prevents race conditions in multi-process systems. citeturn0search19
3. **Cross-platform file system quirks** (network mounts, case sensitivity, rename semantics) — Reason: production bugs often come from subtle OS differences. citeturn0search17
4. **Transactional file stores (e.g., LevelDB, SQLite)** — Reason: when many writers or strong consistency is required, use a purpose-built store rather than raw files.

---

## Quick Reference: Commands & Options
- `fs.promises.readFile(path)` / `fs.readFile(path, cb)` — async read. citeturn0search17  
- `fs.createReadStream(path, { highWaterMark })` — streaming read. citeturn0search20  
- `fs.watch(path, { recursive: true })` — OS-level watcher (Windows/macOS support varies). citeturn0search17  
- `npm: write-file-atomic` / `chokidar` — recommended libs for atomic writes and watching. citeturn0search5turn0search18

---

### Short checklist before shipping
- No sync fs calls in request handlers.  
- Stream large files; handle `error` events.  
- Use atomic write patterns for critical files.  
- Test watchers on target OS and network filesystems.  

---

*Cheatsheet generated for quick interview prep and practical usage.*

# Node.js — **Networking** (Cheatsheet)

---

## I. 💡 Basic Details of Node.js Networking

Node’s networking layer is built on top of **libuv**, a cross‑platform asynchronous I/O library. This foundation lets Node efficiently handle HTTP servers, TCP/UDP sockets, TLS-secured connections, and raw streaming protocols — all using the event-driven model.

The built‑in modules — `http`, `net` (TCP), `dgram` (UDP), and `tls` — give low-level control for implementing clients, servers, binary protocols, and secure channels.

---

## II. 🧠 Important Concepts to Remember

1. **HTTP vs TCP vs UDP**
   - HTTP: request/response, text or binary, built on TCP. Node’s `http` module is optimized for speed.
   - TCP (`net`): stream-based, reliable, ordered. Good for protocols that maintain a connection.
   - UDP (`dgram`): message-based, unreliable, no connection. Great for discovery, games, telemetry.

2. **Socket lifecycle**
   - States: creation → connect/accept → data events → half-close or full close → destroy.
   - Key events: `connect`, `data`, `end`, `close`, `error`, `timeout`.
   - Sockets are duplex streams.

3. **Backpressure & flow control**
   - Writing too fast fills internal buffers. Check `socket.write()` boolean return and listen for `'drain'`.

4. **TLS/SSL basics**
   - TLS wraps TCP with encryption & authentication.
   - Uses certificates (public/private key pairs). Clients validate server certificates.
   - Node's `tls` module can create secure servers/clients or wrap existing sockets.

5. **Key TLS options**
   - `key`, `cert`: PEM-encoded private key + certificate.
   - `ca`: trusted certificate authorities.
   - `rejectUnauthorized`: whether to validate peer certificate.
   - `servername`: SNI extension.

6. **Nagle’s algorithm & TCP optimizations**
   - `socket.setNoDelay(true)` disables Nagle, reducing latency for small packets.
   - Timeouts: `socket.setTimeout(ms)` emits `'timeout'` event.

7. **HTTP keep-alive & pipelining**
   - Reusing connections reduces overhead.
   - Node's agent pool handles this through `http.Agent`.

---

## III. 📝 Theory — Most Asked Networking Questions

**Q1: Difference between HTTP, TCP, and UDP?**
**A:** HTTP is an application protocol (request/response); TCP is a reliable byte stream; UDP is an unreliable message-based protocol. Node exposes them through `http`, `net`, and `dgram`.

**Q2: What events does a TCP socket emit?**
**A:** `connect`, `data`, `end`, `close`, `error`, and optional `timeout`.

**Q3: How does backpressure work in sockets?**
**A:** When `socket.write()` returns `false`, internal buffers are full. Pause writes and resume when `'drain'` fires.

**Q4: How does TLS secure a connection?**
**A:** TLS negotiates cipher suites, verifies certificates, and establishes symmetric keys for encrypted communication.

**Q5: Explain HTTPS handshake in Node.**
**A:** The client initiates TLS; server responds with certificate; client validates; both derive encryption keys; HTTP flows over the encrypted TCP tunnel.

**Q6: How does Node's HTTP server handle concurrency?**
**A:** Single-threaded JS with an asynchronous event loop — nonblocking IO allows many parallel clients.

**Q7: What is SNI and why does Node support it?**
**A:** SNI (Server Name Indication) lets one server present different certificates based on requested hostname.

---

## IV. 💻 Coding / Practical — Most Asked Questions

### Problem 1 — Build a simple HTTP server
**Approach:**
```js
const http = require('http');
http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello');
}).listen(3000);
```
Uses the built-in request/response pipeline.

---

### Problem 2 — Create a TCP echo server
**Approach:**
```js
const net = require('net');
net.createServer(socket => {
  socket.on('data', chunk => socket.write(chunk));
}).listen(4000);
```
TCP sockets are duplex streams with event-driven data.

---

### Problem 3 — UDP message send/receive
**Approach:**
```js
const dgram = require('dgram');
const sock = dgram.createSocket('udp4');

sock.on('message', (msg, rinfo) => {
  console.log('Received:', msg.toString());
});

sock.bind(5000);
```
UDP uses discrete datagrams; no connection handshake.

---

### Problem 4 — TLS-secured server
**Approach:**
```js
const tls = require('tls');
const fs = require('fs');

const opts = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

tls.createServer(opts, socket => {
  socket.write('secure hello');
  socket.pipe(socket);
}).listen(6000);
```
TLS behaves like a secure variant of TCP.

---

### Problem 5 — HTTP client with keep-alive
**Approach:**
```js
const http = require('http');
const agent = new http.Agent({ keepAlive: true });

http.get({ hostname: 'example.com', agent }, res => {
  res.on('data', () => {});
});
```
Reuses connections for better performance.

---

## V. 🚀 Follow-Up Topics to Learn

1. **HTTP/2 & HTTP/3** — Multiplexing, header compression, QUIC for faster web transport.
2. **WebSockets** — Full-duplex communication for real-time systems.
3. **Load Balancing & Reverse Proxies** — Nginx, HAProxy for scaling Node servers.
4. **ZeroMQ, gRPC, and custom binary protocols** — Advanced inter-service communication.
5. **Network security & hardening** — TLS best practices, certificate rotation, DDoS protection.

---

*Use this cheatsheet as a fast reference for interviews and day-to-day system design involving HTTP, TCP/UDP, TLS, and socket behavior.*

# Node.js — Child Processes Cheatsheet

**Previewable + Downloadable Link in the top right corner.**

---

## I. 💡 Basic Details of Node.js Child Processes
**Definition & purpose:**
Node.js child processes let you run external programs or spawn separate Node.js instances from a parent process. They’re used to parallelize CPU-bound work, use existing CLI tools, isolate work, or run background tasks while the main event loop stays responsive.

**History & relevance:**
Built on libuv and the OS process APIs, Node’s `child_process` module exposes multiple ways to create processes (`exec`, `spawn`, `fork`, `execFile`) and manage their I/O and lifecycle. As JS apps grown (build tools, native tooling, microservices), child processes are essential for orchestration and integration.

---

## II. 🧠 Important Concepts to Remember

1. **`spawn` — streaming, low overhead**
   - Use when you need to stream large amounts of data to/from a subprocess (e.g., piping stdout). It gives you `ChildProcess` streams (`stdin`, `stdout`, `stderr`).
   - Analogy: `spawn` is like opening a live phone call — data flows continuously.

2. **`exec` / `execSync` — buffered, simple command execution**
   - Runs command in a shell; collects stdout/stderr into buffers and returns them when the process exits. Risk: buffer overflow for large output (default 200KB in Node—configurable via `maxBuffer`).
   - Analogy: `exec` is like recording the entire phone call and listening to it only after it ends.

3. **`execFile` — like `exec` but skips the shell**
   - Safer (no shell expansion), slightly faster. Good for invoking binaries with args when you don’t need shell features.

4. **`fork` — spawn a new Node.js process with built‑in IPC**
   - Specialization of `spawn` that runs a Node module and sets up an IPC channel (`process.send()` / `process.on('message')`). Ideal for multi-process Node apps or worker pools.
   - `fork` uses an IPC channel over stdio; messages are serialized as JSON and optionally can transfer handles.

5. **StdIO options and piping**
   - `stdio` config: `pipe` (default), `inherit`, `ignore`, or an array to configure per-stream. Use `inherit` to share terminal with child (tty), `pipe` to programmatically read/write, `ignore` to drop streams.

6. **IPC, sending handles and pickling**
   - IPC supports passing messages and, on some platforms, passing TCP/IPC server handles (useful for zero-downtime restarts or load balancing across workers).

7. **Lifecycle management & cleanup**
   - Always handle `exit`, `error`, and `close` events. Use `child.kill()` to terminate and prefer signaling over SIGTERM before SIGKILL. Beware of zombie processes and detached processes (use `detached: true` + `child.unref()` carefully).

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

1. **Q: When would you use `spawn` vs `exec`?**
   **A:** Use `spawn` for streaming data or long-running processes because it exposes streams and avoids buffering large outputs. Use `exec` for short commands with small output where convenience (shell features) matters.

2. **Q: What is `fork` and how does it differ from `spawn`?**
   **A:** `fork` is a specialized `spawn` that starts a new Node.js process and sets up an IPC channel for `message` passing. `spawn` runs any executable and gives back stdio streams but no built-in message channel.

3. **Q: How can you avoid command injection when running shell commands?**
   **A:** Avoid `exec`/shell parsing when possible; use `execFile` or `spawn` with an args array. Validate or sanitize inputs. If you must use a shell, escape inputs or run under a constrained environment.

4. **Q: How do you handle a child process that becomes defunct/zombie?**
   **A:** Ensure the parent listens to the child's `exit`/`close` events and reaps children. If the parent dies, use `detached`+`child.unref()` to let child live independently, but handle cleanup policies to avoid orphaned resources.

5. **Q: How does Node’s IPC messaging serialize data? Are there limits?**
   **A:** Messages are serialized (usually JSON-like) — structured clone algorithm for handles and common objects; large objects may impact performance; handles like server sockets can be passed but platform specifics apply.

---

## IV. 💻 Coding/Practical — Most Asked Questions (with approaches)

1. **Q: Spawn a process and stream its stdout to the parent console while capturing exit code.**
   **Approach:** Use `child_process.spawn(cmd, args, { stdio: ['ignore', 'pipe', 'pipe'] })`. Attach `child.stdout.on('data')` to forward chunks, listen to `close` for exit code.

2. **Q: Execute a shell command and fail if output exceeds 1MB.**
   **Approach:** Use `exec` with `maxBuffer: 1024 * 1024`. Check `error` callback for `ERR_CHILD_PROCESS_STDIO_MAXBUFFER` or buffer size and handle accordingly. Prefer streaming with `spawn` for large outputs.

3. **Q: Create a worker pool using `fork` to parallelize CPU-bound tasks.**
   **Approach:** `fork` a worker script multiple times, maintain a task queue and round-robin / least-loaded assignment. Communicate tasks via `worker.send({task})` and receive results via `worker.on('message', ...)`. Recycle crashed workers by monitoring `exit`.

4. **Q: Run a child process detached from parent (background daemon).**
   **Approach:** `const child = spawn(cmd, args, { detached: true, stdio: 'ignore' }); child.unref();` Ensure the child redirects or ignores stdio and handles its own lifecycle.

5. **Q: Safely run a user-provided program with timeouts and resource limits.**
   **Approach:** Use a combination of `spawn`, OS-level tools (like `timeout`, `ulimit`, `cgroups` on Linux), and Node timers. Kill the process on timeout, and monitor resource usage externally or via native bindings.

6. **Q: Pass a server handle to a worker for zero-downtime restarts.**
   **Approach:** Parent opens the server, then `worker.send('server', server)` where `server` is the handle. Worker receives and `server.listen({handle})`. Use clustering pattern or `cluster` module for higher-level API.

---

## V. 🚀 Follow-Up Topics to Learn

1. **`cluster` module & Node worker threads** — For process-level and in-process parallelism; `worker_threads` are lighter weight for shared memory tasks.
   *Why:* Cluster simplifies load-balancing across cores; worker threads allow shared memory buffers.

2. **Process managers (PM2, systemd) & zero-downtime deploys**
   *Why:* Real-world deployment, process supervision, logs, and graceful restarts.

3. **OS-level resource control (cgroups, ulimit)**
   *Why:* For robust sandboxing and production-safe resource limits when running untrusted code.

4. **Native addons & child process alternatives (gRPC/microservices)**
   *Why:* For heavy native computation consider native addons or moving work to separate services.

5. **Security patterns for executing external code**
   *Why:* Prevent injection, privilege escalation, and resource exhaustion when accepting external inputs.

---

### Quick reference: Common `child_process` functions
- `spawn(command, args, options)` — streams, best for large output
- `exec(command, options, callback)` — buffered, runs in a shell
- `execFile(file, args, options, callback)` — runs executable directly
- `fork(modulePath, args, options)` — spawns Node with IPC

---

If you want examples, sample worker code, or a one-page PDF export, use the download link in the top-right or request the specific additions and I’ll extend the cheatsheet (examples, diagrams, or a worker-pool implementation).


# Node.js Worker Threads — Cheatsheet

**Previewable + Downloadable Link:** Use the panel's top-right corner to preview or download this document.

---

## I. 💡 Basic Details of Worker Threads

**Definition & purpose**
Worker Threads (module: `worker_threads`) provide a way to run JavaScript in parallel in multiple threads inside a single Node.js process. They enable CPU-bound tasks (math, image processing, data transformation, compression, cryptography) to run off the main event loop so I/O remains responsive.

**History & relevance**
Introduced experimentally in Node 10.5 and stabilized later, worker threads addressed Node's single-threaded CPU-bound limitation without the overhead of spawning separate OS processes. For modern server and tooling workloads where CPU work matters, `worker_threads` is often the right tool.

**When to use vs alternatives**
- Use `worker_threads` for fine-grained parallel CPU-bound tasks and when you want lower IPC overhead and the ability to share memory.  
- Use `child_process` (fork/spawn) when you need isolated processes, separate V8 instances, or to run different binaries. Child processes are better for fault isolation.

---

## II. 🧠 Important Concepts to Remember

1. **Worker and parent relationship**
   - `Worker` instances are created from a filename or string. They run in separate V8 isolates but inside the same OS process.
   - Parent and worker communicate via `postMessage`/`on('message')`.
   - Analogy: Think of the main thread as a conductor and workers as musicians playing independently but passing messages like sheet music.

2. **Transferable objects (zero-copy)**
   - `ArrayBuffer`/`MessagePort` can be *transferred* (ownership moves) rather than copied, enabling zero-copy data handoff.
   - Use `worker.postMessage(obj, [transferList])` to transfer.

3. **SharedArrayBuffer (shared memory)**
   - `SharedArrayBuffer` allows multiple threads to *share* memory concurrently. Must use synchronization primitives (e.g., `Atomics`) to avoid race conditions.
   - Analogy: SharedArrayBuffer is a communal whiteboard; `Atomics` are the pens with rules so people don't scribble over one another.

4. **Performance tradeoffs**
   - Workers have lower startup cost than spawning processes but still have overhead (module loading, thread creation). Reuse pools for many small tasks.

5. **Worker pools & task queues**
   - For many short tasks, use a pool (reuse worker threads) to amortize creation cost. Libraries like `workerpool` or `Piscina` implement efficient pools.

6. **Error propagation & termination**
   - Worker exceptions won't crash parent automatically; listen to `worker.on('error')` and `worker.on('exit')`. Use `worker.terminate()` to stop a worker cleanly.

7. **Security & resource limits**
   - Workers share process-level resources (file descriptors, etc.). They are not full isolation like processes — use `child_process` for stronger isolation.

---

## III. 📝 Theory — Most Asked Interview Questions (with model answers)

**Q1: How do Worker Threads differ from child processes?**
**A:** Workers run in the same OS process but separate V8 isolates and can share memory via `SharedArrayBuffer`. Child processes are separate OS processes with stronger isolation but heavier IPC and memory overhead.

**Q2: When would you use `SharedArrayBuffer` vs `ArrayBuffer` transfer?**
**A:** Transfer moves ownership (one side), fast for handing off large buffers. `SharedArrayBuffer` is used when multiple threads must simultaneously read/write the same memory region and coordinate using `Atomics`.

**Q3: How does `Atomics` help in worker threads?**
**A:** `Atomics` provides atomic operations and waiting/waking primitives (e.g., `Atomics.wait`/`Atomics.notify`) for synchronizing access to `SharedArrayBuffer` to prevent race conditions.

**Q4: What are pitfalls of using SharedArrayBuffer?**
**A:** Complexity of synchronization, potential deadlocks or livelocks if misused, and harder-to-debug concurrency bugs. Also, serialization or memory-consistency issues if `Atomics` are not used.

**Q5: How do you handle worker crashes?**
**A:** Listen for `error` and `exit` events, implement supervisor logic to restart or recycle workers, and use pools to control lifecycle.

---

## IV. 💻 Coding / Practical — Most Asked Questions

**Task 1: Basic worker example**
```js
// main.js
const { Worker } = require('worker_threads');
const worker = new Worker('./worker.js');
worker.on('message', msg => console.log('from worker:', msg));
worker.postMessage({ cmd: 'start', payload: 42 });
```

```js
// worker.js
const { parentPort } = require('worker_threads');
parentPort.on('message', ({ cmd, payload }) => {
  if (cmd === 'start') parentPort.postMessage(payload * 2);
});
```

**Task 2: Transfer an ArrayBuffer (zero-copy)**
```js
// main
const buf = new ArrayBuffer(1e6);
worker.postMessage({ buf }, [buf]); // buf transferred; main's `buf` becomes neutered
```

**Task 3: SharedArrayBuffer with Atomics (simple counter)**
```js
// shared.js (used by main and worker)
const sab = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT);
const ia = new Int32Array(sab);

// worker increments
Atomics.add(ia, 0, 1);
// main can read using Atomics.load(ia, 0)
```
Note: Use `Atomics.wait` / `Atomics.notify` for blocking/wakeup coordination.

**Task 4: Create a worker pool (high-level approach)**
- Pre-spawn N workers. Maintain a task queue. Assign tasks round-robin or by idle worker. Return results via Promise. Use `worker.terminate()` on shutdown.

**Task 5: Debugging tips**
- Add meaningful `console.error` in workers; forward errors via `postMessage` or `worker.on('error')`. Use `--inspect` flags on worker processes for stepping into threads.

---

## V. 🚀 Follow-Up Topics to Learn

1. **Worker Pools & Piscina** — Learn pool implementations and patterns for scaling throughput and reducing latency.
   - *Why:* Reusing workers reduces startup cost and simplifies scheduling for many small tasks.

2. **Native Addons (N-API / C++)** — Offload CPU work to native code and combine with workers.
   - *Why:* For extreme performance you may want native optimized code called from worker threads.

3. **Concurrency Primitives & Lock-free Algorithms** — Study `Atomics`, memory models, and lock-free queues.
   - *Why:* Building correct, high-performance shared-memory code requires familiarity with these primitives.

4. **Child Processes & Clustering** — Understand when OS-level process isolation and multi-process scaling are preferable.
   - *Why:* For memory isolation, security boundaries, or running different binaries.

5. **Observability for Multithreaded Apps** — Logging, tracing, and profiling techniques for threaded Node apps.
   - *Why:* Debugging concurrency requires better tooling and telemetry.

---

### Quick references (function names)
`Worker`, `parentPort`, `isMainThread`, `workerData`, `MessageChannel`, `MessagePort`, `SharedArrayBuffer`, `Atomics`, `postMessage`, `worker.terminate()`

---

_End of cheatsheet._



# Node.js — Cluster & Scaling (Cheatsheet)

## Preview & Download
Use the previewable + downloadable link in the top-right to export this cheatsheet.

---

# I. 💡 Basic Details of Node.js Cluster & Scaling
**Definition & purpose**
The Node.js `cluster` concept and ecosystem techniques are about running multiple Node.js worker processes (workers) to fully utilize multi-core servers, increase availability, and scale throughput for CPU-bound or concurrent workloads. Clustering complements Node's single-threaded event loop by distributing incoming connections and work across processes.

**Brief history & relevance**
Originally Node.js offered the `cluster` module to enable forking multiple processes sharing the same server port. Over time, production systems evolved to use process managers (PM2, systemd), container orchestration (Kubernetes), and service-level load balancing. Understanding cluster fundamentals remains crucial for designing horizontally-scalable Node services and diagnosing performance/availability behaviors.

---

# II. 🧠 Important Concepts to Remember
1. **Event loop ≠ CPU parallelism** — Node's event loop runs JS on a single thread; clustering creates multiple Node processes so each process has its own event loop. Analogy: one cashier (event loop) vs multiple tills (cluster workers).

2. **Master vs Worker** — The `cluster` master (or primary) manages worker lifecycle and can distribute connections. Workers handle the actual JS execution. Think: manager spawns baristas.

3. **Load distribution models**
   - *Round-robin (OS or Node)*: Node's cluster or the OS can distribute new connections round-robin.
   - *External load balancer*: Preferred in production (Nginx, HAProxy, cloud LB) because it handles health checks and sticky-session policies.

4. **Sticky sessions** — When using session affinity (client must consistently hit same worker), you need sticky routing (IP hash, cookie-based). Sticky sessions are a code smell for scalability — prefer stateless services or shared session storage (Redis). Analogy: giving customers a reserved seat — convenient but complicates scaling.

5. **State management** — Keep workers stateless. Use shared data stores (Redis, databases) or IPC/SharedArrayBuffer only for non-critical coordination. Horizontal scaling is hampered by in-memory session/state.

6. **Process managers & zero-downtime restarts** — Tools like PM2, systemd, or Kubernetes ensure process auto-restart, graceful shutdown, and rolling updates. PM2 also abstracts clustering for you.

7. **Horizontal vs Vertical scaling**
   - *Vertical*: bigger machine, more cores/memory — quick but has limits.
   - *Horizontal*: more instances across machines or containers — the recommended cloud-native approach.

8. **Health checks & graceful shutdown** — Implement `SIGINT`/`SIGTERM` handlers, stop accepting new connections, finish in-flight requests, then exit. Proper health probes allow orchestrators to avoid sending traffic to dying workers.

9. **Observability & tracing** — Use metrics (latency, event-loop lag, CPU), logs, and distributed tracing to detect overloaded workers and bottlenecks.

---

# III. 📝 Theory — Most Asked Interview Questions (with concise model answers)

**Q1: What is the Node.js `cluster` module and when should you use it?**
**A:** The `cluster` module forks the main Node process into worker processes to utilize multiple CPU cores. Use it to increase throughput for CPU-bound work or to improve availability on a multi-core machine. For I/O-bound and highly-scalable cloud setups, prefer running multiple replicas behind an external load balancer.

**Q2: Explain sticky sessions and why they can be problematic.**
**A:** Sticky sessions route requests from the same client to the same worker so stored in-memory session data remains accessible. They are problematic because they reduce flexibility for load balancing, complicate scaling, and create uneven load; stateless services or shared session stores are preferred.

**Q3: How do you perform a graceful shutdown in a clustered Node.js app?**
**A:** On `SIGTERM`/`SIGINT`, stop accepting new connections (server.close or stop LB traffic), allow ongoing requests to finish or time out, flush logs, close DB/Redis connections, and then exit. The master can spawn new workers before killing old ones for zero-downtime deploys.

**Q4: Compare using Node's built-in cluster vs process managers like PM2.**
**A:** The `cluster` module is a low-level API for spawning workers and sharing ports. PM2 is a production-focused process manager that simplifies clustering, zero-downtime restarts, log management, and monitoring. For containers & orchestration, Kubernetes typically replaces the need for PM2.

**Q5: When should you use SharedArrayBuffer / worker_threads instead of clustering?**
**A:** Use `worker_threads` when you need shared-memory concurrency within a single Node instance for compute-heavy tasks where copying is too expensive. Clustering is better for scaling network services across cores and processes; `worker_threads` are for offloading CPU work without IPC overhead.

**Q6: How does an external load balancer affect your architecture?**
**A:** An external LB provides health checks, TLS termination, global traffic management, and session affinity options. It allows simpler, stateless application design and better horizontal scaling across machines/availability zones.

---

# IV. 💻 Coding / Practical — Most Asked Questions (with approaches)

**P1: Implement a simple cluster that spawns workers equal to CPU cores and restarts a worker on exit.**
- *Approach*: Use `os.cpus().length`, `cluster.fork()`, listen for `exit` on worker and `cluster.fork()` a replacement. Have master handle signals.

**P2: Add graceful shutdown to the worker so it finishes requests before exiting.**
- *Approach*: On `SIGTERM`, call `server.close()` to stop accepting new connections, set a timeout for forced shutdown, and when connections drain, `process.exit(0)`.

**P3: Implement sticky sessions with a TCP proxy (simple cookie-based method).**
- *Approach*: Use an external layer (nginx or a Node TCP gate) that inspects a session cookie and routes to the worker's port. If using pure Node, create a master process that accepts socket connections and forwards sockets to a worker chosen by hashed cookie/IP.

**P4: Measure event-loop lag and restart worker on sustained high lag.**
- *Approach*: Use `perf_hooks.monitorEventLoopDelay()` or measure `setInterval` drift. If lag or CPU usage exceeds threshold for a window, notify master via IPC to restart the worker gracefully.

**P5: Handle shared cache with Redis for sessions in a clustered app.**
- *Approach*: Replace in-memory session store with Redis (e.g., `connect-redis` for `express-session`). Ensure TTLs and correct serialization. This allows any worker to handle any request.

**P6: Rolling redeploy with zero downtime using cluster + master.**
- *Approach*: Master spawns new worker(s) with updated code, waits for them to pass health checks, then signals old workers to gracefully shutdown and exits them.

---

# V. 🚀 Follow-Up Topics to Learn
1. **Kubernetes & Deployments** — Learn how Pods, Deployments, and Services manage replicas and rolling updates; critical for production horizontal scaling.
   - *Why*: Modern cloud-native deployments use orchestration instead of VM-based clustering.

2. **Service meshes & traffic management (Istio, Linkerd)** — Understand circuit breaking, retries, observability at the networking layer.
   - *Why*: Offers advanced routing and reliability features beyond LBs.

3. **Worker threads & native addons** — Deepen understanding of `worker_threads` and native modules for high-performance compute tasks.
   - *Why*: Enables CPU-bound tasks without spawning heavy processes; good for image processing, ML inference.

4. **Distributed caching & session strategies (Redis, Memcached)** — Patterns for cache invalidation, session replication, and consistent hashing.
   - *Why*: Essential for stateless scaling and consistent performance.

5. **Observability: Prometheus + Grafana + tracing (OpenTelemetry)** — Instrument Node.js apps for metrics, logs, and traces.
   - *Why*: Detecting and diagnosing scale-related issues depends on good telemetry.

---

## Quick Practical Checklist (copyable)
- Keep app stateless; use shared stores.
- Use external load balancer for production.
- Implement graceful shutdown and health checks.
- Monitor event-loop lag, CPU, and memory.
- Automate restarts with a process manager or orchestrator.

---

*End of cheatsheet.*
