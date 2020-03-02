const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const mongoose = require('mongoose');
const helmet = require('helmet');
const bodyParser = require('body-parser');
const morgan = require('morgan');

const articlesRouter = require('./routes/articles.router');
const blogsRouter = require('./routes/blogs.router');
const infoRouter = require('./routes/info.router');
const reportsRouter = require('./routes/reports.router');
const usersRouter = require('./routes/users.router');

// Configure dotenv
require('dotenv').config()

// Setup the app
const app = express();

// Setting up some options
app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(morgan('combined'));

// Setting up the routes
app.use('/api/v1', express.static(path.join(__dirname, 'public')));
app.use('/api/v1/articles', articlesRouter);
app.use('/api/v1/blogs', blogsRouter);
app.use('/api/v1/reports', reportsRouter);
app.use('/api/v1/info', infoRouter);
app.use('/api/v1/users', usersRouter);

// Error handling
app.use((req, res, next) => {
  const error = new Error('Not Found')
  res.status(404);
  next(error)
});

app.use((error, req, res, next) => {
  const statusCode = res.statusCode === 200 ? 500 : res.statusCode
  res.status(statusCode);
  res.json({
    message: error.message
  })
})

// Connecting to the database
const mongoOptions = {
  useNewUrlParser: true,
  useCreateIndex: true,
  auto_reconnect: true,
  useUnifiedTopology: true,
};

try {
  mongoose.connect(process.env.MONGODB_URI, mongoOptions);
  mongoose.connection.on('connected', function() {
    console.log('MongoDB connected!');
  });
  mongoose.connection.on('error', function(error) {
    console.log('MongoDB error: ' + error);
    mongoose.disconnect();
  });
  mongoose.connection.on('disconnected', function(error) {
    console.log('MongoDB disconnected!');
    mongoose.connect(process.env.MONGODB_URI, mongoOptions);
  });
} catch (e) {
  console.log(e);
}

module.exports = app;
