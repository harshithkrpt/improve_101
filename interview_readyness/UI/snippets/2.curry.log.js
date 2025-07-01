// Our trusty curry function from before
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn(...args);
    } else {
      return function(...nextArgs) {
        return curried(...args, ...nextArgs);
      };
    }
  };
}

// The generic log function we want to specialize
function log(level, date, message) {
  console.log(`[${level}] [${date.toISOString()}] ${message}`);
}


// --- YOUR TASK STARTS HERE ---

// 1. Create a `curriedLog` function by applying `curry` to our `log` function.
const curriedLog = curry(log); // Replace null with your code

// 2. Use `curriedLog` to create a specialized `logInfo` function.
//    This new function should be pre-filled with the "INFO" level.
const logInfo = curriedLog("INFO"); // Replace null with your code

// 3. Now use your new `logInfo` function to log a message.
//    You only need to provide the date and the message now!
logInfo(new Date())("User clicked the button");
logInfo(new Date())("Data fetched successfully");


// --- EXPECTED OUTPUT in the console ---
// [INFO] [2025-06-27TXX:XX:XX.XXX] User clicked the button
// [INFO] [2025-06-27TXX:XX:XX.XXX] Data fetched successfully