#!/usr/bin/node
/* a script that prints two arguments passed to it
    in the following format: “ is ”
*/
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log((process.argv[2] || 'undefined') + ' is ' + (process.argv[3] || 'undefined'));
}
