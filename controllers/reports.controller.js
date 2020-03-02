const Report = require('../models/report.model');

const getReports = async (req, res) => {
  const options = {
    page: parseInt(req.query.page, 10) || 1,
    limit: parseInt(req.query.limit, 10) || 10,
    sort: req.query.sort || '-date_published',
  };

  Object.keys(options).forEach((key) => {
    // since options has hard codes keys, we can disable no-prototype-builtins
    // eslint-disable-next-line no-prototype-builtins
    if (options.hasOwnProperty(key)) {
      delete req.query[key];
    }
  });

  if (req.query.search) {
    try {
      const result = await Report.paginate(
        { $text: { $search: req.query.search } },
        options,
      );
      return res.send(result);
    } catch (e) {
      // TODO: implement Sentry
      // eslint-disable-next-line
      console.log(e);
      return res.send({ message: 'Uh-oh, something went wrong. Please try again!' });
    }
  }

  try {
    const result = await Report.paginate(req.query, options);
    return res.send(result);
  } catch (e) {
    // TODO: implement Sentry
    // eslint-disable-next-line
    console.log(e);
    return res.send({ message: 'Uh-oh, something went wrong. Please try again!' });
  }
};

module.exports = {
  getReports,
};
