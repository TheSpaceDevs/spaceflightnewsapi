/* eslint-disable radix,camelcase */
const Article = require('../models/article');

exports.articlesEndpoint = (req, res) => {
  const {
    limit,
    news_site,
    tags,
    categories,
    title,
    url,
    date_published,
    date_added,
    since_published,
    since_added,
  } = req.query;

  // We're getting the various parameters of the request and assign them to a new object.
  // We do this so that we:
  // 1) only pass a request with valid parameters and
  // 2) can change the object a bit and include a regex
  const query = {};

  if (news_site) {
    query.news_site = { $regex: news_site, $options: 'i' };
  }
  if (tags) {
    query.tags = { $regex: tags, $options: 'i' };
  }
  if (categories) {
    query.categories = { $regex: categories, $options: 'i' };
  }
  if (title) {
    query.title = { $regex: title, $options: 'i' };
  }
  if (url) {
    query.url = { $regex: url, $options: 'i' };
  }
  if (date_published) {
    query.date_published = date_published;
  }
  if (date_added) {
    query.date_added = date_added;
  }
  if (since_published) {
    query.date_published = { $gt: since_published };
  }
  if (since_added) {
    query.date_added = { $gt: since_added };
  }

  // Make sure people don't mix since_* and date_*
  if () {
    res.status(405).json({ message: 'Please do not mix since_* and date_*' });
  } else { // Proceed if there's nothing mixed
    Article.find({ $or: [query] }, (err, article) => {
      if (err) { res.send(err); }
      if (article === undefined || article.length === 0) {
        res.status(404).json({ message: 'No articles found! Please refine your search. No worries, it happens to all of us sometimes.' });
      } else {
        res.send(article);
      }
    })
      .limit(parseInt(limit))
      .sort({ date_published: -1 });
  }
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
