#!/usr/bin/node

exports.esrever = function (list) {
  const listcon = [];
  for (let index = list.length - 1; index >= 0; index--) {
    listcon.push(list[index]);
  }
  return listcon;
};
