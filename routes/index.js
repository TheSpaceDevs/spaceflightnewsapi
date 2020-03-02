const express = require('express');

const router = express.Router();

/* GET home page. */
router.get('/', (req, res) => {
  res.sendFile(`${__dirname}/index.html`);
});

module.exports = router;
