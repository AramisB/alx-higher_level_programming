#!/usr/bin/node
// a script that prints the addition of 2 integers
function add (a, b) {
  return (a + b);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (isNaN(a) || isNaN(b) || process.argv.length - 2 <= 1) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
