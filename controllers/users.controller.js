const jwt = require('jsonwebtoken');
const User = require('../models/user.model');

const getUsers = async (req, res, next) => {
  if (!req.user.roles.includes('admin')) {
    return res.status(403).json({ message: 'you are not authorized to do this' });
  }

  try {
    const users = await User.find({});
    return res.status(200).json(users);
  } catch (err) {
    const error = new Error('Uh-oh, something went wrong. Please try again!');
    res.status(500);
    return next(error);
  }
};

const addUser = async (req, res) => {
  if (!req.user.roles.includes('admin')) {
    return res.status(403).json({ message: 'you are not authorized to do this' });
  }

  const user = new User(req.body);
  try {
    await user.save();
    return res.status(201).send({ message: 'user created', user: { email: user.email } });
  } catch (e) {
    if (e.errors.email.kind === 'unique') {
      return res.status(409).send({ error: 'user already exists' });
    }
    return res.status(500).send({ error: 'server error' });
  }
};

const signToken = (userId) => jwt.sign({
  iss: 'Spaceflight News API',
  sub: userId,
}, process.env.SECRET, { expiresIn: '1h' });

// User is already authenticated by Passport at this point. Now we set issue the token
const loginUser = (req, res) => {
  if (req.isAuthenticated()) {
    const { _id } = req.user;
    const token = signToken(_id);
    res.cookie('access_token', token, { httpOnly: true, sameSite: true });
    res.status(200).json({ access_token: token });
  }
};

const logOut = (req, res) => {
  res.clearCookie('access_token');
  res.status(200).json({ message: 'logged out' });
};

module.exports = {
  getUsers,
  addUser,
  loginUser,
  logOut,
};
