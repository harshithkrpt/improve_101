
# Vite Basics Cheat Sheet

## What is Vite?
Vite is a modern frontend build tool that provides extremely fast development startup by using native ES modules (ESM) instead of bundling during development. It still uses Rollup for optimized production builds.

## ESM-Based Dev Server
Vite serves source code directly over ESM. The browser handles module graph resolution, so Vite doesn't need to bundle during development. This results in instant startup and very fast HMR.

## Vite vs Webpack
- Webpack bundles first; Vite serves unbundled ESM.
- Webpack HMR slows as projects grow; Vite updates only the changed module.
- Vite uses Rollup for production builds.

## Interview Questions

### What is Vite?
A fast frontend tooling system using ESM for development and Rollup for production.

### Why is Vite faster?
It avoids bundling during development and loads modules on demand.

### What is ESM?
Native browser-supported module system enabling Vite's no-bundle dev workflow.

### Does Vite bundle during dev?
No, bundling happens only during production.

### What does Vite use for production builds?
Rollup.

### How does Vite improve HMR?
It only updates changed modules.

### React support?
Yes, via @vitejs/plugin-react.

### TypeScript?
Supported via esbuild for fast transforms.

## Coding Questions

### Setup Vite + React
```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

### Alias Example
```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
})
```

### Env Variables
```env
VITE_API_URL=https://api.example.com
```

```js
const apiUrl = import.meta.env.VITE_API_URL
```

### Custom Plugin
```js
export default function myPlugin() {
  return {
    name: "logger-plugin",
    transform(code, id) {
      console.log("Transforming:", id)
      return code
    }
  }
}
```


# Vite Configuration Cheat Sheet

## Vite Configuration Basics
Vite uses a single config file—vite.config.js or vite.config.ts—built around defineConfig(). It controls dev server behavior, plugins, aliasing, env variables, and Rollup production settings.

```js
import { defineConfig } from 'vite'

export default defineConfig({
  server: { port: 5173, open: true },
  build: { outDir: 'dist' }
})
```

## Plugins
Vite plugins extend functionality and follow a Rollup-like hook system.

```js
export default function myPlugin() {
  return {
    name: "my-plugin",
    transform(code, id) {
      return code
    }
  }
}
```

Usage:
```js
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()]
})
```

## Aliasing
```js
import path from 'path'

export default defineConfig({
  resolve: {
    alias: { '@': path.resolve(__dirname, 'src') }
  }
})
```

## Environment Variables
Vite loads .env files automatically. Only variables prefixed with VITE_ are exposed.

.env:
```
VITE_API_URL=https://api.example.com
```

Usage:
```js
console.log(import.meta.env.VITE_API_URL)
```

## Interview Questions
### What is vite.config.js?
Controls Vite's core behavior including server, build, plugins, and aliases.

### What does defineConfig do?
Provides typings and structure.

### How do plugins work?
Through hooks that modify code or config.

### Why aliasing?
To avoid long relative imports.

### How does Vite load env variables?
From .env* files, exposing only VITE_-prefixed keys.

## Coding Questions

### React + Alias + Custom Port
```js
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  resolve: { alias: { '@': path.resolve(__dirname, 'src') } },
  server: { port: 4000 }
})
```

### Mode-based Config
```js
export default defineConfig(({ mode }) => ({
  define: { __MODE__: JSON.stringify(mode) }
}))
```

### Timestamp Plugin
```js
export default function timestampPlugin() {
  return {
    name: "timestamp-plugin",
    transform(code) {
      return code.replace(/console\.log/g, `console.log("[ts:" + Date.now() + "]")`)
    }
  }
}
```

# Topic : Vite

## Sub Topic : Plugins — `@vitejs/plugin-react`, `vite-plugin-svgr`, `@vitejs/plugin-legacy`, Custom plugin creation

---

## 1) Quick summary

Vite plugins extend Vite's dev server and build pipeline. They are compatible with Rollup plugin hooks and can be added inline in `vite.config.*` or published as npm packages. Common official/community plugins for React workflows include `@vitejs/plugin-react` (React fast-refresh / JSX handling), `vite-plugin-svgr` (SVG → React components via SVGR), and `@vitejs/plugin-legacy` (produces transpiled bundles + polyfills for older browsers).

---

## 2) How to add plugins (basic)

Install as dev dependency and add to `plugins` array in `vite.config.js` / `vite.config.ts`:

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import svgr from 'vite-plugin-svgr'
import legacy from '@vitejs/plugin-legacy'

export default defineConfig({
  plugins: [
    react(),
    svgr({ /* options */ }),
    legacy({ targets: ['defaults', 'not IE 11'], additionalLegacyPolyfills: ['regenerator-runtime/runtime'] })
  ]
})
```

---

## 3) Plugin details & examples

### @vitejs/plugin-react
- Purpose: React-specific transforms — JSX runtime support, Fast Refresh (HMR), optional SWC-based transforms.
- Install: `npm add -D @vitejs/plugin-react` (or use `@vitejs/plugin-react-swc` for SWC-based).
- Minimal example: `import react from '@vitejs/plugin-react';` then `react()` in `plugins`.

Example options (JSX runtime, babel plugin usage):

```js
react({
  jsxRuntime: 'automatic',
  babel: {
    plugins: ['babel-plugin-macros']
  }
})
```


### vite-plugin-svgr
- Purpose: Let you `import Icon from './icon.svg'` as a React component using SVGR.
- Install: `npm i -D vite-plugin-svgr` or use `@svgr/rollup` for Rollup compatibility if you prefer custom integration.
- Usage in config:

```js
import svgr from 'vite-plugin-svgr'

export default defineConfig({
  plugins: [svgr({ svgrOptions: { icon: true } })]
})
```

Import usage in React:

```jsx
import { ReactComponent as Logo } from './logo.svg' // depending on config
// or
import Logo from './logo.svg'

export default () => <Logo width={24} height={24} />
```

