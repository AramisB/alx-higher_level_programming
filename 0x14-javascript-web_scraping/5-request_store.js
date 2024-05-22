#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  process.exit(1);
}

request(url, (err, response, body) => {
  if (err) {
    return err;
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      return err;
    }
  });
});
