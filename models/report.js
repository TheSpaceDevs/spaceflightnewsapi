const mongoose = require('mongoose');

const { Schema } = mongoose;

const reportSchema = new Schema({
  title: String,
  date_added: String,
  date_published: String,
});

const Report = mongoose.model('reports', reportSchema);

module.exports = Report;
