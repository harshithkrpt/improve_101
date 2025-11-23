# Next.js — Pages Router Cheat Sheet

**Topic**: Next.js

**Sub Topic**: Pages folder routing, dynamic routes, file-based routing

---

## Quick overview

- The **Pages Router** is Next.js's file-system based router: each file inside the `pages/` directory automatically becomes a route (e.g. `pages/about.js` → `/about`).
- The Pages Router co-exists with the newer **App Router** (the `app/` directory) but remains fully supported — you can use either depending on your project needs.

---

## Table of contents

1. Basics: file-based routing
2. Nested routes and folders
3. Dynamic routes (`[param]`)
4. Catch-all and optional catch-all (`[...slug]`, `[[...slug]]`)
5. Linking & client navigation
6. API routes in `pages/api`
7. Common pitfalls & migration notes (Pages ↔ App)
8. Interview theory questions + concise answers
9. Related coding interview questions (practical tasks)

---

## 1) Basics: file-based routing

- Any React component exported from `pages/*.js`, `pages/*.tsx` etc becomes a server route.
- `pages/index.js` is the root route `/`.
- `pages/blog/index.js` maps to `/blog`; `pages/blog/post.js` maps to `/blog/post`.

**Example**

```js
// pages/about.js
export default function About() {
  return <h1>About</h1>
}
```

---

## 2) Nested routes and folders

- Use directories to reflect URL hierarchy.

```
/pages
  /users
    index.js        -> /users
    [id].js         -> /users/:id
```

- `pages/_app.js` wraps all pages (global layout, providers).
- `pages/_document.js` controls HTML shell for SSR (custom `<html>` and `<body>`).

---

## 3) Dynamic routes (`[param]`)

- Bracket syntax makes a segment dynamic: `pages/posts/[id].js` maps `/posts/42` to `params.id === '42'`.
- On the page, access the param via `useRouter()` from `next/router` (client) or through `context.params` in `getStaticProps`/`getServerSideProps` (server).

**Example (SSG)**

```js
// pages/posts/[id].js
import { useRouter } from 'next/router'

export async function getStaticPaths() {
  return {
    paths: [{ params: { id: '1' } }, { params: { id: '2' } }],
    fallback: false,
  }
}

export async function getStaticProps({ params }) {
  // fetch post by params.id
  return { props: { id: params.id } }
}

export default function Post({ id }) {
  const router = useRouter()
  if (router.isFallback) return <div>Loading...</div>
  return <div>Post id: {id}</div>
}
```

---

## 4) Catch-all and optional catch-all

- `pages/docs/[...slug].js` matches `/docs/a`, `/docs/a/b/c` and exposes `params.slug` as an array.
- `pages/docs/[[...slug]].js` is optional: it matches `/docs` as well as `/docs/a/b`.

**Use-cases**: multi-level CMS pages, flexible nested paths.

---

## 5) Linking & client navigation

- Use `next/link` for client-side transitions and prefetching.

```jsx
import Link from 'next/link'

<Link href="/posts/1">View post</Link>
```

- For programmatic navigation use `useRouter()` and `router.push('/path')`.

---

## 6) API routes in `pages/api`

- Files under `pages/api/*` become serverless API endpoints.

```js
// pages/api/hello.js
export default function handler(req, res) {
  res.status(200).json({ message: 'hello' })
}
```

- If using the App Router, route handlers in `app/` are the recommended alternative.

---

## 7) Common pitfalls & migration notes

- Pages Router and App Router can coexist, but decide on conventions for consistency.
- `getStaticProps` / `getServerSideProps` and `getStaticPaths` belong to the Pages Router; App Router uses `fetch`, Server Components, and special conventions.
- Remember `pages/_app.js` and `pages/_document.js` behavior when migrating.

---

## 8) Interview theory questions (concise answers)

Q1: What is file-based routing in Next.js?  
A: A convention where files and folders inside `pages/` map directly to routes; filenames determine the URL structure.

Q2: How do you create a dynamic route?  
A: Wrap the segment in square brackets, e.g. `pages/users/[id].js` and access `id` via router or data-fetching context.

Q3: What is `getStaticProps` vs `getServerSideProps`?  
A: `getStaticProps` runs at build time to produce static pages (good for SSG); `getServerSideProps` runs on every request (SSR).

Q4: When to use catch-all routes?  
A: When a route must match variable-depth segments (e.g., CMS pages), use `[...slug]`; add double brackets `[[...slug]]` to make it optional.

Q5: How do API routes differ from App Router route handlers?  
A: API routes live in `pages/api` and behave like serverless endpoints; App Router route handlers live in `app/` and integrate with React server components and new conventions.

---

## 9) Related coding / interview tasks (practical)

1. Implement a blog with `pages/posts/[slug].js`, SSG using `getStaticPaths` and `getStaticProps`.
2. Create a catch-all product page `pages/shop/[[...slug]].js` that renders category/product pages depending on `params.slug`.
3. Build an API route `pages/api/subscribe.js` to accept POST requests (body parsing and status codes).
4. Migrate a small `pages/` app to `app/` for a single page — list the required changes (layout, data fetching, page -> server components).

---

## References & further reading

- Official Next.js Pages Router docs — Next.js website
- Dynamic routes & catch-all segments — Next.js docs
- API routes — Next.js docs

---

*Generated: Next.js Pages Router cheat sheet — ready for quick study and interview prep.*

# Next.js — App Router vs Pages Router

**Topic**: Next.js

**Sub Topic**: App Router vs Pages Router — `app/` directory, `layout.tsx`, Server & Client Components

---

## Quick summary

- **Pages Router** (`pages/`) is the older, battle-tested file-based router where files in `pages/` map to routes and data-fetching helpers like `getStaticProps` / `getServerSideProps` are used.
- **App Router** (`app/`) is the newer router built around React Server Components, nested `layout.tsx` files, streaming, and simplified data fetching (server-first by default). Use `app/` to leverage layouts, server components, and improved routing patterns.

---

## Table of contents

1. High-level differences
2. `app/` folder conventions: `layout.tsx`, `page.tsx`, `loading.tsx`, `error.tsx`
3. Server Components vs Client Components (`'use client'` directive)
4. Data fetching comparison (Pages helpers vs App Router approach)
5. Migration and coexistence notes
6. Interview theory Q&A (concise answers)
7. Related coding tasks (practical interview questions)

---

## 1) High-level differences

- **Routing style**: both are file-system-based, but the App Router is segment-and-layout oriented (nested layouts) while Pages Router maps pages directly to files.
- **Rendering model**: App Router defaults to React Server Components (RSC) for pages/layouts — less client JS by default. Pages Router historically used client-side React components and SSG/SSR helpers.
- **Data fetching**: Pages Router uses `getStaticProps`, `getServerSideProps`, and `getStaticPaths`. App Router encourages async server components, `fetch` with caching/revalidation, and server actions (and server functions).
- **Layouts**: App Router introduces colocated, nested `layout.tsx` files that persist state/UI between navigations; Pages Router uses `_app.js`/`_document.js` for global behavior but not nested per-segment layouts.
- **API/Edge**: Pages Router uses `pages/api/*` for API routes; App Router uses route handlers colocated in `app/` when desired (more flexible for server functions).

---

## 2) `app/` folder conventions

Basic structure:

```
/app
  layout.tsx        -> shared layout (required root layout)
  page.tsx          -> route entry (like index)
  loading.tsx       -> suspense/loading UI for async segments
  error.tsx         -> error boundary for segment
  (segment)/
    layout.tsx
    page.tsx
```

- `app/layout.tsx` must be the root layout and include `<html>` and `<body>` tags.
- `layout.tsx` files are nested: a child layout composes inside parent layouts, enabling UI that persists across navigations.

**Example root layout (TypeScript)**

```tsx
// app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

---

## 3) Server Components vs Client Components

- **Server Components (default in `app/`)**
  - Render on the server, can access server-side resources (databases, secrets) without shipping them to the client.
  - They reduce client JS bundle size and improve initial performance.
  - They can be async and fetch data directly.

- **Client Components**
  - Marked by the top-line directive: `"use client"` (must be the first line).
  - Required for interactive features: hooks (`useState`, `useEffect`), browser APIs, event handlers.
  - Client Components can be nested inside Server Components so only interactive parts become client-side.

**Rule of thumb**: make UI Server Components by default; add `use client` only for parts that need interactivity.

---

## 4) Data fetching comparison

- **Pages Router**: `getStaticProps` (build-time), `getServerSideProps` (per-request), `getStaticPaths` (dynamic paths).
- **App Router**: fetch in server components (async `page.tsx` or layout), use `fetch()` with `{ next: { revalidate: X } }` for ISR-like behavior, and server actions (for mutations) using `export const actions = {}` patterns and/or `use server` (framework-specific directives may vary across versions).

**Example (App Router page)**

```tsx
// app/blog/page.tsx (server component)
async function getPosts() {
  const res = await fetch('https://.../posts', { cache: 'no-store' })
  return res.json()
}

