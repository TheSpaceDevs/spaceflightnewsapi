const mongoose = require('mongoose');

const {Schema} = mongoose;

const astronautSchema = new Schema({
  name: String,
  birthday: String,
  nationality: String,
  agency: String,
  twitter: String,
  facebook: String,
  instagram: String,
});

const astronautModel = mongoose.model('astronauts', astronautSchema);

module.exports = astronautModel;
