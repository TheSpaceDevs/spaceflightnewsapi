'use strict';
const { sanitizeEntity } = require('strapi-utils');

/**
 * Read the documentation (https://strapi.io/documentation/developer-docs/latest/development/backend-customization.html#core-controllers)
 * to customize this controller
 */

module.exports = {
  async find(ctx) {
    let entities;
    if (ctx.query._q) {
      entities = await strapi.services.article.search(ctx.query);
    } else {
      entities = await strapi.services.article.find({
        ...ctx.query,
        _limit: ctx.query._limit || 10,
        _sort: ctx.query._sort || "publishedAt:DESC",
      }, ['newsSite', 'launches.provider', 'events.provider']);
    }

    return entities.map(entity => strapi.services.utils.sanitizeEntity(entity));
  },

  async findOne(ctx) {
    const { id } = ctx.params;

    const entity = await strapi.services.article.findOne({ id }, ['newsSite', 'launches.provider', 'events.provider']);
    return strapi.services.utils.sanitizeEntity(entity);
  },
};
