#!/usr/bin/node

const request = require('request');
const filmurl = process.argv[2];
const idcharacter = '18';
let count = 0;
request.get(filmurl, (error, response, body) => { // fixed typo here
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    film.results.forEach((filmname) => {
      filmname.characters.forEach((character) => { // fixed typo here
        if (character.includes(idcharacter)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
