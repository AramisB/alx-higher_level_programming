#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1)
{
    console.log(0);
}
else
{
    const integers = args.map(Number).sort((a, b) => (b - a));
    console.log(integers[1]);
}
