const jwt = require('jsonwebtoken');
const Article = require('../models/article.model');

const getArticles = async (req, res) => {
  const options = {
    page: parseInt(req.query.page, 10) || 1,
    limit: parseInt(req.query.limit, 10) || 10,
    sort: req.query.sort || '-date_published',
  };

  Object.keys(options).forEach((key) => {
    // since options has hard codes keys, we can disable no-prototype-builtins
    // eslint-disable-next-line no-prototype-builtins
    if (options.hasOwnProperty(key)) {
      delete req.query[key];
    }
  });

  if (req.query.search) {
    try {
      const result = await Article.paginate(
        { $text: { $search: req.query.search } },
        options,
      );
      return res.send(result);
    } catch (e) {
      if (e.name === 'CastError' && e.path === '_id') {
        return res.status(400).send({ error: 'wrong _id format received. do not wrap it in quotes' });
      }
      // TODO: implement Sentry
      // eslint-disable-next-line
      console.log(e);
      return res.send({ message: 'Uh-oh, something went wrong. Please try again!' });
    }
  }

  try {
    const result = await Article.paginate(req.query, options);
    return res.send(result);
  } catch (e) {
    if (e.name === 'CastError' && e.path === '_id') {
      return res.status(400).send({ error: 'wrong _id format received. do not wrap it in quotes' });
    }
    // TODO: implement Sentry
    // eslint-disable-next-line
    console.log(e);
    return res.send({ message: 'Uh-oh, something went wrong. Please try again!' });
  }
};

const postArticles = (req, res) => {
  jwt.verify(req.token, process.env.SECRET, async (err, authData) => {
    if (err || !authData.user.roles.includes('admin')) {
      return res.sendStatus(403);
    }

    const newArticle = new Article(req.body);

    try {
      const result = await newArticle.save();
      return res.status(201).json({
        message: 'Article saved',
        article: result,
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

const deleteArticles = async (req, res) => {
  jwt.verify(req.token, process.env.SECRET, async (err, authData) => {
    if (err || !authData.user.roles.includes('admin')) {
      return res.sendStatus(403);
    }

    try {
      // We need the _id
      // eslint-disable-next-line
      await Article.deleteMany({ _id: { $in: req.query._id } });
      // eslint-disable-next-line
      return res.json({ deleted: req.query._id });
    } catch (e) {
      // TODO: implement Sentry
      // eslint-disable-next-line
      console.log(e);
      return res.json({ error: 'Something went wrong with deleting!' });
    }
  });
};

module.exports = {
  getArticles,
  postArticles,
  deleteArticles,
};
