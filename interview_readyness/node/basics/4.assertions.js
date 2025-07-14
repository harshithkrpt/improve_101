const assert = require('node:assert/strict');

const actual = [[[1, 2, 3]], 4, 5];
const expected = [[[1, 2, '3']], 4, 5];
// Normal Assertion
require("node:assert").deepEqual(actual, expected);

try {
  assert.deepEqual(actual, expected);  
}
catch(err) {
    console.error(err);
}

