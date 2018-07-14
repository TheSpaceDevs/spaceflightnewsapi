'use strict';

let errors = require('./errors.js');

exports.findAll = (req, res, next) => {
  // Simulate task list, normally this would be retrieved from a database
  let tasks = [
    {'_id': 1, 'name': 'milk'},
    {'_id': 2, 'name': 'cheese'},
    {'_id': 3, 'name': 'milk'}
  ];

  res.json(tasks);
};

exports.buggyRoute = (req, res, next) => {
  // Simulate a custom error
  next(errors.newHttpError(400, 'bad request'));
};
