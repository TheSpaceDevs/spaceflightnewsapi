const mongoose = require('mongoose');

const { Schema } = mongoose;

const expeditionSchema = new Schema({
  spacecraft: String,
  mission: String,
  flight_status: String,
  destination: String,
  begin: Number,
  end: Number,
  astronauts: Array,
  mission_url: String,
  mission_patch: String,
  missions_crew_portret: String,
});

const expeditionModel = mongoose.model('mannedflights', expeditionSchema);

module.exports = expeditionModel;
