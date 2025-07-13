const fs = require("fs");

const data = fs.readFileSync('./meta/sample_file.txt', 'utf8');
console.log(data);
console.log("After Reading File");


// Below CODE IS NON BLOCKING
fs.readFile('./meta/sample_file.txt', 'utf8', (err, data) => {
    console.log(data);
});

console.log("this will be printed first");