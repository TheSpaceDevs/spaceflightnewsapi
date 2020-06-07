const jwt = require('jsonwebtoken');
const Article = require('../models/article.model');
const checkAdmin = require('../helpers/checkAdmin');


const getArticles = async (req, res, next) => {
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
    const error = new Error("Uh-oh, something went wrong. Please try again!")
    res.status(500)
    return next(error)
  }
};

const postArticles = async (req, res, next) => {
  if (!await checkAdmin(req.token)) {
    const error = new Error('you are not allowed to do that')
    res.status(403)
    return next(error)
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
      const error = new Error(err.errors)
      res.status(422)
      return next(error)
    }
  }
};

const patchArticles = async (req, res, next) => {
  const {id} = req.params;

  if (!await checkAdmin(req.token)) {
    const error = new Error('you are not allowed to do that')
    res.status(403)
    return next(error)
  }

  try {
    await Article.findByIdAndUpdate({_id: id}, req.body);
    const article = await Article.findById({_id: id});
    return res.status(202).json(article);
  } catch (err) {
    return next(err);
  }
}

const deleteArticles = async (req, res, next) => {
  if (!await checkAdmin(req.token)) {
    const error = new Error('you are not allowed to do that')
    res.status(403)
    return next(error)
  }

  try {
    // We need the _id
    // eslint-disable-next-line
    const result = await Article.deleteMany({ _id: { $in: req.params.id } });
    // eslint-disable-next-line
    return res.json({ deleted: req.params.id});
  } catch (err) {
    return next(err)
  }
};

module.exports = {
  getArticles,
  postArticles,
  patchArticles,
  deleteArticles,
};
