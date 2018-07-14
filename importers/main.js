const nsf = require('./nasaspaceflight');

exports.combinedImporter = () => {
  nsf.importArticles();
};
