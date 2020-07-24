/* eslint-disable max-len */
const router = require('express').Router();
const passport = require('passport');
const BlogsController = require('../controllers/blogs.controller');

router.get('/', BlogsController.getBlogs);
router.get('/:id', BlogsController.getBlog);
router.post('/', passport.authenticate('jwt', { session: false }), BlogsController.postBlog);
router.patch('/:id', passport.authenticate('jwt', { session: false }), BlogsController.patchBlog);
router.delete('/', passport.authenticate('jwt', { session: false }), BlogsController.deleteBlog);

module.exports = router;
