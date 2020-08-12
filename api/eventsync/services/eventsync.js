'use strict';

/**
 * `eventsync` service.
 */

module.exports = {
  syncLl2Events: async () => {
    // Get the Upcoming launches
    const upcomgingEventResult = await axios.get('https://lldev.thespacedevs.com/2.0.0/event/upcoming/?limit=100')
    upcomgingEventResult.data.results.forEach(async event => {
      await strapi.query('event').model.findOneAndUpdate({eventId: event.id}, {
        name: event.name,
        eventId: event.id,
        eventProvider: '5f29a7834ebcc784f56e4f2c'
      }, {upsert: true});
    })

    // Get the previous launches
    const previousEventResult = await axios.get('https://lldev.thespacedevs.com/2.0.0/event/previous/?limit=100')
    previousEventResult.data.results.forEach(async event => {
      await strapi.query('event').model.findOneAndUpdate({eventId: event.id}, {
        name: event.name,
        eventId: event.id,
        eventProvider: '5f29a7834ebcc784f56e4f2c'
      }, {upsert: true});
    })
  }
};
