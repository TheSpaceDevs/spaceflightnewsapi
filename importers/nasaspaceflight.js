const axios = require('axios');
const _ = require('lodash');

const Article = require('../models/article');

exports.importArticles = () => {
  // Fetch the posts, and create a new document for each post found, if not already exists.
  axios.get('https://www.nasaspaceflight.com/wp-json/wp/v2/posts/?per_page=5')
    .then((resp) => {
      _.forEach(resp.data, (article) => {
        const newArticle = Article({
          id: article.id,
          title: article.title.rendered,
          url: article.link,
          news_site: 'nasaspaceflight',
          date_gmt: article.date_gmt,
        });
        Article.findOneAndUpdate({ id: article.id, date_gmt: article.date_gmt }, newArticle, { upsert: true }, () => {
          // Since the article only have category ID's, we need to find the name of the ID.
          _.forEach(article.categories, (categoryId) => {
            axios.get(`https://www.nasaspaceflight.com/wp-json/wp/v2/categories/${categoryId}`)
              .then((catResp) => {
                // Now that we now the name of the category ID, update the article with that information.
                Article.findOneAndUpdate({ id: article.id, date_gmt: article.date_gmt },
                  { $addToSet: { categories: catResp.data.name.toLowerCase() } }, (err) => {
                    if (err) console.log(err);
                  });
              });
          });
        });
      });
    })
    .catch(err => console.log(err));
};
