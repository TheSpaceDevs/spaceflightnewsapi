// Handle any errors that come up
exports.errorHandler = (err, req, res, next) => {
  if (err.status) {
    res.status(err.status).json({ message: err.message });
  } else {
    res.status(500).json({ message: 'internal server error' });
  }
};

// Handle case where user requests nonexistent endpoint
exports.nullRoute = (req, res, next) => {
  res.status(404).json({ Error: 'Nothing found! Please refine your search. No worries, it happens to all of us sometimes.' });
};

// Create an error for the api error handler
exports.newHttpError = (status, message) => {
  let err;

  // Eliminates problem where a null message would get passed in and the final
  // error message would become 'null' (stringified null)
  if (message == null) {
    err = new Error();
  } else {
    err = new Error(message);
  }

  err.status = status;
  return err;
};