export default async function BlogPage() {
  const posts = await getPosts()
  return (
    <main>
      {posts.map(p => <article key={p.id}>{p.title}</article>)}
    </main>
  )
}
```

---

## 5) Migration & coexistence

- Both routers can coexist in the same app — but a single route path cannot be defined in both `app/` and `pages/` simultaneously.
- Migration guides recommend incremental migration: move pages into `app/` under a new folder (e.g., `/app/new`) and adapt patterns gradually.
- Mind differences: `_app.js`/`_document.js` semantics are different; App Router relies on nested `layout.tsx` and Server Components.

---

## 6) Interview theory Q&A (concise answers)

Q1: What is the App Router?  
A: A file-system router using the `app/` directory that leverages React Server Components, nested layouts, and async server-first data fetching.

Q2: Why use `layout.tsx`?  
A: To define nested, persistent UI across child routes (root layout required and must include `<html>`/`<body>`).

Q3: How do you opt a component into client-side behavior?  
A: Add `"use client"` as the first line in the file to make it a Client Component.

Q4: When should you keep using Pages Router?  
A: When you maintain a legacy codebase that relies heavily on `getStaticProps`/`getServerSideProps` or when incremental migration is desired; Pages is still supported.

Q5: How do Server Components help performance?  
A: They offload rendering to the server, avoid shipping component code and data to the client, and allow streaming and selective hydration of interactive parts.

---

## 7) Related coding interview tasks

1. Implement a nested layout with `app/layout.tsx` and a child `dashboard/layout.tsx` that preserves sidebar state across route changes.
2. Build an `app/blog/page.tsx` that fetches posts server-side and a nested `app/blog/[slug]/page.tsx` for post pages.
3. Convert a `pages/api/subscribe.js` endpoint to an App Router route handler in `app/api/subscribe/route.ts`.
4. Create a small interactive widget as a Client Component (`use client`) and compose it inside a Server Component page.

---

*End of cheat sheet. Use this file for interview prep and quick reference.*

# Next.js — Data Fetching Cheat Sheet

**Topic**: Next.js

**Sub Topic**: getStaticProps, getServerSideProps, revalidation (ISR) — Pages & App Router

---

## Quick overview

- **getStaticProps** (Pages Router): runs at build time to pre-render pages. Can be combined with **Incremental Static Regeneration (ISR)** by returning a `revalidate` value to refresh pages in the background. Use when content is mostly static and benefits from fast CDN delivery.
- **getServerSideProps** (Pages Router): runs on every request (server-side rendering). Use when you need fresh, per-request data (e.g., authentication-based content, rapidly changing data).
- **App Router / fetch revalidation**: in the `app/` directory, use async Server Components with `fetch()` that support `next.revalidate` or export `revalidate` from a segment to control cache and ISR-like behavior. App Router encourages server-first data fetching with granular cache controls.

---

## Table of contents

1. getStaticProps — usage, return values, examples
2. getServerSideProps — usage, examples
3. Incremental Static Regeneration (ISR) & revalidation patterns
4. App Router equivalents (fetch + revalidate, export const revalidate)
5. When to use which pattern — decision matrix
6. Performance & caching considerations
7. Interview theory Q&A (concise answers)
8. Related coding interview tasks

---

## 1) getStaticProps

- Runs at build time to generate static HTML for a page.
- Returns an object with `{ props, revalidate?, notFound?, redirect? }`.
- `revalidate` (seconds) enables ISR — Next.js will serve the static page and re-generate it in the background when the cached page is older than `revalidate` seconds.

**Example**

```js
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/posts')
  const posts = await res.json()
  return { props: { posts }, revalidate: 60 } // revalidate every 60s
}
```

**Notes**: In development, `getStaticProps` runs on every request. It does not have access to the raw `req`/`res` objects and thus cannot access request headers or cookies for personalization. Use `getServerSideProps` for per-request needs. citeturn0search6turn0search9

---

## 2) getServerSideProps

- Runs on the server on every request and can access `req`/`res`.
- Useful for user-specific content, authentication, or frequently changing data.

**Example**

```js
export async function getServerSideProps(context) {
  const { req } = context
  const token = req.cookies.token
  const res = await fetch('https://api.example.com/private', { headers: { Authorization: token } })
  const data = await res.json()
  return { props: { data } }
}
```

**Notes**: Higher latency/cost per request compared to static strategies; not cached by default. citeturn0search3

---

## 3) Incremental Static Regeneration (ISR) & revalidation

- ISR allows static pages to be updated after build time without a full rebuild. Two main approaches:
  1. **Time-based revalidation**: set `revalidate` in `getStaticProps` (Pages Router) or export `revalidate` / use `next.revalidate` in `app/` fetchs (App Router). Next.js will regenerate the page in the background when stale.
  2. **On-demand revalidation**: call Next.js' revalidation API (`res.revalidate()` from a server/route handler or Vercel-provided revalidation endpoints) to trigger regeneration for a path immediately.

**Example (on-demand ISR)**

```js
// pages/api/revalidate.js
export default async function handler(req, res) {
  // verify webhook token
  await res.revalidate('/posts/42')
  return res.json({ revalidated: true })
}
```

**Notes**: ISR lets you scale to millions of pre-rendered pages while still keeping content fresh. citeturn0search0turn0search4turn0search17

---

## 4) App Router equivalents (fetch + revalidate)

- In `app/` routes, prefer async Server Components and use `fetch()` with `{ next: { revalidate: seconds } }` or export `export const revalidate = 60` in a segment to declare revalidation. This provides fine-grained caching per-request or per-segment.

**Example**

```tsx
export const revalidate = 60
export default async function Page() {
  const posts = await fetch('https://api.example.com/posts', { next: { revalidate: 60 } }).then(r => r.json())
  return <PostsList posts={posts} />
}
```

**Notes**: The App Router's fetch cache and revalidation semantics are more flexible and integrate with React Server Components and nested layouts. citeturn0search2turn0search19

---

## 5) When to use which pattern (decision matrix)

- Use `getStaticProps` + ISR when:
  - Content is mostly static but updated periodically (blogs, docs, marketing). Improves performance and reduces server cost.
- Use `getServerSideProps` when:
  - Content must be fresh on every request or relies on request-specific data (auth, per-user content).
- Use App Router `fetch` + `revalidate` when:
  - You want server components with fine-grained cache controls, nested layouts, and streaming.

---

## 6) Performance & caching considerations

- Static pages served from CDN are fastest and cheapest. ISR adds background regeneration to keep them fresh.
- SSR (`getServerSideProps`) costs CPU and increases latency per request — cache proxied responses where possible.
- Avoid over-fetching: request only needed data and set sensible revalidation intervals.
- For highly dynamic sections mixed into largely static pages, prefer Server Components + Client Components composition in `app/`.

References: Next.js docs for `getStaticProps`, `getServerSideProps`, ISR, and caching. citeturn0search6turn0search3turn0search17turn0search13

---

## 7) Interview theory Q&A (concise answers)

Q1: When would you use `getStaticProps` instead of `getServerSideProps`?  
A: Use `getStaticProps` when page content can be generated at build time and served statically; add ISR (`revalidate`) if it needs periodic updates. Use `getServerSideProps` when the content depends on the incoming request or must be fresh on every request. citeturn0search6turn0search3

Q2: How does ISR work?  
A: ISR serves a pre-built static page and regenerates it in the background when the `revalidate` interval expires or when triggered on-demand; users receive the cached page while regeneration occurs. citeturn0search17turn0search0

Q3: How do you perform on-demand revalidation?  
A: Expose a server route (API route or App Router route handler) and call the framework revalidate function (`res.revalidate()` or the server utilities) after validating the request. citeturn0search0turn0search4

Q4: Can `getStaticProps` access request headers or cookies?  
A: No — `getStaticProps` runs at build time and doesn't receive `req`/`res`. For request-scoped data, use `getServerSideProps`. citeturn0search9

Q5: What's the App Router equivalent of `revalidate`?  
A: Use `fetch(..., { next: { revalidate } })` or export `export const revalidate = N` in a segment to enable ISR-like behavior. citeturn0search2turn0search16

---

## 8) Related coding interview tasks

1. Implement a blog with `pages/posts/[slug].js` using `getStaticPaths` + `getStaticProps` and `revalidate: 60`.
2. Create an admin webhook `pages/api/publish.js` that calls `res.revalidate('/posts/[slug]')` to trigger on-demand ISR after a new post is published.
3. Build an `app/blog/page.tsx` using `fetch(..., { next: { revalidate: 120 } })` and a nested dynamic `app/blog/[slug]/page.tsx`.
4. Convert an SSR `getServerSideProps` page to SSG + ISR and explain trade-offs (latency, cache invalidation, SEO).

---

*End of cheat sheet.*

# Next.js — Rendering Modes Cheat Sheet

**Topic**: Next.js

**Sub Topic**: Rendering Modes — SSR, SSG, ISR, CSR (differences and use cases)

---

## Quick summary

This cheat sheet explains the four primary rendering modes you'll encounter in Next.js:

- **SSR (Server-Side Rendering):** HTML is generated on each request on the server.
- **SSG (Static Site Generation):** HTML is generated at build time and served statically.
- **ISR (Incremental Static Regeneration):** SSG + background revalidation to keep static pages fresh.
- **CSR (Client-Side Rendering):** The browser renders content using JavaScript after initial load.

Use the right tool for each route; hybrid strategies are common (static shell + client-side widgets, or static pages with dynamic SSR-recommended segments).

---

## Table of contents

1. Definitions
2. How they work (step-by-step)
3. Performance & SEO implications
4. When to use each (use cases)
5. Trade-offs and common pitfalls
6. Interview theory Q&A (concise answers)
7. Related coding tasks (practical)

---

## 1) Definitions

- **SSR (Server-Side Rendering)**: Render HTML on the server at request time (Next.js `getServerSideProps` or App Router dynamic server rendering). Good for frequently-changing, per-request content.

- **SSG (Static Site Generation)**: Pre-render HTML at build time (`getStaticProps` / `getStaticPaths` in Pages Router, or using `export const revalidate` in App Router). Fast, cacheable, ideal for stable content.

- **ISR (Incremental Static Regeneration)**: Allows static pages to be regenerated after build time — either time-based (`revalidate`) or on-demand (revalidate API). Users receive the cached static content while a background regeneration occurs.

- **CSR (Client-Side Rendering)**: Initial HTML is minimal (shell); JavaScript in the browser fetches data and renders content dynamically. Useful for highly interactive parts that don’t need SEO.

---

## 2) How they work (step-by-step)

- **SSR**
  1. Client requests page.
  2. Server runs data-fetching code, renders React to HTML.
  3. Server returns fully-rendered HTML + JS bundle for hydration.

- **SSG**
  1. During build, framework runs data-fetching and outputs HTML files.
  2. CDN serves static HTML instantly to users; hydration occurs client-side.

- **ISR**
  1. Page served from CDN as with SSG.
  2. When cache age > `revalidate` or on-demand revalidation is triggered, server regenerates the page in the background.
  3. New version replaces the old on subsequent requests.

- **CSR**
  1. Server returns a minimal HTML shell.
  2. Browser downloads JS, fetches data from APIs, renders UI.

---

## 3) Performance & SEO implications

- **SSG/ISR**: Best for performance (CDN-cached HTML) and SEO because crawlers get fully-rendered HTML. ISR adds freshness while keeping SSG benefits.
- **SSR**: Good for SEO and freshest content, but each request costs CPU and adds latency compared to static pages.
- **CSR**: Lower initial SEO value unless content is hydrated or rendered server-side; initial load often slower for first contentful paint but can be snappier for subsequent interactions.

---

## 4) When to use each (use cases)

- **SSG**: Blogs, marketing pages, docs, landing pages — content changes infrequently.
- **ISR**: Large sites with many pages (e-commerce catalogs, docs with frequent updates) where you want CDN speed but periodic freshness.
- **SSR**: Personalized dashboards, admin panels, pages that depend on request-specific headers/cookies or require up-to-the-second data.
- **CSR**: Highly interactive widgets, single-page app parts (e.g., complex client-only visualizations) or when server-rendered HTML isn’t needed for SEO.

Hybrid example: SSG for article pages + CSR for comments widget; or SSG listing pages + SSR/edge for price-sensitive parts.

---

## 5) Trade-offs and common pitfalls

- Overusing SSR increases server cost and latency. Measure and only SSR where necessary.
- Over-relying on CSR can harm SEO for public content; combine SSG/SSR with CSR for interactivity.
- Misconfiguring `revalidate` intervals can either overtax your regeneration pipeline (too short) or leave content stale (too long).
- Remember caching layers (CDN, browser, server) — invalidation matters.

---

## 6) Interview theory Q&A (concise answers)

Q1: What’s the main difference between SSR and SSG?  
A: SSR renders pages on every request on the server; SSG pre-renders pages at build time.

Q2: How does ISR help at scale?  
A: ISR lets you keep the CDN-delivered speed of static pages while allowing background regeneration to refresh content, enabling millions of pages without full rebuilds.

Q3: When is CSR the right choice?  
A: When content is user-specific or highly interactive and SEO/first-load HTML isn’t required.

Q4: How do you perform on-demand revalidation?  
A: Use Next.js revalidate APIs via a server route (or App Router route handler) to trigger regeneration for a path after verifying the request.

Q5: Which rendering mode is best for SEO?  
A: SSG and SSR are best for SEO since they provide pre-rendered HTML to crawlers; ISR also provides SEO-friendly static pages with freshness.

---

## 7) Related coding tasks

1. Implement a blog with `getStaticPaths` + `getStaticProps` and `revalidate: 60` for ISR.  
2. Build a product page using SSR (`getServerSideProps`) that reads cookies to personalize offers.  
3. Create a static marketing site (SSG) and add a CSR comment widget fetching an API client-side.  
4. Implement an API route to call `res.revalidate('/posts/[slug]')` for on-demand ISR.

---

*End of cheat sheet.*

# Next.js — Server Components Cheat Sheet

**Topic**: Next.js

**Sub Topic**: Server Components — data fetching in server layer, client boundaries

---

## Quick overview

- Server Components (RSC) run on the server by default and are the core of the App Router's rendering model. They let you fetch data, access server-only resources (databases, files, secrets), and render UI without sending component code to the client.
- Client Components are marked with the `'use client'` directive and create a client boundary — they are bundled and run in the browser for interactivity.

---

## Table of contents

1. What are Server Components?
2. Data fetching in the server layer — patterns & APIs
3. Client boundaries and the `'use client'` directive
4. Server Actions and mutations
5. Best practices & performance patterns
6. Common pitfalls
7. Interview theory Q&A (concise answers)
8. Related coding interview tasks

---

## 1) What are Server Components?

- Server Components are React components executed on the server. They can be async, use `await` directly, and fetch data during rendering without client-side lifecycle hooks.
- They help minimize client JavaScript since only interactive parts (Client Components) are shipped to the browser.

---

## 2) Data fetching in the server layer — patterns & APIs

- **Direct fetch in Server Components**: use `fetch()` (or any server-side library/ORM) inside async Server Components or `page.tsx`/`layout.tsx` to retrieve data. Use the `next` options (`{ next: { revalidate } }`) to control caching and ISR-like behavior.

```tsx
// app/blog/page.tsx (Server Component)
export const revalidate = 60
export default async function BlogPage() {
  const res = await fetch('https://api.example.com/posts', { next: { revalidate: 60 } })
  const posts = await res.json()
  return (
    <main>
      {posts.map(p => <article key={p.id}>{p.title}</article>)}
    </main>
  )
}
```

- **Use `server-only` & `cache` utilities**: mark modules as server-only (`import 'server-only'`) and use `cache` from React to memoize expensive fetches across requests within server runtime.

- **Preload pattern**: export utility functions that call cached fetches and optionally preload data for navigation to reduce TTFB.

- **Route Handlers**: for API-like endpoints colocated in `app/api/*/route.ts` use server code to expose REST/JSON endpoints; helpful for client components to call.

---

## 3) Client boundaries and the `'use client'` directive

- Place `'use client'` at the top of files that need React hooks, browser APIs, event handlers, or local state.
- The directive creates a boundary: once a component is marked client, all its imports become client-side as well (they will be bundled into the client JS). Keep client subtrees small to avoid shipping unnecessary JS.

```tsx
// app/ui/LikeButton.tsx
'use client'
import { useState } from 'react'
export default function LikeButton({ id }: { id: string }) {
  const [liked, setLiked] = useState(false)
  return <button onClick={() => setLiked(v => !v)}>{liked ? '♥' : '♡'}</button>
}
```

- Best practice: fetch data in Server Components and pass it as props to Client Components for interactive behavior.

---

## 4) Server Actions and mutations

- Server Actions are async functions that run on the server but can be invoked from Client Components. They simplify form handling and mutations without writing explicit API endpoints.

```tsx
// app/actions.ts
export async function addComment(data: FormData) {
  'use server'
  // server-side logic: insert into DB
}

// app/post/page.tsx (Server Component)
import CommentForm from './CommentForm'
export default function Post({ post }) {
  return <CommentForm />
}

// app/post/CommentForm.tsx ('use client')
'use client'
import { addComment } from '../actions'
export default function CommentForm() {
  return (
    <form action={addComment}>
      <input name="text" />
      <button type="submit">Add</button>
    </form>
  )
}
```

- Server Actions can improve DX and reduce boilerplate but must be used with care (validate inputs, authenticate, handle idempotency).

---

## 5) Best practices & performance patterns

- Fetch on the server where possible; keep Client Components minimal (UI only).
- Use `revalidate` and the App Router's caching features to balance freshness and performance.
- Cache heavy server fetches with `cache()` or a shared server-only data layer to avoid redundant calls.
- Preload data for likely navigation targets to improve perceived performance.

---

## 6) Common pitfalls

- Accidentally marking large modules as client by importing them into a `'use client'` file.
- Trying to use client-only APIs (e.g., `window`, `localStorage`) inside Server Components.
- Forgetting to secure Server Actions (they run on the server and must validate/authenticate inputs).

---

## 7) Interview theory Q&A (concise answers)

Q1: What are Server Components and why use them?  
A: Server Components run on the server, let you fetch data and access server-only resources during render, and reduce client JS by shipping only interactive parts.

Q2: How do you mark a component as a Client Component?  
A: Add `'use client'` as the first line in the module; this creates a client boundary and bundle.

Q3: Where should data fetching happen in an App Router app?  
A: Prefer Server Components (async code inside `page.tsx`/`layout.tsx`) for data fetching; pass data to Client Components as props.

Q4: What are Server Actions?  
A: Server Actions are server-side async functions callable from the client to handle mutations without separate API routes.

Q5: How do you avoid shipping unnecessary JS to the client?  
A: Keep client boundaries small, avoid importing heavy libraries in `'use client'` modules, and use Server Components for non-interactive UI and data logic.

---

## 8) Related coding interview tasks

1. Implement `app/blog/page.tsx` as a Server Component that fetches posts (cached) and renders a `LikeButton` Client Component for each post.
2. Create a `server-only` data layer with `cache()` and a preload pattern to optimize repeated fetches.
3. Build a comment form using Server Actions to insert comments into a mock DB without creating an explicit API route.
4. Identify a page where a Client Component was accidentally made global; refactor to minimize client bundle size.

---

*End of cheat sheet.*

# Next.js — Static Assets & Images Cheat Sheet

**Topic**: Next.js

**Sub Topic**: next/image optimization, public folder, static asset handling

---

## Quick overview

This cheat sheet explains how Next.js handles static assets and images, focusing on the `public/` folder, `next/image` optimization, caching, and best practices for performance and deploy-time behavior.

---

## Table of contents

1. `public/` folder & static files
2. `next/image` (Image component) — features and API
3. Configuration (next.config.js): images, remotePatterns, localPatterns
4. Caching & headers for static assets
5. On-demand image optimization, Image CDN, and unoptimized images
6. Best practices and performance checklist
7. Interview theory Q&A (concise answers)
8. Related coding interview tasks

---

## 1) `public/` folder & static files

- The `public/` directory at the project root is the place for static assets that you want served as-is from the root path (`/`).
- Anything placed in `public/avatars/me.png` is accessible at `/avatars/me.png` after build and on the server.
- The `public/` folder is not intended to be modified at runtime after deployment; it’s static content baked into the build output.

**Usage example**

```html
<!-- reference a public asset in HTML/JSX -->
<img src="/avatars/me.png" alt="me" />
```

Note: prefer `next/image` for optimized images, but `public/` is fine for static files, favicons, robots.txt, etc.

---

## 2) `next/image` (Image component)

- `next/image` is the recommended component to serve images: it provides automatic size optimization, responsive variants, modern formats (WebP/AVIF when supported), layout stability, and lazy loading.
- Required props for local/static images: `src`, `width`, `height`, and `alt`. You can also use `fill` layout to have the image fill a container.
- Supports attributes: `priority` (preload important images), `loading` (lazy by default, `eager` for above-the-fold), `placeholder='blur'` with `blurDataURL` for a blur-up effect.
- For remote images, configure `remotePatterns` in `next.config.js` to allow external origins to be optimized.

**Example**

```jsx
import Image from 'next/image'

export default function Avatar() {
  return <Image src="/me.png" width={120} height={120} alt="me" />
}
```

---

## 3) Configuration: `next.config.js`

- `images.remotePatterns` or `images.localPatterns` lets you whitelist external or local paths that the Image Optimization API can fetch and resize. This is a security step.
- You can set custom `deviceSizes`, `imageSizes`, and default loader behaviors in `next.config.js`.

**Basic example**

```js
module.exports = {
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: 'images.example.com', pathname: '/**' }
    ]
  }
}
```

---

## 4) Caching & headers for static assets

- Static files under `public/` and `_next/static/*` are typically served with cache-friendly `Cache-Control` headers (long `max-age` + `immutable`) to allow CDNs/browser caching.
- You can add custom headers for specific paths via the `headers` key in `next.config.js`, but note that in some hosting setups (or when using an Image CDN) those headers may be overridden by the platform’s CDN behavior — test on your target platform.

**Example header config**

```js
// next.config.js
module.exports = {
  async headers() {
    return [
      {
        source: '/(.*).(jpg|jpeg|png|gif|webp)',
        headers: [
          { key: 'Cache-Control', value: 'public, max-age=31536000, immutable' }
        ]
      }
    ]
  }
}
```

---

## 5) On-demand image optimization, Image CDN, and `unoptimized`

- Next.js can optimize images on-demand (server-side resizing/format conversion). For large scale, you may use the Next.js Image CDN or a third-party image CDN to offload work and gain global caching.
- If you use Image CDN features, be aware the CDN may serve images with its own headers; configuration and header behavior can differ between platforms.
- For some use-cases (like pre-optimized images or a custom external image pipeline), you can mark `<Image unoptimized />` or bypass the Image Optimization API.

---

## 6) Best practices & performance checklist

- Prefer `next/image` for public-facing images to get automatic optimization and better Lighthouse scores.
- Use `priority` for hero images that should be preloaded; leave the rest lazy-loaded.
- Provide `width` and `height` (or `fill`) to avoid layout shift.
- Use `placeholder='blur'` with `blurDataURL` for nicer perceived loading of images.
- Leverage `remotePatterns` to whitelist allowed remote sources; avoid enabling broad remote access.
- Compress and pre-convert large assets to modern formats where possible (WebP/AVIF) before uploading.
- Configure cache headers for static assets; when deploying, verify CDN behavior and adjust headers as needed.

---

## 7) Interview theory Q&A (concise answers)

Q1: Where should I put static files in a Next.js project?  
A: Put static assets in the `public/` folder to serve them from the root path; use `next/image` for optimized images.

Q2: Why use `next/image` instead of `<img>`?  
A: `next/image` provides automatic optimization (size, format), lazy loading, layout stability, and optional placeholders — improving performance and UX.

Q3: How do you allow external images to be optimized?  
A: Configure `images.remotePatterns` (or `localPatterns`) in `next.config.js` to whitelist remote hosts or local paths for optimization.

Q4: How do you handle caching for static assets?  
A: Static assets are served with cache-friendly headers by default; you can add path-based headers via `next.config.js` `headers()` but verify platform/CDN behavior.

Q5: When would you use `unoptimized`?  
A: Use `unoptimized` when images are already optimized and served by an external CDN or when you want to bypass Next.js image optimization entirely.

---

## 8) Related coding interview tasks

1. Build a component that uses `next/image` to display responsive images for different breakpoints and uses `placeholder='blur'` for the hero image.  
2. Configure `next.config.js` to allow images from `https://cdn.example.com` and add a custom header for `/images/*` assets.  
3. Create a small script to pre-generate `blurDataURL` placeholders for a set of static images and wire them into components.  
4. Migrate a legacy app that uses `<img>` tags to `next/image` and measure performance improvements (Lighthouse metrics).

---

*End of cheat sheet.*

# Topic : Next.js

## Sub Topic : Routing & Navigation (useRouter, Link, Dynamic Routes, Nested Layouts)

---

### Overview

This cheat sheet covers both the **App Router** (recommended for Next.js 13+) and the legacy **Pages Router**, focusing on file-system routing, `Link`, `useRouter` (and the App-router equivalents), dynamic route segments, nested layouts, shallow routing, and typical data-fetching patterns tied to routes.

---

## 1) File-system routing basics

- **Pages Router** (legacy): `pages/` folder maps files to routes. `pages/index.js` → `/`, `pages/blog/[slug].js` → `/blog/:slug`.
- **App Router** (recommended): `app/` folder with `page.js/tsx`, `layout.js/tsx`, and special files like `loading.js` and `error.js`. Nested folders correspond to nested routes and layouts.

**When to prefer App Router:** it supports Server Components, streaming, React Suspense, and colocated layouts. If starting a new project, prefer `app/`. (Pages Router still supported for some use-cases.)

---

## 2) Navigating: `Link`, client transitions, prefetching

- Use `next/link`'s `<Link href="/path">` for client-side transitions. It wraps an anchor and enables prefetching.
- App Router supports automatic prefetching and streaming; avoid adding `prefetch={false}` unless you need to.
- For imperative navigation use `useRouter().push()` (Pages) or `useRouter()` / `usePathname` / `useSearchParams` in App Router client components.

**Example — Link (App or Pages):**

```jsx
import Link from 'next/link'

export default function Nav(){
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/blog/hello-world">Post</Link>
    </nav>
  )
}
```

---

## 3) Imperative routing: `useRouter` (Pages) and App-router hooks

### Pages Router

```jsx
import { useRouter } from 'next/router'

function Component(){
  const router = useRouter()
  const go = () => router.push('/dashboard')
  // shallow routing: router.push('/?page=2', undefined, { shallow: true })
}
```

### App Router (Client component)

App Router splits responsibilities: `useRouter()` is lighter; prefer `usePathname`, `useSearchParams`, and `useParams` inside client components for reading route state.

```jsx
'use client'
import { useRouter, usePathname } from 'next/navigation'

export default function Cmp(){
  const router = useRouter()
  const pathname = usePathname()
  return <button onClick={() => router.push('/about')}>Go</button>
}
```

**Note:** In App Router, `useRouter()` does not return `query`; use `useSearchParams()` and `useParams()` instead.

---

## 4) Dynamic routes

### Pages Router style

- Create `pages/posts/[id].js` to capture `/posts/42`.
- For SSG with dynamic routes use `getStaticPaths` + `getStaticProps` to pre-render specific paths.

```js
// pages/posts/[id].js
export async function getStaticPaths(){
  return { paths: [{ params: { id: '1' } }], fallback: 'blocking' }
}

export async function getStaticProps({ params }){
  const post = await fetchPost(params.id)
  return { props: { post } }
}
```

### App Router style

- Create `app/posts/[id]/page.js` and use `params` passed to the page/server component.
- Use `generateStaticParams()` to statically generate dynamic routes at build time.

```js
// app/posts/[id]/page.js
export default function PostPage({ params }){
  return <div>Post id: {params.id}</div>
}

// optionally
export async function generateStaticParams(){
  const posts = await fetchAllIds()
  return posts.map(id => ({ id }))
}
```

---

## 5) Nested layouts & route composition (App Router)

- Create `app/dashboard/layout.js` to provide a persistent layout for any `app/dashboard/*` route.
- Layouts can be nested and can include shared UI (sidebars, nav) that persists across child page navigations.

```jsx
// app/layout.js  (root)
export default function RootLayout({ children }){
  return (<html><body>{children}</body></html>)
}

// app/dashboard/layout.js
export default function DashboardLayout({ children }){
  return (<div className="dashboard"> <Sidebar/> <main>{children}</main></div>)
}
```

**Key idea:** Layouts persist across client navigations, so component state inside a layout survives child page changes.

---

## 6) Shallow routing & partial updates

- Shallow routing (Pages Router) allows URL change without running full data fetching again: `router.push('/?tab=2', undefined, { shallow: true })`.
- Use with care—works only within the same page and can cause mismatches if server data is expected to refresh.

---

## 7) Route protection & middleware

- Protect routes by checking auth state in layouts, server components, or using Next.js Middleware for edge-level checks.
- Middleware runs before the request and can rewrite/redirect based on cookies, headers, etc.

---

## 8) Common pitfalls & gotchas

- In App Router, `useRouter()` is **different** from Pages Router. `query` is not returned — use `useSearchParams` and `useParams`.
- Client-side hooks (usePathname, useSearchParams, useParams) only work in Client Components (`'use client'`).
- Overusing prefetch for thousands of links may waste bandwidth; rely on Next.js intelligent prefetching.

---

## Interview theory questions (concise answers)

1. **Q:** Difference between Pages and App Router?
   **A:** Pages Router maps `pages/` files to routes; App Router (app/) supports nested layouts, server components, streaming and colocated data fetching; App Router is recommended for new apps.

2. **Q:** How do you create a dynamic route in Next.js App Router?
   **A:** Create a folder with `[param]` (e.g., `app/posts/[id]/page.js`) and read `params` in the page or `generateStaticParams()` for SSG.

3. **Q:** What is shallow routing?
   **A:** A router push that changes URL without calling data fetching methods again—useful for small UI state changes.

4. **Q:** How do nested layouts affect state?
   **A:** Layouts persist between child navigations, so state inside a layout is preserved while only leaf pages re-render.

5. **Q:** When use `getStaticPaths` vs `generateStaticParams`?
   **A:** `getStaticPaths` is Pages Router SSG; `generateStaticParams` is App Router equivalent for statically generated dynamic routes.

---

## Coding-style & practical tasks (short)

1. Build a `blog` with list page (`/blog`) and dynamic post routes (`/blog/[slug]`) using App Router and `generateStaticParams`.
2. Implement a dashboard with `app/dashboard/layout.js` and nested routes for `app/dashboard/settings/page.js`.
3. Migrate a `pages/` project using `useRouter` to `app/` using `usePathname`, `useSearchParams`, and `useParams` in client components.

---

## Related coding interview problems

1. Implement a breadcrumbs component that derives crumbs from `usePathname()`.
2. Create a client-only component which performs a `router.replace()` when a query param is invalid.
3. Implement optimistic UI when navigating: update local state immediately and `router.push()` to new route.

---

## Appendix: Quick reference

- `Link` — client transitions.
- `useRouter()` (pages) — imperative pushes, query access.
- `usePathname(), useSearchParams(), useParams()` (app) — read URL state in Client Components.
- `generateStaticParams()` — App Router static dynamic routes.
- `getStaticPaths()`/`getStaticProps()` — Pages Router SSG.

---

*Saved as* `Next.js - Routing & Navigation Cheat Sheet.md`. You can preview and download the Markdown from the canvas viewer.

# Topic : Next.js

## Sub Topic : API Routes — creating backend endpoints inside Next.js

---

### Quick overview

API Routes let you create backend endpoints inside a Next.js app by adding files under the `/pages/api` (Pages Router) or `app/api` (App Router with Route Handlers) directories. These endpoints run as server-side functions (serverless or edge) and let you handle requests (GET/POST/etc.), talk to databases, call third-party APIs, manage auth, and receive webhooks — all without a separate backend service.

---

## 1. Two flavours: Pages Router vs App Router

**Pages Router (`/pages/api`)**
- Each file exports a default function: `export default function handler(req, res) { ... }`.
- Uses Node-style `req` (IncomingMessage) and `res` (ServerResponse).
- Ideal for apps using `pages/` already.

**App Router (`/app/api`) — Route Handlers**
- Newer, file-based route handlers use Web Fetch API style: `export async function GET(request) { ... }` and `export async function POST(request) { ... }`.
- Use `NextResponse` to control response and cookies.
- Better suited for edge runtimes and streaming.

---

## 2. Basic examples

### Pages Router (pages/api/hello.js)
```js
export default function handler(req, res) {
  if (req.method === 'GET') {
    res.status(200).json({ message: 'Hello from pages API' });
  } else {
    res.setHeader('Allow', ['GET']);
    res.status(405).end('Method Not Allowed');
  }
}
```

### App Router (app/api/hello/route.js)
```js
import { NextResponse } from 'next/server';

export async function GET(request) {
  return NextResponse.json({ message: 'Hello from route handler' });
}
```

---

## 3. Request parsing & body handling
- **Pages Router**: `req.body` exists for JSON requests (Next parses body by default). For streaming or raw bodies (e.g., webhooks, file uploads) set `export const config = { api: { bodyParser: false } }` and parse manually.
- **App Router**: `request` is a Web `Request` object — use `await request.json()` or `await request.text()`.

**Raw body example for Stripe webhooks (pages router)**
```js
export const config = { api: { bodyParser: false } };

export default async function handler(req, res) {
  const buf = await readRaw(req); // custom util to collect raw buffer
  // verify signature using raw buffer
}
```

---

## 4. Runtimes: Node vs Edge
- You can configure per-route runtime with `export const config = { runtime: 'edge' }` in App Router or `export const runtime = 'edge'` in pages (depending on Next version).
- **Edge runtime**: runs on V8 isolates, faster cold starts, limited Node API (no filesystem, no native modules). Use the Web Fetch API.
- **Node runtime**: full Node APIs available; good for heavy server-side libs.

---

## 5. Responses and utilities
- **Pages Router**: `res.status(200).json({})` or `res.setHeader()`.
- **App Router**: `return NextResponse.json({})` or `return new Response('text')`.
- **Cookies**: In App Router with `NextResponse`, use `NextResponse.next()` and `response.cookies.set(...)` (or `cookies()` helper in server components). In Pages Router, set `Set-Cookie` header or use the `cookie` library.

---

## 6. CORS
- Handle CORS manually by setting `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, and responding to OPTIONS preflight.
- Example (simple):
```js
if (req.method === 'OPTIONS') {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST');
  return res.status(204).end();
}
```

---

## 7. Error handling & best practices
- Always validate input and return clear error codes (400/401/403/404/500).
- Limit what you expose in error messages (avoid stack traces in production).
- Use a try/catch and return structured error responses.
- Keep routes small and single-responsibility.

---

## 8. Security considerations
- Protect secrets using environment variables (`process.env`) — never commit them.
- Sanitize input to prevent injection attacks.
- Implement rate limiting / throttling for public endpoints.
- Use CSRF protection if endpoints are used from browser forms (or rely on same-site cookies and tokens).
- For authentication, prefer signed cookies, JWTs, or third-party providers (NextAuth, Clerk).

---

## 9. Common patterns & examples

### a) CRUD REST-style example (App Router)
```
app/api/todos/route.js
export async function GET(request) { /* list todos */ }
export async function POST(request) { /* create todo */ }
export async function PUT(request) { /* update */ }
export async function DELETE(request) { /* delete */ }
```

### b) Webhook receiver (Stripe/SendGrid)
- Disable automatic body parsing; verify signature using raw body.
- Respond with `200` quickly to acknowledge receipt.

### c) File upload (multipart)
- Use `formidable` or `busboy` in Node runtime (pages router) with `bodyParser: false`.
- For App Router + Edge, prefer client-side direct uploads to S3/Cloud Storage with signed URLs.

### d) Streaming responses
- App Router supports streaming with `ReadableStream` and `new Response(stream)`.
- Useful for server-sent events (SSE) or chunked responses.

---

## 10. Deployment notes
- On Vercel, API routes are deployed as serverless functions or Edge Functions depending on runtime config.
- Cold starts are mitigated by Edge runtime but be mindful of Node modules not supported on edge.
- Keep function bundle small to reduce latency.

---

## 11. When NOT to use API routes
- Heavy compute tasks (use background workers).
- Long-running processes — serverless has timeout limits.
- Complex microservice architecture that requires independent scaling — consider an external API service.

---

## Interview-style theory questions (with concise answers)

1. **What are Next.js API Routes and where are they located?**
   - API routes are server-side endpoints inside a Next.js app, placed under `/pages/api` (Pages Router) or `/app/api` (App Router route handlers).

2. **Difference between pages API routes and app route handlers?**
   - Pages Router uses Node `req/res` handler; App Router uses Web `Request`/`Response` and `NextResponse`, and integrates better with edge runtimes and streaming.

3. **How do you disable body parsing and why?**
   - In pages: `export const config = { api: { bodyParser: false } }`. Disable to access raw body for signature verification or to handle multipart streams.

4. **What is an Edge Runtime?**
   - A V8 isolate environment that runs closer to users with low latency, but has limited Node APIs.

5. **How to set cookies from an API route?**
   - Pages: set `Set-Cookie` header or use cookie helpers. App Router: use `NextResponse` and `response.cookies.set()`.

6. **How to handle CORS in Next.js API routes?**
   - Set appropriate `Access-Control-Allow-*` headers and handle `OPTIONS` preflight.

7. **When would you prefer direct uploads to S3 over server uploads?**
   - For large files or to reduce server bandwidth & latency; generate signed upload URLs from API routes and upload directly from client.

8. **How to protect a webhook endpoint?**
   - Verify provider signature using raw request body and shared secret; limit origin access; respond quickly.

---

## Related coding interview questions (practical tasks)

1. **Write an API route that paginates results from a database.**
   - Expect candidates to validate `page`/`limit`, use `OFFSET/LIMIT` or cursor-based pagination, and return `meta` with total/pages.

2. **Implement an authenticated `/api/me` endpoint.**
   - Validate JWT or session cookie, fetch user data, return 401 on invalid.

3. **Build a rate-limited endpoint (basic token bucket).**
   - Use in-memory store for demo or Redis for production; decrement tokens per request and return 429 when exhausted.

4. **Create a webhook handler that verifies a signature (Stripe example).**
   - Disable body parser, compute HMAC with raw body and compare to header signature, return 200 on success.

5. **Implement a `POST /api/upload` that returns a signed S3 URL for direct uploads.**
   - Use AWS SDK server-side to create a pre-signed PUT URL and return it to the client.

---

## Example: `route.js` for App Router with simple auth check
```js
import { NextResponse } from 'next/server';

