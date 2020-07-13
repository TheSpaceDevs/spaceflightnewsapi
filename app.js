const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const mongoose = require('mongoose');
const helmet = require('helmet');
const morgan = require('morgan');

const articlesRouter = require('./routes/articles.router');
const blogsRouter = require('./routes/blogs.router');
const infoRouter = require('./routes/info.router');
const reportsRouter = require('./routes/reports.router');
const usersRouter = require('./routes/users.router');

// Setup the app
const app = express();

// Setting up some options
app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(morgan('combined'));

// Setting up the routes
app.use('/v2', express.static(path.join(__dirname, 'public')));
app.use('/v2/articles', articlesRouter);
app.use('/v2/blogs', blogsRouter);
app.use('/v2/reports', reportsRouter);
app.use('/v2/info', infoRouter);
app.use('/v2/users', usersRouter);

// Handling the not found cases
app.use((req, res, next) => {
  const error = new Error('Not Found');
  res.status(404);
  next(error);
});

// We need the next() for a correct function signature
// eslint-disable-next-line no-unused-vars
app.use((error, req, res, next) => {
  const statusCode = res.statusCode === 200 ? 500 : res.statusCode;
  res.status(statusCode);
  res.json({
    message: error.message,
  });
});

// Connecting to the database
const mongoOptions = {
  useNewUrlParser: true,
  useCreateIndex: true,
  auto_reconnect: true,
  useUnifiedTopology: true,
  useFindAndModify: false,
};

try {
  mongoose.connect(process.env.MONGODB_URI, mongoOptions);
  mongoose.connection.on('connected', () => {
    // We'd like to know this
    // eslint-disable-next-line no-console
    console.log('MongoDB connected!');
  });
  mongoose.connection.on('error', (error) => {
    // We'd like to know this.
    // eslint-disable-next-line no-console
    console.log(`MongoDB error: ${error}`);
    mongoose.disconnect();
  });
  mongoose.connection.on('disconnected', (error) => {
    // We'd like to know this
    // eslint-disable-next-line no-console
    console.log(`MongoDB disconnected! :${error}`);
    mongoose.connect(process.env.MONGODB_URI, mongoOptions);
  });
} catch (e) {
  // We'd like to know this
  // eslint-disable-next-line no-console
  console.log(e);
}

module.exports = app;
