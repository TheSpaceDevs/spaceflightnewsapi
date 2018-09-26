const Article = require('../models/article');

exports.articlesCount = (req, res) => {
  Article.countDocuments({}, (err, count) => {
    if (err) { res.send(err); }
    res.json({ total_number_of_articles: count });
  });
};
