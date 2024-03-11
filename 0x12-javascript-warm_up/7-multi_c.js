#!/usr/bin/node

const argc = parseInt(process.argv[2]);
const argctwo = 'C is fun';
if (!isNaN(argc)) {
  for (let index = 0; index < argc; index++) {
    console.log(argctwo);
  }
} else {
  console.log('Missing number of occurrences');
}
