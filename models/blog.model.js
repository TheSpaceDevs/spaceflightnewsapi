const mongoose = require('mongoose');
const mongoosePaginate = require('mongoose-paginate-v2');

const { Schema } = mongoose;

const blogSchema = new Schema({
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

blogSchema.index({news_site: 'text', news_site_long: 'text', title: 'text'});

blogSchema.plugin(mongoosePaginate);

const BlogModel = mongoose.model('Blogs', blogSchema);

module.exports = BlogModel;
