const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const mongoose = require('mongoose');
const helmet = require('helmet');
const bodyParser = require('body-parser');
const AdminBro = require('admin-bro');
const AdminBroExpress = require('admin-bro-expressjs');

const usersRouter = require('./routes/users.router');
const articlesRouter = require('./routes/articles.router');
const blogsRouter = require('./routes/blogs.router');
const infoRouter = require('./routes/info.router');

const Articles = require('./models/article.model');
const Blogs = require('./models/blog.model');
const Users = require('./models/user.model');

const app = express();

const ADMIN = {
  email: 'test@example.com',
  password: 'password',
};

AdminBro.registerAdapter(require('admin-bro-mongoose'));
const adminBro = new AdminBro({
  resources: [Articles, Blogs, Users],
  rootPath: '/admin',
});
const router = AdminBroExpress.buildAuthenticatedRouter(adminBro, {
  authenticate: async (email, password) => {
    if (ADMIN.password === password && ADMIN.email === email) {
      return ADMIN
    }
    return null
  },
  cookieName: 'adminbro',
  cookiePassword: 'somepassword',
});
app.use(adminBro.options.rootPath, router);

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
app.use('/api/v1/info', infoRouter);
app.use('/auth', usersRouter);

try {
  mongoose.connect(process.env.MONGODB_URI, {useNewUrlParser: true, useCreateIndex: true})
  console.info('[x] Connected to database')
} catch (e) {
  console.log(e)
}

module.exports = app;
