const express = require('express');
const router = express.Router();
const BlogsController = require('../controllers/blogs.controller');

router.get('/', BlogsController.getBlogs);

module.exports = router;
