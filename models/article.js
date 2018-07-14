const mongoose = require('mongoose');

const { Schema } = mongoose;

const articleSchema = new Schema({
  id: String,
  title: String,
  url: String,
  news_site: String,
  date_gmt: String,
  categories: Array,
  tags: Array,
});

const Article = mongoose.model('Articles', articleSchema);

module.exports = Article;
