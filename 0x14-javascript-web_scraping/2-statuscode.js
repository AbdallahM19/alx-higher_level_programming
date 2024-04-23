#!/usr/bin/node

const request = require('request');
const urltext = process.argv[2];
request.get(urltext, (error, res) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
