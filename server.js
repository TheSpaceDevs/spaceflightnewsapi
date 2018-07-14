

// API boilerplate
const express = require('express');

const app = express();

// Logging
const bodyParser = require('body-parser');
const morgan = require('morgan');
const fs = require('fs');
const FileStreamRotator = require('file-stream-rotator');

const logDirectory = `${__dirname}/log`;

// Config
const config = require('config');
const routes = require('./routes');

// BodyParser allows us to get data out of URLs
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Log all requests in a daily log file using morgan
if (fs.existsSync(logDirectory) === false) {
  fs.mkdirSync(logDirectory);
}
const accessLogStream = FileStreamRotator.getStream({
  filename: `${logDirectory}/access-%DATE%.log`,
  frequency: 'daily',
  date_format: 'YYYYMMDD',
  verbose: false,
});
app.use(morgan('combined', { stream: accessLogStream }));

// Load up the routes
app.use('/', routes);

// Start the API
app.listen(config.apiPort);
console.log(`API running on port ${config.apiPort}`);

// Export API server for testing
module.exports = app;
