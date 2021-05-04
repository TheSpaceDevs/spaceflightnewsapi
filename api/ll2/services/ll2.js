'use strict';
const axios = require('axios')

/**
 * `ll2` service.
 */

let config = {
  headers: {
    Authorization: `Token ${process.env.LL_TOKEN}`,
    'User-Agent': 'SNAPI integration'
  }
}

const saveLaunch = async (launch) => {
  try {
    const exists = await strapi.query('launches').findOne({launchId: launch.id})
    if (exists) {
      return strapi.query('launches').update({launchId: launch.id}, {
        name: launch.name,
        launchId: launch.id,
        provider: 1
      });
    } else {
      return strapi.query('launches').create({
        name: launch.name,
        launchId: launch.id,
        provider: 1
      });
    }
  } catch (e) {
    console.error(`error while saving ${launch.name}`, e)
  }
}

const LL2URL = 'https://lldev.thespacedevs.com/2.2.0'

module.exports = {
  syncAllLaunches: async () => {
    let next = `${LL2URL}/launch?limit=100`;

    console.log("getting all launches");

    while (next) {
      const launches = await axios.get(next, config);

      for (const launch of launches.data.results) {
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
