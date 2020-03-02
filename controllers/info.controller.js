const ArticleModel = require('../models/article.model');
const pjson = require('../package');

const getInfo = async (req, res) => {
  const count = await ArticleModel.countDocuments({});
  const newsSites = await ArticleModel.distinct('news_site');

  res.send({
    total_number_of_articles: count,
    api_version: pjson.version,
    news_sites: newsSites,
  });
};

module.exports = {
  getInfo,
};
