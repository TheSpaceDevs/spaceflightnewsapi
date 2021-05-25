'use strict';

/**
 * `utils` service.
 */

module.exports = {
  sanitizeEntity: (item => {
    console.log(item)
    const sanitizedItem = {
      id: item.id,
      title: item.title,
      url: item.url,
      imageUrl: item.imageUrl,
      newsSite: item.newsSite.name,
      summary: item.summary,
      publishedAt: item.publishedAt,
      updatedAt: item.updated_at,
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
      strapi.log.error(`error while saving launch: ${launch.name}`, e)
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
      strapi.log.error(`error while saving event: ${event.name}`, e)
    }
  },
  saveMessage: (async (msg, channel) => {
    const message = JSON.parse(msg.content.toString())
    try {
      strapi.log.info(`saving ${message.type} from mq: ${message.data.title}`);
      await strapi.services[message.type].create(message.data);
      await channel.ack(msg);
    } catch (e) {
      // Update an existing one with updated values. Only if from the same news site.
      // URL is mostly consistent, so using that to get the duplicate one.
      const dup = await strapi.services[message.type].findOne({url: message.data.url});
      if (message.data.newsSite === dup.newsSite.id) {
        try {
          strapi.log.info(
            `duplicate ${message.type} from mq: ${dup.id} - updating instead...`
          );
          await strapi.services[message.type].update(
            { id: dup.id },
            message.data
          );
          await channel.ack(msg);
        } catch (e) {
          strapi.log.error(`error updating ${message.type}`, e);
        }
      } else {
        // when there's a duplicate, but from another website
        strapi.log.error(
          `duplicate from another site found: ${message.data.title} ${dup.newsSite.name}`
        );
        await channel.ack(msg);
      }
    }
  })
};
