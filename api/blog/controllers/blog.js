'use strict';
const {validate: uuidValidate} = require('uuid')

/**
 * Read the documentation (https://strapi.io/documentation/developer-docs/latest/development/backend-customization.html#core-controllers)
 * to customize this controller
 */

module.exports = {
  async find(ctx) {
    let entities;
    if (ctx.query._q) {
      entities = await strapi.services.blog.search(ctx.query);
    } else {
      try {
        entities = await strapi.services.blog.find({
          ...ctx.query,
          _limit: ctx.query._limit || 10,
          _sort: ctx.query._sort || "publishedAt:DESC",
        }, ['newsSite', 'launches.provider', 'events.provider']);
      } catch (e) {
        console.log(e.code)
        if (e.code === '22P02' || e.code === '42703' || e.status === 400 || e.code === '42703') {
          ctx.throw(400, 'Bad Request - please take a look at your query params')
        } else {
          strapi.log.error("Something went wrong:", e)
          ctx.throw(500)
        }
      }
    }

    return entities.map(entity => strapi.services.utils.sanitizeEntity(entity));
  },

  async findOne(ctx) {
    const { id } = ctx.params;

    const entity = await strapi.services.blog.findOne({ id }, ['newsSite', 'launches.provider', 'events.provider']);
    return strapi.services.utils.sanitizeEntity(entity);
  },

  async findPerLaunch(ctx) {
    const launchId = ctx.params.id;

    // Check if the id is a uuid, as used in LL2 for launches
    const validId = uuidValidate(launchId)
    if (!validId) {
      ctx.throw(400, 'not a valid uuid')
    }

    const entities = await strapi.query('blog').find({ 'launches.launchId': launchId }, ['newsSite', 'launches.provider', 'events.provider']);

    return entities.map(entity => strapi.services.utils.sanitizeEntity(entity));
  },

  async findPerEvent(ctx) {
    const eventId = ctx.params.id;

    // Check if the id is an int, as used as id's in LL2 for events
    // Since the id comes in as a string and I don't want to cast it to an id yet, use regex to test
    if (!eventId.match(/^\d+$/)) {
      ctx.throw(400, 'not a valid id - should be an integer')
    }

    const entities = await strapi.query('blog').find({ 'events.eventId': eventId }, ['newsSite', 'launches.provider', 'events.provider']);

    return entities.map(entity => strapi.services.utils.sanitizeEntity(entity));
  }
};
