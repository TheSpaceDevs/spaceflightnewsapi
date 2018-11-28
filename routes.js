const router = require('express').Router();

// Middleware
const middleware = require('./controllers/middleware');

router.use(middleware.doSomethingInteresting);

// Articles
const articles = require('./controllers/articles');

router.get('/articles/', articles.articlesEndpoint);
router.get('/articles/search/', articles.articleSearchEndpoint);
router.get('/article/', articles.articleEndpoint);

// Blogs
const blogs = require('./controllers/blogs');

router.get('/blogs/', blogs.blogsEndpoint);
router.get('/blog/', blogs.blogEndpoint);

// Mannend flights endpoint
const mannedFlights = require('./controllers/mannedFlights');

router.get('/mannedFlights/', mannedFlights.mannedFlightsEndpoint);

// ISS
router.get('/iss/', mannedFlights.issStatus);
router.get('/iss/dailyreports', mannedFlights.issDailyReports);
router.get('/iss/dailyreport', mannedFlights.issDailyReport);

// Info
const info = require('./controllers/info');

router.get('/info/', info.infoEndpoint);

// Astronauts
const astronauts = require('./controllers/astronauts');

router.get('/astronauts/', astronauts.astronautsEndpoint);
router.get('/astronaut/', astronauts.astronautEndpoint);

// Error Handling
const errors = require('./controllers/errors');

router.use(errors.errorHandler);

// Request was not picked up by a route, send 404
router.use(errors.nullRoute);

// Export the router
module.exports = router;
