/* eslint-disable */
const Astronauts = require('../models/astronaut');

exports.astronautsEndpoint = (req, res) => {
  const reqLimit = parseInt(req.query.limit);
  const reqPage = parseInt(req.query.page);
  delete req.query.limit;
  delete req.query.page;
  const query = Object.keys(req.query).reduce((mappedQuery, key) => {
    const param = req.query[key];
    if (param) {
      mappedQuery[key] = param;
    }
    return mappedQuery;
  }, {});

  // Making sure we don't continue if we get page 0.
  if (reqPage < 0 || reqPage === 0) {
    res.json({ Error: 'Requested page can not be 0' });
  } else {
    Astronauts.find(query)
      .limit(reqLimit)
      .skip(reqLimit * (reqPage - 1))
      .select('-status')
      .collation({ locale: 'en', strength: 2 })
      .then((astronaut) => {
        if (astronaut === undefined || astronaut.length === 0) {
          res.status(404).json({ Error: 'Nothing found! Please refine your search. No worries, it happens to all of us sometimes.' });
        } else {
          res.send(astronaut);
        }
      });
  }
};


exports.astronautEndpoint = (req, res) => {
  Astronauts.findOne(req.query)
    .then((astronaut) => {
      if (astronaut === undefined || astronaut.length === 0) {
        res.status(404).json({ Error: 'Nothing found! Please refine your search. No worries, it happens to all of us sometimes.' });
      } else {
        res.send(astronaut);
      }
    });
};
