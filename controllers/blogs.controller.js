const jwt = require('jsonwebtoken');
const Blog = require('../models/blog.model');

module.exports.getBlogs = async (req, res, next) => {
  const options = {
    page: parseInt(req.query.page, 10) || 1,
    limit: parseInt(req.query.limit, 10) || 10,
    sort: req.query.sort || '-date_published',
  };

  for (const key in options) {
    if (options.hasOwnProperty(key)) {
      delete req.query[key];
    }
  }

  if (!req.query.search) {
    try {
      let result = await Blog.paginate(req.query, options);
      res.send(result);
    } catch (e) {
      res.send({ message: 'Uh-oh, something went wrong. Please try again!' });
      console.log(e);
    }
  } else {
    try {
      let result = await Blog.paginate(
        { $text: { $search: req.query.search } },
        options,
      );
      res.send(result);
    } catch (e) {
      res.send({ message: 'Uh-oh, something went wrong. Please try again!' });
      console.log(e);
    }
  }
};

module.exports.postBlogs = (req, res) => {
  jwt.verify(req.token, process.env.SECRET, async (err, authData) => {
    if (err || !authData.user.roles.includes('admin')) {
      return res.sendStatus(403);
    }

    const newBlog = new Blog(req.body);

    try {
      const result = await newBlog.save();
      return res.status(201).json({
        message: 'Blog saved',
        blog: result,
      });
    } catch (e) {
      if (e.name === 'ValidationError') {
        return res
          .status(400)
          .json({ error: 'title, url and _id must be unique' });
      }
      return res.status(500).json({ message: 'error' });
    }
  });
};

module.exports.deleteBlogs = async (req, res) => {
  jwt.verify(req.token, process.env.SECRET, async (err, authData) => {
    if (err || !authData.user.roles.includes('admin')) {
      return res.sendStatus(403);
    }

    try {
      await Blog.deleteMany({ _id: { $in: req.query._id } });
      return res.json({ deleted: req.query._id });
    } catch (e) {
      console.log(e);
      return res.json({ error: 'Something went wrong with deleting!' });
    }
  });
};
