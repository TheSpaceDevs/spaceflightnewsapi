const mongoose = require('mongoose');
const mongoosePaginate = require('mongoose-paginate-v2');
const uniqueValidator = require('mongoose-unique-validator');

const { Schema } = mongoose;

const blogSchema = new Schema({
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
  imageUrl: {
    type: String,
    required: true,
  },
  newsSite: {
    type: String,
    required: true
  },
  summary: {
    type: String,
    required: false,
    default: "No summary available"
  },
  publishedAt: {
    type: Date,
    required: true,
  },
  launches: [{"provider": String, "id": {}}],
  events: [{"provider": String, "id": {}}],
  deleted: {
    type: Boolean,
    required: false,
    default: false,
    select: false
  },
  featured: {
    type: Boolean,
    required: false,
    default: false
  }
}, {
  timestamps: true,
  versionKey: false
});

blogSchema.index({
  title: 'text',
  newsSite: 'text'
});

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
