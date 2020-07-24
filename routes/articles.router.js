/* eslint-disable max-len */
const router = require('express').Router();
const passport = require('passport');
const ArticleController = require('../controllers/articles.controller');


router.get('/', ArticleController.getArticles);
router.get('/:id', ArticleController.getArticle);
router.post('/', passport.authenticate('jwt', { session: false }), ArticleController.postArticle);
router.patch('/:id', passport.authenticate('jwt', { session: false }), ArticleController.patchArticle);
router.delete('/:id', passport.authenticate('jwt', { session: false }), ArticleController.deleteArticle);

module.exports = router;
