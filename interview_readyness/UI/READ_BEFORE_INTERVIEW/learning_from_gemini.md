## HTML Semantic Markup

- use relevant tags not just div
- use header, nav, main, article , section, footer

usage: accessibility, seo, maintainability

flexbox -> layout of elements in single dimension
group -> layout of elements in two dimension


js hoisting 
    -> functions vars are moved to top when interpreting
    -> but let and const are not and accessing before will throw reference error

```js
    console.log(a); // undefined
    var a = 10;
    console.log(b); // Reference Error
    let b = 20;
```

closures
    -> inner function has the access to outer function variables even after outer function completed executing

```js
    function outerFunction() {
        let outerVar = "hello world";
        function innerFun() {
            console.log(outerVar);
        }

        return innerFun
    }

    const myClosure = outerFunction();
    myClosure();
```

```js
    for(var i=0;i <= 3; i++) {
        setTimeout(() => {
            console.log(i);
        }, 1000)
    } // 4 4 4

    for(let i=0;i <= 3; i++) {
        setTimeout(() => {
            console.log(i);
        }, 1000)
    } // 1 2 3
```

CoreJs
    -> global : this usually refers to window
    -> method -> this refers to instance from which it is called
    -> arrow functions -> do not that their own this, it inherit from this parents scope



JavaScript's Engine & Runtimne:

The Event Loop, Call Stack, and Task Queues: A deep dive into how asynchronous code actually works. We'll explore the difference between microtasks (Promise callbacks) and macrotasks (setTimeout, I/O) and why Promise.resolve().then() runs before setTimeout(..., 0).
Prototypal Inheritance: Moving beyond ES6 class syntax. We'll explore how inheritance truly works in JavaScript using prototype, __proto__, and Object.create().
Memory Management: Discussing garbage collection (specifically the Mark-and-Sweep algorithm) and, more importantly, common causes of memory leaks in front-end applications (e.g., detached DOM nodes, forgotten timers, closures).
Advanced Asynchronous Patterns:

Advanced Promises: Going beyond .then(). We'll tackle Promise.all(), Promise.race(), Promise.allSettled(), and Promise.any(), with practical scenarios for each.
Generators & Custom Iterators: Understanding how async/await is built on top of promises and generators.
Software Architecture & Design Patterns:

CSS Architecture (BEM/ITCSS): How to write scalable and maintainable CSS for large applications. We'll discuss the principles of BEM (Block, Element, Modifier).
JavaScript Design Patterns: Discussing key patterns relevant to UI development, like the Module Pattern, Observer Pattern (the foundation of frameworks like React/Vue), and the Singleton Pattern.


```js
console.log('start');

setTimeout(function() {
  console.log('inside timeout');
}, 0);

console.log('end');
```

three componente 
    - callstack
    - web apis
    - callback queue

```js
console.log('A');

setTimeout(() => console.log('B'), 0);

Promise.resolve().then(() => console.log('C'));

console.log('D');
```

At its core, JavaScript's inheritance model is simple but powerful: objects inherit from other objects. This connection is called the prototype chain.

function.prototype: This is an object that exists on every function. Its sole purpose is to be the blueprint. When you create a new object from a function using the new keyword, the new object's prototype will be set to this prototype object.

object.__proto__: This is the actual, hidden property on every object instance that points to its prototype in the chain. It's the physical link.

```js
// This is our "class" constructor
function Dog(name) {
  this.name = name; // This is an "own" property
}

// We add a shared method to the Dog's prototype object.
// This is more memory efficient than putting it in the constructor!
Dog.prototype.bark = function() {
  console.log('Woof! My name is ' + this.name);
};

// When we use 'new', the magic happens:
const dog1 = new Dog('Rex');

// 1. A new empty object {} is created.
// 2. The new object's __proto__ is linked to Dog.prototype.
// 3. The Dog function is called with `this` set to the new object.
// 4. The new object is returned.

dog1.bark(); // JS doesn't find bark() on dog1, so it looks up the chain to Dog.prototype and finds it there.
```


```js
function SuperDog(name) {
  // 1. Call the parent constructor to set own properties like 'name'.
  Dog.call(this, name);
}

// 2. Set up the inheritance chain. SuperDog's prototype should inherit from Dog's.
SuperDog.prototype = Object.create(Dog.prototype);

// 3. (Best Practice) Reset the constructor property.
SuperDog.prototype.constructor = SuperDog;


// 4. Add SuperDog-specific methods.
SuperDog.prototype.fly = function() {
  console.log('I am flying!');
};


// --- Let's test it! ---
const superpup = new SuperDog('Clark');

superpup.bark(); // It finds .bark() on Dog.prototype! Logs: 'Woof! My name is Clark'
superpup.fly();  // It finds .fly() on SuperDog.prototype! Logs: 'I am flying!'
```

Modern browsers use a sophisticated algorithm called Mark-and-Sweep. Here's the simple version:

The Concept of "Reachability": The GC's core principle is to determine if a piece of memory is "reachable." An object is reachable if your code can still get to it, starting from a set of "roots" (like the global object, currently running functions, etc.).
Mark Phase: The GC starts at the roots and traverses every reference to every other object. Every object it can visit is "marked" as in-use.
Sweep Phase: The GC then sweeps through all the memory. Any object that was not marked is considered unreachable garbage and is deallocated.

Forgotten Event Listeners: This is the most common leak. If you add an event listener to a DOM element and then remove that element from the page, the listener might still exist in memory, holding onto references to the element and any variables in its scope.

Fix: Always explicitly call removeEventListener when a component unmounts or an element is destroyed. Modern frameworks handle this for you in their lifecycle methods (like a React useEffect cleanup function).
Forgotten Timers/Intervals: setTimeout and setInterval work similarly. If you start an interval that updates a component and the user navigates away, that interval can keep running forever, holding onto the component and its data.

Fix: Always store the timer ID and call clearTimeout or clearInterval when the component unmounts.
Closures Holding DOM References: A closure that holds a reference to a DOM element can prevent it from being collected, even if that element is removed from the page.