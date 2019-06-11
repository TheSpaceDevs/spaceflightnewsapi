const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const mongoose = require('mongoose');
const helmet = require('helmet');
const bodyParser = require('body-parser');

const articlesRouter = require('./routes/articles.router');
const blogsRouter = require('./routes/blogs.router');
const infoRouter = require('./routes/info.router');
const reportsRouter = require('./routes/reports.router');

const app = express();

app.use(helmet());
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use('/api/v1', express.static(path.join(__dirname, 'public')));
app.use('/api/v1/articles', articlesRouter);
app.use('/api/v1/blogs', blogsRouter);
app.use('/api/v1/reports', reportsRouter);
app.use('/api/v1/info', infoRouter);

try {
  mongoose.connect(process.env.MONGODB_URI, {useNewUrlParser: true, useCreateIndex: true, auto_reconnect: true});
  mongoose.connection.on('connected', function() {
    console.log('MongoDB connected!');
  });
  mongoose.connection.on('error', function(error) {
    console.log('MongoDB error: ' + error);
    mongoose.disconnect()
  });
  mongoose.connection.on('disconnected', function(error) {
    console.log('MongoDB disconnected!');
    mongoose.connect(process.env.MONGODB_URI, {useNewUrlParser: true, useCreateIndex: true, auto_reconnect: true});
  });
} catch (e) {
  console.log(e)
}

module.exports = app;
