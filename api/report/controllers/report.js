'use strict';

/**
 * Read the documentation (https://strapi.io/documentation/v3.x/concepts/controllers.html#core-controllers)
 * to customize this controller
 */

module.exports = {
  /**
   * Retrieve a record.
   *
   * @return {Object}
   */

  async findOne(ctx) {
    const { id } = ctx.params;

    let entity = await strapi.services.report.findOne({ id });

    // Finally, return the response
    return entity = {
      title: entity.title,
      url: entity.url,
      imageUrl: entity.imageUrl,
      newsSite: entity.newsSite.name,
      summary: entity.summary,
      publishedAt: entity.publishedAt,
      updatedAt: entity.updatedAt
    }
  },

  /**
   * Retrieve records.
   *
   * @return {Array}
   */

  async find(ctx) {
    let entities;
    if (ctx.query._q) { // search for an report if a search query was given
      entities = await strapi.services.report.search(ctx.query);
    } else { // just find everything
      entities = await strapi.services.report.find({...ctx.query, _limit: ctx.query._limit || 10});
    }

    // Build the response we want to return
    entities = entities.map(entity => {
      return {
        id: entity._id,
        title: entity.title,
        url: entity.url,
        imageUrl: entity.imageUrl,
        newsSite: entity.newsSite.name,
        summary: entity.summary,
        publishedAt: entity.publishedAt,
        updatedAt: entity.updatedAt
      }
    })

    // Finally, return the response
    return entities
  }
};
