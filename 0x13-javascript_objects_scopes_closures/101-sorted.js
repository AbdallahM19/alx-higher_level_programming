#!/usr/bin/node

const { dict  } = require('./101-data');
const occurdict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!occurdict[occurrences]) {
    occurdict[occurrences] = [];
  }
  occurdict[occurrences].push(userId);
}
console.log(occurdict);
