const jwt = require('jsonwebtoken');
const User = require('../models/user.model');

const getToken = (req, res, next) => {
  const bearerHeader = req.headers.authorization;
  if (typeof bearerHeader !== 'undefined') {
    const bearer = bearerHeader.split(' ');
    // Destructuring gives problems right now
    // eslint-disable-next-line prefer-destructuring
    req.token = bearer[1];
    return next();
  }
  const error = new Error('no valid token found');
  res.status(401);
  return next(error);
};

const isAdmin = async (req, res, next) => {
  try {
    const decoded = jwt.verify(req.token, process.env.SECRET);
    const user = await User.findOne({ email: decoded.user.email });

    if (user && user.roles.includes('admin')) {
      return next();
    }

    const error = new Error('you are not allowed to do that');
    res.status(403);
    return next(error);
  } catch (err) {
    const error = new Error('no valid jwt found');
    res.status(401);
    return next(error);
  }
};

module.exports = {
  getToken,
  isAdmin,
};
