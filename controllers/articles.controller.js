const Article = require('../models/article.model');

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

  // First return the results of searched articles if this was requested
  if (req.query.search !== undefined) {
    try {
      const result = await Article.paginate({ title: { $regex: req.query.search, $options: 'i' } }, options);
      return res.send(result);
    } catch (e) {
      const error = new Error('Uh-oh, something went wrong. Please try again!');
      res.status(500);
      return next(error);
    }
  }

  try {
    const result = await Article.paginate({}, options);
    return res.send(result);
  } catch (e) {
    const error = new Error('Uh-oh, something went wrong. Please try again!');
    res.status(500);
    return next(error);
  }
};

const postArticle = async (req, res, next) => {
  const newArticle = new Article(req.body);

  try {
    const result = await newArticle.save();
    return res.status(201).json({
      message: 'Article saved',
      article: result,
    });
  } catch (err) {
    if (err.name === 'ValidationError') {
      const error = new Error(err.errors);
      res.status(422);
      return next(error);
    }
  }
};

const patchArticle = async (req, res, next) => {
  const { id } = req.params;

  try {
    await Article.findByIdAndUpdate({ _id: id }, req.body);
    const article = await Article.findById({ _id: id });
    return res.status(202).json(article);
  } catch (err) {
    return next(err);
  }
};

const deleteArticle = async (req, res, next) => {
  const { id } = req.params;

  try {
    await Article.deleteMany({ _id: { $in: id } });
    return res.json({ deleted: id });
  } catch (err) {
    return next(err);
  }
};

module.exports = {
  getArticles,
  postArticle,
  patchArticle,
  deleteArticle,
};
