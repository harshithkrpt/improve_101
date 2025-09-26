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