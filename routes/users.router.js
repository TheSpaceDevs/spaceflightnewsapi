const router = require('express').Router();
const passport = require('passport');
const UserController = require('../controllers/users.controller');

router.get('/', passport.authenticate('jwt', { session: false }), UserController.getUsers);
router.post('/register', passport.authenticate('jwt', { session: false }), UserController.addUser);
router.post('/login', passport.authenticate('local', { session: false }), UserController.loginUser);
router.get('/logout', passport.authenticate('jwt', { session: false }), UserController.logOut);

module.exports = router;
