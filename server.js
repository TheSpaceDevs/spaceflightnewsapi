// API boilerplate
const express = require('express');

const app = express();

// Logging
const bodyParser = require('body-parser');

// Config
const mongoose = require('mongoose');
const routes = require('./routes');

// BodyParser allows us to get data out of URLs
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Connecting to the database
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true }).catch(err => console.log(err));
mongoose.connection.on('connected', () => {console.log('Connected!')});

// Load up the routes
app.use('/', routes);

// Start the API
app.listen(process.env.PORT);
console.log(`API running on port ${process.env.PORT}`);

// Export API server for testing
module.exports = app;
