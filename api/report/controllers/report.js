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
      try {
        entities = await strapi.services.report.find({
          ...ctx.query,
          _limit: ctx.query._limit || 10,
          _sort: ctx.query._sort || "publishedAt:DESC",
        }, ['newsSite']);
      } catch (e) {
        if (e.code === '22P02' || e.code === '42703' || e.status === 400) {
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

    const entity = await strapi.services.report.findOne({ id }, ['newsSite']);
    if (!entity) {
      ctx.throw(404, "Not Found, please take a look at your query params")
    }

    return strapi.services.utils.sanitizeEntity(entity);
  },
};