Notes: plugin exposes config like `include`, `exclude`, and `svgrOptions` that map to SVGR options. If you need TypeScript types for `*.svg` imports, add a declaration to `vite-env.d.ts`.


### @vitejs/plugin-legacy
- Purpose: Build-time transformations to support legacy browsers (babeled bundles via Babel + polyfills, `nomodule` pattern). Useful when you must support older browsers that lack native ESM.
- Install: `npm i -D @vitejs/plugin-legacy` and configure `targets` or `modernPolyfills`.

```js
legacy({
  targets: ['defaults', 'not IE 11'],
  additionalLegacyPolyfills: ['regenerator-runtime/runtime']
})
```

Caveat: adds extra build output and runtime wrappers — only enable when you must support older browsers.


### Creating a custom Vite plugin (inline or packaged)
Vite plugins follow the Rollup plugin hooks and can be trivial or complex. You can inline a simple plugin directly in `vite.config.*` without publishing.

**Simple inline plugin example — replace `.foo` files with transformed JS:**

```js
// vite.config.js
import { defineConfig } from 'vite'

function fooPlugin() {
  return {
    name: 'foo-transform',
    enforce: 'pre',
    resolveId(id) {
      if (id.endsWith('.foo')) return id
    },
    load(id) {
      if (id.endsWith('.foo')) {
        const content = "export default 'hello from .foo'"
        return content
      }
    },
    transform(code, id) {
      // optional transform for matched files
      return null
    }
  }
}

export default defineConfig({
  plugins: [fooPlugin()]
})
```

**HMR-aware plugin tip:** implement `handleHotUpdate({ file, server, read })` hook to integrate with Vite's dev server HMR pipeline.

**When to publish as a package:** if a plugin is generic and useful across projects, follow npm package conventions, include `vite-plugin` prefix in name, provide types, README, and indicate compatibility.


---

## 4) Interview-style theory questions (concise answers)

**Q1: What is the difference between a Vite plugin and a Rollup plugin?**
A: Vite uses Rollup-compatible plugin hooks for build; during dev, Vite also runs plugins in a different ESM-based dev server stage. Most Rollup plugins work, but dev-time behavior differs; prefer Vite-aware plugins when HMR/dev semantics matter.

**Q2: How does `@vitejs/plugin-react` help development?**
A: Enables React Fast Refresh (HMR for React), configures JSX transforms (automatic runtime), and lets you plug Babel or SWC transforms easily.

**Q3: Why use `vite-plugin-svgr` instead of importing SVG as URL?**
A: `vite-plugin-svgr` converts SVGs into React components (JSX), allowing props (className, width, fill) and tree-shaking, rather than a raw URL string.

**Q4: When should you use `@vitejs/plugin-legacy`?**
A: Only when you must support older browsers lacking ES modules (e.g., older Safari/IE). It adds extra bundles and polyfills—use sparingly.

**Q5: Name three plugin hooks you might use when writing a Vite plugin.**
A: `resolveId`, `load`, `transform`. For HMR/dev: `handleHotUpdate`.

**Q6: How do you debug plugin issues?**
A: Reproduce the error with minimal config, add `console.log` in hooks, inspect resolved ids and transforms, use `--debug` or verbose logs and unit tests for plugin logic.


---

## 5) Coding-style interview questions (practice)

**C1: Write an inline Vite plugin that converts `.txt` files into JS modules exporting the file content.**
- Expected: use `load` to return `export default ${JSON.stringify(content)}`.

**C2: How would you make a plugin that inlines small images as base64 during build?**
- Expected: implement `load`/`transform` to detect `import` of images, check size (read file), and return `export default "data:image/...;base64,..."` for small files, otherwise return `null` to let asset handling continue.

**C3: Implement `handleHotUpdate` to trigger HMR for files with extension `.xyz` and send a full-reload.**
- Expected: call `server.ws.send({ type: 'full-reload' })` when relevant; alternatively return modified modules via Vite's HMR protocol.

**C4: How to integrate SVGR options (e.g., `icon: true`) in vite-plugin-svgr config? Show example.**

```js
svgr({
  svgrOptions: { icon: true, replaceAttrValues: { '#000': 'currentColor' } }
})
```


---

## 6) Practical tips & gotchas

- Order matters: plugin order can affect transforms (e.g., run `svgr` before other asset plugins that treat `.svg` as asset URLs).
- Use `include` / `exclude` globs in plugin options to limit scope and avoid conflicts.
- For TypeScript projects, add `declare module '*.svg'` types when importing SVGs as React components.
- Publish plugins with `vite-plugin-` prefix to help discoverability, but Vite doesn't require the prefix.


---

## 7) Quick reference snippets

**Add React + SVGR + Legacy**

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import svgr from 'vite-plugin-svgr'
import legacy from '@vitejs/plugin-legacy'

