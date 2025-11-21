# Box Model Cheat Sheet
## Topic: Box Model
## Sub Topic: content-box vs border-box, padding, margin, border, overflow

### Box Model Explained
The CSS box model describes how every element on a webpage is represented as a rectangular box composed of content, padding, border, and margin.

**Content**: The actual text or image inside the box.  
**Padding**: Space between content and border. Increases element’s visual size.  
**Border**: A line surrounding padding and content.  
**Margin**: Space outside the border. Used for spacing between elements.

### content-box vs border-box
**content-box (default)**  
Width/height apply *only* to the content box. Padding + border add to the final rendered size.

Example:  
Element styled with width: 200px, padding: 20px, border: 5px → total width = 200 + 40 + 10 = **250px**

**border-box**  
Width/height include padding + border. The content area shrinks to make room.

Example:  
Width: 200px, padding: 20px, border: 5px → final width = **200px**

### Overflow
Controls how content behaves when it exceeds its box.

- **visible**: content spills out  
- **hidden**: excess content clipped  
- **scroll**: scrollbars appear always  
- **auto**: scrollbars appear only when needed  

### Theory-based Interview Q&A
1. **What is the CSS box model?**  
   A structure describing how content, padding, borders, and margins define an element’s layout.

2. **Difference between margin and padding?**  
   Padding is inside the border; margin is outside the border and separates elements.

3. **When would you use border-box?**  
   When consistent sizing is needed without manual padding/border calculations.

4. **Does margin affect an element’s size?**  
   No. Margin affects spacing, not the element’s actual box size.

5. **Explain margin collapse.**  
   Adjacent vertical margins combine into one larger margin instead of adding.

### Coding-Based Questions
**1. Create a card layout where padding does not increase the card’s width.**
```css
.card {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 2px solid #333;
}
```

**2. Make text overflow ellipsis with hidden overflow.**
```css
.text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

**3. Demonstrate margin collapse.**
```css
.div1 {
  margin-bottom: 40px;
}
.div2 {
  margin-top: 30px;
}
/* Collapsed margin = 40px */
```

**4. Prevent overflow in a container.**
```css
.container {
  width: 400px;
  height: 200px;
  overflow: auto;
}
```

# CSS Positioning Cheat Sheet

## Topic: Positioning  
## Sub Topic: Position Types (static, relative, absolute, fixed, sticky)

---

## 1. Detailed Explanation

### Static Positioning
Default position of all elements.  
Elements follow normal document flow.  
`top`, `left`, `right`, `bottom`, `z-index` do not apply.

### Relative Positioning
Element stays in normal flow *but can be nudged* using `top`, `left`, `right`, `bottom`.  
The space it originally occupies remains.

### Absolute Positioning
Element is removed from normal flow.  
Positioned relative to the nearest ancestor with `position: relative | absolute | fixed | sticky`.  
If none found, it positions relative to the viewport.

### Fixed Positioning
Element is removed from layout flow.  
Always positioned relative to the viewport (window).  
Stays fixed even when scrolling.

### Sticky Positioning
Hybrid of relative + fixed.  
Acts like `relative` until scroll reaches a threshold, then sticks like `fixed`.  
Needs a parent with enough scrollable space.

---

## 2. Theory-Based Interview Questions (With Concise Answers)

### 1. What is the default `position` property in CSS?
Static. The element follows normal flow.

### 2. How does `relative` differ from `absolute`?
Relative stays in flow; absolute is removed from flow and positioned relative to nearest positioned ancestor.

### 3. What does `position: sticky` require to work?
A scrollable parent and defined top/left offsets.

### 4. Why isn’t `absolute` positioning working sometimes?
Because no positioned ancestor exists; it defaults to viewport.

### 5. Does `fixed` depend on parent elements?
No, fixed is always relative to viewport.

### 6. Can `z-index` work on static elements?
No, element must be positioned (non-static).

---

## 3. Coding-Based Questions

### Q1: Create a sticky header
```css
header {
  position: sticky;
  top: 0;
  background: white;
  padding: 10px;
}
```

### Q2: Center an element using absolute positioning
```css
.box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

### Q3: Make a floating fixed button in bottom-right
```css
.fab {
  position: fixed;
  right: 20px;
  bottom: 20px;
  padding: 15px;
  border-radius: 50%;
}
```

### Q4: Element positioned relative to parent
```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 10px;
  left: 10px;
}
```

---

File ready for download.

# Display & Visibility Cheat Sheet

## Topic: Display & Visibility  
## Sub Topic: display types (inline, block, flex, grid, none), visibility

### Display Types Explained

inline  
- Elements flow with text.  
- No line breaks before/after.  
- Width/height cannot be set.

block  
- Takes full available width.  
- Starts on a new line.  
- Width/height can be set.

inline-block  
- Behaves like inline but allows width/height.

none  
- Removes element from layout entirely.

flex  
- Enables Flexbox layout.  
- Ideal for one‑dimensional alignment.  
- Children become flex items.

grid  
- Enables Grid layout.  
- Ideal for two‑dimensional layouts (rows + columns).  
- Children become grid items.

### Visibility

visibility: visible  
- Default; element is shown.

visibility: hidden  
- Element is hidden but still occupies space.

visibility: collapse  
- Mostly for table rows; collapses layout spacing.

---

## Theory Questions for Interviews (With Short Answers)

What is the difference between display: none and visibility: hidden?  
- display: none removes element from layout; visibility: hidden hides but keeps space.

Difference between inline and block?  
- inline flows with text, can’t set width/height; block starts new line and supports dimensions.

Why use inline-block?  
- For inline placement with width/height control.

When choose flex vs grid?  
- Flex for one-dimensional layouts; Grid for two-dimensional.

Does display: none remove event listeners?  
- Element becomes non-interactive, but listeners remain when shown again.

---

## Coding-Based Questions

1. Center a div with flexbox  
```css
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

2. Create a 3‑column grid  
```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

3. Convert inline elements to blocks  
```css
span {
  display: block;
}
```

4. Hide element while keeping layout  
```css
.box {
  visibility: hidden;
}
```

5. Responsive card layout with flex wrap  
```css
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
```

# Flexbox Cheat Sheet  
## Topic: Flexbox  
## Sub Topic: Flex Container Properties, Alignment, Ordering, Wrapping

---

