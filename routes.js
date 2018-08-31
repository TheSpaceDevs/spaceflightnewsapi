const router = require('express').Router();

// Middleware
const middleware = require('./controllers/middleware');

router.use(middleware.doSomethingInteresting);

// Articles
const articles = require('./controllers/articles');

router.get('/articles/newssite/:newssite', articles.findByNewsSite);
router.get('/articles/category/:category', articles.findByCategory);
router.get('/articles/tag/:tag', articles.findByTag);
router.get('/articles/:limit*?', articles.allArticles);

// Article
router.get('/article/:id', articles.findByID);

// Error Handling
const errors = require('./controllers/errors');

router.use(errors.errorHandler);

// Request was not picked up by a route, send 404
router.use(errors.nullRoute);

// Export the router
module.exports = router;
