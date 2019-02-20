const express = require('express');
const router = express.Router();
const UsersController = require('../controllers/users.controller');
const jwtVerify = require('../helpers/jwtVerify');

/**
 * @api {post} /auth/register Register
 * @apiName Register
 * @apiGroup Auth
 * @apiVersion 1.0.0
 * @apiHeader {String} Authorization A bearer token
 * @apiPermission admin
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 201 Created
 * {
 *   "title": "User Registration Successful",
 *   "detail": "Successfully registered new user"
 * }
 *
 * @apiErrorExample Forbidden-Response:
 *     HTTP/1.1 403 Forbidden
 *     Forbidden
 *
 * @apiErrorExample Bad-Request-Response:
 * HTTP/1.1 400 Bad Request
 * {
 *   "errors": [
 *     {
 *       "title": "Registration Error",
 *       "detail": "Something went wrong during registration process.",
 *       "errorMessage": "Users validation failed: email: Error, expected `email` to be unique. Value: `derk@derkweijers.me2`"
 *      }
 *    ]
 * }
 */
router.post('/register', jwtVerify, UsersController.register);

/**
 * @api {post} /auth/login Login
 * @apiName Login
 * @apiGroup Auth
 * @apiVersion 1.0.0
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "title": "Login Successful",
 *   "detail": "Successfully validated user credentials",
 *   "token": ""
 * }
 *
 * @apiErrorExample Unauthorized-Response:
 *   HTTP/1.1 401 Unauthorized
 * "errors": [
 * {
 *  "title": "Invalid Credentials",
 *  "detail": "Check email and password combination",
 *  "errorMessage": ""
 * }
 * ]
 */
router.post('/login', UsersController.login);

module.exports = router;
