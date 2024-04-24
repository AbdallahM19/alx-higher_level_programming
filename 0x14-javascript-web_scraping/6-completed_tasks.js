#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const i = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!i[todo.userId]) {
        i[todo.userId] = 1;
      } else {
        i[todo.userId] += 1;
      }
    }
  });
  console.log(i);
});