## 1. Flexbox Overview  
Flexbox (Flexible Box Layout) is a one‑dimensional layout system designed to arrange items along a single axis — either horizontally (row) or vertically (column). It simplifies alignment, distribution of space, and responsiveness.

---

## 2. Flex Container Properties  

### `display: flex` / `display: inline-flex`  
Turns an element into a flex container.

### `flex-direction`  
Controls main axis direction.  
- `row` (default)  
- `row-reverse`  
- `column`  
- `column-reverse`

### `flex-wrap`  
Controls wrapping of flex items.  
- `nowrap` (default)  
- `wrap`  
- `wrap-reverse`

### `flex-flow`  
Shorthand for `flex-direction` + `flex-wrap`.

### `justify-content` (main-axis alignment)  
- `flex-start`  
- `flex-end`  
- `center`  
- `space-between`  
- `space-around`  
- `space-evenly`

### `align-items` (cross-axis alignment)  
- `stretch` (default)  
- `flex-start`  
- `flex-end`  
- `center`  
- `baseline`

### `align-content`  
Controls alignment of multiple lines (when wrapping).  
- `stretch`  
- `flex-start`  
- `flex-end`  
- `center`  
- `space-between`  
- `space-around`

---

## 3. Flex Item Ordering & Alignment  

### `order`  
Controls the visual order of items (default = 0).

### `align-self`  
Overrides `align-items` for a single item.  
- `auto`  
- `flex-start`  
- `flex-end`  
- `center`  
- `baseline`  
- `stretch`

### `flex-grow`  
Defines how much an item can grow relative to others.

### `flex-shrink`  
Defines how much an item shrinks when space is tight.

### `flex-basis`  
Initial size of the item before free space is distributed.

### `flex` shorthand  
`flex: grow shrink basis;`

Examples:  
- `flex: 1` → grow:1, shrink:1, basis:0  
- `flex: 0 0 auto` (no grow/shrink, size based on content)

---

## 4. Frequently Asked Interview Theory Q&A  

### Q1: What problem does Flexbox solve?  
A: It simplifies alignment and spacing of items in one dimension, handling dynamic space distribution and responsiveness better than float‑based layouts.

### Q2: Difference between `justify-content` and `align-items`?  
A: `justify-content` aligns items along the main axis; `align-items` aligns them along the cross axis.

### Q3: What is the default flex-direction?  
A: `row`, meaning items flow left to right.

### Q4: How does `order` work?  
A: It changes the visual order without affecting the DOM order; items with smaller values appear first.

### Q5: When does `align-content` work?  
A: Only when there are multiple rows/columns created by wrapping.

---

## 5. Coding-Based Questions  

### 1. Center a div horizontally & vertically using flexbox  
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### 2. Create a responsive row that wraps  
```css
.row {
  display: flex;
  flex-wrap: wrap;
}
```

### 3. Make one flex item grow and fill available space  
```css
.item {
  flex: 1;
}
```

### 4. Reverse order of items  
```css
.container {
  display: flex;
  flex-direction: row-reverse;
}
```

### 5. Align one item differently from the others  
```css
.item.special {
  align-self: flex-end;
}
```

---

This concludes the Flexbox cheatsheet with container properties, alignment rules, item ordering, wrapping, interview questions, and coding examples.

# CSS Grid Layout Cheat Sheet

## Topic: Grid Layout  
## Sub Topic: Rows, Columns, Grid Template, Gap, Grid Areas, FR Units

CSS Grid is a two‑dimensional layout system that lets you arrange elements in rows and columns with remarkable control.

---

## Defining Rows & Columns
```css
display: grid;
grid-template-rows: 100px 200px auto;
grid-template-columns: 1fr 2fr 1fr;
```

## Grid Template
```css
grid-template:
  "header header" 80px
  "sidebar main" 1fr
  "footer footer" 60px
  / 200px 1fr;
```

## Gap
```css
gap: 20px;
row-gap: 10px;
column-gap: 30px;
```

## Grid Areas
```css
grid-template-areas:
  "nav nav"
  "aside main"
  "footer footer";
```

## fr Units
```css
grid-template-columns: 1fr 3fr;
```

## Interview Questions
**What is CSS Grid?**  
A two‑dimensional layout module for rows and columns.

**Difference between fr and px?**  
px is fixed; fr shares remaining space proportionally.

**Implicit vs explicit grid?**  
Explicit is defined; implicit auto‑generated for overflow.

## Coding Examples
```css
grid-template-columns: 1fr 2fr;
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
```


# Responsive Design Cheat Sheet

## Topic: Responsive Design  
### Sub Topic: Media Queries, Breakpoints, Mobile-First vs Desktop-First

## Responsive Design Overview
Responsive design ensures a website adapts smoothly to different screen sizes and devices. The layout, typography, spacing, and components adjust using CSS features like media queries and flexible units.

### Media Queries
Media queries allow conditional CSS based on viewport characteristics such as width, height, resolution, or orientation.

```css
@media (min-width: 768px) {
  .container {
    padding: 20px;
  }
}
```

---

### Breakpoints
Common breakpoints include:

- Mobile: 0–576px  
- Tablet: 577–768px  
- Laptop: 769–992px  
- Desktop: 993–1200px  
- Wide screens: 1200px+

---

### Mobile-First vs Desktop-First

#### Mobile-First
Start with small screens and scale up using min-width queries.

#### Desktop-First
Start with desktop screens and scale down using max-width queries.

---

## Theory Questions with Answers

**1. What is responsive design?**  
Design that adapts layouts to different viewport sizes.

**2. What are media queries?**  
CSS conditions that apply rules based on screen properties.

**3. Why mobile-first?**  
Lightweight, performance-oriented approach starting from constrained devices.

---

## Coding Questions

**Responsive columns:**
```css
.container { display: flex; flex-direction: column; }
@media (min-width: 768px) { .container { flex-direction: row; } }
```

**Responsive image:**
```css
img { max-width: 100%; height: auto; }
```

**Navbar hide on mobile:**
```css
.navbar { display: none; }
@media (min-width: 1024px) { .navbar { display: block; } }
```

---


# CSS Units Cheat Sheet

## Topic: CSS Units
## Sub Topic: px, em, rem, %, vw, vh, ch, calc(), min(), max(), clamp()

---

## 1. Core CSS Units

### px (Pixels)
- Absolute unit.
- Fixed regardless of parent or root font size.
- Commonly used for borders, small spacing, icons.

