const Astronauts = require('../models/astronaut');

exports.astronautsEndpoint = (req, res) => {
  Astronauts.find()
    .then((astronauts) => { res.send(astronauts); });
};
