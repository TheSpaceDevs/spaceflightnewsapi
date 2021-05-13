'use strict';

/**
 * `utils` service.
 */

module.exports = {
  sanitizeEntity: (item => {
    const sanitizedItem = {
      id: item.id,
      title: item.title,
      url: item.url,
      imageUrl: item.imageUrl,
      newsSite: item.newsSite.name,
      summary: item.summary,
      publishedAt: item.publishedAt,
      updatedAt: item.updatedAt,
      featured: item.featured,
    };

    if (item.launches) {
      sanitizedItem.launches = item.launches.map(launch => {
        return {
          id: launch.launchId,
          provider: launch.provider.name
        }
      })
    }

    if (item.events) {
      sanitizedItem.events = item.events.map(event => {
        return {
          id: event.eventId,
          provider: event.provider.name
        }
      })
    }

    return sanitizedItem;
  }),
  saveLaunch: async (launch) => {
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
      console.error(`error while saving launch: ${launch.name}`, e)
    }
  },
  saveEvent: async (event) => {
    try {
      const exists = await strapi.query('event').findOne({eventId: event.id})
      if (exists) {
        return strapi.query('event').update({eventId: event.id}, {
          name: event.name,
          eventId: event.id,
          provider: 1
        });
      } else {
        return strapi.query('event').create({
          name: event.name,
          eventId: event.id,
          provider: 1
        });
      }
    } catch (e) {
      console.error(`error while saving event: ${event.name}`, e)
    }
  }
};
