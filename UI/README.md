<!-- TODO:
    IMPROVE ON MATH OPERATIONS WITH TYPE CONVERSIONS
    LEARN MORE ABOUT ADVANED BITWISE OPERATORS -> 32 bit number conversions
    
 -->

- use strict is used on top of the file for making it as modern code being written in that file
- var is old school of code, let & const are modern where const cannot be reassigned
- using of ; is optional but we need to add for issues like below 

```
// this code throws error
alert("hello")
[1,2].forEach(alert);
```

- data types
    - number 
        - integer, floating point number, Infinity, NaN 
    - bigint
        const bigInt = 1234567890123456789012345678901234567890n;
        - n at the end is big int
    - string
        let name = "abcd";
        let name2 = 'abcd';
        let name3 = `
            hello world,
            this is the representation
            ${name}
        `;
    - boolean
        let boolean = true;
        let falsy = false;
    - special null value
    - undefined value
    - objects
        let obj = {};
        let obj2 = {name: 1, value: 2};
    - symbol
        - creates a unique id
        const id = Symbol('id');
- type of operator 
    typeof undefined // "undefined"

    typeof 0 // "number"

    typeof 10n // "bigint"

    typeof true // "boolean"

    typeof "foo" // "string"

    typeof Symbol("id") // "symbol"

    typeof Math // "object"  (1)

    typeof null // "object"  (2)

    typeof alert // "function"  (3)


- alert , prompt , confirm
    - alert("hello");
    - const value = prompt("enter name", "default name");
    - const boolean = confirm("are you single ?");

- type conversions
    const convertString = String(100);
    const convertNumber = Number("122");
    alert( Number("   123   ") ); // 123
    alert( Number("123z") );      // NaN (error reading a number at "z")
    alert( Number(true) );        // 1
    alert( Number(false) );       // 0
    const booleanConversion = Boolean(1); // true
    const booleanCon = Boolean(0); // false
    const bool3 = Boolean("hello"); // true
    const bool4 = Boolean(""); // false

- basic operations, maths
    - unary, binary & operand
    const uniry = -10; // - is unary operator
    const binary = 10 + 2; // + now becomes binary operator & 10, 2 are operands
    +, -, *, % , /, **, 
    - unary + converts the non number values to 0 / 1 based on truth statement
    ++ , -- increment and decrement operators
    const a = 2;
    const b = a++; // a: 3, b: 2 
    const aa = 2;
    const bb = ++aa; // aa: 3, bb: 3

- bitwise operators
    - & , | , ^ , ~, <<, >>, >>>
    The list of operators:

    AND ( & )
    OR ( | )
    XOR ( ^ )
    NOT ( ~ )
    LEFT SHIFT ( << )
    RIGHT SHIFT ( >> )
    ZERO-FILL RIGHT SHIFT ( >>> )
