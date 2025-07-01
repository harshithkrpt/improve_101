// The function we want to protect from being called too often
function makeApiCall(query) {
  console.log(`Making API call for query: "${query}"`);
}

// --- YOUR TASK: Implement this debounce function ---

function debounce(fn, delay) {
  // You'll need a variable to hold the timer ID here.
  let timerId;

  // The debounce function should return a NEW function.
  return function(...args) {
    if(timerId) {
        clearTimeout(timerId);
    }
    timerId = setTimeout(() => {
        fn.apply(this, args);
    }, delay);
  }
}

// --- End of your task ---


// Let's create a debounced version of our API call function
const debouncedApiCall = debounce(makeApiCall, 500); // 500ms delay

// Attach it to the input event
const searchInput = document.getElementById('searchInput');
searchInput.addEventListener('input', (event) => {
  // We call our new debounced function here
  debouncedApiCall(event.target.value);
});