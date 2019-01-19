const express = require('express');
const router = express.Router();
const ArticleController = require('../controllers/articles.controller');

router.get('/', ArticleController.getArticles);

module.exports = router;
