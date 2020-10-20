'use strict';
const axios = require('axios')

/**
 * `eventsync` service.
 */

let config = {
  headers: {
    Authorization: `Token ${process.env.LL_TOKEN}`
  }
}

module.exports = {
  syncLl2Events: async () => {
    console.log("getting upcoming events")
    try {
      const upcomgingEventResult = await axios.get('https://ll.thespacedevs.com/2.0.0/event/upcoming/?limit=100', config)
      upcomgingEventResult.data.results.forEach(async event => {
        await strapi.query('event').model.findOneAndUpdate({eventId: event.id}, {
          name: event.name,
          eventId: event.id,
          provider: '5f34e4055379f026924c61cf'
        }, {upsert: true});
      })
    } catch (e) {
      console.error(`getting upcoming events failed with status: ${e.response.status}`)
    }


    console.log("getting previous events")
    try {
      const previousEventResult = await axios.get('https://ll.thespacedevs.com/2.0.0/event/previous/?limit=100', config)
      previousEventResult.data.results.forEach(async event => {
        await strapi.query('event').model.findOneAndUpdate({eventId: event.id}, {
          name: event.name,
          eventId: event.id,
          provider: '5f34e4055379f026924c61cf'
        }, {upsert: true});
      })
    } catch (e) {
      console.error(`getting previous events failed with status: ${e.response.status}`)
    }
  }
};