### em
- Relative to the **font-size of the element’s parent**.
- `1em = parent font-size`.
- Stacks cumulatively, so nested elements can compound scaling.

### rem (Root em)
- Relative to the **root (html) font-size**.
- Avoids compounding issues of `em`.
- Helpful for responsive typography.

### %
- Relative to the parent property’s size (depends on context).
- Width: % of parent width.
- Font-size: % of parent font-size.

### vw / vh  
- Viewport-based units.  
- `1vw = 1% of viewport width`  
- `1vh = 1% of viewport height`

### ch  
- Width of the “0” glyph in the current font.  
- Useful for text-based sizing (e.g., input widths).

---

## 2. Functional Units

### calc()
- Combines values using +, -, *, /.
- Example: `width: calc(100% - 50px);`

### min()
- Chooses the smallest of provided values.
- Example: `font-size: min(4vw, 2rem);`

### max()
- Chooses the largest of provided values.
- Example: `height: max(300px, 50vh);`

### clamp()
- Responsive min → preferred → max value.
- Example: `font-size: clamp(1rem, 2vw, 2rem);`

---

## 3. Theory-Based Interview Questions

**Q1: Difference between px, em, and rem?**  
**A:** px is absolute; em depends on parent font-size; rem depends only on root font-size.

**Q2: Why are rem units preferred over em for scalable design?**  
**A:** rem avoids compounding scaling because it references a single root value.

**Q3: What are viewport units used for?**  
**A:** Making layouts respond to screen dimensions (fullscreen sections, fluid text).

**Q4: When would you use ch?**  
**A:** When sizing elements based on characters, like input fields or monospace layouts.

**Q5: How does clamp() help in responsive design?**  
**A:** It keeps a value responsive within safe min/max limits.

---

## 4. Coding-Based Interview Tasks

**Task 1: Create a responsive heading using clamp()**
```css
h1 {
  font-size: clamp(1.5rem, 5vw, 3.5rem);
}
```

**Task 2: Create a box whose width is responsive but never below 300px**
```css
.box {
  width: min(80vw, 300px);
}
```

**Task 3: Input field with fixed character width using ch**
```css
input {
  width: 30ch;
}
```

**Task 4: Sidebar with calc() combining fixed and fluid units**
```css
.sidebar {
  width: calc(100% - 250px);
}
```

---

End of cheat sheet.

# CSS Transitions, Animations & Transforms — Cheat Sheet

## Topic: Transitions & Animations  
## Sub Topic: transition property, keyframes, easing functions, transforms

---

## Transitions

Transitions let a CSS property glide from one value to another. The browser interpolates the values over time.

### Core Properties
- `transition-property`: Which properties should animate.  
- `transition-duration`: How long the transition lasts.  
- `transition-timing-function`: How the acceleration feels (the easing).  
- `transition-delay`: When it begins.

### Example
```css
.box {
  transition: transform 0.4s ease-in-out;
}
.box:hover {
  transform: scale(1.1);
}
```

---

## Animations (Keyframes)

Animations break free from the “start → end” limits of transitions. They use keyframes to map intermediate states.

### Key Concepts
- `@keyframes`: Defines animation steps.  
- `animation-name`: Which keyframe set to use.  
- `animation-duration`: Time per cycle.  
- `animation-timing-function`: Easing.  
- `animation-iteration-count`: How many times it runs.  
- `animation-direction`: forward, reverse, alternate.  
- `animation-fill-mode`: Keep end state or reset.

### Example
```css
@keyframes pulse {
  0%   { transform: scale(1); }
  50%  { transform: scale(1.2); }
  100% { transform: scale(1); }
}

.circle {
  animation: pulse 2s ease-in-out infinite;
}
```

---

## Easing Functions

Easing shapes the “feel” of movement.

- `linear`: Constant speed.  
- `ease`: Starts slow → speeds up → slows.  
- `ease-in`: Accelerates into motion.  
- `ease-out`: Decelerates at the end.  
- `ease-in-out`: Starts slow + ends slow.  
- `cubic-bezier(x1, y1, x2, y2)`: Custom curves.

### Example
```css
transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
```

---

## Transforms

Transforms manipulate an element in 2D/3D space *without* affecting document flow.

### Useful Transform Functions
- `translate(x, y)`  
- `scale(x, y)`  
- `rotate(deg)`  
- `skew(x, y)`  
- `matrix(a, b, c, d, e, f)`  
- `perspective(n)`

### Example
```css
.card:hover {
  transform: translateY(-10px) rotate(2deg);
}
```

---

## Common Theory-Based Interview Q&A

1. **What is the difference between transitions and animations?**  
   Transitions animate *between two states*, requiring a trigger like `:hover`. Animations run via `@keyframes`, enabling multi-step, automated motion without user interaction.

2. **Why don’t all properties animate smoothly?**  
   Only *animatable* properties can interpolate numerical values. Some properties (like `display`) cannot animate.

3. **What does the timing function actually control?**  
   It shapes the rate of change over time—essentially the acceleration curve.

4. **What is the purpose of `animation-fill-mode`?**  
   Determines how the element behaves before and after animation—whether it keeps the final keyframe or resets.

5. **Why use `transform` for motion instead of `top/left`?**  
   GPU acceleration. Transforms avoid layout recalculations, making animations smoother.

---

## Coding Practice Questions

1. Create a button that slides 20px to the right on hover using transitions.  
2. Make a loader using a spinning animation with `@keyframes rotate`.  
3. Animate an element that grows, fades, and rotates using a single keyframe sequence.  
4. Recreate an easing curve using `cubic-bezier()` that starts slow and ends very fast.  
5. Build a 3D card flip animation using `transform: rotateY()` and perspective.

---

## End

# CSS Pseudo-Elements & Pseudo-Classes Cheat Sheet

## Topic: CSS Pseudo Elements & Pseudo Classes  
## Sub Topic: ::before, ::after, :hover, :focus, :nth-child

## 1. Detailed Explanation

### Pseudo-Elements
Pseudo-elements let you style specific parts of an element without requiring extra markup.

#### ::before
Creates a virtual element before the actual content.

#### ::after
Creates a virtual element after the actual content.

### Pseudo-Classes
Selectors that activate based on element state.

#### :hover
Triggers when pointer enters element.

#### :focus
Triggers on keyboard or programmatic focus.