export default defineConfig({
  plugins: [
    react(),
    svgr({ svgrOptions: { icon: true } }),
    legacy({ targets: ['defaults', 'not IE 11'] })
  ]
})
```


---

## 8) Where to read next

- Vite official docs: plugin guide and API
- Plugin repositories: `vite-plugin-react`, `vite-plugin-svgr`, `@vitejs/plugin-legacy` on npm/GitHub
- Tutorials on writing Vite plugins (articles, blog posts linked from ecosystem)


---

*Generated for interview prep — copy or download this Markdown (use the preview & download button at the top-right of this document).*


# Topic : Vite

## Sub Topic : Environment Variables — `import.meta.env` and `.env` handling

---

## 1) What Vite does differently with environment variables
Vite treats environment variables as **statically replaced** during build. Anything accessed via `import.meta.env` becomes part of the final bundle based on which mode you run (`development`, `production`, or custom).

Files like `.env`, `.env.development`, `.env.production`, and `.env.[mode]` are auto‑loaded. Variables that begin with `VITE_` get exposed to client-side code; everything else stays server-only for security.

This prevents you from accidentally shipping secrets—only intentional `VITE_` prefixed ones reach the browser.

---

## 2) The lifecycle of environment variable loading
Vite loads env files in the following order (later overrides earlier):
1. `.env`
2. `.env.local` (ignored in git usually)
3. `.env.[mode]`
4. `.env.[mode].local`

When you run `vite`, `vite dev`, or `vite build --mode staging`, Vite loads variables matching that mode.

Example: Running `vite --mode staging` → loads `.env`, `.env.staging`, `.env.staging.local`.

---

## 3) Accessing environment variables in client code
All variables must be prefixed with **VITE_** to be available:

```env
# .env
VITE_APP_TITLE=My Vite App
API_SECRET_KEY=super-secret   # This WILL NOT be available in browser
```

Use in code:
```js
console.log(import.meta.env.VITE_APP_TITLE)
```

By default, available env constants include:
- `import.meta.env.MODE`
- `import.meta.env.DEV`
- `import.meta.env.PROD`
- `import.meta.env.SSR`

These are injected by Vite.

---

## 4) Examples of common `.env` setups

### Example `.env.development`
```env
VITE_API_URL=http://localhost:5000
VITE_DEBUG=true
```

### Example `.env.production`
```env
VITE_API_URL=https://api.example.com
VITE_DEBUG=false
```

### Using in React code
```js
const apiUrl = import.meta.env.VITE_API_URL

