const ArticleModel = require('../models/article.model');
const BlogModel = require('../models/blog.model');
const ReportModel = require('../models/report.model');
const pjson = require('../package');

const getInfo = async (req, res) => {
    const count = await ArticleModel.countDocuments({});
    const newsSites = await ArticleModel.distinct('newsSite');
    const blogSites = await BlogModel.distinct('newsSite');
    const reportSites = await ReportModel.distinct('newsSite');

    res.json({
        totalNumberOfArticles: count,
        apiVersion: pjson.version,
        newsSites: newsSites,
        blogSites: blogSites,
        reportSites: reportSites,
    });
};

module.exports = {
    getInfo,
};
