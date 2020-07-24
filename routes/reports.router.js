/* eslint-disable max-len */
const router = require('express').Router();
const ReportController = require('../controllers/reports.controller');

router.get('/', ReportController.getReports);
router.get('/:id', ReportController.getReport);

module.exports = router;
