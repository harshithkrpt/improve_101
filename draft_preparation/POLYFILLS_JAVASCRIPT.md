# Polyfills in Javascript

- Polyfills in javascript are useful when the implementation for that browser is not present

## Map polifill in javascript

```js
    Array.prototype.pMap = function(cb) {
        if(typeof cb !== "function") {
            throw new Error("Please Pass Function as Argument");
        }

        let data = [];
        for(let i=0;i<this.length;i++) {
            data.push(cb(this[i], i, this))
        }

        return data
    }

    let arr = [1,3,3];
    console.log(arr.pMap((item) => {
        return item * 2;
    }))
```

## Filter Polyfill in javascript

```js
    Array.prototype.pFilter = function(cb) {
        if(typeof cb !== "function") {
            throw new Error("Please Pass Function as Argument");
        }

        let data = [];

        for(let i=0;i<this.length;i++) {
            if(cb(this[i], i, this)) {
                data.push(this[i]);
            }
        }

        return data;
    }

     let arr = [1,3,3];
    console.log(arr.pFilter((item) => {
        return item === 1;
    }))
```


## Reduce Polyfills in javascript

```js
    Array.prototype.pReduce = function(cbFunc, initialValue) {
        if(typeof cbFunc !== "function") {
            throw new Error("Please Pass Function as Argument");
        }

        let acc = initialValue;

        for(let i=0;i<this.length;i++) {
            acc = acc ? cbFunc(acc, this[i], i, this) : this[i]; 
        }

        return acc;
    }

    let arr = [1,2,3];
    arr.pReduce((acc, item) => {
        return item + acc
    }, 0);
```

## Polyfills for Call , Apply & Bind 

### Call 

```js
    Function.prototype.pCall = function(context = {}, ...args) {
        if(typeof this !== "function") {
            throw new Error(this + "it is not callable");
        }

        context.fn = this;
        return context.fn(...args);
    }


```

### Apply

```js
    Function.prototype.pApply = function(context = {}, args = []) {
        if(typeof this !== "function") {
            throw new Error("the variable is non callble");
        }
        if(!Array.isArray(args)) {
            throw new Error("The Second Argument should be array");
        }

        const fnSymbol = Symbol();
        context[fnSymbol] = this;

        const result = context[fnSymbol](...args);
        delete context[fnSymbol];
        return result;
     }
```


### Bind

```js
    const object = {
        name: "Harshith",
        age: 25
    };

    const fn = function(honestOpinion) {
        return this.name + " " + this.age +  " " + honestOptnion;
    }

    fn.bind(object, "This is my read name & age");

    Function.prototype.pBind = function(context = {}, ...args) {
        if(typeof this != "function") {
            throw new Error("binding method is not callable");
        }

        context.fn = this;

        return function(...remArgs) {
            return context.fn(...args, ...remArgs)
        }

    }

    fn.pBind(object, "This is my read name & age");
```


### Once

```js
    Function.prototype.pOnce = function() {
        if(typeof this !== "function") {
            throw new Error("pOnce must be called with function");
        }

        let called = false;
        let result;

        return (...args) => {
            if(!called) {
                result = this.apply(this, args);
                called = true;
            }

            return result;
        }
    }
```

### Memoise

```js
    Function.prototype.pMemory = function() {
        if(typeof this !== "function") {
            throw new Error("pMemoize must be called with function");
        }

        const cache = new Map();
        const fn = this;

        return function(...args) {
            const key = JSON.stringify(args);
            if(cache.has(key)) {
                return cache.get(key);
            }

            const curResult = fn.apply(this, args);
            cache.set(key, curResult);
            
            return curResult;
        }
    }
```


### Debounce

```js
    const debounce = (cb, delay) => {
        let timer;

        return function(...args) {
            const fn = this;

            if(timer) {
                clearTimeout(timer);
            }

            timer = setTimeout(() => {
               cb.apply(fn, ...args);

            }, delay);
        }
    }
```


### Throttle

```js

const throttle = (cb, delay) => {
    let prevCalled = 0;

    return function(...args) {
        const context = this;
        const now = Date.now();

        if (now - prevCalled >= delay) {
            cb.apply(context, args);
            prevCalled = now;
        }
    };
};

```


## Promise Polyfills

### Promise 


### Promise.all 