export async function GET(request) {
  const auth = request.headers.get('authorization');
  if (!auth || !auth.startsWith('Bearer ')) {
    return new NextResponse(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }
  // verify token (pseudo)
  return NextResponse.json({ message: 'ok' });
}
```

---

## Cheat-sheet: Quick config snippets
- Disable body parsing (pages):
```js
export const config = { api: { bodyParser: false } };
```
- Set edge runtime (App Router):
```js
export const config = { runtime: 'edge' };
```
- Return JSON (App Router):
```js
import { NextResponse } from 'next/server';
return NextResponse.json({});
```

---

## Further reading & references
- Next.js official docs: API routes and Route Handlers (searchable on nextjs.org)
- Vercel docs: Serverless vs Edge Functions

---

*This file is designed to be previewable and downloadable as a Markdown document.*


# Topic : Next.js

## Sub Topic : Middleware — Edge Functions, Request Interception

---

## What is Middleware in Next.js?
Middleware in Next.js is a lightweight function that runs **before a request is completed**, allowing you to intercept, rewrite, redirect, block, or modify incoming requests. It runs **on the Edge Runtime**, meaning extremely low latency and global distribution.

You place a file named **`middleware.js`** or **`middleware.ts`** in the root of your project (or inside matching directories for granular control).

---

## How Middleware Works
Middleware runs **before** Next.js routes (both pages and API routes). It receives a `NextRequest` and returns one of the following:
- `NextResponse.next()` → continue request
- `NextResponse.redirect()`
- `NextResponse.rewrite()`
- `NextResponse.json()` (App Router only)

Because it runs on **Edge Runtime**, it uses **Web APIs** instead of Node.js APIs.

---

## Basic Example — middleware.js
```js
import { NextResponse } from 'next/server';

export function middleware(request) {
  console.log('Middleware hit:', request.nextUrl.pathname);
  return NextResponse.next();
}
```

---

## Use Cases

### Authentication / Authorization
Protect specific routes by checking cookies or headers.
```js
export function middleware(request) {
  const token = request.cookies.get('auth-token');
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}
```

### URL Rewrites
```js
export function middleware(request) {
  return NextResponse.rewrite(new URL('/maintenance', request.url));
}
```

### Locale / Geo-based routing
Middleware can access geolocation headers.
```js
export function middleware(request) {
  const country = request.geo.country || 'IN';
  if (country === 'US') {
    return NextResponse.rewrite(new URL('/us', request.url));
  }
  return NextResponse.next();
}
```

### Bot detection, rate limits, feature flags
You can block/shape traffic early without hitting your backend.

---

## Runtime: Edge Functions
Middleware only runs on **Edge Runtime**, which:
- uses V8 isolates
- offers ultra‑fast cold starts
- supports Web APIs (Request, Response, crypto)
- does **not** support Node APIs (fs, net, Buffer, etc.)

If you try to use unsupported Node features, your middleware will throw.

---

## Matcher — Limit where middleware runs
Add a `config` export to run middleware only on certain routes.

```js
export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};
```

Examples:
- `/dashboard/*` → protect user-only sections
- `/api/*` → filter requests before API handlers
- `'/((?!_next/static|favicon.ico).*)'` → run on everything except static files

---

## Reading & Modifying Requests
### Accessing URL
```js
request.nextUrl.pathname
request.nextUrl.searchParams
```

### Reading headers
```js
const ua = request.headers.get('user-agent');
```

### Updating request headers
```js
const response = NextResponse.next();
response.headers.set('x-custom', 'edge-powered');
return response;
```

---

## Rewrites vs Redirects
**Rewrite** → user stays on same URL but receives content from different route.
**Redirect** → browser changes URL and navigates.

```js
// rewrite
NextResponse.rewrite(new URL('/new-content', request.url));

// redirect
NextResponse.redirect(new URL('/login', request.url));
```

---

## Cookie Handling in Middleware
```js
export function middleware(request) {
  const response = NextResponse.next();
  response.cookies.set('visited', 'true', { path: '/' });
  return response;
}
```

Reading:
```js
request.cookies.get('token');
```

---

## Middleware vs API Routes vs Route Handlers
| Feature | Middleware | API Routes | Route Handlers |
|--------|-----------|------------|----------------|
| Runs before routing | ✔ | ✖ | ✖ |
| Edge Runtime only | ✔ | optional | optional |
| Can rewrite/redirect | ✔ | ✖ | ✔ |
| Access to Node APIs | ✖ | ✔ | depends on runtime |
| Good for auth, bot filtering | ✔ | ✖ | ✔ |
| Handles response body | limited | full | full |

---

## Limitations
- No Node API (fs, Buffer, path, etc.)
- No heavy computation (Edge runtime limits)
- No streaming responses directly from Middleware
- Cannot access database directly (use API route or Route Handler instead)

---

## Interview-style theory questions (with concise answers)

**1. What is Next.js Middleware?**
A request interceptor that runs on the Edge Runtime before routing, used for auth, rewriting, redirects, and filtering.

**2. Where do you place Middleware?**
In the project root as `middleware.js` or nested for segmented routing.

**3. Why does Middleware run on the Edge Runtime?**
To achieve low-latency global performance with instant cold starts.

**4. Difference between Middleware and API Routes?**
Middleware intercepts before routing; API routes execute as backend endpoints and support business logic.

**5. Can Middleware access Node.js APIs?**
No, only Web APIs are supported.

**6. What is the purpose of the `matcher` config?**
Choose specific paths where Middleware applies.

**7. What is the difference between `rewrite` and `redirect`?**
Rewrite keeps URL same; redirect updates URL in browser.

---

## Coding-based interview tasks

### 1. Implement route protection using Middleware
- Check auth cookie; redirect unauthorized users.
- Validate URL pattern via matcher.

### 2. Add logging Middleware
- Log IP address, country, user-agent with minimal performance cost.

### 3. Implement feature flags
- Read cookies or headers.
- Rewrite to `/beta` for beta-enabled users.

### 4. Add geo-based personalization
- Use `request.geo.country` to choose region landing pages.

### 5. Rate-limit specific endpoints
- Use an external KV store (Redis, Upstash) to track user requests.

---

## Example: Auth Middleware with matcher
```js
import { NextResponse } from 'next/server';

export function middleware(request) {
  const token = request.cookies.get('session');

  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*'],
};
```

---

## Final Notes
Middleware brings powerful pre-routing capabilities to Next.js with extremely fast execution on the edge. It unlocks modern patterns like zero-latency auth checks, dynamic rewrites, and traffic shaping — vital for high-performance apps.

---

*Previewable and downloadable as Markdown.*

# Topic : Next.js

# Sub Topic : Head & Metadata — SEO tags, `next/head`, App Router Metadata API

---

## Quick overview

This cheat sheet explains how to manage page `<head>` content and metadata in Next.js (both **Pages Router** and **App Router**). It covers `next/head`, the App Router `metadata` API, dynamic metadata, Open Graph/Twitter, canonical/robots, structured data (JSON‑LD), best practices, and common pitfalls. Examples use JavaScript.

---

## 1. When to use what

- **Pages Router (`pages/`)**: use `next/head` to insert tags into the document `<head>` for a page or component.
- **App Router (`app/`)**: prefer the **Metadata API** (`export const metadata = { ... }` in `layout.js`/`page.js`) or `generateMetadata` for dynamic metadata. `next/head` is not needed and is discouraged in the App Router.

---

## 2. `next/head` (Pages Router)

### Basic usage

```jsx
// pages/index.js
import Head from 'next/head'

export default function Home() {
  return (
    <>
      <Head>
        <title>Home • MySite</title>
        <meta name="description" content="Short description" />
        <link rel="canonical" href="https://example.com/" />
      </Head>
      <main>...</main>
    </>
  )
}
```

### Notes
- `next/head` deduplicates tags (same `name`/`property`/`rel`) across renders.
- Avoid placing `<html>`/`<body>` attributes via `next/head`. Use `_document.js` for html/body attributes.
- For reusable SEO components, create an `<SEO />` component that renders `<Head>` with props.

---

## 3. Metadata API (App Router)

### Static metadata (file-based)

```js
// app/about/page.js
export const metadata = {
  title: 'About — MySite',
  description: 'About page description',
  openGraph: {
    title: 'About — MySite',
    description: 'About page description',
    url: 'https://example.com/about',
    images: ['/og-about.png'],
  },
}

export default function Page() { return <h1>About</h1> }
```

### Dynamic metadata with `generateMetadata`

```js
// app/blog/[slug]/page.js
export async function generateMetadata({ params, searchParams }, parent) {
  const post = await fetchPost(params.slug)
  return {
    title: post.title,
    description: post.excerpt,
    openGraph: { title: post.title, description: post.excerpt, images: [post.og] }
  }
}
```

### Where to export
- `page.js` or `layout.js` in the route segment hierarchy. Metadata merges from root → nested segments.

---

## 4. Open Graph & Twitter Cards (social previews)

Include both if you want rich previews on social platforms.

```js
export const metadata = {
  title: 'Post title',
  openGraph: {
    title: 'Post title',
    description: 'Summary',
    url: 'https://example.com/post',
    images: [
      { url: 'https://example.com/og.png', width: 1200, height: 630 }
    ]
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Post title',
    images: ['https://example.com/og.png']
  }
}
```

---

## 5. Canonical URLs, robots, indexing

- Use `<link rel="canonical" href="..." />` to suggest the canonical URL.
- Use `<meta name="robots" content="noindex, nofollow" />` for private pages.
- Prefer server-side canonical logic for paginated content to avoid duplicate-indexing.

---

## 6. Structured data (JSON‑LD)

Include `application/ld+json` inside `Head` (Pages Router) or as `metadata` entries (App Router allows `alternates`/`other` fields) — when using App Router and you need custom script tags, place them inside `head` via page components or `_document` if global.

Example (Pages Router):

```jsx
<Head>
  <script type="application/ld+json">{JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Post title",
    "author": { "@type": "Person", "name": "Author" }
  })}</script>
</Head>
```

---

## 7. Best practices

- Prefer file-based Metadata API for App Router apps — central, mergeable, and optimized.
- Keep server-rendered metadata where possible (SEO benefits). Static or `generateMetadata` is preferable to client-side injection.
- Provide `og:image` with recommended dimensions (1200×630) and serve via static optimized images or an image generation endpoint.
- Avoid duplicate meta tags; use dedupe behaviour of Next.js but keep an eye on custom `Head` components in client components.
- Use canonical links for pagination and filtered content.
- Localize metadata for i18n routes: set `alternates` and localized titles/descriptions.

---

## 8. Common pitfalls

- Adding metadata in client-only code: may not be seen by crawlers or when generating social previews.
- Trying to set `<html lang>` with `Head` — use `next/document` or `i18n` config.
- Double-fetching when using `generateMetadata` and also fetching page data — structure fetches so you can reuse results.

---

## 9. Theory-style interview questions (concise answers)

**Q: What is the difference between `next/head` and the App Router Metadata API?**
A: `next/head` inserts tags in Pages Router at runtime and dedupes them; Metadata API is file-based for App Router (`export const metadata`) and supports static/dynamic metadata with hierarchical merging and server-side generation.

**Q: Why is server-rendered metadata preferred for SEO?**
A: Search engines and social scrapers read server-rendered `<head>` on first request; client-only injections may be missed or delayed, harming indexing and previews.

**Q: How does Next.js avoid duplicate metadata across nested routes?**
A: App Router metadata merges along the route segments; when duplicates exist, the more specific segment overrides parent values. `next/head` dedupes tags by key attributes.

**Q: When would you use `generateMetadata`?**
A: For dynamic pages (e.g., blog posts) where metadata depends on remote data (title, excerpt, image) that must be generated server-side.

---

## 10. Related coding interview questions (practical)

1. **Implement a reusable `SEO` component for Pages Router that accepts title, description, canonical, ogImage.**
2. **Show how to export static `metadata` in App Router at `app/layout.js` for default site metadata.**
3. **Write `generateMetadata` for a blog post route that fetches post data and returns fully formed metadata (including OG image).**
4. **Explain how you’d localize metadata for English and Spanish versions of a page.**

_Code hints are included in the examples above — these are common take-home or pair-programming tasks._

---

## Appendix — quick code snippets

- Pages Router `SEO` component (JSX)

```jsx
import Head from 'next/head'
export default function SEO({ title, description, canonical, ogImage }){
  return (
    <Head>
      <title>{title}</title>
      <meta name="description" content={description} />
      {canonical && <link rel="canonical" href={canonical} />}
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      {ogImage && <meta property="og:image" content={ogImage} />}
    </Head>
  )
}
```

- App Router default metadata in `app/layout.js`

```js
export const metadata = {
  title: 'MySite',
  description: 'Default description for MySite',
  openGraph: { images: ['/default-og.png'] },
}

export default function RootLayout({ children }){
  return <html lang="en"><body>{children}</body></html>
}
```

---

## Sources & further reading

- Next.js official docs: `next/head`, App Router Metadata API, `generateMetadata`, OG examples.

---

*End of cheat sheet.*

# Topic : Next.js

# Sub Topic : Environment Variables — `NEXT_PUBLIC_`, `process.env`, Runtime Config

---

## Overview
Environment variables in Next.js help you manage secrets, public config, build‑time vs runtime values, and environment‑specific behavior. This guide covers:
- `.env` files
- `process.env` usage
- `NEXT_PUBLIC_` variables
- Runtime configuration in App Router
- Server vs client visibility
- Edge/runtime considerations

---

## 1. How Next.js loads environment variables

Next.js automatically loads variables from these files:
```
.env            # defaults
.env.local      # gitignored, overrides .env
.env.development
.env.production
```
Variables are injected **at build time** unless otherwise specified.

---

## 2. Public vs Private variables

### Private (server only)
Default behavior — available only in:
- Server Components
- API Routes
- Route Handlers
- getServerSideProps / getStaticProps

Example:
```
API_SECRET_KEY=abc123
```

Usage:
```js
const key = process.env.API_SECRET_KEY
```

### Public (exposed to browser)
Variables **starting with `NEXT_PUBLIC_`** become visible to the client.
They are replaced at build time.

Example:
```
NEXT_PUBLIC_API_URL=https://api.example.com
```
Usage:
```js
const url = process.env.NEXT_PUBLIC_API_URL
```

---

## 3. Using env variables in App Router

### Server Component
```js
export default function Page() {
  const token = process.env.API_TOKEN   // OK
  return <div>Server Page</div>
}
```

### Client Component
Client components can **only** read `NEXT_PUBLIC_` variables.
```jsx
'use client'
export default function ClientComponent(){
  console.log(process.env.NEXT_PUBLIC_API_URL) // OK
  console.log(process.env.API_TOKEN) // ❌ server-only
}
```

---

## 4. Environment variables in Route Handlers / API Routes

```js
// app/api/user/route.js
export async function GET() {
  const key = process.env.API_KEY
  return Response.json({ ok: true })
}
```
These run on the server, so private variables are safe.

---

## 5. Edge Runtime considerations

Edge runtime has limited access:
- Must use `NEXT_PUBLIC_` unless marked as allowed
- No access to arbitrary Node APIs

```js
export const runtime = 'edge'

export function GET() {
  const v = process.env.NEXT_PUBLIC_FLAG  // OK
  const secret = process.env.SECRET       // ❌ not allowed unless defined via middleware config
}
```

---

## 6. Runtime Configuration (next.config.js)

You can map env variables inside Next config.

```js
// next.config.js
module.exports = {
  env: {
    CUSTOM_VALUE: process.env.CUSTOM_VALUE
  }
}
```

These become available both on server and client (not recommended for secrets).
Prefer direct `.env` usage in modern Next.js apps.

---

## 7. Best practices

- Never expose secrets without using `NEXT_PUBLIC_` prefix.
- .env.local should not be committed.
- For dynamic runtime changes (post-build), consider deploying platforms that support runtime env injection.
- For App Router, prefer using server components for logic requiring private env values.
- When debugging, print `Object.keys(process.env)` only on server.

---

## 8. Common pitfalls

- Forgetting `NEXT_PUBLIC_` prefix → variable won't be available on client.
- Changing env variables without rebuilding → old values remain baked into bundle.
- Using private env vars in client components causes `undefined`.
- Using env vars inside static exports (`next export`) requires them to be present at build time.

---

## 9. Interview‑style theory questions

**Q: Why isn’t `process.env.API_KEY` available on the client?**
A: Next.js removes non‑public variables from client bundles for security; only `NEXT_PUBLIC_` variables are included.

**Q: Are environment variables in Next.js evaluated at build time or runtime?**
A: Mostly build time. Runtime only applies when the hosting provider injects env vars for server code.

**Q: How do you expose a server variable to the browser?**
A: Rename it with the `NEXT_PUBLIC_` prefix so Next.js can embed it in client-side bundles.

**Q: What happens if env variables change after a production build?**
A: Client-visible variables stay baked into the build; server variables update only if your hosting platform reloads them at runtime.

---

## 10. Coding practice questions

1. Create a `getConfig()` helper that safely reads server-only env variables and throws if missing.
2. Build a client component that uses `NEXT_PUBLIC_FEATURE_FLAG` to toggle UI.
3. Implement an API route that uses `API_SECRET` to call an external service.
4. Implement `generateMetadata` using an env variable for base URLs.

---

## Quick Snippets

**Safe env loader on server**
```js
export function requireEnv(name) {
  const value = process.env[name]
  if (!value) throw new Error(`${name} is missing`)
  return value
}
```

**Client feature flags**
```jsx
'use client'
export default function FeatureFlagged() {
  return process.env.NEXT_PUBLIC_NEW_UI === 'true'
    ? <NewUI />
    : <OldUI />
}
```

---

*End of cheat sheet.*

# Topic : Next.js

## Sub Topic : Styling — CSS Modules, Tailwind, styled-jsx, global.css

---

### Quick overview

Next.js supports multiple styling approaches. Choose between:

- **Global CSS** (`app/global.css` or `pages/_app.js` import) for site-wide rules and resets.
- **CSS Modules** (`*.module.css`) for locally scoped, component-level styles.
- **Tailwind CSS** utility-first framework that composes styles via classes.
- **styled-jsx** built-in CSS-in-JS for scoped styles written inline with components.

This cheat-sheet gives quick setup steps, code examples, pros/cons, interview-style Q&A, and coding exercises.

---

## 1) Global CSS

**When to use:** Resets, typography, design tokens, global utilities.

**How (App Router):** create `app/global.css` and import it in `app/layout.js` / `app/layout.tsx`:

```js
// app/layout.jsx
import './global.css'
export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  )
}
```

**Pages Router:** import global CSS only in `pages/_app.js`.

**Pitfall:** global CSS affects entire app; import rules are strict in Next.js to avoid accidental leakage.

---

## 2) CSS Modules

**When to use:** Component-level styles with predictable scoping.

**How:** create `Button.module.css` next to your component and import it:

```css
/* components/Button.module.css */
.btn { padding: 8px 12px; border-radius: 6px; }
```

```jsx
// components/Button.jsx
import styles from './Button.module.css'
export default function Button({ children }) {
  return <button className={styles.btn}>{children}</button>
}
```

**Notes:** Next.js auto-generates unique class names so same `.btn` can be reused in other modules without collisions.

**Pros:** simple, predictable, zero runtime cost.
**Cons:** limited to class-based CSS; composition via `:global()` and `:local()` is possible but slightly awkward.

---

## 3) Tailwind CSS

**When to use:** Rapid UI building, consistent design system, utility-driven styling.

**Setup (summary):** install `tailwindcss` and follow Next.js Tailwind guide—create `tailwind.config.js`, add Tailwind directives to `app/globals.css` or equivalent, configure content paths to include `app/` and `pages/`.

```css
/* app/global.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**Usage:** Use utility classes directly in JSX: `<div className="flex items-center gap-4">`.

**Pros:** Extremely fast to iterate; small runtime CSS when purged.
**Cons:** Verbose class lists in markup; requires deciding on utility vs component classes strategy.

---

## 4) styled-jsx

**When to use:** Scoped component styles written inside the component file.

**How:** Styled-jsx is supported out of the box in Next.js:

```jsx
export default function Card() {
  return (
    <article>
      <h2>Title</h2>
      <style jsx>{`
        article { padding: 12px; border-radius: 8px; }
        h2 { color: #222; }
      `}</style>
    </article>
  )
}
```

**Notes:** For server-rendered CSS-in-JS you may use the app router CSS-in-JS guide (style registry + `useServerInsertedHTML`) when using other CSS-in-JS libs.

**Pros:** Localized styles colocated with component, no external files.
**Cons:** Can grow messy for large styles, limited ecosystem vs styled-components or emotion.

---

## Best practices

- Put global resets and typography in `app/global.css` or `pages/_app.js`.
- Prefer CSS Modules or component-scoped solutions for encapsulation.
- Use Tailwind for fast prototyping and utility-driven design systems.
- Keep styles small and composable: prefer tokens, variables, and design-system components.
- For performance, ensure unused CSS is purged (Tailwind) and avoid heavy runtime CSS libraries unless needed.

---

## Interview-style theory questions (short answers)

1. **Why use CSS Modules over global CSS?**
   CSS Modules scope class names locally, preventing collisions and making components portable.

2. **How do you add global CSS in Next.js app router?**
   Create `app/global.css` and import it in `app/layout.js` (or root layout).

3. **What is Tailwind's purge/content config for?**
   It tells Tailwind which files to scan for class names so unused utilities are removed from the final CSS.

4. **When to choose styled-jsx vs a library like emotion?**
   styled-jsx is lightweight and built-in for simple scoped CSS. Choose emotion/styled-components when you need advanced dynamic theming, rich ecosystems, or SSR-aware style registries.

5. **How does Next.js ensure CSS imported in a page doesn’t leak?**
   Next.js enforces importing global CSS only at top-level (`_app.js` or root layout) and encourages scoped approaches (CSS Modules) to avoid leakage.

---

## Coding interview questions (practical)

1. **Implement a `Button` component using CSS Modules with a `primary` variant.**
   *Expected:* `Button.module.css` with `.btn` and `.primary`, component imports module and applies conditionally.

2. **Set up Tailwind in a Next.js app and create a responsive navbar.**
   *Expected:* Tailwind config with `content` paths, `app/global.css` directives, `<nav className="flex ...">` responsive utilities.

3. **Convert a small component using styled-jsx into CSS Modules.**
   *Expected:* Move styles into `Component.module.css`, swap `className` usages.

4. **Explain how you'd add theme variables for dark mode that work across CSS Modules and Tailwind.**
   *Expected:* Use CSS custom properties on `:root` and `[data-theme="dark"]`, use Tailwind's `dark` mode config and reference CSS variables in custom classes.

---

## Closing

This cheat-sheet is provided as a Markdown file you can preview and download. It includes all code snippets so you can copy-paste into a Next.js project.

---

*Created for quick interview prep and practical usage.*

# Topic : Next.js

## Sub Topic : Authentication — NextAuth.js basics, JWT session handling

---

### Quick overview

NextAuth.js (now often referred to as Auth.js) is the official, flexible authentication solution for Next.js. It supports:

- OAuth providers (Google, GitHub, Facebook, etc.)
- Email (passwordless/magic links)
- Credentials (username/password via custom APIs)
- Database-backed sessions or JWT-based sessions

This cheat-sheet covers installation, core concepts, JWT vs database sessions, callbacks (jwt/session), token rotation/refresh, security best practices, interview Q&A, and coding exercises.

---

## 1) Installation & basic setup

```bash
npm install next-auth
# or
yarn add next-auth
```

Create the dynamic route for NextAuth API:

```js
// pages/api/auth/[...nextauth].js  (Pages Router)
import NextAuth from 'next-auth'
import GoogleProvider from 'next-auth/providers/google'

export default NextAuth({
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_ID,
      clientSecret: process.env.GOOGLE_SECRET,
    }),
  ],
  secret: process.env.NEXTAUTH_SECRET,
})
```

For the App Router (Next.js 13+), the same API route works; there are also helper functions like `getServerSession` to avoid client-side fetches.

---

## 2) Sessions: Database vs JWT

**Database sessions (default)**
- Session state stored server-side in a sessions table (requires an adapter, e.g., Prisma, TypeORM, MongoDB).
- Shorter access to session data, server can revoke sessions centrally.

**JWT sessions**
- Session data stored in an encrypted JWT (sent as cookie). No DB needed.
- Good for serverless and simple apps, but revocation and rotation need extra care.

Configure session strategy:

```js
export default NextAuth({
  session: { strategy: 'jwt', maxAge: 30 * 24 * 60 * 60 }, // jwt or database
  jwt: { maxAge: 30 * 24 * 60 * 60 },
})
```

---

## 3) JWT lifecycle and callbacks

NextAuth exposes callbacks to control tokens and sessions.

Key callbacks:

- `jwt({ token, user, account, profile, isNewUser })` — runs when the JWT is created or updated. Use this to add provider tokens, user id, roles.
- `session({ session, token, user })` — runs when a session object is returned to the client; copy fields from the token into `session` so the client sees them.

Example pattern to persist provider access tokens in the JWT and expose to the client:

```js
export default NextAuth({
  // ...providers
  callbacks: {
    async jwt({ token, user, account }) {
      // first sign in
      if (account && user) {
        token.accessToken = account.access_token
        token.id = user.id
      }
      return token
    },
    async session({ session, token }) {
      session.user.id = token.id
      session.accessToken = token.accessToken
      return session
    }
  }
})
```

**Important:** The `jwt` callback runs before `session`, so anything added to the token is immediately available in the session callback.

---

## 4) Token rotation & refresh strategies

NextAuth does not automatically exchange refresh tokens for providers in every case — you implement refresh in the `jwt` callback if you need long-lived provider tokens.

Pattern:

1. On sign-in, store `accessToken`, `refreshToken`, and `expires_at` in the token.
2. On subsequent `jwt` calls, check expiry; if expired, call the provider refresh endpoint, update token fields.

Simplified refresh skeleton:

```js
async function refreshAccessToken(token) {
  try {
    const url = `https://oauth.provider.com/token`;
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        grant_type: 'refresh_token',
        refresh_token: token.refreshToken,
        client_id: process.env.CLIENT_ID,
        client_secret: process.env.CLIENT_SECRET,
      }),
    })
    const refreshed = await response.json()
    return {
      ...token,
      accessToken: refreshed.access_token,
      accessTokenExpires: Date.now() + refreshed.expires_in * 1000,
      refreshToken: refreshed.refresh_token ?? token.refreshToken,
    }
  } catch (err) {
    console.error('Refresh access token error', err)
    return { ...token, error: 'RefreshAccessTokenError' }
  }
}
```

Then call `refreshAccessToken(token)` inside your `jwt` callback when token is near expiry.

---

## 5) Security best practices

- **Set NEXTAUTH_SECRET** using `npx auth secret` or `openssl rand -base64 32`. This signs/encrypts tokens.
- **Use HTTPS** in production to protect cookies.
- **Use secure cookies and SameSite** settings (NextAuth sets good defaults; review `useSecureCookies` in the config).
- **Prefer database sessions** when you need server-side revocation and session introspection.
- **Limit JWT payload** size—do not store large objects; store IDs & minimal claims.
- **Rotate refresh tokens** where supported by provider.
- **Avoid trusting client-side session storage** — always validate tokens server-side for protected APIs.

---

## 6) Protecting pages & API routes

Server-side:

```js
import { getServerSession } from 'next-auth/next'
import { authOptions } from './api/auth/[...nextauth]'

export async function getServerSideProps(ctx) {
  const session = await getServerSession(ctx.req, ctx.res, authOptions)
  if (!session) return { redirect: { destination: '/api/auth/signin', permanent: false } }
  return { props: { session } }
}
```

API route protection:

```js
import { getToken } from 'next-auth/jwt'

export default async function handler(req, res) {
  const token = await getToken({ req, secret: process.env.NEXTAUTH_SECRET })
  if (!token) return res.status(401).json({ error: 'Not authenticated' })
  // token contains your JWT payload
}
```

Client-side: use `useSession()` and `signIn()` helpers from `next-auth/react`.

---

## 7) Interview-style theory questions (concise answers)

1. **What is the difference between session strategies in NextAuth?**
   Database sessions store session state server-side; JWT sessions store encrypted session data in a cookie. Database supports revocation; JWT is DB-less and serverless friendly.

2. **How do you expose a provider access token to the client?**
   Persist the token in the JWT inside the `jwt` callback, then copy it to the `session` object in the `session` callback.

3. **Why set NEXTAUTH_SECRET?**
   It signs and encrypts tokens and other sensitive data; without it token security is weakened.

4. **How to revoke a JWT-based session?**
   JWTs are stateless — to revoke, either switch to database sessions or maintain a server-side blacklist/rotation mechanism keyed by user/session id.

5. **What are common pitfalls when using refresh tokens with NextAuth?**
   Not refreshing before expiry, not saving refreshed tokens, exposing long-lived tokens to the client, and inconsistent token formats between NextAuth and provider libraries.

---

## 8) Coding interview / practical tasks

1. **Create a NextAuth setup with Google provider and persist the `access_token` into the client session.**
   *Expect:* providers configured, `jwt` & `session` callbacks implemented to transfer `access_token`.

2. **Protect an API route using `getToken()` to verify JWT and return user id.**
   *Expect:* use `getToken({ req, secret })`, handle expired/invalid tokens.

3. **Implement token refresh flow for OAuth provider in the `jwt` callback.**
   *Expect:* logic to detect expiry, call provider token endpoint, update token payload.

4. **Migrate database sessions to JWT sessions and explain tradeoffs.**
   *Expect:* change `session.strategy`, discuss revocation, scaling, and payload size.

---

## 9) Quick reference snippets

- `getSession()` — client-only helper to read session.
- `getServerSession()` — recommended server-side helper.
- `getToken()` — read/verify JWT directly from API routes or middleware.

---

## Closing

This markdown contains copy-paste-ready examples and practical interview prep for NextAuth.js and JWT session handling in Next.js. Download the file from the preview panel (top-right) to save locally.

---

*Created for interview prep and practical implementation.*

# Topic : Next.js

## Sub Topics :
- Error Handling — custom error pages, middleware-level handling
- Deployment — Vercel pipeline, static export, build optimization
- Performance — next/script, prefetching, lazy loading

---

### Summary
This cheat-sheet covers practical patterns, code examples, pitfalls, interview-style Q&A, and coding tasks for Error Handling, Deployment, and Performance in Next.js (Pages & App Router). Copy-paste-ready snippets included.

---

## 1) Error Handling

### Concepts
- **Pages Router**: create `pages/404.js`, `pages/500.js`, and `pages/_error.js` for custom handling.
- **App Router**: use `error.js` (route segment) for runtime error boundaries and `not-found.js` / `notFound()` for 404 flows.
- **Error boundaries**: client-only components (`'use client'`) that catch rendering errors in children.
- **Middleware-level handling**: Next.js Middleware can intercept requests, respond with custom responses or redirects, and run before routing. For centralized error logging or feature flags you can throw or return responses from middleware.

### Examples
**Pages Router — custom 404 & 500**
```jsx
// pages/404.js
export default function Custom404(){
  return <h1>404 — Page not found</h1>
}
// pages/500.js
export default function Custom500(){
  return <h1>500 — Server error</h1>
}
```

**Pages Router — _error.js for SSR/SSG errors**
```jsx
// pages/_error.js
function Error({ statusCode }){
  return (<p>{statusCode ? `Error ${statusCode} on server` : 'Client error'}</p>)
}
Error.getInitialProps = ({ res, err }) => {
  const statusCode = res ? res.statusCode : err ? err.statusCode : 404
  return { statusCode }
}
export default Error
```

**App Router — route segment error boundary**
```jsx
// app/dashboard/error.js
'use client'
export default function DashboardError({ error, reset }){
  return (
    <div>
      <h2>Something went wrong</h2>
      <pre>{error.message}</pre>
      <button onClick={() => reset()}>Try again</button>
    </div>
  )
}
```

**Middleware: returning a custom Response**
```js
// middleware.js
import { NextResponse } from 'next/server'
export function middleware(req){
  try{
    // some logic
  } catch (err) {
    return new NextResponse('Middleware error', { status: 500 })
  }
}
```

### Best practices
- Handle expected errors explicitly (validation, 401/403) and use error boundaries for unexpected crashes.
- Avoid leaking sensitive error details in production — show friendly messages and log full error server-side.
- Use structured logging (Sentry, Datadog) in both API routes and middleware.
- For App Router, prefer granular `error.js` files in segments for better UX and isolation.

### Interview Q&A (concise)
- **How do you build a custom 404 in Next.js?** Create `pages/404.js` (Pages) or `not-found.js` segment (App Router) and export a component.
- **When to use middleware vs API route for error handling?** Middleware for request-level checks and redirects; API routes for business logic and detailed error responses.

---

## 2) Deployment (Vercel pipeline, static export, build optimization)

### Options
- **Vercel (managed)** — zero-config for Next.js, edge functions, image optimization on-demand, automatic builds on push.
- **Self-host Node server / Docker** — full control, required for features that need a Node server.
- **Static export (`next export`)** — good for purely static sites without server-side rendering or API routes.

### Vercel pipeline basics
- Push to Git (GitHub/GitLab/Bitbucket) → Vercel builds your app automatically.
- Configure Environment Variables in Vercel dashboard; secrets use `NEXTAUTH_SECRET`, etc.
- Choose Build & Output Settings (you usually can leave defaults: `next build`).
- Use Vercel Analytics and Edge Caching for performance insights.

### Static export notes
- `next export` produces an `out/` folder of HTML files. Limitations: no dynamic server-side rendering, API routes, or image optimization that requires server.

### Build optimization tips
- **Image optimization**: use `next/image` or rely on Vercel's on-demand optimizer when deployed to Vercel.
- **Code splitting**: dynamic `import()` and React.lazy for large components.
- **Bundle analysis**: use `next build && next analyze` (with `@next/bundle-analyzer`) to inspect heavy deps.
- **Avoid large node_modules** in client bundles — mark libs as server-only where possible.
- **Font loading**: use the Next.js font optimization (next/font) to reduce layout shift.

### CI/CD best practices
- Run linting and tests in pipeline before deploying.
- Cache `node_modules` and `.next/cache` when building in CI to speed up builds.
- Use Vercel Preview Deployments for PRs.

### Interview Q&A (concise)
- **When would you use `next export`?** For static sites with no server-side needs (no API routes or SSR). It generates static HTML per route.
- **How to reduce build time?** Cache build artifacts, use image CDNs rather than building heavy image processing locally, split monorepo builds.

---

## 3) Performance (next/script, prefetching, lazy loading)

### next/script
- `<Script>` component lets you control loading strategy for third-party scripts: `beforeInteractive`, `afterInteractive`, `lazyOnload`.
- Use `beforeInteractive` only for scripts required for initial render (rare). Prefer `afterInteractive` for analytics.

```jsx
import Script from 'next/script'
export default function MyApp(){
  return (
    <>
      <Script src="/analytics.js" strategy="afterInteractive" />
    </>
  )
}
```

### Prefetching & Link
- `<Link/>` auto-prefetches routes when in viewport in production to speed client navigation.
- Control `prefetch={false}` to reduce bandwidth if needed.

### Lazy loading
- Use dynamic imports for large components: `const Heavy = dynamic(() => import('./Heavy'))`.
- For images, `next/image` lazy-loads by default for offscreen images; use `priority` for hero images.

### Other performance techniques
- **Server Components (App Router)** reduce client JS by rendering on the server.
- **Streaming & Suspense** for faster Time-to-First-Byte UX.
- **Critical CSS & CSS Modules**: keep CSS small and use modular styles to avoid shipping unused CSS.
- **HTTP caching & CDN** — set proper cache headers for static assets; rely on Vercel/CDN.

### Diagnostics & Tools
- Lighthouse and Web Vitals (Core Web Vitals) — measure LCP, FID/INP, CLS.
- Next.js has built-in metrics and Vercel provides analytics.
- Bundle analyzers (`@next/bundle-analyzer`) and `next dev --profile` for profiling.

### Interview Q&A (concise)
- **What does `next/script` do?** Controls loading & execution strategy of third-party scripts to minimize blocking the main thread.
- **How to lazy-load a component in Next.js?** Use `next/dynamic` or React.lazy with Suspense (prefer `next/dynamic` in Next.js).

---

## Coding tasks (practical)
1. Create an `error.js` for an App Router route that shows friendly message and a retry button. (App Router)
2. Configure Vercel environment and a preview deployment for a Next.js app with image optimization enabled. (Deployment)
3. Replace a heavy analytics script with `<Script strategy="lazyOnload">` and demonstrate lazy loading a large component using `next/dynamic`. (Performance)

---

## Quick references
- Next.js docs: routing & error pages, app router error handling, deployment guides.
- Vercel docs: Next.js deployments and image optimization on Vercel.
- Tools: Lighthouse, `@next/bundle-analyzer`, Vercel analytics.

---

*This markdown is ready to preview and download.*

# Next.js Cheat Sheet — Image Optimization, File System Routing, App Router Advanced, Best Practices

> **Topic:** Next.js
> **Sub Topics:** Image Optimization; File System Routing; App Router Advanced (loading.tsx, error.tsx, layout nesting); Best Practices (server-side data hydration, minimal client bundle)

---

## 1. Image Optimization (next/image)

### Overview
Next.js provides a built-in Image component (`next/image`) that extends the HTML `<img>` element to deliver automatic image optimization: responsive sizes, modern formats (WebP/AVIF), lazy loading, placeholders, and on-demand resizing. Use it anywhere you render images for automatic performance gains.

### Key props
- `src` — string | StaticImport
- `width` / `height` — numbers for intrinsic sizing (or use `fill` for responsive parents)
- `alt` — accessibility text (required for meaningful images)
- `priority` — boolean for LCP images
- `placeholder` — `'blur'` with smallBase64 preloaded placeholder
- `sizes` — responsive `sizes` attribute for srcset control
- `quality` — 1–100; usually avoid changing unless needed

### Layout strategies
- `width`/`height`: preferred for stable layout and CLS prevention.
- `fill`: when the parent controls size (use with `position: relative` on parent).
- `responsive`: provide `sizes` and let Next.js serve best sized images.

### Configuration (next.config.js)
- `images.domains` — allow remote hostnames.
- `images.formats` — enable AVIF/WebP outputs.
- Custom loader or unoptimized option for special cases.

### Practical tips
- Use `priority` for LCP hero images.
- Set `placeholder='blur'` for UX polish on slow networks.
- When using `fill`, ensure parent has explicit dimensions and `position: relative`.

---

## 2. File System Routing (app & pages)

### App Router (file conventions)
- Folders map to URL segments.
- `page.jsx/ts` or `page.tsx` defines the UI for that segment.
- `layout.jsx/ts` defines UI that persists for that segment and its children (nested layouts).

### Dynamic routes & catch-all
- Dynamic segment: `[id]` or `[slug]` → captures a single segment.
- Catch-all: `[...rest]` → matches `/a/b/c` as an array param.
- Optional catch-all: `[[...rest]]` → matches zero or more segments.

### Route handlers
- `route.ts`/`route.js` inside a segment creates serverless handlers for REST-like APIs in that route.

### Nested routing
- Nest folders to create nested layouts and segments (e.g. `/blog/[slug]/comments`).
- Use `not-found.js` / `notFound()` to return 404s from server components.

---

## 3. App Router Advanced — loading.tsx, error.tsx, layout nesting

### `loading.tsx`
- Place `loading.tsx` inside a route segment folder to provide a Suspense fallback while Server Components or data fetches suspend.
- Nested `loading.tsx` screens appear for each segment that suspends; careful layout design prevents double-loading flashes.

### `error.tsx` / Error Boundaries
- `error.tsx` inside a segment provides a React Error Boundary for that segment and its children, isolating runtime exceptions and enabling graceful recovery UI.

### `layout.tsx` patterns
- Root layout must include `<html>` and `<body>`.
- Use nested layouts to persist navigation, sidebars, and chunk client bundles.
- Keep layouts as Server Components where possible; adopt Client Components only when interactivity is required.

---

## 4. Best Practices — Server-side data hydration & minimal client bundle

### Server vs Client Components
- Prefer Server Components for static and non-interactive UI: improved TTFB, smaller client JS.
- Use Client Components (`'use client'`) only for interactivity (hooks, browser APIs).

### Hydration strategies
- Hydrate minimal interactive islands (only the components that need client JS).
- Avoid heavy client-side state for parts that can be handled server-side or via Server Actions.

### Data fetching & caching
- Use server-side fetches in Server Components and cache results when appropriate.
- Server Actions can handle form submissions and mutations without exposing API routes.

### Bundle size & performance
- Tree-shake and lazy-load client-only code.
- Move third-party libraries behind Client Components or dynamic imports.
- Monitor bundle sizes with `next build` analyzers and split large dependencies.

---

## Interview Prep — Theory Questions (concise answers)

1. **What does `next/image` do?**
   - Automatically optimizes images (size, format, lazy-loading) and prevents layout shift.

2. **When to use `fill` vs width/height in `next/image`?**
   - `width`/`height` for intrinsic sizing; `fill` when parent controls layout (parent must be positioned and sized).

3. **How do dynamic routes work in the App Router?**
   - Use `[param]` for single dynamic segments and `[...rest]` / `[[...rest]]` for catch-all and optional catch-all segments; params are available to server components.

4. **What is `loading.tsx` used for?**
   - Suspense fallback for a route segment while server rendering or streaming content; it lets Next.js stream HTML progressively.

5. **How do `error.tsx` boundaries help?**
   - They isolate errors to a segment and its children, allowing the rest of the app to continue rendering.

6. **How to minimize client bundle size in Next.js?**
   - Prefer Server Components, lazy-load heavy libraries, use dynamic imports, and isolate third-party libs to client-only components.

7. **What is hydration and why does it matter?**
   - Hydration attaches client-side React to server-rendered HTML; mismatches cause runtime errors and visual glitches, so server and client renders should match.

---

## Interview Prep — Coding Questions (with brief guidance)

1. **Implement a responsive hero image using `next/image` with a blur placeholder.**
   - Use `Image` with `fill`, parent `position: relative`, and `placeholder='blur'` plus small base64 blurDataURL or imported static image.

2. **Create nested layouts: root layout + blog layout + post page.**
   - Show folder structure `app/layout.tsx`, `app/blog/layout.tsx`, `app/blog/[slug]/page.tsx` and keep shared nav in `blog/layout`.

3. **Add `loading.tsx` to show an animated skeleton while a slow data fetch resolves.**
   - Place `loading.tsx` inside the route segment folder and return skeleton markup; ensure server fetch suspends so fallback appears.

4. **Write a route handler `app/api/users/route.ts` that returns JSON with typed params.**
   - Export `GET` and use `RouteContext<'/api/users/[id]'>` for typed params and `Response.json()`.

5. **Optimize a page that currently hydates a large chart library on load.**
   - Dynamically import the chart component with `ssr: false` or move it into a Client Component that lazy-loads the library.

---

## Quick Reference Snippets

**Responsive Image (fill + blur)**
```tsx
import Image from 'next/image'
export default function Hero(){
  return (
    <div style={{position:'relative', width:'100%', height: '60vh'}}>
      <Image src="/hero.jpg" alt="hero" fill placeholder="blur" blurDataURL="data:image/..." priority />
    </div>
  )
}
```

**Dynamic route folder structure**
```
app/
  layout.tsx
  page.tsx
  blog/
    layout.tsx
    page.tsx
    [slug]/
      page.tsx
      loading.tsx
      error.tsx
```

**Simple route handler**
```ts
// app/api/users/[id]/route.ts
import type { NextRequest } from 'next/server'
export async function GET(_req: NextRequest, ctx: RouteContext<'/api/users/[id]'>) {
  const { id } = await ctx.params
  return Response.json({ id })
}
```

---

## Where to read next
- Official Next.js docs pages for Image, App Router file conventions, loading & error conventions, and Server/Client Components.

---

*Generated for quick interview prep and as a downloadable cheat-sheet.*

