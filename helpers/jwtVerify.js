module.exports = (req, res, next) => {
  const bearerHeader = req.headers.authorization;
  if (typeof bearerHeader !== 'undefined') {
    const bearer = bearerHeader.split(' ');
    // Destructuring gives problems right now
    // eslint-disable-next-line prefer-destructuring
    req.token = bearer[1];
    next();
  } else {
    res.status(401).send({ error: 'no valid token found' });
  }
};
