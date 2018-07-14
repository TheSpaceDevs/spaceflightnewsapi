'use strict';

exports.doSomethingInteresting = (req, res, next) => {
    // Middleware goes here
    next();
};
