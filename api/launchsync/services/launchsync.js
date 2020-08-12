'use strict';
const axios = require('axios');

/**
 * `launchsync` service.
 */

module.exports = {
  syncLl2Launches: async () => {
    // Get the Upcoming launches
    const upcomingLaunchResults = await axios.get('https://lldev.thespacedevs.com/2.0.0/launch/upcoming/?limit=100')
    upcomingLaunchResults.data.results.forEach(async launch => {
      await strapi.query('launches').model.findOneAndUpdate({launchId: launch.id}, {
        name: launch.name,
        launchId: launch.id,
        launchProvider: '5f29a7834ebcc784f56e4f2c'
      }, {upsert: true});
    })

    // Get the previous launches
    const previousLaunchResults = await axios.get('https://lldev.thespacedevs.com/2.0.0/launch/previous/?limit=100')
    previousLaunchResults.data.results.forEach(async launch => {
      await strapi.query('launches').model.findOneAndUpdate({launchId: launch.id}, {
        name: launch.name,
        launchId: launch.id,
        launchProvider: '5f29a7834ebcc784f56e4f2c'
      }, {upsert: true});
    })
  }
};
