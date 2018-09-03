/* eslint-disable radix */
const Article = require('../models/article');

exports.articlesEndpoint = (req, res) => {
  // set the limit to a separate variable and then remove it from the object
  const limit = req.query.limit;
  delete req.query.limit;
  Article.find({ $or: [req.query] }, (err, article) => {
    if (err) { res.send(err); }
    res.send(article);
  })
    .limit(parseInt(limit))
    .sort({ date_published: -1 });
};

exports.findByID = (req, res) => {
  Article.find({ _id: req.params.id }, (err, article) => {
    if (err) { res.send(err); }
    res.send(article);
  });
};
