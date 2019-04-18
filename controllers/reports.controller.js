const Report = require('../models/report.model');

module.exports.getReports = async (req, res, next) => {
  const options = {
    page: parseInt(req.query.page, 10) || 1,
    limit: parseInt(req.query.limit, 10) || 10,
    sort: req.query.sort || '-date_published'
  };

  for (const key in options) {
    if (options.hasOwnProperty(key)) {
      delete req.query[key]
    }
  }

  if (req.query.search) {
    try {
      let result = await Report.paginate({$text: {$search: req.query.search}}, options);
      res.send(result);
    } catch (e) {
      res.send({'message': 'Uh-oh, something went wrong. Please try again!'});
      console.log(e)
    }
  } else {
    try {
      let result = await Report.paginate(req.query, options);
      res.send(result);
    } catch (e) {
      res.send({'message': 'Uh-oh, something went wrong. Please try again!'});
      console.log(e)
    }
  }
};
