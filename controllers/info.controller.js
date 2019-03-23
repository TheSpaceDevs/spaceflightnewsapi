const ArticleModel = require('../models/article.model');
const pjson = require('../package');

module.exports.getInfo = async (req, res, next) => {
  let count = await ArticleModel.countDocuments({});

  res.send({
    total_number_of_articles: count,
    api_version: pjson.version
  })
};
