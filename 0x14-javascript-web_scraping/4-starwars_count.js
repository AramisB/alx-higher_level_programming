#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  process.exit(1);
}

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  const film = JSON.parse(body).results;

  let wedgeAntillesCount = 0;

  film.forEach(film => {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      wedgeAntillesCount++;
    }
  });
  console.log(wedgeAntillesCount);
});
