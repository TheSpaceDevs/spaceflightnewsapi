const jwt = require('jsonwebtoken');
const Article = require('../models/article.model');
const checkAdmin = require('../helpers/checkAdmin');


const getArticles = async (req, res) => {
  const options = {
    page: parseInt(req.query.page, 10) || 1,
    limit: parseInt(req.query.limit, 10) || 10,
    sort: req.query.sort || '-publishedAt',
  };

  Object.keys(options).forEach((key) => {
    // since options has hard codes keys, we can disable no-prototype-builtins
    // eslint-disable-next-line no-prototype-builtins
    if (options.hasOwnProperty(key)) {
      delete req.query[key];
    }
  });

  try {
    const result = await Article.paginate({}, options);
    return res.send(result);
  } catch (e) {
    // TODO: implement Sentry
    // eslint-disable-next-line
    console.log(e);
    return res.status(500).send({ message: 'Uh-oh, something went wrong. Please try again!' });
  }
};

const postArticles = async (req, res) => {
  if (!await checkAdmin(req.token)) {
    return res.status(403).send({ error: 'you are not allowed to do that' });
  }
  const newArticle = new Article(req.body);

  try {
    const result = await newArticle.save();
    return res.status(201).json({
      message: 'Article saved',
      article: result,
    });
  } catch (err) {
    console.log(err);
    if (err.name === 'ValidationError') {
      return res
        .status(422)
        .json({ error: err.errors });
    }
    return res.status(500).json({ message: 'error' });
  }
};

const deleteArticles = async (req, res) => {
  if (!await checkAdmin(req.token)) {
    return res.status(403).send({ error: 'you are not allowed to do that' });
  }

  try {
    // We need the _id
    // eslint-disable-next-line
    const result = await Article.deleteMany({ _id: { $in: req.params.id } });
    // eslint-disable-next-line
    return res.json({ deleted: req.params.id});
  } catch (e) {
    // TODO: implement Sentry
    // eslint-disable-next-line
    console.log(e);
    return res.json({ error: 'Something went wrong with deleting!' });
  }
};

module.exports = {
  getArticles,
  postArticles,
  deleteArticles,
};
