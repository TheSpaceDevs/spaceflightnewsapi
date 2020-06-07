const express = require('express');

const router = express.Router();
const { isAdmin, getToken } = require('../helpers/authHelpers');
const UserController = require('../controllers/users.controller');

router.get('/', getToken, isAdmin, UserController.getUsers);
router.post('/register', getToken, isAdmin, UserController.addUser);
router.post('/login', UserController.loginUser);

module.exports = router;
