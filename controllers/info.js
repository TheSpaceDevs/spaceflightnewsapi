const Article = require('../models/article');
const pjson = require('../package.json');

exports.infoEndpoint = (req, res) => {
  Article.countDocuments({}, (err, count) => {
    if (err) { res.send(err); }
    res.json({
      total_number_of_articles: count,
      api_version: pjson.version,
    });
  });
};
