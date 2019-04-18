const mongoose = require('mongoose');
const mongoosePaginate = require('mongoose-paginate-v2');
const uniqueValidator = require('mongoose-unique-validator');

const { Schema } = mongoose;

const reportSchema = new Schema({
  news_site: {
    type: String,
    required: true,
  },
  news_site_long: {
    type: String,
    required: true,
  },
  title: {
    type: String,
    required: true,
    unique: true
  },
  url: {
    type: String,
    required: true,
    unique: true
  },
  date_published: {
    type: Number,
    default: Math.floor(Date.now() / 1000)
  },
  date_added: {
    type: Number,
    default: Math.floor(Date.now() / 1000)
  }
});

reportSchema.index({title: 'text', news_site: 'text', news_site_long: 'text'});

reportSchema.plugin(mongoosePaginate);
reportSchema.plugin(uniqueValidator);

const ReportModel = mongoose.model('Reports', reportSchema);

module.exports = ReportModel;
