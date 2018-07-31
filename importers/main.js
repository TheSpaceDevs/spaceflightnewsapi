const nsf = require('./nasaspaceflight');

exports.combinedImporter = () => {
  setInterval(nsf.importArticles, 900000);
};
