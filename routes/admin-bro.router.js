const AdminBro = require('admin-bro');
const AdminBroExpress = require('admin-bro-expressjs');
const bcrypt = require('bcryptjs');

const Article = require('../models/article.model');
const Blog = require('../models/blog.model');
const User = require('../models/user.model');

AdminBro.registerAdapter(require('admin-bro-mongoose'));
const adminBro = new AdminBro({
  resources: [Article, Blog, User]
});

module.exports = AdminBroExpress.buildAuthenticatedRouter(adminBro, {
  authenticate: async (email, password) => {
    const user = await User.findOne({email});
    if (user) {
      const passwordValidated = await bcrypt.compare(password, user.password);
      if (!passwordValidated) {
        return null
      }
      if (!user.roles.includes('admin')) {
        return null
      }
      return user
    }
    return null
  },
  cookieName: 'adminbro',
  cookiePassword: process.env.COOKIE_SECRET,
});
