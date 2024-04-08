#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed
const argCount = process.argv.length - 2;

if (argCount === 0)
{
    console.log("No argument");
}
else if (argCount == 1)
{
    console.log("Argument found");
}
else
{
    console.log("Arguments found");
}
