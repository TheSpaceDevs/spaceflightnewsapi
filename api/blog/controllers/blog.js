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
    const {id} = ctx.params;

    let entity = await strapi.services.blog.findOne({id});

    // Create the launch and event objects
    // Using Promise.all since it's an async map (async to wait for the result)
    const launches = await Promise.all(entity.launches.map(async launch => {
      const lp = await strapi.services.provider.findOne({_id: launch.provider})
      return {id: launch.launchId, provider: lp.name}
    }))

    const events = await Promise.all(entity.events.map(async event => {
      const ep = await strapi.services.provider.findOne({_id: event.provider})
      return {id: event.eventId, provider: ep.name}
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
      launches: launches,
      events: events
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
      entities = await strapi.services.blog.find({
        ...ctx.query,
        _limit: ctx.query._limit || 10,
        _sort: ctx.query._sort || 'publishedAt:DESC'
      });
    }

    // Build the response we want to return
    entities = await Promise.all(entities.map(async entity => {
      // Create the launch and event objects
      // Using Promise.all since it's an async map (async to wait for the result)
      const launches = await Promise.all(entity.launches.map(async launch => {
        const lp = await strapi.services.provider.findOne({_id: launch.provider})
        return {id: launch.launchId, provider: lp.name}
      }))

      const events = await Promise.all(entity.events.map(async event => {
        const ep = await strapi.services.provider.findOne({_id: event.provider})
        return {id: event.eventId, provider: ep.name}
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
        launches: launches,
        events: events
      }
    }))

    // Finally, return the response
    return entities
  }
};
