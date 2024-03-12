#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const argcone = parseInt(process.argv[2]);
const argctwo = parseInt(process.argv[3]);

if (!isNaN(argcone) && !isNaN(argctwo)) {
  console.log(add(argcone, argctwo));
} else {
  console.log('NaN');
}
