const express = require('express');
const router = express.Router();
const BlogsController = require('../controllers/blogs.controller');

/**
 * Returns an object that contains metadata an array with found blogs.
 * @route GET /blogs
 * @group Blogs
 * @param {string} title.query - Title of the blog.
 * @param {string} news_site.query - Short and stripped down name of the news site that published the blog.
 * @param {string} news_site_long.query - Long name of the news site that published the blog.
 * @param {string} _id.query - The ID of an blog.
 * @param {string} url.query - The URL of an blog.
 * @param {string} sort.query - Sort on what field. Default: -date_published.
 * @param {number} date_added.query - The date an blog was added.
 * @param {number} date_published.query - The date an blog was published.
 * @param {number} page.query - The page to be fetched.
 * @param {number} limit.query - Amount of blogs per page. Default: 10
 * @returns {object} 200 - An object that contains metadata an array with found blogs.
 */
router.get('/', BlogsController.getBlogs);

module.exports = router;
