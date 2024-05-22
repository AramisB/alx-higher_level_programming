#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  const movie = JSON.parse(body);

  movie.characters.forEach(characterUrl => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
