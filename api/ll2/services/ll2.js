'use strict';
const axios = require('axios')

/**
 * `ll2` service.
 */

const LL_URL = strapi.config.get('server.ll_url')
const LL_TOKEN = strapi.config.get('server.ll_token')

let config = {
  headers: {
    Authorization: `Token ${LL_TOKEN}`,
    'User-Agent': 'SNAPI integration'
  }
}



module.exports = {
  syncAllLaunches: async () => {
    let next = `${LL_URL}/launch?limit=100`;

    console.log(`getting all launches from ${LL_URL}`);

    while (next) {
      try {
        const launches = await axios.get(next, config);

        for (const launch of launches.data.results) {
          try {
            await strapi.services.utils.saveLaunch(launch)
          } catch (e) {
            console.error(e);
          }
        }
        next = launches['data']['next'];
      } catch (e) {
        if (e.response) {
          if (e.response.status === 401) {
            return console.error('LL token not valid')
          }
        }
        console.error(e)
      }
    }
  },

  syncAllEvents: async () => {
    let next = `${LL_URL}/event?limit=100`;

    console.log(`getting all events from ${LL_URL}`);

    while (next) {
      try {
        const events = await axios.get(next, config);

        for (const event of events.data.results) {
          try {
            await strapi.services.utils.saveEvent(event)
          } catch (e) {
            console.error(e);
          }
        }
        next = events['data']['next'];
      } catch (e) {
        if (e.response) {
          if (e.response.status === 401) {
            return console.error('LL token not valid')
          }
        }
        console.error(e)
      }
    }
  }

};
