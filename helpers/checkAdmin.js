const jwt = require('jsonwebtoken');
const User = require('../models/user.model');

module.exports = async (token) => {
  try {
    const decoded = jwt.verify(token, process.env.SECRET);
    const user = await User.findOne({ email: decoded.user.email });
    if (user && user.roles.includes('admin')) {
      return true;
    }
    return false;
  } catch (e) {
    // TODO: implement Sentry
    // eslint-disable-next-line
    console.log(e);
    return false;
  }
};