#### :nth-child(n)
Pattern-based selection of siblings.

## 2. Interview Q&A

1. Difference between pseudo-elements and pseudo-classes?  
Pseudo-classes = state. Pseudo-elements = virtual elements.

2. Do ::before/::after need content?  
Yes.

3. When does :focus activate?  
When focused via keyboard or script.

4. Difference between :hover and :focus?  
:hover = pointer; :focus = keyboard/programmatic.

5. nth-child vs nth-of-type?  
nth-child counts all siblings; nth-of-type only same tag.

## 3. Coding Exercises

### Tooltip using ::after + :hover
```css
.tooltip { position: relative; }
.tooltip::after {
  content: attr(data-tip);
  position: absolute;
  opacity: 0;
}
.tooltip:hover::after { opacity: 1; }
```

### Alternating table rows
```css
tr:nth-child(even) { background: #eee; }
```

### Ripple button using ::after
```css
.button { position: relative; overflow: hidden; }
.button::after { content:""; transform: scale(0); }
.button:hover::after { transform: scale(1); }
```

# CSS Variables Cheat Sheet  
## Topic: CSS Variables  
## Sub Topic: --var Syntax, var() Usage, Scoping, Fallback Values

### 1. Detailed Explanation  

CSS variables (also called **custom properties**) let you store reusable values directly in CSS. They behave like tiny named containers that can be inherited, overridden, and dynamically changed.

#### • `--var` Syntax  
A CSS variable must start with **two hyphens**.  
Example:  
```css
:root {
  --primary-color: #3498db;
  --spacing-lg: 24px;
}
```

#### • `var()` Usage  
You retrieve a variable using `var(--name)`  
```css
button {
  color: var(--primary-color);
  padding: var(--spacing-lg);
}
```

#### • Scoping  
CSS variables follow **normal CSS cascade + inheritance rules**.  
You can define them globally:  
```css
:root {
  --font-size: 16px;
}
```

And override them locally:  
```css
.card {
  --font-size: 20px;
  font-size: var(--font-size);
}
```

Child elements inherit the overridden value unless they override again.

#### • Fallback Values  
`var()` lets you specify a fallback if the variable is **not defined**:  
```css
color: var(--unknown-color, black);
```

Fallback can even be another variable:  
```css
color: var(--theme-text, var(--default-text, #333));
```

---

### 2. Theory-Based Interview Questions (with concise answers)

**1. What are CSS variables?**  
Custom properties that store reusable values and participate in the CSS cascade and inheritance.

**2. How do CSS variables differ from preprocessor variables (Sass/LESS)?**  
CSS variables are dynamic, evaluated at runtime, can be changed by JS, and are inherited. Sass variables are static at compile time.

**3. Why do CSS variables start with two hyphens?**  
This syntax distinguishes custom properties from normal CSS properties.

**4. What happens if a CSS variable is not defined?**  
The browser uses the fallback value in `var()`, or the property becomes invalid.

**5. Where are CSS variables most commonly defined?**  
In `:root` for app-wide theme values.

**6. Are CSS variables inherited?**  
Yes, unlike many standard properties.

**7. Can CSS variables be animated?**  
Yes, if the underlying value is animatable (like colors or lengths).

---

### 3. Coding-Based Questions  

**Q1. Implement a theme switcher using CSS variables.**  
```css
:root {
  --bg: white;
  --text: black;
}

.dark {
  --bg: black;
  --text: white;
}

body {
  background: var(--bg);
  color: var(--text);
}
```
```js
document.body.classList.toggle("dark");
```

**Q2. Create a button component that adjusts size using CSS variables.**  
```css
button {
  --padding: 12px;
  padding: var(--padding);
}

button.large {
  --padding: 20px;
}
```

**Q3. Write CSS that uses fallback values when variables are missing.**  
```css
.box {
  width: var(--box-width, 200px);
  background: var(--box-bg, #eee);
}
```

---

This file covers CSS Variables in depth and includes theory plus coding examples for interview prep.


# Advanced CSS Selectors  
## Topic: Selectors Advanced  
## Sub Topic: Attribute Selectors, :is(), :where(), :has()

---

## 1. Attribute Selectors (Detailed)

CSS attribute selectors let you target elements based on the presence or value of attributes, without adding extra classes. They fit beautifully into the web’s ecosystem of semantic markup.

### Common Forms

- `[attr]`  
  Selects elements that have the given attribute.  
  Example: `input[required]`.

- `[attr="value"]`  
  Exact match.  
  Example: `a[target="_blank"]`.

- `[attr^="value"]`  
  Prefix match (“starts with”).  
  Example: `img[src^="/assets"]`.

- `[attr$="value"]`  
  Suffix match (“ends with”).  
  Example: `a[href$=".pdf"]`.

- `[attr*="value"]`  
  Substring match (“contains”).  
  Example: `div[class*="theme-dark"]`.

- `[attr~="value"]`  
  Contains a whitespace‑separated value.  
  Example: `[title~="admin"]`.

- `[attr|="value"]`  
  Matches exact value or prefix followed by hyphen.  
  Example: `[lang|="en"]` → `en`, `en-US`, `en-GB`.

---

## 2. The :is() Pseudo-Class

`:is()` groups selectors while preserving overall specificity.  
It picks the *selector with the highest specificity inside it*.

### Example
```css
:is(h1, h2, h3).highlight {
  color: tomato;
}
```
Behaves as if you wrote:
```css
h1.highlight, h2.highlight, h3.highlight { ... }
```

### Why It’s Useful
It reduces repetition while keeping intentional specificity.

---

## 3. The :where() Pseudo-Class

`:where()` behaves like `:is()` except it **always has zero specificity**.  
This makes it powerful for writing global/utility rules without accidentally overriding component styles.

### Example
```css
:where(nav ul) {
  list-style: none;
  padding: 0;
}
```

### Use Case
Reset-style helpers that should never “win” in specificity battles.

---

## 4. The :has() Pseudo‑Class (Parent Selector)

`:has()` allows selecting an element *based on its descendants, children, or contained elements*.  
This is the long‑awaited “parent selector”.

### Example: Highlight a card if it contains an error
```css
.card:has(.error) {
  border: 2px solid red;
}
```

### Example: Style a `<label>` if its input is checked
```css
label:has(input:checked) {
  font-weight: bold;
}
```

