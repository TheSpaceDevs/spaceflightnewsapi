'use strict';

/**
 * Read the documentation (https://strapi.io/documentation/developer-docs/latest/development/backend-customization.html#core-controllers)
 * to customize this controller
 */

module.exports = {
  async find(ctx) {
    let entities;
    if (ctx.query._q) {
      entities = await strapi.services.report.search(ctx.query);
    } else {
      entities = await strapi.services.report.find({
        ...ctx.query,
        _limit: ctx.query._limit || 10,
        _sort: ctx.query._sort || "publishedAt:DESC",
      }, ['newsSite']);
    }

    return entities.map(entity => strapi.services.utils.sanitizeEntity(entity));
  },

  async findOne(ctx) {
    const { id } = ctx.params;

    const entity = await strapi.services.report.findOne({ id }, ['newsSite']);
    return strapi.services.utils.sanitizeEntity(entity);
  },
};
