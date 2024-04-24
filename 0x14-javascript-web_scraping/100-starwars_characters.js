#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const movie = JSON.parse(body);
    movie.characters.forEach(chars => {
      request.get(chars, (error, response, body) => {
        if (error) {
          console.log(error);
          return;
        }
        const i = JSON.parse(body);
        console.log(i.name);
      });
    });
});