### Example: Select an empty container that *should* have content
```css
.container:not(:has(*)) {
  min-height: 200px;
  background: #f5f5f5;
}
```

---

## 5. Interview Theory Questions & Answers

**Q1. Difference between :is() and :where()?**  
`:is()` keeps the highest specificity of its arguments.  
`:where()` always has zero specificity and never wins tie-breakers.

**Q2. Why is :has() called the parent selector?**  
Because it lets you style an element based on what it contains, enabling upward logic like selecting a parent when a child matches some condition.

**Q3. When do you use attribute selectors instead of classes?**  
When styling based on semantic attributes (like `type`, `required`, `target`) without polluting HTML with unnecessary classes.

**Q4. How does `[attr^="value"]` differ from `[attr*="value"]`?**  
`^=` matches from the start (prefix).  
`*=` matches anywhere (substring).

**Q5. Why is :where() useful in CSS resets?**  
It applies styles without adding specificity, ensuring these rules cannot override component‑level styles.

---

## 6. Coding / Practical Exercises

### Task 1: Select all external links
Write CSS that adds an icon to links leaving the domain:
```css
a[href^="http"]:not([href*="mysite.com"])::after {
  content: "↗";
}
```

### Task 2: Highlight empty FAQ sections
```css
.faq:has(.question:empty) {
  background: #fff3cd;
}
```

### Task 3: Custom input focus wrapper using parent selector
```css
.field:has(input:focus) {
  border-color: royalblue;
  box-shadow: 0 0 4px rgba(65, 105, 225, 0.4);
}
```

### Task 4: Case-insensitive attribute match
(HTML attributes can be matched case‑insensitive using `i`)
```css
a[href$=".pdf" i] {
  color: crimson;
}
```

---

This cheat sheet embraces the more expressive edges of CSS selector logic, where you start shaping structure by reasoning about relationships instead of piling on classes. A good next path is combining these selectors with container queries and modern cascade strategies.


# Topic : Preprocessors
## Sub Topic : SASS basics, nesting, mixins, variables, extends

---

## 1. Quick Overview
Sass (Syntactically Awesome Stylesheets) is a CSS preprocessor that adds powerful features—variables, nesting, mixins, inheritance, functions, and control directives—that compile into standard CSS. It speeds development, reduces repetition, and makes large stylesheets maintainable.

Sass comes in two syntaxes:
- **SCSS**: CSS-compatible; uses `{}` and `;`. Most popular.
- **Sass (indented)**: Older indentation-based syntax.

This cheat sheet uses SCSS syntax.

---

## 2. Basics & Installation
- Install with npm: `npm install -D sass`
- Compile single file: `sass input.scss output.css`
- Watch files: `sass --watch scss:css`
- Recommended workflow: Use build tools (Vite, Webpack, Parcel) or the Dart Sass CLI.

---

## 3. Variables
Declare reusable values.
```scss
$primary: #0d6efd;
$gap: 16px;
$font-stack: 'Inter', system-ui, sans-serif;

body {
  font-family: $font-stack;
  color: $primary;
}
```
- Variables can hold colors, numbers, strings, maps, lists.
- Use interpolation: `#{$variable}` inside selectors or properties.

---

## 4. Nesting
Nest selectors to reflect DOM structure; be careful not to over-nest.
```scss
.nav {
  ul {
    margin: 0;
    li {
      display: inline-block;
      a {
        text-decoration: none;
        &:hover { color: darken($primary, 10%); }
      }
    }
  }
}
```
- Use `&` to refer to parent selector (`&:hover`, `&.mod`, `& > span`).
- Avoid deep nesting (2–3 levels recommended).

---

## 5. Mixins
Reusable chunks of styles; can accept arguments and default values.
```scss
@mixin clearfix {
  &::after {
    content: "";
    display: table;
    clear: both;
  }
}

@mixin responsive($break: 768px) {
  @media (max-width: $break) {
    @content;
  }
}

/* Usage */
.container { @include clearfix; }
.header {
  @include responsive(600px) {
    font-size: 14px;
  }
}
```
- Use `@content` to inject nested child rules into mixin.
- Prefer mixins for repeated property groups (vendor prefixes, common patterns).

---

## 6. Functions
Create reusable functions returning values.
```scss
@function rem($px, $base: 16) {
  @return #{$px / $base}rem;
}

h1 { font-size: rem(32); }
```

---

## 7. Extends / Inheritance
Share whole selectors with `%placeholder` and `@extend`.
```scss
%btn-base {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 6px;
}

.btn-primary {
  @extend %btn-base;
  background: $primary;
  color: white;
}
```
- `@extend` merges selectors at compile-time; results in combined selectors.
- Use `%placeholder` to avoid generating standalone CSS.
- Be cautious: `@extend` can produce long combined selectors if overused.

---

## 8. Partials & Imports
- Create partials `_variables.scss`, `_mixins.scss`, `_buttons.scss`.
- Import in main file: `@use 'variables'; @use 'mixins';`
- **Prefer `@use` / `@forward` over `@import`** (modern Sass modules).
```scss
// variables.scss
$brand: #111;

// main.scss
@use 'variables' as vars;
body { color: vars.$brand; }
```

---

## 9. Control Directives
Logic and loops inside styles.
```scss
@for $i from 1 through 5 {
  .col-#{$i} { width: 20% * $i; }
}

@mixin generate-grid($cols) {
  @for $i from 1 through $cols {
    .grid-#{$i} { width: 100% / $cols * $i; }
  }
}
```

---

## 10. Maps & Lists
Powerful data structures.
```scss
$themes: (
  light: (bg: #fff, fg: #222),
  dark: (bg: #111, fg: #fff)
);

@each $name, $map in $themes {
  .theme-#{$name} {
    background: map-get($map, bg);
    color: map-get($map, fg);
  }
}
```

---

## 11. Best Practices
- Prefer `@use` + `@forward` for modular code.
- Keep nesting shallow (max 3 deep).
- Use variables for design tokens (spacing, colors, type).
- Use mixins for behavioral blocks, placeholders `%` for structural sharing.
- Avoid `@extend` for unrelated selectors; use with `%placeholder` to limit scope.
- Name partials clearly: `_variables.scss`, `_utils.scss`, `_components/_button.scss`.
- Favor composition over inheritance for predictable output.

---

## 12. Interview Theory Questions (with concise answers)

