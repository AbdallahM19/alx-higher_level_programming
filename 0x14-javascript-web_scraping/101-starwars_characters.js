#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;
  const printCharacters = (index) => {
    if (index >= characters.length) {
      return;
    }
    request.get(characters[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(index + 1);
    });
  };
  printCharacters(0);
});