export function fetchUser() {
  return fetch(`${apiUrl}/users`).then(r => r.json())
}
```

---

## 5) Custom modes and switching environments
You can create arbitrary modes such as `staging`.

Create file:
```
.env.staging
```
Add variables:
```env
VITE_API_URL=https://staging.example.com
```
Run Vite with this mode:
```bash
vite build --mode staging
```

This produces a build pointing to the staging API.

---

## 6) Using `loadEnv` inside `vite.config.js`
Sometimes you need env variables **in your config file**, not in the app.

Use Vite’s helper:

```js
import { defineConfig, loadEnv } from 'vite'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd())

  return {
    define: {
      __APP_VERSION__: JSON.stringify(env.VITE_APP_VERSION)
    }
  }
})
```

`loadEnv` loads variables even if they don’t start with `VITE_`. But to expose something to the client, you still need the prefix.

---

## 7) Security note
Variables **without** the `VITE_` prefix **never** become visible to client code. This is by design.

If you accidentally try to access non‑prefixed env vars:
```js
console.log(import.meta.env.API_SECRET)  // undefined
```

This prevents leaking secrets.

---

## 8) Theory-oriented interview questions (concise answers)

**Q1: Why does Vite require `VITE_` prefix for client-exposed variables?**
To prevent accidental exposure of sensitive server-only values. Only intentionally prefixed variables reach the browser.

**Q2: How do you load environment variables in Vite config?**
Use `loadEnv(mode, process.cwd())` inside `defineConfig`.

**Q3: What is `import.meta.env.MODE` used for?**
To detect the current Vite mode (`development`, `production`, or custom). Useful for toggling features.

**Q4: Can Vite environment variables change at runtime?**
No. They are statically injected during build time. A rebuilt bundle is required for changes.

**Q5: What is the precedence of env files?**
`.env` → `.env.local` → `.env.[mode]` → `.env.[mode].local`.

---

## 9) Coding-oriented interview practice

**C1: Write code that prints different log levels based on mode.**
Expectation: use `import.meta.env.MODE` and a conditional.

**C2: Implement a `config.js` helper that returns env values with validation.**
Expectation: wrap `import.meta.env` and throw if required variables missing.

**C3: Use `loadEnv` to generate a dynamic `base` path in `vite.config.js`.**
Expectation: `base: env.VITE_PUBLIC_PATH || '/'`.

**C4: Build-time flag injection using `define`.**
Example:
```js
define: { __FEATURE_X__: JSON.stringify(import.meta.env.VITE_FEATURE_X) }
```

---

## 10) Practical tips

- Restart dev server after editing `.env` files; Vite doesn't auto-reload them.
- Add `.env.local` to `.gitignore` to avoid leaking local secrets.
- To use TypeScript autocompletion for env variables, extend `ImportMetaEnv` in `vite-env.d.ts`.

```ts
interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
}
```

---

*This document is ready to download. Use the preview/download button in the top-right corner of the canvas.*

# Topic : Vite

## Sub Topic : Hot Module Replacement (HMR) — How HMR works & React Fast Refresh

---

## 1) What HMR really means in Vite
HMR (Hot Module Replacement) lets your app update code **without a full page reload**. Instead of replacing the entire page, Vite patches only the changed modules. This preserves state whenever possible, especially in React with Fast Refresh.

Vite’s dev server runs on native ES modules. When a file changes:
1. The dev server detects the file update.
2. It sends a WebSocket message to the browser.
3. Only modules affected by the update are invalidated.
4. The browser fetches the new module version and executes update callbacks.
5. React Fast Refresh ensures UI + component states stay intact.

The magic comes from Vite’s lightweight ESM pipeline—no bundling step during dev.

---

## 2) How Vite implements HMR internally
### Step-by-step flow
1. **File changes** detected via chokidar watcher.
2. **Vite transforms** the file again (e.g., TS → JS, JSX transform, plugin transforms).
3. **Dev server pushes** an update message over WebSocket to the client.
4. The client compares updated modules and reloads only what’s necessary.
5. If a module exports `import.meta.hot.accept`, Vite executes the callback.
6. If not, it bubbles up the dependency graph until it finds a boundary.
7. If no boundary is found → full page reload.

### Why Vite HMR is fast
- No bundling → updates are patch-level.
- Only changed ESM modules are re-imported.
- Works with plugin pipeline so JSX, TS, CSS, etc. update instantly.

---

## 3) `import.meta.hot` — the HMR API
You can explicitly control HMR behavior in modules.

```js
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    console.log('Module updated', newModule)
  })
}
```

Useful for:
- Custom plugins
- Renderers
- Non-React frameworks

### Key APIs
- `hot.accept(cb)` — accepts module update
- `hot.dispose(cb)` — cleanup before module is replaced
- `hot.invalidate()` — forces full reload

---

## 4) React Fast Refresh in Vite (`@vitejs/plugin-react`)
React Fast Refresh sits on top of HMR.

### What Fast Refresh preserves
- Component state
- Hooks state
- Context
- DOM position

### What it cannot preserve
- Changes to component state logic itself
- Class components losing state
- Changes to component signature (props → different structure)

### Real example
```jsx
function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>
}
```
Updating the button text preserves `count` during Fast Refresh.

Update the hook order? Fast Refresh forces a full reload.

### How Vite enables Fast Refresh
`@vitejs/plugin-react` injects Babel/SWC transforms that:
- Wrap components in refresh boundaries
- Track edited modules
- Replace only component code
- Re-render updated components without full re-mount

---

## 5) HMR + CSS in Vite
CSS gets special handling:
- CSS updates are always hot-reloaded without JS execution.
- CSS modules trigger only style updates, not component reloads.
- PostCSS + Tailwind files also update instantly.

Example:
```css
.button {
  background: red; /* update → instant refresh */
}
```

---

## 6) HMR boundaries explained
A **boundary** is a module that can accept updates without propagating changes.

Examples:
- React components via Fast Refresh
- Vue SFCs
- Modules using `import.meta.hot.accept()`

If no boundary catches an updated module → full reload.

---

## 7) Using HMR in custom Vite plugins
Example:
```js
function timestampPlugin() {
  return {
    name: 'timestamp-watch',
    handleHotUpdate({ file, server }) {
      if (file.endsWith('.timestamp')) {
        server.ws.send({ type: 'full-reload' })
      }
    }
  }
}
```

Custom plugins can:
- Trigger partial updates
- Trigger full reload
- Modify payload

---

## 8) Theory-based interview questions (short answers)

**Q1: What makes Vite HMR faster than Webpack/Vite?**  
It avoids bundling; updates use native ESM modules.

**Q2: What triggers a full reload instead of HMR?**  
If no HMR boundary handles the update.

**Q3: How does React Fast Refresh keep state?**  
It re-renders components in-place while preserving hook order and local state.

**Q4: Why does changing hook order break Fast Refresh?**  
React can't match previous hook positions → invalidates refresh → full reload.

**Q5: Can `import.meta.env` change at runtime with HMR?**  
No, env variables are build-time only.

**Q6: Does CSS always support HMR in Vite?**  
Yes, Vite injects Hot CSS updates without JS.

---

## 9) Coding-oriented interview tasks

**C1: Implement a custom HMR accept callback for a module.**  
Expectation: use `import.meta.hot.accept()`.

**C2: Write a Vite plugin that triggers full reload when `.config.json` changes.**  
Expectation: use `handleHotUpdate` + `server.ws.send({ type: 'full-reload' })`.

**C3: Wrap an external renderer with manual HMR support.**  
Expectation: store cleanup, re-render on accept.

**C4: Build a counter component and explain why its state persists after editing.**  
Expectation: React Fast Refresh preserves it.

---

## 10) Practical notes
- HMR works only in dev mode.
- Large dependency graphs may slow down updates—optimize with aliasing.
- Restart dev server after editing config files.
- HMR may break if plugins mis-handle module transforms.

---

*This document is ready for preview and download using the button on the top-right of the canvas.*

# Vite — Build Optimization

**Topic:** Vite

**Sub Topic:** Build Optimization — code splitting, chunking, pre-bundling with esbuild

---

## Quick summary

This cheat sheet covers practical techniques and configuration for optimizing production builds in Vite: code splitting, chunking strategies, and pre-bundling with esbuild. Includes `vite.config` examples, theory questions (for interviews) with concise answers, and coding tasks to practice.

---

## 1. Concepts & why they matter

- **Code splitting**: Splitting your codebase into smaller bundles so the browser only downloads what's needed. Improves initial load time and perceived performance.
- **Chunking**: How the bundler groups modules into files (chunks). Proper chunking reduces duplication and cache invalidation.
- **Pre-bundling (esbuild)**: Vite uses esbuild during dev to pre-bundle dependencies (optimize `node_modules`) for faster cold-start. In build, Rollup + terser/esbuild do final bundling/minification. Pre-bundling in dev reduces number of ESM imports the browser must request.

---

## 2. Vite architecture (brief)

- **Dev**: Native ESM + esbuild pre-bundling of dependencies -> fast server start and HMR.
- **Build**: Rollup under the hood for production — supports code splitting, tree-shaking, and plugins. Vite exposes Rollup options via `build.rollupOptions`.

---

## 3. Practical strategies

### 3.1 Entry points & manualChunks

Define multiple entry points or use `manualChunks` to control chunking. Useful to separate vendor, large libs, or feature routes.

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        main: 'index.html',
        admin: 'admin.html'
      },
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            if (id.includes('react')) return 'vendor_react'
            return 'vendor'
          }
        }
      }
    }
  }
})
```

Notes:
- `manualChunks` receives module id; return a chunk name to force grouping.
- Keep chunk names stable across builds to improve long-term caching.

### 3.2 Dynamic imports for route-based splitting

Use `import()` for lazy-loading pages/components.

```jsx
// React route example
const Home = lazy(() => import('./pages/Home'))
const Admin = lazy(() => import('./pages/Admin'))
```

Benefits: load only code needed for current route.

### 3.3 Vendor splitting

Let Rollup create a large `vendor` chunk for `node_modules`. Use `manualChunks` or rely on Rollup's default behavior (it often groups deps). For deterministic caching, explicitly split big libs (React, lodash, charting libs).

