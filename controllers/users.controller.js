const User = require('../models/user.model');

const getUsers = async (req, res, next) => {
  res.send('Hello World!')
};

const addUser = async (req, res, next) => {
  const user = new User(req.body);
  try {
    await user.save();
    return res.status(201).send({message: 'user created', user: {email: user.email}})
  } catch (ValidationError) {
    if (ValidationError.errors.email.kind === 'unique') {
      return res.status(409).send({error: 'user already exists'})
    }
  }
};

module.exports = {
  getUsers,
  addUser
};