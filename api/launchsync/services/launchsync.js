'use strict';
const axios = require('axios');

/**
 * `launchsync` service.
 */

module.exports = {
  syncLL2: async () => {
    const launchResults = await axios.get('https://lldev.thespacedevs.com/2.0.0/launch/upcoming/')
    launchResults.data.results.forEach(launch => {
      strapi.query('launches').create({
        name: launch.name,
        launchId: launch.id,
        launchProvider: '5f29a7834ebcc784f56e4f2c'
      })
    })
  }
};
