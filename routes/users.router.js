const express = require('express');

const router = express.Router();
const jwtVerify = require('../helpers/jwtVerify');
const UserController = require('../controllers/users.controller');

router.get('/', jwtVerify, UserController.getUsers);
router.post('/register', jwtVerify, UserController.addUser);
router.post('/login', UserController.loginUser);

module.exports = router;
