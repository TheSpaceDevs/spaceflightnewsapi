const express = require('express');
const router = express.Router();
const InfoController = require('../controllers/info.controller');

router.get('/', InfoController.getInfo);

module.exports = router;
