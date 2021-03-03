'use strict';
const axios = require('axios');

/**
 * `launchsync` service.
 */

let config = {
  headers: {
    Authorization: `Token ${process.env.LL_TOKEN}`
  }
}

const saveLaunch = async (launch) => {
  return strapi.query('launches').model.findOneAndUpdate({launchId: launch.id}, {
    name: launch.name,
    launchId: launch.id,
    provider: '5f34e4055379f026924c61cf'
  }, {upsert: true});
}

module.exports = {
  syncLl2RecentUpcoming: async () => {
    console.log("getting upcoming launches")
    try {
      const upcomingLaunchResults = await axios.get('https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=100', config)
      for (const launch of upcomingLaunchResults['data']['results']) {
        try {
          await saveLaunch(launch)
        } catch (e) {
          console.error(e);
        }
      }
    } catch (e) {
      console.error(`getting upcoming launches failed with status: ${e.response.status}`)
    }

    console.log("getting previous launches")
    try {
      const previousLaunchResults = await axios.get('https://ll.thespacedevs.com/2.2.0/launch/previous/?limit=100', config)
      for (const launch of previousLaunchResults['data']['results']) {
        try {
          await saveLaunch(launch)
        } catch (e) {
          console.error(e);
        }
      }
    } catch (e) {
      console.error(`getting previous launches failed with status: ${e.response.status}`)
    }
  },

  syncLl2All: async (initialUrl) => {
    let next = initialUrl;

    console.log("getting all launches");

    while (next) {
      const launches = await axios.get(next, config);

      for (const launch of launches['data']['results']) {
        try {
          await saveLaunch(launch)
        } catch (e) {
          console.error(e);
        }
      }
      next = launches['data']['next'];
    }
  }
};
