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

    let entity = await strapi.services.blog.findOne({ id });

    // Create the launch object
    // Using Promise.all since it's an async map (async to wait for the result)
    const launches = await Promise.all(entity.launches.map(async launch => {
      const lp = await strapi.services['launch-providers'].findOne({_id: launch.launchProvider})
      return {id: launch.launchId, provider: lp.name}
    }))

    // Finally, return the response
    return entity = {
      title: entity.title,
      url: entity.url,
      imageUrl: entity.imageUrl,
      newsSite: entity.newsSite.name,
      summary: entity.summary,
      publishedAt: entity.publishedAt,
      updatedAt: entity.updatedAt,
      launches: launches
    }
  },

  /**
   * Retrieve records.
   *
   * @return {Array}
   */

  async find(ctx) {
    let entities;
    if (ctx.query._q) { // search for an blog if a search query was given
      entities = await strapi.services.blog.search(ctx.query);
    } else { // just find everything
      entities = await strapi.services.blog.find(ctx.query);
    }

    // Build the response we want to return
    entities = await Promise.all(entities.map(async entity => {
      // Create the launch object
      // Using Promise.all since it's an async map (async to wait for the result)
      const launches = await Promise.all(entity.launches.map(async launch => {
        const lp = await strapi.services['launch-providers'].findOne({_id: launch.launchProvider})
        return {id: launch.launchId, provider: lp.name}
      }))

      return {
        id: entity._id,
        title: entity.title,
        url: entity.url,
        imageUrl: entity.imageUrl,
        newsSite: entity.newsSite.name,
        summary: entity.summary,
        publishedAt: entity.publishedAt,
        updatedAt: entity.updatedAt,
        launches: launches
      }
    }))

    // Finally, return the response
    return entities
  }
};