### 3.4 Shared chunks & deduplication

If multiple pages import the same big dependency, extract it into shared chunk(s) so it's downloaded once.

### 3.5 Priority: cacheability over tiny savings

Prefer long-lived vendor chunk names and hashed filenames for app code. Avoid frequent changes to vendor chunk boundaries.

### 3.6 Asset optimization

- Use `build.assetsInlineLimit` to inline tiny images/fonts as base64.
- Use `vite-plugin-imagemin` for raster/ vector compression in build.
- Use hashed file names (default) for cache-busting.

### 3.7 CSS splitting & preloading

- Vite extracts CSS into separate files by default; keep critical CSS small.
- Use `<link rel="preload">` for fonts and critical JS or `prefetch`/`preload` hints for important chunks.

### 3.8 Brotli/Gzip and server config

Generate compressed assets at build time (optional). Example plugin: `rollup-plugin-gzip` or `vite-plugin-compression`. Configure your server to serve compressed files with correct `Content-Encoding`.

### 3.9 Analyze bundle

Use `rollup-plugin-visualizer` or `vite-bundle-analyzer` to visualize chunk sizes and dependencies.

```bash
# install
npm i -D rollup-plugin-visualizer
```

Add plugin or run `vite build --report` depending on tooling.

---

## 4. Pre-bundling with esbuild

- Vite runs esbuild to pre-bundle `node_modules` in dev for faster cold start and fewer network requests.
- You can control pre-bundling via `optimizeDeps` in `vite.config`.

```js
export default defineConfig({
  optimizeDeps: {
    include: ['lodash-es', 'some-lib'],
    exclude: ['some-cjs-lib']
  }
})
```

Tips:
- If a dependency uses non-standard exports or causes HMR issues, add it to `optimizeDeps.exclude`.
- Pre-bundling is only for dev; production uses Rollup.

---

## 5. Example `vite.config.js` combining techniques

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import visualizer from 'rollup-plugin-visualizer'
import compress from 'vite-plugin-compression'

export default defineConfig({
  plugins: [react(), visualizer({ open: false }), compress()],
  build: {
    sourcemap: true,
    assetsInlineLimit: 4096,
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name].[hash].js',
        chunkFileNames: 'assets/chunk-[name].[hash].js',
        assetFileNames: 'assets/[name].[hash].[ext]',
        manualChunks(id) {
          if (id.includes('node_modules')) {
            if (id.includes('react')) return 'vendor_react'
            if (id.includes('chart.js')) return 'vendor_chart'
            return 'vendor'
          }
        }
      }
    }
  },
  optimizeDeps: {
    include: ['lodash-es'],
    exclude: ['some-cjs-lib']
  }
})
```

---

## 6. Interview theory questions (concise answers)

1. **What is code splitting and why is it important?**
   - Splitting code into smaller bundles so clients download only needed code; reduces initial load and improves performance.

2. **How does Vite handle dev vs production builds?**
   - Dev: native ESM + esbuild pre-bundling for fast HMR. Production: Rollup bundles and optimizes assets.

3. **What's `manualChunks` and when would you use it?**
   - A Rollup option to control how modules are grouped into chunks; use it to create stable vendor chunks or split large libraries.

4. **What's the difference between `preload` and `prefetch`?**
   - `preload`: high priority, used for resources needed for current navigation. `prefetch`: low priority, for future navigations.

5. **How would you reduce bundle size of a large UI library?**
   - Use tree-shakeable imports (`lodash-es`), import only required components, use code-splitting, replace large libs with lighter alternatives.

6. **What is esbuild's role in Vite?**
   - Used for extremely fast dependency pre-bundling in dev and optionally for minification. Not used as the final bundler (Rollup is).

7. **How to debug large chunks and unexpected modules in bundles?**
   - Use bundle analysers (visualizer), inspect `manualChunks` logic, check transitive imports, and examine package exports.

---

## 7. Coding / practical interview questions

1. **Implement route-based code splitting in React using React.lazy + Suspense.**
   - Practice: create three routes with lazy-loaded components and demonstrate network tab showing separate chunk downloads.

2. **Create a `manualChunks` function that groups all charting libs into `vendor_charts`.**
   - Small task: update `vite.config.js` `manualChunks` to detect `chart.js|recharts|d3` and return `vendor_charts`.

3. **Measure performance impact of inlining assets**
   - Task: build twice with `assetsInlineLimit` 0 and 8192 and compare total transferred bytes on first load.

4. **Add gzip + brotli generation to build**
   - Task: add `vite-plugin-compression` with `{ algorithm: 'brotliCompress' }` and show resulting `.br` and `.gz` files.

5. **Fix a dependency causing pre-bundling issues**
   - Task: given an example dependency that exports both CJS and ESM, configure `optimizeDeps.include`/`exclude` to ensure correct behavior.

---

## 8. Best practices checklist

- [ ] Keep vendor chunk names stable.
- [ ] Use dynamic imports for route-level components.
- [ ] Analyze bundle with a visualizer regularly.
- [ ] Inline only very small assets.
- [ ] Serve pre-compressed files when possible.
- [ ] Prefer tree-shakeable libraries.

---

## 9. Resources & further reading

- Vite docs: build options, optimizeDeps, Rollup guide
- Rollup docs: manualChunks, output options
- esbuild docs: why it's fast and what it does


---

*Generated for quick interview prep and implementation. Previewable here and downloadable as a Markdown file (use the top-right download in this canvas).*

# Vite — Integration with React

**Topic:** Vite

**Sub Topic:** Integration with React — setup, JSX transform, TypeScript + Vite setup

---

## Quick summary

This cheat sheet shows how to scaffold a React app with Vite, configure JSX transform (automatic vs classic), and set up TypeScript. Includes working `vite.config` examples, `tsconfig` tips, common pitfalls and interview-friendly theory + coding questions.

---

## 1. Scaffolding a Vite + React project

Recommended quick scaffold (official):

```bash
# using npm
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

