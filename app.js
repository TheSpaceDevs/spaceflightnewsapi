const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const mongoose = require('mongoose');
const helmet = require('helmet');
const bodyParser = require('body-parser');
const pino = require('pino');
const expressPino = require('express-pino-logger');

const articlesRouter = require('./routes/articles.router');
const blogsRouter = require('./routes/blogs.router');
const infoRouter = require('./routes/info.router');
const reportsRouter = require('./routes/reports.router');
const usersRouter = require('./routes/users.router');

const logger = pino({ level: process.env.LOG_LEVEL || 'info' });
const expressLogger = expressPino({ logger });

const app = express();

app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(expressLogger);

app.use('/api/v1', express.static(path.join(__dirname, 'public')));
app.use('/api/v1/articles', articlesRouter);
app.use('/api/v1/blogs', blogsRouter);
app.use('/api/v1/reports', reportsRouter);
app.use('/api/v1/info', infoRouter);
app.use('/api/v1/users', usersRouter  );

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
