const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const mongoose = require('mongoose');
const helmet = require('helmet');
const bodyParser = require('body-parser');

const indexRouter = require('./routes/index');
const usersRouter = require('./routes/users');
const articlesRouter = require('./routes/articles.router');
const blogsRouter = require('./routes/blogs.router');
const infoRouter = require('./routes/info.router');

const swaggerOptions = require('./config/swaggerOptions');

const app = express();
app.use(helmet());
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use('/api/v1', indexRouter);
app.use('/api/v1/users', usersRouter);
app.use('/api/v1/articles', articlesRouter);
app.use('/api/v1/blogs', blogsRouter);
app.use('/api/v1/info', infoRouter);

const expressSwagger = require('express-swagger-generator')(app);
expressSwagger(swaggerOptions);

try {
  mongoose.connect(process.env.MONGODB_URI, {useNewUrlParser: true})
} catch (e) {
  console.log(e)
}

module.exports = app;
