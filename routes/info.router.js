const express = require('express');
const router = express.Router();
const InfoController = require('../controllers/info.controller');

/**
 * @api {get} /v1/info Get general info
 * @apiName GetInfo
 * @apiGroup Info
 * @apiVersion 1.0.0
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *  "total_number_of_articles": 721,
 *  "api_version": "1.0.0"
 * }
 */
router.get('/', InfoController.getInfo);

module.exports = router;
