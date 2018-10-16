/* eslint-disable radix,camelcase,no-param-reassign */
const iss = require('../models/iss');

exports.issEndpoint = (req, res) => {
  iss.find({}, (err, thingie) => {
    if (err) { console.log(err); }
    console.log(thingie);
    return res.send(thingie);
  });
};