1. **What is Sass and why use it?**  
   Sass is a CSS preprocessor adding variables, nesting, mixins, functions, and modules to write maintainable CSS. It reduces repetition and improves scalability.

2. **Difference between SCSS and Sass syntax?**  
   SCSS uses block braces and semicolons (CSS-compatible). Sass uses indentation and no braces/semicolons.

3. **What are Sass variables and their scope?**  
   Variables store values. By default they are file-scoped when using `@use`—namespaced unless explicitly `@forward`ed. Global variables can be created but are discouraged.

4. **How does `@mixin` differ from `@extend`?**  
   `@mixin` injects code where called (can accept args). `@extend` merges selectors to share rules and avoids duplication in output but can create complex selectors.

5. **When to use mixins vs functions?**  
   Use functions to compute and return values. Use mixins to emit rulesets or multiple properties and accept `@content`.

6. **Explain `@use` vs `@import`.**  
   `@use` is the modern module system (namespaced, avoids duplication). `@import` is deprecated and concatenates files leading to variable pollution.

7. **How to prevent excessive specificity with nesting?**  
   Keep nesting shallow, prefer utility classes, and use `&` carefully. Limit to 2–3 levels.

8. **What are placeholders (`%`) and why use them?**  
   Placeholders are silent selectors used with `@extend`. They let you share styles without generating standalone CSS.

9. **How does Sass handle control directives like loops?**  
   Sass compiles directives (`@for`, `@each`, `@while`, `@if`) into repeated CSS rules at compile time.

10. **What is the recommended way to structure a large Sass project?**  
    Use modular partials with `@use` and `@forward`, keep variables centralized, split components into folders, and avoid global side-effects.

---

## 13. Coding / Practical Interview Questions (with short solutions/snippets)

1. **Create a responsive grid generator mixin**  
```scss
@mixin grid($cols, $gap: 16px) {
  display: grid;
  gap: $gap;
  grid-template-columns: repeat($cols, 1fr);
}
.container { @include grid(3); }
```

2. **Write a button mixin with variant support**
```scss
@mixin button($bg, $color: #fff, $pad: 12px 20px) {
  display: inline-block;
  padding: $pad;
  background: $bg;
  color: $color;
  border-radius: 6px;
  text-align: center;
}
.btn { @include button($primary); }
.btn.secondary { @include button(#6c757d); }
```

3. **Generate utilities for spacing (margin helpers)**
```scss
@for $i from 0 through 5 {
  .m-#{$i} { margin: $i * 4px; }
  .p-#{$i} { padding: $i * 4px; }
}
```

4. **Use map-driven theming**
```scss
$themes: (
  primary: #0d6efd,
  success: #198754
);

@each $name, $color in $themes {
  .btn-#{$name} { background: $color; color: white; }
}
```

5. **Avoid duplication: placeholder + modifier**
```scss
%card-base { padding: 16px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.06); }
.card { @extend %card-base; }
.card-compact { @extend %card-base; padding: 8px; }
```

---

## 14. Quick Reference (Common Functions & Directives)
- Color: `lighten($c, 10%)`, `darken($c, 10%)`, `mix($a, $b, 30%)`
- Math: `percentage()`, arithmetic: `1px * 2`
- Lists: `nth($list, n)`, `length($list)`
- Maps: `map-get($map, key)`, `map-merge($a, $b)`
- Control: `@if`, `@else`, `@for`, `@each`, `@while`
- Modules: `@use`, `@forward`, `@import` (deprecated)

---

## 15. Closing Tips
- Start components with small focused partials.
- Use design tokens (variables) for theming.
- Use linters (stylelint) + Prettier for style and consistency.
- Test compiled CSS size when using `@extend` vs mixins.

---

*Prepared as an interview-focused cheat sheet for "Preprocessors — SASS basics, nesting, mixins, variables, extends".*

# Topic: Performance

## Sub Topic: Critical CSS, Render-Blocking, CSSOM, File Size Optimization

---
## 1) Overview — what we mean by performance here

This sheet focuses on reducing time-to-first-render and time-to-interactive by addressing CSS-related bottlenecks. Key goals: reduce render-blocking work, make the browser paint meaningful content quickly, and minimize bytes over the network.

---
## 2) Critical CSS — concept and workflow

**What is Critical CSS?**
Critical CSS is the small subset of CSS rules required to render above-the-fold (initial viewport) content. You inline or prioritize these rules so the browser can paint the page without waiting for the full stylesheet.

**Why it helps**
- Avoids blocking the first paint on external stylesheet fetch + CSSOM construction.
- Reduces layout/paint thrashing caused by late style changes.

**Typical workflow**
1. Identify above-the-fold styles for a set of common viewports.
2. Extract those rules into a small chunk (the "critical" CSS).
3. Inline that chunk into `<head>` (small size) or deliver via `rel="preload"` + onload swap.
4. Load the full stylesheet asynchronously.

**Tools**
- `penthouse` (Node) — extracts critical CSS per URL.
- `critical` (npm) — integrates with build pipelines.
- Build-time: webpack, rollup plugins; frameworks may provide helpers.

**Caveats**
- Device/resolution differences: critical CSS for desktop and mobile can differ; aim for a conservative common subset or generate multiple critical snippets and serve based on UA/viewport.
- Over-inlining bloats HTML. Keep critical <style> under ~14–20 KB ideally.

---
## 3) Render-blocking CSS — how browsers treat CSS

**Browser steps affecting rendering:**
1. Fetch HTML, parse.
2. Encounter `<link rel="stylesheet">` → fetch CSS synchronously by default.
3. Build CSSOM while building DOM → combine into Render Tree.
4. Layout & paint happen only after stylesheet is known.

Thus, external stylesheets are *render-blocking* because the browser cannot accurately layout and paint without them.

**Mitigations:**
- Inline critical CSS.
- Use `rel="preload" as="style" onload="this.rel='stylesheet'"` (preload+onload pattern).
- Use `media` attributes (e.g. `media="print"` then switch) for non-critical styles.
- Load non-critical CSS asynchronously via JavaScript (`loadCSS`, `fetch` + `rel='stylesheet'` swap).
- HTTP/2 helps (multiplexing) but doesn't remove CSSOM dependency.

---
## 4) CSSOM (CSS Object Model) — what to know

**What:** the tree structure the browser builds from CSSOM + DOM to compute the render tree.

