

const router = require('express').Router();

// Middleware
const middleware = require('./controllers/middleware');

router.use(middleware.doSomethingInteresting);

// Tasks
const tasks = require('./controllers/tasks');

router.get('/tasks', tasks.findAll);
router.post('/buggyroute', tasks.buggyRoute);

// Error Handling
const errors = require('./controllers/errors');

router.use(errors.errorHandler);

// Request was not picked up by a route, send 404
router.use(errors.nullRoute);

// Export the router
module.exports = router;
