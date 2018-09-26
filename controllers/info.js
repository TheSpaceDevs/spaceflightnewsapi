const Article = require('../models/article');
var pjson = require('../package.json');

exports.articlesCount = (req, res) => {
  Article.countDocuments({}, (err, count) => {
    if (err) { res.send(err); }
    res.json({ total_number_of_articles: count });
  });
};

exports.version = (req, res) => {
  res.json({ api_version: pjson.version });
};
