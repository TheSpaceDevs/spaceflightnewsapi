const express = require('express');
const router = express.Router();
const UserController = require('../controllers/users.controller');

router.get('/', UserController.getUsers);
router.post('/register', UserController.addUser);
router.post('/login', UserController.loginUser);

module.exports = router;