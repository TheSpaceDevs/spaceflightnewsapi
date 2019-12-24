const express = require('express');
const router = express.Router();
const UserController = require('../controllers/users.controller');

router.get('/', UserController.getUsers);
router.post('/', UserController.addUser);

module.exports = router;