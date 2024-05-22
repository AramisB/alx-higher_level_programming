#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  process.exit(1);
}
request(url, (err, response) => {
  if (err) {
    return (err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
