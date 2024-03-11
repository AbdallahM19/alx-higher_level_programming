#!/usr/bin/node

const argc = parseInt(process.argv[2]);
if (!isNaN(argc)) {
  console.log('My number: ' + argc);
} else {
  console.log('Not a number');
}
