## concepts

### When you write a Node.js file, Node secretly wraps your entire code inside this function before executing it:

Answer: - module wrapper function

```js
(function (exports, require, module, __filename, __dirname) {
  // your code here
});

```

- It provides scope isolation and useful context variables for each module.




| Parameter    | Description                                                        |
| ------------ | ------------------------------------------------------------------ |
| `exports`    | A shortcut to `module.exports`. Used to export things from a file. |
| `require`    | Function used to import other modules.                             |
| `module`     | Represents the current module itself (metadata + exports).         |
| `__filename` | The absolute path of the current file.                             |
| `__dirname`  | The absolute directory path of the current file.                   |


### what is module caching in nodejs & explain with an example ?

Module caching in Node.js is one of those behind-the-scenes optimizations that makes your code faster than you might realize.

- When you require() a module in Node.js for the first time, Node does three things:

    -   Loads the file (JavaScript, JSON, or native module).
    - Executes the module code (i.e., runs it once).
    - Stores (caches) the module’s exports object in memory.

If you require() the same module again, Node does not reload or re-execute it — it simply returns the cached exports object.

file: counter.js

```js
console.log("counter.js is loaded!");

let count = 0;

module.exports = {
  increment: () => ++count,
  getCount: () => count
};

```

file: app.js

```js
const counter1 = require('./counter');
const counter2 = require('./counter');

counter1.increment();
counter1.increment();

console.log("Counter1:", counter1.getCount());
console.log("Counter2:", counter2.getCount());

```

### difference between module.exports , exports


```js
var exports = module.exports = {}; // node js internally does this so if you reassign export = it will refer to new object and we cannot use that in some other file or module of nodejs

// greetings.js

// Works fine
exports.sayHi = () => console.log("Hi");
exports.sayBye = () => console.log("Bye");

// Or alternatively:
module.exports = {
  sayHi: () => console.log("Hi"),
  sayBye: () => console.log("Bye")
};


exports = () => console.log("Hi"); // ❌ won't be exported

```

### ES Modules

At the time Node.js was created, there was no built-in module system in JavaScript

Node.js defaulted to CommonJS as its module system

As of ES2015, JavaScript does have a standardized module system as part of the language itself

That module system is called EcmaScript Modules or ES Modules or ESM for short

2. Enabling ES Modules in Node.js

Option 1 – Use .mjs file extension
Option 2 – Add this to your package.json:

```json
{
    "type": "module"
}
```

Now Node will treat all .js files in that project as ES Modules.

| Feature        | CommonJS                       | ES Modules                     |
| -------------- | ------------------------------ | ------------------------------ |
| Syntax         | `require()` / `module.exports` | `import` / `export`            |
| Loading        | Synchronous                    | Asynchronous                   |
| Scope          | Exports are mutable            | Exports are read-only bindings |
| File extension | `.js` (default)                | `.mjs` or `"type": "module"`   |
| Compatibility  | Older, used everywhere in Node | Modern, native in browsers too |


### path module

```js
// Import the built-in 'path' module
const path = require('path');

// ---------------------------------------------
// 1. path.join() → joins path segments
// ---------------------------------------------
const joinedPath = path.join('users', 'harshith', 'projects', 'node');
console.log('path.join():', joinedPath);
// ✅ OS-independent path: 'users/harshith/projects/node'

// ---------------------------------------------
// 2. path.resolve() → gives absolute path
// ---------------------------------------------
const absPath = path.resolve('src', 'index.js');
console.log('path.resolve():', absPath);
// ✅ Example: '/Users/harshith/project/src/index.js'

// ---------------------------------------------
// 3. path.basename() → gets file name
// ---------------------------------------------
const fileName = path.basename('/users/harshith/readme.txt');
console.log('path.basename():', fileName);
// ✅ 'readme.txt'

// You can also remove extension if needed
console.log('path.basename() without ext:', path.basename('/users/harshith/readme.txt', '.txt'));
// ✅ 'readme'

// ---------------------------------------------
// 4. path.dirname() → gets directory name
// ---------------------------------------------
const dirName = path.dirname('/users/harshith/readme.txt');
console.log('path.dirname():', dirName);
// ✅ '/users/harshith'

// ---------------------------------------------
// 5. path.extname() → gets file extension
// ---------------------------------------------
const ext = path.extname('index.html');
console.log('path.extname():', ext);
// ✅ '.html'

// ---------------------------------------------
// 6. path.parse() → breaks path into parts
// ---------------------------------------------
const parsed = path.parse('/users/harshith/docs/resume.pdf');
console.log('path.parse():', parsed);
/*
{
  root: '/',
  dir: '/users/harshith/docs',
  base: 'resume.pdf',
  ext: '.pdf',
  name: 'resume'
}
*/

// ---------------------------------------------
// 7. path.format() → builds path from parts
// ---------------------------------------------
const formatted = path.format({
  dir: '/users/harshith/docs',
  name: 'resume',
  ext: '.pdf'
});
console.log('path.format():', formatted);
// ✅ '/users/harshith/docs/resume.pdf'

// ---------------------------------------------
// 8. path.normalize() → cleans up messy paths
// ---------------------------------------------
const normalized = path.normalize('/users//harshith/../node/./server.js');
console.log('path.normalize():', normalized);
// ✅ '/users/node/server.js'

// ---------------------------------------------
// 9. path.isAbsolute() → checks if path is absolute
// ---------------------------------------------
console.log('path.isAbsolute("/home/harshith"):', path.isAbsolute('/home/harshith')); // true
console.log('path.isAbsolute("docs/readme.txt"):', path.isAbsolute('docs/readme.txt')); // false

// ---------------------------------------------
// 10. path.relative() → relative path between two
// ---------------------------------------------
const relativePath = path.relative('/users/harshith', '/users/harshith/projects/node');
console.log('path.relative():', relativePath);
// ✅ 'projects/node'

// ---------------------------------------------
// Bonus: Constants for platform-specific values
// ---------------------------------------------
console.log('path.sep:', path.sep);         // '\' on Windows, '/' on POSIX
console.log('path.delimiter:', path.delimiter); // ';' on Windows, ':' on POSIX

```

### events in node js

- In Node.js, events are at the heart of its asynchronous, non-blocking architecture.
- Node.js uses the EventEmitter pattern — much like how browsers handle events (like clicks or keypresses), but on the server side.

Node.js runs on the Event-Driven Architecture where:

The application emits events when something happens.

Listeners (or event handlers) are registered to handle those events.

```js
const EventEmitter = require("node:events");
const emitter = EventEmitter();

// Register an event listener
emitter.on('greet', (name) => {
  console.log(`Hello, ${name}!`);
});

// Emit (trigger) the event
emitter.emit('greet', 'Harshith');

```