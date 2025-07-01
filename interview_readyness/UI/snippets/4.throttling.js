// The "expensive" function we want to protect
function onMouseMove(event) {
  const box = document.getElementById('box');
  box.textContent = `X: ${event.clientX}, Y: ${event.clientY}`;
  console.log('Updating coordinates...');
}

// --- YOUR TASK: Implement this throttle function ---

function throttle(fn, delay) {
  let lastExecutionTime = 0;

  // The throttle function should return a NEW function.
  return function(...args) {
    const currentTime = new Date().getTime();

    if(lastExecutionTime - currentTime > delay) {
        lastExecutionTime = currentTime;
        fn(...args);
    }
  }
}

// --- End of your task ---


// Let's create a throttled version of our mouse move function
const throttledMouseMove = throttle(onMouseMove, 100); // 100ms delay

// Attach it to the mousemove event
const box = document.getElementById('box');
box.addEventListener('mousemove', throttledMouseMove);

function throttlev2(fn, delay) {
  // 1. A flag to know if we're "on cooldown". Initially false.
  let isThrottled = false;

  // We'll also need a way to store the arguments of the last call
  let savedArgs;
  let savedThis;

  return function wrapper(...args) {
    // 4. Save the 'this' context and arguments of the latest call
    savedThis = this;
    savedArgs = args;

    // 2. If we are on cooldown, do nothing. Just exit.
    if (isThrottled) {
      return;
    }

    // 3. If NOT on cooldown, run the function immediately!
    fn.apply(savedThis, savedArgs);

    // 5. Start the cooldown period.
    isThrottled = true;

    // 6. After the delay, the cooldown is over.
    setTimeout(() => {
      isThrottled = false;
    }, delay);
  };
}