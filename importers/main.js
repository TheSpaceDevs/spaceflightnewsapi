const nsf = require('./nasaspaceflight');

exports.combinedImporter = () => {
  setInterval(nsf.importArticles, 900000);
  console.log('Importer ran!');
};
