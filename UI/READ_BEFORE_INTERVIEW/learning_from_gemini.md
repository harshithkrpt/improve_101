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

