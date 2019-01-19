const express = require('express');
const router = express.Router();
const ArticleController = require('../controllers/articles.controller');

/**
 * Returns an object that contains an array with articles.
 * @route GET /articles
 * @group Articles
 * @param {string} title.query - Title of the article.
 * @param {string} news_site.query - Short and stripped down name of the news site the published the article.
 * @param {string} news_site_long.query - Long name of the news site the published the article.
 * @param {string} _id.query - The ID of an article.
 * @param {string} url.query - The URL of an article.
 * @param {number} date_added.query - The date an article was added.
 * @param {number} date_published.query - The date an article was published.
 * @param {number} page.query - The page to be fetched.
 * @param {number} limit.query - Amount of articles per page.
 * @returns {object} 200 - An object that contains an array with articles.
 */
router.get('/', ArticleController.getArticles);

module.exports = router;
