/* eslint-disable radix,camelcase,no-param-reassign */
const Article = require('../models/article');

exports.articlesEndpoint = (req, res) => {
  const reqLimit = parseInt(req.query.limit);
  const reqPage = parseInt(req.query.page);
  const sinceAdded = parseInt(req.query.since_added);
  const sincePublished = parseInt(req.query.since_published);
  delete req.query.limit;
  delete req.query.page;
  delete req.query.since_added;
  delete req.query.since_published;
  const query = Object.keys(req.query).reduce((mappedQuery, key) => {
    const param = req.query[key];
    if (param) {
      mappedQuery[key] = param;
    }
    return mappedQuery;
  }, {});

  if (sinceAdded) {
    query.date_added = { $gte: sinceAdded };
  }

  if (sincePublished) {
    query.date_published = { $gte: sincePublished };
  }

  // Making sure we don't continue if we get page 0.
  if (reqPage < 0 || reqPage === 0) {
    res.json({ Error: 'Requested page can not be 0' });
  } else {
    Article.find(query)
      .limit(reqLimit)
      .skip(reqLimit * (reqPage - 1))
      .sort({ date_published: -1 })
      .select('-id')
      .collation({ locale: 'en', strength: 2 })
      .then((articles) => {
        if (articles === undefined || articles.length === 0) {
          res.status(404).json({ Error: 'Nothing found! Please refine your search. No worries, it happens to all of us sometimes.' });
        } else {
          res.send(articles);
        }
      });
  }
};

exports.articleSearchEndpoint = (req, res) => {
  Article.find({ $text: { $search: req.query.term } }, { score: { $meta: 'textScore' } })
    .sort({ score: { $meta: 'textScore' } })
    .then((articles) => {
      if (articles === undefined || articles.length === 0) {
        res.status(404).json({ Error: 'Nothing found! Please refine your search. No worries, it happens to all of us sometimes.' });
      } else {
        res.send(articles);
      }
    });
};

exports.articleEndpoint = (req, res) => {
  Article.findOne(req.query, (err, article) => {
    if (err) { res.send(err); }
    if (article === undefined || !article) {
      res.status(404).json({ Error: 'Article not found! Please refine your search. No worries, it happens to all of us sometimes.' });
    } else {
      res.send(article);
    }
  });
};
