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
  const todos = JSON.parse(body);

  const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId] = 0;
      }
      completedTasksByUser[todo.userId]++;
    }
  });

  console.log(completedTasksByUser);
});
