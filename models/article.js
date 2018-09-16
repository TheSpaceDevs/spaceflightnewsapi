const mongoose = require('mongoose');

const { Schema } = mongoose;

const articleSchema = new Schema({
  news_site: String,
  news_site_long: String,
  title: String,
  url: String,
  date_published: Number,
  date_added: Number,
  tags: Array,
  categories: Array,
  featured_image: String,
});

const Article = mongoose.model('Articles', articleSchema);

module.exports = Article;
