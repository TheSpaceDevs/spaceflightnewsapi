const mongoose = require('mongoose');

const { Schema } = mongoose;

const issSchema = new Schema({
  name: String,
  expedition_number: Number,
  astronauts: Array,
  flight_status: String,
  status: String,
  begin: Number,
  end: Number,
  expedition_url: String,
  expedition_patch: String,
  expedition_crew_pic: String,
});

const ISS = mongoose.model('iss', issSchema);

module.exports = ISS;