Notes:
- `create-vite` templates provide ready-to-go React or React+TS templates.
- Vite requires a modern Node.js — check the Vite docs for the minimum required Node version.

---

## 2. @vitejs/plugin-react and JSX transform

- Install the plugin to add Fast Refresh, JSX transform compatibility, and optional Babel support.

```bash
npm install -D @vitejs/plugin-react
```

- Default behavior: automatic JSX runtime (no need to `import React from 'react'` for JSX). If you need the classic runtime or custom `jsxImportSource`, configure the plugin.

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react({ jsxRuntime: 'automatic' /* or 'classic' */ })]
})
```

- If you use emotion/other JSX factories, pass `jsxImportSource` or use `jsxRuntime: 'classic'` as needed.

---

## 3. TypeScript + Vite setup (React)

1. Install types and TypeScript:

```bash
npm install -D typescript @types/react @types/react-dom
```

2. Use the `react-ts` template or add a `tsconfig.json` with recommended settings:

```json
{
  "compilerOptions": {
    "target": "ES2019",
    "lib": ["DOM", "ESNext"],
    "jsx": "react-jsx",
    "module": "ESNext",
    "moduleResolution": "Node",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src"]
}
```

- `jsx: "react-jsx"` enables the automatic JSX runtime typing for React 17+ behavior. If using classic runtime, set `jsx: "react"`.
- Use `.tsx` extension for files with JSX when using TypeScript.

---

## 4. Example `vite.config.ts` for React + TS

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': '/src'
    }
  },
  server: {
    port: 3000,
    open: true
  }
})
```

---

## 5. Common pitfalls & fixes

- **JSX errors for .js files**: Rename to `.jsx`/`.tsx` or configure Vite to treat `.js` as JSX.
- **`JSX.IntrinsicElements` Type errors**: Ensure `@types/react` is installed and `jsx` compilerOption is correct.
- **Conflicting JSX runtimes**: If a dependency expects classic runtime, set `jsxRuntime: 'classic'` in plugin options or configure `optimizeDeps` to avoid transformation side effects.

---

## 6. Interview theory (concise answers)

1. **Why use @vitejs/plugin-react?**
   - Provides Fast Refresh, integrates JSX transforms, and allows optional Babel plugins for compatibility.

2. **What does `jsx: "react-jsx"` do in `tsconfig`?**
   - Tells TypeScript to emit calls to the automatic runtime (no `React.createElement`), matching modern React JSX transform.

3. **When would you use the classic JSX runtime?**
   - When working with older libraries or tooling that expect `React.createElement`, or when you need explicit `React` in scope.

4. **How does Vite handle JSX transpilation?**
   - Vite uses esbuild for fast JSX transpilation in dev; `@vitejs/plugin-react` can apply additional transforms (Babel) and enable Fast Refresh.

---

## 7. Coding / practical interview tasks

1. **Create a TypeScript React app with Vite**
   - Scaffold with `--template react-ts`, add a lazy-loaded component and show separate chunk in Network tab.

2. **Switch JSX runtime and observe bundle size**
   - Toggle `jsxRuntime` between `automatic` and `classic` in plugin configuration and compare build output.

3. **Integrate emotion (or similar) with custom jsxImportSource**
   - Configure `@vitejs/plugin-react` with `{ jsxImportSource: '@emotion/react' }` and validate styles and HMR.

4. **Fix type errors for intrinsic elements**
   - Reproduce `JSX.IntrinsicElements` errors (remove `@types/react`) and fix by installing correct types and adjusting `tsconfig`.

---

## 8. Best practices checklist

- Use `react-ts` template for TypeScript projects.
- Prefer automatic JSX runtime unless compatibility requires classic.
- Keep `tsconfig` strict and use `skipLibCheck` to avoid noisy type errors from deps.
- Install `@types/react` and `@types/react-dom` for TypeScript typing support.
- Use plugin options to add Babel plugins only when necessary.

---

*Generated to be previewable and downloadable as Markdown. Use the top-right download in this canvas to get the `.md` file.*

# Vite — SSR Support

**Topic:** Vite

**Sub Topic:** SSR Support — Vite SSR entry points, VitePress, vite-plugin-ssr

---

## Quick summary

This cheat sheet explains how to add Server-Side Rendering (SSR) to Vite-powered apps: app entry points for server and client builds, key Vite SSR config options, VitePress (a markdown-centered SSG with SSR/SSG behavior), and `vite-plugin-ssr` for flexible app-level SSR features. Includes `vite.config` examples, interview theory, and practical coding tasks.

---

## 1. Core concepts

- **SSR vs SSG vs CSR**: SSR renders HTML on the server per-request; SSG pre-renders at build time; CSR renders in the browser. Vite supports all modes and can be configured to build SSR bundles alongside client bundles.
- **Dual entry points**: SSR requires separate server and client entry points (e.g. `entry-server.js` and `entry-client.js`). The server bundle exports a render function; the client bundle hydrates.
- **Vite + Rollup**: Vite uses Rollup for production builds; server bundles typically use `build.ssr` and Rollup options.

---

## 2. Typical file structure / entry points

```
/src
  /entry-client.jsx      // client hydration entry
  /entry-server.jsx      // server render entry
  /App.jsx
  /routes.jsx
/server
  server.js              // express/fastify/solid-start style server
vite.config.js
```

`entry-server` typically exports a `render(url, manifest)` function used by your Node server to produce HTML; `entry-client` mounts/hydrates the app on the client.

---

## 3. Vite config and SSR options

- Use `build.ssr` to produce a server bundle: `vite build --ssr src/entry-server.jsx` or set `build: { ssr: 'src/entry-server.jsx' }` in config.
- Important SSR config keys: `ssr.external`, `ssr.noExternal` (control dependency externalization), and `build.rollupOptions` for multiple outputs.

```js
// vite.config.js (snippet)
export default defineConfig({
  build: {
    ssr: 'src/entry-server.jsx',
    rollupOptions: {
      input: {
        client: 'index.html'
      }
    }
  },
  ssr: {
    external: ['some-server-only-lib'],
    noExternal: ['some-esm-only-dep']
  }
})
```

Notes:
- By default Vite externalizes dependencies for SSR; use `ssr.noExternal` to bundle ESM-only deps into the server build.

---

## 4. Example server (Node + Express) flow

1. Start a Node server that creates a Vite dev server in middleware mode when `NODE_ENV !== 'production'`.
2. In dev, use Vite's `ssrLoadModule` to import server entry and call the render function per request.
3. In production, serve pre-built server bundle and client assets; the server bundle is a CommonJS/ESM module that renders HTML using `render(url)`.

---

## 5. vite-plugin-ssr

- `vite-plugin-ssr` is a community plugin that provides a higher-level framework-like experience (routing, data fetching, pre-rendering, layouts, HMR) while staying unopinionated about the UI framework.
- It supports multiple render modes per page (SSR, SSG, SPA) and works with React, Vue, Preact, etc.

Use it when you want Next.js-like features without committing to a full framework.

---

## 6. VitePress (SSG with SSR compatibility)

- VitePress is a markdown-first static site generator built on Vite and Vue. It pre-renders pages during production build (SSG) and provides SSR compatibility rules for custom theme code.
- VitePress optimizes static markdown content to reduce client JS payload and serializes build-time data loaders into the bundle.

---

## 7. Interview theory (concise answers)

1. **Why separate server and client entry points for SSR?**
   - Server needs rendering logic and must avoid browser-only APIs; client needs hydration code. Separating entries keeps builds correct and minimal.

2. **What does `ssr.noExternal` do?**
   - Bundles named dependencies into the server build instead of externalizing them; useful for ESM-only dependencies that Node cannot require by name.

3. **When to use vite-plugin-ssr vs Vite alone?**
   - Use `vite-plugin-ssr` to get routing, data loading, pre-rendering, and per-page render modes with less boilerplate. Use Vite alone for minimal or custom SSR setups.

4. **How does dev-mode SSR differ from production SSR in Vite?**
   - Dev: Vite runs a dev server and uses `ssrLoadModule` to run server code with native ESM and transforms. Prod: you build server and client bundles ahead of time and the server imports the built server bundle.

---

## 8. Coding / practical interview tasks

1. **Build a minimal Vite + React SSR app**
   - Create `entry-server.jsx` exporting `render(url)` and `entry-client.jsx` for hydration. Implement a Node server that uses Vite dev middleware to call `ssrLoadModule` in dev.

2. **Configure `ssr.noExternal` for an ESM-only dependency**
   - Demonstrate build failure when a dependency is externalized, then fix by adding it to `ssr.noExternal`.

3. **Pre-render a set of pages (SSG) with vite-plugin-ssr**
   - Configure `vite-plugin-ssr` to pre-render routes at build time and compare produced HTML files.

4. **Use VitePress data loaders**
   - Create a VitePress site with a data loader that reads local markdown/JSON during build and injects it into pages.

---

## 9. Best practices checklist

- [ ] Keep server entry lean and free of browser APIs.
- [ ] Use `ssr.noExternal` for ESM-only dependencies.
- [ ] Serve pre-built assets in production; use dev middleware only in development.
- [ ] Use `vite-plugin-ssr` for feature-rich apps needing routing/data-fetching and flexible render modes.
- [ ] Use VitePress for docs/content sites that benefit from static pre-rendering and markdown tooling.

---

*Generated to be previewable and downloadable as Markdown. Use the top-right download in this canvas to get the `.md` file.*

# Vite — Performance & Deployment

**Topic:** Vite

**Sub Topic:** Performance — esbuild, Rollup under the hood, cold start optimization

**Sub Topic 2:** Deployment — build output, asset base, static hosting setup

---

## Quick summary

Covers Vite's runtime architecture for performance (how esbuild and Rollup are used, why cold-start is fast), practical techniques to optimize dev cold-start and production builds, and deployment best practices: build output structure, `base`/`publicDir` config, static hosting considerations (Netlify, Vercel, custom servers), and common pitfalls.

---

## 1. How Vite achieves speed (esbuild + Rollup)

- **Dev (cold start & HMR):** Vite serves source files over native ESM and pre-bundles large dependencies using **esbuild** to avoid many small HTTP requests and to transform non-ESM packages to ESM. This makes the dev server start fast and HMR snappy. citeturn0search0turn0search5

- **Production build:** Vite delegates to **Rollup** for production bundling. Rollup performs tree-shaking, code-splitting, and optimized chunking to create small, cache-friendly bundles with hashed filenames. citeturn0search3turn0search4

- **Why both?** esbuild is extremely fast (written in Go) and ideal for quick transforms and dependency pre-bundling during dev. Rollup offers mature production optimizations and plugin ecosystem, producing high-quality final bundles. Vite currently uses both to get the best of both worlds. citeturn0search10turn0search21

---

## 2. Cold-start optimization (practical tips)

- **Dependency pre-bundling (`optimizeDeps`)**: Vite scans dependencies and pre-bundles them with esbuild into `node_modules/.vite/deps` so the browser makes fewer requests. Use `optimizeDeps.include`, `exclude`, or `force` to control behavior for tricky packages. citeturn0search5turn0search9

- **Caching:** Pre-bundled deps are cached on disk. On subsequent runs Vite reuses the cache unless you change the dependency graph or force a re-optimize. Use `optimizeDeps.force` for debugging. citeturn0search9

- **Avoid large, dynamic imports in entry modules:** Keep your entry module small so the dev server doesn't need to transform many files eagerly. Prefer lazy/dynamic `import()` for large feature sets or rarely-used libs.

- **Tune `optimizeDeps.esbuildOptions`**: For ESM-only packages that require special transforms, pass esbuild options to handle the syntax correctly. citeturn0search9

- **Minimize plugins that run at dev start:** Heavy plugins can slow dev server bootstrap. Use debug builds of plugins or toggle plugin usage in dev vs prod.

- **Keep node version and filesystem fast**: I/O and native platform can impact cold start; SSDs and newer Node versions help.

---

## 3. Production performance techniques

- **Code splitting & manualChunks**: Let Rollup split code and use `manualChunks` to create stable vendor chunks for long-term caching. Smaller initial payload = faster Time to Interactive. (See separate cheat sheet on chunking.) citeturn0search3

- **Tree-shaking friendly imports**: Prefer ESM/tree-shakeable packages (e.g., `lodash-es`) and import only what's needed.

- **Asset optimization**: Use `assetsInlineLimit` to inline tiny assets, compress images (plugins like `vite-plugin-imagemin`), and serve optimized images (responsive sizes, WebP). citeturn0search13

- **Generate pre-compressed assets**: Use `vite-plugin-compression` or server-side compression to serve `.br`/.gz files for smaller transfers. Configure your host to prefer pre-compressed assets.

- **Analyze bundles**: Use `rollup-plugin-visualizer` or similar to inspect bundle composition and spot large dependencies. citeturn0search3

---

## 4. Build output & asset base configuration

- **Default build**: `vite build` uses `index.html` as the entry and outputs static files in `dist/` by default. Files are hashed for cache-busting. citeturn0search3

- **`base` option**: Use `base` in `vite.config` to control the public path at which assets are served (useful when deploying to a subpath or CDN). Example: `base: '/my-app/'` so built assets reference `/my-app/assets/...`. citeturn0search3

- **`publicDir`**: Files in `public/` are copied as-is to the build output root and served at `/` in dev. Use `publicDir` to include static files that shouldn't be processed. citeturn0search17

- **Asset hashing & paths**: Vite hashes filenames by default. For single-page apps served from nested routes, configure the server to redirect 404s to `index.html` (SPA fallback) or set correct base path. See Netlify/Vercel docs for hosting specifics. citeturn0search12turn0search16

---

## 5. Static hosting & deployment (common targets)

- **Netlify**: Set build command `npm run build` and publish directory `dist`. For SPAs, configure redirects (`_redirects`) to route all requests to `index.html`. Netlify docs have Vite-specific tips. citeturn0search12

- **Vercel**: Vercel supports Vite out-of-the-box. Use `vercel.json` for custom headers or static routes; it will detect frameworks and run build automatically. citeturn0search16

- **Static servers (S3/CloudFront, GitHub Pages)**: Upload `dist/` to the static host, configure correct base paths and caching headers, and add SPA fallback rules if needed.

- **Custom servers / CDNs**: Serve files from `dist/`, set `Cache-Control` and `Content-Encoding` for compressed files. If serving from a subpath, set `base` during build.

---

## 6. Troubleshooting & common pitfalls

- **Broken asset paths after deploy**: Usually `base` is misconfigured. If hosting under a subpath (e.g., `https://host.com/app/`), set `base: '/app/'` before building. citeturn0search3

- **404s on refresh (SPA)**: Host must be configured to serve `index.html` for unknown routes (SPA fallback). Netlify/Vercel have guides for this. citeturn0search12turn0search16

- **Large `node_modules` causing slow dev start**: Use `optimizeDeps.include` to pre-bundle heavy deps, and `exclude` to avoid problematic packages. Clean cache if dependencies change unexpectedly. citeturn0search5turn0search9

---

## 7. Interview theory questions (concise answers)

1. **Q: Why does Vite start so fast compared to traditional bundlers?**
   - Because Vite serves native ESM modules in dev and only pre-bundles dependencies with esbuild instead of eagerly bundling the whole app. This avoids a full bundle step at startup. citeturn0search0

2. **Q: What roles do esbuild and Rollup play in Vite?**
   - esbuild is for fast dependency pre-bundling and transforms in dev; Rollup is used for production bundling and optimizations. citeturn0search5turn0search3

3. **Q: When should you configure `base` in Vite?**
   - When deploying to a subpath or CDN so that asset URLs reference the correct public path. citeturn0search3

4. **Q: How to fix 404s for client-side routes after deployment?**
   - Configure the host to serve `index.html` for unknown routes (SPA fallback) or use proper server rewrite rules. citeturn0search12turn0search16

---

## 8. Coding / practical interview tasks

1. **Measure dev cold start**: Create a Vite app and time `vite dev` startup. Add a large dependency and compare startup times with and without adding it to `optimizeDeps.include`.

2. **Build with different `base` values**: Build once with `base: '/'` and once with `base: '/my-app/'` and deploy to a subpath to observe asset path differences.

3. **Add pre-compression step**: Add `vite-plugin-compression` to the build and verify `.gz`/`.br` files in `dist/` and served responses include `Content-Encoding` when hosted.

4. **Analyze bundle composition**: Add `rollup-plugin-visualizer` to `vite.config` and inspect the generated `stats.html` to find large dependencies.

---

## 9. Quick config snippets

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  base: '/my-app/',
  plugins: [react()],
  build: {
    sourcemap: true,
    assetsInlineLimit: 4096
  },
  optimizeDeps: {
    include: ['lodash-es'],
    esbuildOptions: {
      target: 'es2020'
    }
  }
})
```

---

## 10. Resources

- Vite guide: Why Vite, Build, Dep pre-bundling, Assets, Deploying a static site. citeturn0search0turn0search3turn0search5turn0search13turn0search2
- Hosting guides: Netlify & Vercel Vite docs. citeturn0search12turn0search16

---

*This cheat sheet is previewable and downloadable as Markdown in the canvas top-right. Generated with references to Vite docs and community articles.*

