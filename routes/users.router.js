const express = require('express');
const router = express.Router();
const UsersController = require('../controllers/users.controller');
const jwtVerify = require('../helpers/jwtVerify');

router.post('/register', jwtVerify, UsersController.register);
router.post('/login', UsersController.login);

module.exports = router;