**Why it matters:**
- CSSOM construction must finish before layout; large CSS causes long CSSOM parse times (CPU-bound, not just network-bound).
- Specific selector complexity (deep descendant selectors, complex combinators) increases parse and matching cost.

**Optimization tips:**
- Flatten overly-specific complex selectors. Prefer class-based selectors (`.btn--primary`) over chained descendant selectors.
- Avoid `:nth-child()` and heavy attribute selectors in critical paths if possible.
- Keep stylesheet count low (but not at cost of huge files). Many small files can increase network overhead — but HTTP/2 lessens this.

---
## 5) File-size optimization — network & compression

**Core tactics:**
- Minify CSS (remove whitespace/comments) — build step.
- Remove unused CSS (`purgecss`, `unCSS`, Tailwind purge`) — big wins for utility frameworks.
- Tree-shake component-level styles where possible (CSS-in-JS with SSR that inlines only used styles).
- Compress responses: Gzip or Brotli; Brotli often yields smaller sizes for text content.
- Use `cache-control` headers and long cache lifetimes for immutable assets (include content hashes in filenames).
- Split CSS: critical inline + deferred large bundle.
- Serve over HTTP/2 or HTTP/3 to benefit from multiplexing.

**Assets & fonts:**
- Avoid embedding large SVGs or fonts in CSS unless necessary.
- Subset fonts (only required glyphs), use `font-display: swap`, and preload key font files with `rel="preload" as="font" crossorigin`.

---
## 6) Practical patterns (code snippets & HTML patterns)

**Inline small critical CSS**
```html
<head>
  <style>/* small critical CSS (inlined) */</style>
  <link rel="stylesheet" href="/styles/full.css">
</head>
```

**Preload + onload swap**
```html
<link rel="preload" href="/styles/full.css" as="style" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/styles/full.css"></noscript>
```

**Media swap trick for non-critical**
```html
<link rel="stylesheet" href="/styles/noncritical.css" media="print" onload="this.media='all'">
```

**Asynchronous load via JS (loadCSS idea)**
```js
function loadStyle(href){
  const l = document.createElement('link');
  l.rel = 'stylesheet';
  l.href = href;
  document.head.appendChild(l);
}
loadStyle('/styles/noncritical.css');
```

---
## 7) Interview-style theory questions (concise answers)

**Q1: Why is CSS render-blocking?**
A: Browsers must build CSSOM and combine with DOM to form the render tree; doing so before layout avoids flash-of-unstyled-content and incorrect layout — therefore external CSS blocks rendering.

**Q2: What is Critical CSS and when should you inline it?**
A: Critical CSS is the minimal CSS needed to style above-the-fold content. Inline when it’s small (a few KB) and will significantly reduce first paint time.

**Q3: How does `rel="preload"` differ from `rel="stylesheet"`?**
A: `preload` tells the browser to fetch early but does not apply styles. You must swap `rel` to `stylesheet` (or use `onload`) to apply.

**Q4: How do you reduce CSSOM construction cost?**
A: Reduce total CSS size, simplify selectors, avoid heavy combinators, and split critical/non-critical CSS.

**Q5: When is inlining critical CSS harmful?**
A: When it grows too large (bloated HTML responses), causing HTML to be heavy and slow to parse; also complicates cacheability.

---
## 8) Coding / applied interview questions

**C1: Write a small Node script that uses `penthouse` to produce critical CSS for a given URL.**
- Expectation: know how to use npm packages and run at build time. (Real code often runs in CI to precompute critical CSS.)

**C2: How would you measure the impact of your optimizations?**
- Use Lighthouse (Lab), WebPageTest (waterfall + filmstrip), Real User Monitoring (RUM) metrics: FCP, LCP, TTFB, TTI, CLS.

**C3: How to integrate CSS purge into a build for Tailwind?**
- Configure `content` globs in `tailwind.config.js`, run production build (NODE_ENV=production) which purges unused classes.

**C4: Given a large stylesheet, how would you find unused selectors?**
- Run coverage tools in Chrome DevTools (Coverage tab), or use `purgecss` with the project’s HTML/JSX templates.

---
## 9) Quick checklist for production deployment

- [ ] Extract and inline critical CSS for main templates (keep small).
- [ ] Defer or asynchronously load non-critical CSS.
- [ ] Minify and compress (Brotli/Gzip) CSS files.
- [ ] Purge unused CSS and subset fonts.
- [ ] Set immutable caching (content-hash filenames).
- [ ] Test with Lighthouse and WebPageTest; validate FCP/LCP improvements.

---
## 10) References & next steps

- Use `penthouse` or `critical` for automatic extraction.
- Audit with Lighthouse and DevTools coverage.
- Consider CSS-in-JS / component-level styling if your app benefits from on-demand CSS generation.

---
*Generated as a concise interview-ready cheat sheet. Save as `.md` for use in interview prep or documentation.*


# CSS-in-JS Cheat Sheet

## Topic: CSS-in-JS  
## Sub Topic: Overview, Techniques, Patterns, Interview Q&A, Coding Tasks

---

## 📌 CSS-in-JS Explained

CSS-in-JS is a styling approach where CSS is composed using JavaScript. Instead of writing `.css` files, styles are defined inside JS/TS components. Libraries like **Styled Components**, **Emotion**, **JSS**, and **Stitches** follow this pattern.

It became popular in React ecosystems because styles can be co-located with components, dynamic styling becomes easier, and you avoid global namespace collisions.

---

## 🎯 Why CSS-in-JS?

CSS-in-JS solves classic CSS problems:  
• No global name collisions  
• Component-scoped styles  
• Dynamic styles based on props/state  
• Theming becomes straightforward  
• Dead-code elimination and compile-time optimizations  

At the same time, it has trade-offs:  
• Runtime cost (if library evaluates styles in browser)  
• Debugging class names sometimes harder  
• Bundle size overhead for some libraries  

Modern libs (Stitches, Emotion, Linaria, Vanilla Extract) reduce these issues with **static extraction**.

---

## 🧩 Core Ideas

### Scoped Styles  
Each component gets unique class names via hashing → avoids collisions.

### Dynamic Styling  
Props can change CSS:  
```js
const Button = styled.button`
  background: ${props => props.primary ? "blue" : "gray"};
`;
```

### Theming  
Use theme providers:  
```js
<ThemeProvider theme={{ primary: "#3498db" }}>
```

### Runtime vs Static CSS-in-JS  
**Runtime** — Styles computed in browser  
Examples: Styled Components, Emotion  

**Static** — CSS extracted at build time  
Examples: Linaria, Vanilla Extract  

Static extraction avoids runtime overhead.

---

## 🛠 Common CSS-in-JS Libraries

### Styled Components  
- Tagged template literals  
- Best for React  
- Large ecosystem  

### Emotion  
- Similar to SC but more flexible  
- Object syntax + template literals  

### JSS  
- Mostly used with Material UI (legacy versions)  

### Stitches / Panda CSS / Vanilla Extract  
- Modern, fast, compile-time focused  

---

## 🧠 Interview-Oriented Theory Questions

**1. What is CSS-in-JS?**  
A styling technique where CSS rules are written inside JS/TS, enabling component-level scoping, dynamic styling, and theming.

**2. Why was CSS-in-JS created?**  
To solve global CSS conflicts, simplify component-based styling, and support dynamic styles without manually managing class names.

**3. Differences between Styled Components and Emotion?**  
Emotion is lighter and supports object syntax; Styled Components is template-literal-only with heavier runtime.

**4. Explain static extraction in CSS-in-JS.**  
A technique where libraries extract CSS at build time, eliminating runtime overhead and generating `.css` files.

**5. Downsides of CSS-in-JS?**  
Runtime overhead, bundle bloat, slower SSR in older libraries, potential debugging complexity.

**6. What problem does hashing solve?**  
It ensures unique class names → avoids global namespace collisions.

---

## 💻 Coding Questions for Interviews

### 1. Create a button using Styled Components with dynamic props
```js
const Button = styled.button`
  padding: 10px 20px;
  border-radius: 6px;
  background: ${props => props.primary ? "#0070f3" : "#888"};
  color: white;
`;
```

### 2. Build a themeable card component
```js
const Card = styled.div`
  background: ${({ theme }) => theme.bg};
  border-radius: 8px;
  padding: 16px;
`;
```

### 3. Emotion object-style example
```js
const box = css({
  padding: "20px",
  backgroundColor: "tomato",
});
```

### 4. Write a CSS-in-JS media query
```js
const Wrapper = styled.div`
  width: 100%;
  @media (max-width: 600px) {
    padding: 10px;
  }
`;
```

### 5. Create a reusable mixin
```js
const flexCenter = css`
  display: flex;
  justify-content: center;
  align-items: center;
`;

const Box = styled.div`
  ${flexCenter}
  height: 200px;
`;
```

---

## 📥 End of Cheat Sheet  
Download the file containing all the content above.


# CSS New Features Cheat Sheet
## Topic: New Features
## Sub Topic: Container Queries, Subgrid, Logical Properties, :has()

---

# 1. Container Queries

Container Queries let elements style themselves based on the size of their parent container instead of the viewport. They solve the age‑old “component breaks when placed in a smaller sidebar” nightmare.

### Syntax
```css
.card {
  container-type: inline-size;
  container-name: card-container;
}

@container card-container (min-width: 400px) {
  .card img { float: right; }
}
```

### When to Use
- Responsive components
- Design systems where components adapt to the space they occupy
- Complex layouts placed in unpredictable containers

---

# 2. CSS Subgrid

Subgrid allows child grid items to inherit the grid tracks of their parent, enabling deeply aligned layouts.

### Example
```css
.parent {
  display: grid;
  grid-template-columns: 150px 1fr;
}

.child {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: 1 / -1;
}
```

### Benefits
- Perfect alignment across nested components
- No duplication of grid definitions
- Cleaner layout logic in design systems

---

# 3. Logical Properties

Logical properties adapt layout to writing modes (horizontal, vertical, RTL). Instead of physically tied properties like `margin-left`, they offer direction-agnostic properties like `margin-inline-start`.

### Example
```css
.box {
  padding-block: 1rem;      /* replaces padding-top & padding-bottom */
  margin-inline: 2rem;      /* replaces margin-left & margin-right */
  border-inline-start: 2px solid red;
}
```

### Why Important
- Globalization-ready layouts
- Better maintainability
- Avoids hardcoded directional styles

---

# 4. The `:has()` Selector (Parent Selector)

`:has()` is a relational pseudo-class that allows selecting an element based on its descendants or siblings. This is CSS gaining its long-awaited “if child exists” superpower.

### Example
```css
.form:has(.error) {
  border: 2px solid red;
}

.card:has(img:hover) {
  transform: scale(1.02);
}
```

### What It Enables
- Conditional styling
- Parent-level control based on dynamic content
- Eliminates JS-only styling hacks

---

# Interview Questions (Short Answers)

### Container Queries
1. **Why do we need container queries?**  
   They let components adapt to the size of their container instead of the full viewport.

2. **How are container queries activated?**  
   By defining `container-type` (or shorthand: `container`).

3. **Difference between container queries and media queries?**  
   Media queries depend on viewport size; container queries depend on element size.

### Subgrid
1. **What problem does Subgrid solve?**  
   Aligning nested grids without repeating grid definitions.

2. **Does Subgrid support both rows and columns?**  
   Yes, using `grid-template-columns: subgrid` or `grid-template-rows: subgrid`.

### Logical Properties
1. **Why use logical properties?**  
   They adapt automatically to writing modes (LTR/RTL/vertical).

2. **Example of logical vs physical property?**  
   `margin-inline-start` replaces `margin-left`.

### :has()
1. **Why is :has() considered a parent selector?**  
   Because it can style a parent based on the presence of specific children.

2. **Is :has() expensive?**  
   Browsers optimize it, but heavy combinator chains can slow performance.

---

# Related Coding-Based Questions

### 1. Build a card component that switches layout when parent container is wide.
```css
.card-wrapper {
  container-type: inline-size;
}

@container (min-width: 480px) {
  .card {
    display: flex;
  }
}
```

### 2. Create a nested layout where children align with parent grid using subgrid.
```css
.parent {
  display: grid;
  grid-template-columns: 200px 1fr;
}

.child {
  display: grid;
  grid-template-columns: subgrid;
}
```

### 3. Write RTL-friendly button padding using logical properties.
```css
.btn {
  padding-inline: 1rem;
  padding-block: 0.5rem;
}
```

### 4. Highlight forms that have invalid input using :has().
```css
form:has(input:invalid) {
  border-color: red;
}
```

---

# End