/* eslint-disable radix */
const Article = require('../models/article');

exports.allArticles = (req, res) => {
  Article.find({}, (err, article) => {
    if (err) res.send(err);
    res.send(article);
  })
    .limit(parseInt(req.params.limit))
    .sort({ date_published: -1 });
};

exports.byNewsSite = (req, res) => {
  Article.find({ news_site: req.params.newssite }, (err, articles) => {
    if (err) { res.send(err); }
    if (!articles.length) {
      res.status(404).json({ message: 'Requested news site not found' });
    } else {
      res.send(articles);
    }
  });
};

exports.findByCategory = (req, res) => {
  Article.find({ categories: req.params.category }, (err, articles) => {
    if (err) { res.send(err); }
    res.send(articles);
  });
};

exports.findByTag = (req, res) => {
  Article.find({ tags: req.params.tag }, (err, articles) => {
    if (err) { res.send(err); }
    res.send(articles);
  });
};

exports.findByID = (req, res) => {
  Article.find({ _id: req.params.id }, (err, article) => {
    if (err) { res.send(err); }
    res.send(article);
  });
};
