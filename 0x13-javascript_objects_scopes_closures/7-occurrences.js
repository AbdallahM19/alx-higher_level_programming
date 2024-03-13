#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      num++;
    }
  }
  return num;
};
