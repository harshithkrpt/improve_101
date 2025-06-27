function curry(fn) {
  // This is the function that will be returned and called repeatedly.
  // It uses a closure to remember the original 'fn'.
  return function curried(...args) {
    // 1. BASE CASE: If we have enough arguments...
    if (args.length >= fn.length) {
      // ...call the original function 'fn' with all the arguments.
      // We use the spread operator '...' to pass the array elements as individual arguments.
      return fn(...args);
    } else {
      // 2. RECURSIVE CASE: If we don't have enough arguments yet...
      // ...return a NEW function that waits for the next arguments.
      return function(...nextArgs) {
        // When this new function is called, it calls 'curried' again,
        // but combines the old arguments with the new ones.
        return curried(...args, ...nextArgs);
      }
    }
  };
}

// How we use it:
const sum = (a, b, c) => a + b + c;

const curriedSum = curry(sum);

console.log(curriedSum(1)(2)(3)); // Output: 6
console.log(curriedSum(1, 2)(3)); // Output: 6
console.log(curriedSum(1)(2, 3)); // Output: 6