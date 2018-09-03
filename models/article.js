const mongoose = require('mongoose');

const { Schema } = mongoose;

const articleSchema = new Schema({
  news_site: String,
  title: String,
  url: String,
  date_published: Number,
  date_added: Number,
  tags: Array,
  categories: Array,
});

const Article = mongoose.model('Articles', articleSchema);

module.exports = Article;
