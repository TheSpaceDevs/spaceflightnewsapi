/* eslint-disable radix,camelcase,no-param-reassign */
const Article = require('../models/article');

exports.articlesEndpoint = (req, res) => {
  const reqLimit = parseInt(req.query.limit);
  const reqPage = parseInt(req.query.page);
  delete req.query.limit;
  delete req.query.page;
  const query = Object.keys(req.query).reduce((mappedQuery, key) => {
    const param = req.query[key];
    if (param) {
      mappedQuery[key] = param;
    }
    return mappedQuery;
  }, {});

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

exports.articleEndpoint = (req, res) => {
  Article.findOne(req.query, (err, article) => {
    if (err) { res.send(err); }
    if (article === undefined || article.length === 0) {
      res.status(404).json({ Error: 'Article not found! Please refine your search. No worries, it happens to all of us sometimes.' });
    } else {
      res.send(article);
    }
  });
};
