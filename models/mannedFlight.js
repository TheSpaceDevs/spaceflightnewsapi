const mongoose = require('mongoose');

const { Schema } = mongoose;

const expeditionSchema = new Schema({
  name: String,
  status: String,
  flight_status: String,
  begin: Number,
  end: Number,
  expedition_number: Number,
  astronauts: Array,
  expedition_url: String,
  expedition_patch: String,
  expedition_crew_pic: String,
});

const expeditionModel = mongoose.model('mannedflights', expeditionSchema);

module.exports = expeditionModel;
