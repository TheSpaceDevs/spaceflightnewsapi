const mongoose = require('mongoose');
const mongoosePaginate = require('mongoose-paginate-v2');
const uniqueValidator = require('mongoose-unique-validator');

const { Schema } = mongoose;

const articleSchema = new Schema({
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
    unique: true,
  },
  url: {
    type: String,
    required: true,
    unique: true,
  },
  date_published: {
    type: Number,
    default: Math.floor(Date.now() / 1000),
  },
  date_added: {
    type: Number,
    default: Math.floor(Date.now() / 1000),
  },
  tags: [String],
  categories: [String],
  featured_image: {
    type: String,
    required: true,
  },
  featured: {
    type: Boolean,
    default: false,
  },
  launches: [String],
  events: [String],
  ll: [String],
  published_date: {
    type: Date,
  },
  imported_date: {
    type: Date,
  },
});

articleSchema.index({
  title: 'text',
  news_site: 'text',
  news_site_long: 'text',
});

articleSchema.plugin(mongoosePaginate);
articleSchema.plugin(uniqueValidator);

const ArticleModel = mongoose.model('Articles', articleSchema);

ArticleModel.on('index', (err) => {
  if (err) {
    console.error('Article index error: %s', err);
  } else {
    console.info('Article indexing complete');
  }
});

module.exports = ArticleModel;
