/* eslint-disable radix,camelcase,no-param-reassign */
const Article = require('../models/article');

exports.articlesEndpoint = (req, res) => {
  const query = Object.keys(req.query).reduce((mappedQuery, key) => {
    const param = req.query[key];
    if (param) {
      mappedQuery[key] = param;
    }
    return mappedQuery;
  }, {});

  Article.find(query).then((articles) => {
    if (articles === undefined || articles.length === 0) {
      res.status(404).json({ message: 'Nothing found! Please refine your search. No worries, it happens to all of us sometimes.' });
    } else {
      res.json(articles);
    }
  });
};

exports.articleEndpoint = (req, res) => {
  Article.find(req.query, (err, article) => {
    if (err) { res.send(err); }
    if (article === undefined || article.length === 0) {
      res.status(404).json({ message: 'Article not found! Please refine your search. No worries, it happens to all of us sometimes.' });
    } else {
      res.send(article);
    }
  });
};
