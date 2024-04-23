#!/usr/bin/node

const request = require('request');
const filmid = process.argv[2];
const urlfilem = `https://swapi-api.alx-tools.com/api/films/${filmid}`;
request.get(urlfilem, (error, respose, body) => {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
