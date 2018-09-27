const router = require('express').Router();

// Middleware
const middleware = require('./controllers/middleware');

router.use(middleware.doSomethingInteresting);

// Articles
const articles = require('./controllers/articles');

router.get('/articles/', articles.articlesEndpoint);

// info

const info = require('./controllers/info');

router.get('/info', info.infoEndpoint);

// Article
router.get('/article/', articles.articleEndpoint);

// Error Handling
const errors = require('./controllers/errors');

router.use(errors.errorHandler);

// Request was not picked up by a route, send 404
router.use(errors.nullRoute);

// Export the router
module.exports = router;
