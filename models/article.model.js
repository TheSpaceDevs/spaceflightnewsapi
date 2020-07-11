const mongoose = require('mongoose');
const mongoosePaginate = require('mongoose-paginate-v2');
const uniqueValidator = require('mongoose-unique-validator');

const { Schema } = mongoose;

const articleSchema = new Schema({
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
  imageUrl: {
    type: String,
    required: true,
  },
  newsSite: {
    type: String,
    required: true,
  },
  summary: {
    type: String,
    required: false,
    default: 'No summary available',
  },
  publishedAt: {
    type: Date,
    required: true,
  },
  launches: [{ provider: String, id: {} }],
  events: [{ provider: String, id: {} }],
  deleted: {
    type: Boolean,
    required: false,
    default: false,
    select: false,
  },
  featured: {
    type: Boolean,
    required: false,
    default: false,
  },
}, {
  timestamps: true,
  versionKey: false,
});

articleSchema.index({
  title: 'text',
  newsSite: 'text',
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
