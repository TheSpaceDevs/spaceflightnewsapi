const mongoose = require('mongoose');
const mongoosePaginate = require('mongoose-paginate-v2');

const { Schema } = mongoose;

const articleSchema = new Schema({
  news_site: {
    type: String
  },
  news_site_long: {
    type: String
  },
  title: {
    type: String
  },
  url: {
    type: String
  },
  date_published: {
    type: Number
  },
  date_added: {
    type: Number
  },
  tags: [String],
  categories: [String],
  featured_image: {
    type: String
  }
});

articleSchema.index({news_site: 'text', news_site_long: 'text', title: 'text'});

articleSchema.plugin(mongoosePaginate);

const ArticleModel = mongoose.model('Articles', articleSchema);

module.exports = ArticleModel;
