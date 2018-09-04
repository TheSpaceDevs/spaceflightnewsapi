// API boilerplate
const express = require('express');

const app = express();

// Logging
const bodyParser = require('body-parser');
let morgan = require('morgan');
let fs = require('fs');
let FileStreamRotator = require('file-stream-rotator');
let logDirectory = __dirname + '/log';

// Config
const mongoose = require('mongoose');
const routes = require('./routes');

// BodyParser allows us to get data out of URLs
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Log all requests in a daily log file using morgan
if (fs.existsSync(logDirectory) === false) {
  fs.mkdirSync(logDirectory);
}
let accessLogStream = FileStreamRotator.getStream({
  filename: logDirectory + '/access-%DATE%.log',
  frequency: 'daily',
  date_format: 'YYYYMMDD',
  verbose: false,
});
app.use(morgan('combined', { stream: accessLogStream }));

// Connecting to the database
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true }).catch(err => console.log(err));

// Load up the routes
app.use('/', routes);

// Start the API
app.listen(process.env.PORT);
console.log(`API running on port ${process.env.PORT}`);

// Export API server for testing
module.exports = app;
