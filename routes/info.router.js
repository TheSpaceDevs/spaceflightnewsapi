const express = require('express');
const router = express.Router();
const InfoController = require('../controllers/info.controller');

/**
 * Returns an object that contains general info.
 * @route GET /info
 * @group Info
 * @returns {object} 200 - An object that contains general info.
 */
router.get('/', InfoController.getInfo);

module.exports = router;
