const mongoose = require('mongoose');
const mongoosePaginate = require('mongoose-paginate-v2');
const uniqueValidator = require('mongoose-unique-validator');

const {Schema} = mongoose;

const blogSchema = new Schema({
  news_site: {
    type: String,
    required: true
  },
  news_site_long: {
    type: String,
    required: true
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
  },
  tags: [String],
  categories: [String],
  featured_image: {
    type: String,
    required: true
  },
  launches: [String],
  events: [String]
});

blogSchema.index({news_site: 'text', news_site_long: 'text', title: 'text'});

blogSchema.plugin(mongoosePaginate);
blogSchema.plugin(uniqueValidator);

const BlogModel = mongoose.model('Blogs', blogSchema);

BlogModel.on('index', (err) => {
  if (err) {
    console.error('Blog index error: %s', err);
  } else {
    console.info('Blog indexing complete');
  }
});

module.exports = BlogModel;
