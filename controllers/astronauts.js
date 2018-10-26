const Astronauts = require('../models/astronaut');

exports.astronautsEndpoint = (req, res) => {
  Astronauts.find()
    .then((astronauts) => { res.send(astronauts); });
};


exports.astronautEndpoint = (req, res) => {
  Astronauts.find({ _id: req.params.id })
    .then((astronaut) => {
      if (astronaut === undefined || astronaut.length === 0) {
        res.status(404).json({ Error: 'Nothing found! Please refine your search. No worries, it happens to all of us sometimes.' });
      } else {
        res.send(astronaut);
      }
    });
};
