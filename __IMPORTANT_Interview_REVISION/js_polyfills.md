
- Polyfills 

- polyfill for call

```js
Function.prototype.myCall = function (thisRef, ...args) {

    if(typeof this !== 'function') {
        throw new TypeError("myCall myst be called on a function");
    }

    const context = thisRef == null ? globalThis : Object(thisRef);

    const key = Symbol("fn");
    context[key] = this;
    try {
        return context[key](...args);
    }
    finally {
        delete context[key];
    }

}
function name(a,b,c) {
    console.log(this.name, a,b,c);
}
name.myCall({name: "harshith"}, 1,2,3)
```

- polyfill for apply

```js
Function.prototype.myApply = function(thisRef, args) {
    if (typeof this !== 'function') {
        throw new TypeError('myApply must be called on a function');
    }

    const context = thisRef == null ? globalThis : Object(thisRef);
    const key = Symbol('fn');
    context[key] = this;
    try {
        return context[key](...args);
    }
    finally {
        delete context[key];
    }
 }

 function name(a,b,c) {
    console.log(this.name, a,b,c);
 
 }
name.myApply({name: "harshith"}, [1,2,3])
```

- polyfill for bind

```js

```

- polyfill for myBind

```js
Function.prototype.myBind = function(thisRef, ...primaryArray) {
    if(typeof this != 'function') {
        throw new TypeError("myBind needs to be a function");
    }
    
    let newThis = this;
    return function (...newArgs) {
        
            thisRef = thisRef == null ? globalThis : Object(thisRef);
            return newThis.apply(thisRef, [...primaryArray, ...newArgs]);
       
    }
}
function one(a,b,c) {
    console.log(this.name, a,b,c);
}
let a  = one.myBind({name: "harshith"}, 1)
a(2,3)
```


- polyfill for Map

```js
Array.prototype.myMap = function (fn) {
    if(typeof fn !== 'function') {
        throw new TypeError("1st argument should be a function in the map");
    }
    if(!Array.isArray(this)) {
        throw new TypeError("map can be run only on arrays");
    }
    
    const length = this.length;
    const result = [];
    for(let i=0;i<length;i++) {
        result.push(fn(this[i], i, this));
    }
    return result;
}
```

- polyfill for filter

```js
Array.prototype.myFilter = function (fn) {
    if(typeof fn !== 'function') {
        throw new TypeError("1st argument should be a function in the map");
    }
    if(!Array.isArray(this)) {
        throw new TypeError("map can be run only on arrays");
    }
    
    const length = this.length;
    const result = [];
    for(let i=0;i<length;i++) {
        if(fn(this[i], i, this)) {
            result.push(this[i]);
        }
    }
return result;
}
```


- polyfill for reduce 

```js
Array.prototype.myReduce = function (fn, initalValue = 0) {
    if(typeof fn !== 'function') {
        throw new TypeError("1st argument should be a function in the map");
    }
    if(!Array.isArray(this)) {
        throw new TypeError("map can be run only on arrays");
    }
    
    const length = this.length;
    let acc = initalValue;
    for(let i=0;i<length;i++) {
        acc = fn(acc, this[i], i, this)
        
    }
    return acc;
}
```


- polyfill for throttle

```js
const throttle = (fn, limit = 300) => {
    let lastCall = 0; 
    return (...args) => {
        const now = Date.now();
        if(now - lastCall >= limit) {
            fn(...args);
            lastCall = Date.now();
        }
    }
}

```

- polyfill for debounce

```js
const debounce = (fn, delay = 300) => {
    let timerId;
    return (...args) => {
        clearTimeout(timerId);
        timerId = setTimeout(() => {
            fn(...args);
        }, delay);
    }
}
```

- polyfill for memoise 

```js
const memoise = function (fn) {
    if (typeof fn !== 'function') {
        throw new TypeError("memoise 1st argument should be a function");
    }

    const cache = new Map();

    return function (...args) {
        const key = JSON.stringify(args);
        if(cache.has(key)) {
            return cache.get(key);
        }

        const result = fn.apply(this, args);
        cache.set(key, result);
        return result;
    }
   
}
```