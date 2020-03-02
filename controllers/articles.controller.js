const jwt = require('jsonwebtoken');
const Article = require('../models/article.model');

getArticles = async (req, res, next) => {
  const options = {
    page: parseInt(req.query.page, 10) || 1,
    limit: parseInt(req.query.limit, 10) || 10,
    sort: req.query.sort || '-date_published'
  };

  for (const key in options) {
    if (options.hasOwnProperty(key)) {
      delete req.query[key];
    }
  }

  if (req.query.search) {
    try {
      let result = await Article.paginate(
        { $text: { $search: req.query.search } },
        options,
      );
      res.send(result);
    } catch (e) {
      if (e.name === 'CastError' && e.path === '_id') {
        return res.status(400).send({error: 'wrong _id format received. do not wrap it in quotes'})
      }
      res.send({ message: 'Uh-oh, something went wrong. Please try again!' });
      console.log(e);
    }
  } else {
    try {
      let result = await Article.paginate(req.query, options);
      res.send(result);
    } catch (e) {
      if (e.name === 'CastError' && e.path === '_id') {
        return res.status(400).send({error: 'wrong _id format received. do not wrap it in quotes'})
      }
      res.send({ message: 'Uh-oh, something went wrong. Please try again!' });
      console.log(e);
    }
  }
};

postArticles = (req, res) => {
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

deleteArticles = async (req, res) => {
  jwt.verify(req.token, process.env.SECRET, async (err, authData) => {
    if (err || !authData.user.roles.includes('admin')) {
      return res.sendStatus(403);
    }

    try {
      await Article.deleteMany({ _id: { $in: req.query._id } });
      return res.json({ deleted: req.query._id });
    } catch (e) {
      console.log(e);
      return res.json({ error: 'Something went wrong with deleting!' });
    }
  });
};

module.exports = {
  getArticles,
  postArticles,
  deleteArticles
};