const User = require('../models/user.model');
const jwt = require('jsonwebtoken');
const checkAdmin = require('../helpers/checkAdmin');
const bcrypt = require('bcrypt');

const getUsers = async (req, res) => {
  const admin = await checkAdmin(req.token);
  if (admin) {
    const users = await User.find({});
    return res.status(200).json(users)
  } else {
    return res.status(403).send({error: 'you are not allowed to do that'})
  }
};

const addUser = async (req, res) => {
  const admin = await checkAdmin(req.token);
  if (admin) {
    const user = new User(req.body);
    try {
      await user.save();
      return res.status(201).send({message: 'user created', user: {email: user.email}})
    } catch (ValidationError) {
      if (ValidationError.errors.email.kind === 'unique') {
        return res.status(409).send({error: 'user already exists'})
      }
    }
  } else {
    return res.status(403).send({error: 'you are not allowed to do that'})
  }
};

const loginUser = async (req, res) => {
  // Check if the body has the email field
  if (!req.body.email || !req.body.password) {
    return res.status(400).send({error: 'no email or password field in body'})
  }

  // Trying to login it has the email and password field
  try {
    const user = await User.findOne({email: req.body.email}).select('+password');
    if (user) {
      // Check the password
      const match = await bcrypt.compare(req.body.password, user.password);
      if (match) {
        const token = jwt.sign({user}, process.env.SECRET, {expiresIn: '1h'});
        return res.status(200).send({message: 'logged in', token: token});
      } else {
        return res.status(401).send({error: 'bad credentials'});
      }
    }
    return res.status(404).send({error: 'user not found'})
  } catch (e) {
    res.status(500).send({error: 'server error'});
    console.log(e)
  }
};

module.exports = {
  getUsers,
  addUser,
  loginUser
};