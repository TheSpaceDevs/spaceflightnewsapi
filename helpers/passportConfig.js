const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const JwtStrategy = require('passport-jwt').Strategy;
const bcrypt = require('bcryptjs');
const User = require('../models/user.model');

const cookieExtractor = (req) => {
  let token = null;
  if (req && req.cookies) {
    token = req.cookies['access_token'];
  }
  return token;
};

passport.use(new JwtStrategy({
  jwtFromRequest: cookieExtractor,
  secretOrKey: process.env.SECRET,
}, async (payload, done) => {
  try {
    const user = await User.findById({ _id: payload.sub });
    if (user) {
      return done(null, user);
    }
    return done(null, false);
  } catch (err) {
    return done(err, false);
  }
}));

passport.use(new LocalStrategy(async (username, password, done) => {
  try {
    const user = await User.findOne({ email: username }).select('+password');
    const match = await bcrypt.compare(password, user.password);

    if (match) {
      return done(null, user);
    }
    return done(null, false);
  } catch (err) {
    return done(err, false);
  }
}));