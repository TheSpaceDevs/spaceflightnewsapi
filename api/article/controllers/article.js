"use strict";
const NodeCache = require("node-cache");

const cache = new NodeCache({
  stdTTL: 1800,
});

/**
 * Read the documentation (https://strapi.io/documentation/v3.x/concepts/controllers.html#core-controllers)
 * to customize this controller
 */

module.exports = {
  /**
   * Create a record.
   *
   * @return {Object}
   */

  async create(ctx) {
    let entity;
    try {
      entity = await strapi.services.article.create(ctx.request.body);
    } catch (e) {
      // Update an existing one with update values. Only if from the same news site.
      const dup = await strapi.services.article.findOne(e.keyValue);
      if (ctx.request.body.newsSite === String(dup.newsSite._id)) {
        try {
          entity = await strapi.services.article.update(
            { _id: dup._id },
            ctx.request.body
          );
        } catch (e) {
          console.error(e);
        }
      } else {
        ctx.throw(409);
      }
    }
    ctx.response.status = 201;
    return entity;
  },

  /**
   * Retrieve a record.
   *
   * @return {Object}
   */

  async findOne(ctx) {
    const { id } = ctx.params;

    if (id === "launch") {
      ctx.throw(404);
    }

    let entity = await strapi.services.article.findOne({ id });

    // Create the launch and event objects
    // Using Promise.all since it's an async map (async to wait for the result)
    const launches = await Promise.all(
      entity.launches.map(async (launch) => {
        const lp = await strapi.services.provider.findOne({
          _id: launch.provider,
        });
        return { id: launch.launchId, provider: lp.name };
      })
    );

    const events = await Promise.all(
      entity.events.map(async (event) => {
        const ep = await strapi.services.provider.findOne({
          _id: event.provider,
        });
        return { id: event.eventId, provider: ep.name };
      })
    );

    // Finally, return the response
    return (entity = {
      title: entity.title,
      url: entity.url,
      imageUrl: entity.imageUrl,
      newsSite: entity.newsSite.name,
      summary: entity.summary,
      publishedAt: entity.publishedAt,
      updatedAt: entity.updatedAt,
      featured: entity.featured,
      launches: launches,
      events: events,
    });
  },

  /**
   * Retrieve records.
   *
   * @return {Array}
   */

  async find(ctx) {
    let entities;
    if (ctx.query._q) {
      // search for an article if a search query was given
      entities = await strapi.services.article.search(ctx.query);
    } else {
      // just find everything
      entities = await strapi.services.article.find({
        ...ctx.query,
        _limit: ctx.query._limit || 10,
        _sort: ctx.query._sort || "publishedAt:DESC",
      });
    }

    // Build the response we want to return
    // Use Promise.all to since it's an async map (async for the inner Promise)
    entities = await Promise.all(
      entities.map(async (entity) => {
        // Create the launch and event objects
        // Using Promise.all since it's an async map (async to wait for the result)
        const launches = await Promise.all(
          entity.launches.map(async (launch) => {
            const lp = await strapi.services.provider.findOne({
              _id: launch.provider,
            });
            return { id: launch.launchId, provider: lp.name };
          })
        );

        const events = await Promise.all(
          entity.events.map(async (event) => {
            const ep = await strapi.services.provider.findOne({
              _id: event.provider,
            });
            return { id: event.eventId, provider: ep.name };
          })
        );

        return {
          id: entity._id,
          title: entity.title,
          url: entity.url,
          imageUrl: entity.imageUrl,
          newsSite: entity.newsSite.name,
          summary: entity.summary,
          publishedAt: entity.publishedAt,
          updatedAt: entity.updatedAt,
          featured: entity.featured,
          launches: launches,
          events: events,
        };
      })
    );

    // Finally, return the response
    return entities;
  },

  findPerLaunch: async (ctx) => {
    const launchId = ctx.params.id;
    let entities;

    const cachedLaunch = cache.get(launchId);

    // Check if we have the launch in-memory and return it
    if (cachedLaunch !== undefined) {
      if (cachedLaunch.length === 0) {
        return ctx.notFound();
      }
      return cachedLaunch;
    }

    entities = await strapi.services.article.find({
      "launches.launchId": launchId,
    });

    // The above query will always return. Handle empty array as 404
    if (entities.length === 0) {
      cache.set(launchId, entities, 3600);
      return ctx.notFound();
    }

    // Build the response we want to return
    // Use Promise.all to since it's an async map (async for the inner Promise)
    entities = await Promise.all(
      entities.map(async (entity) => {
        // Create the launch and event objects
        // Using Promise.all since it's an async map (async to wait for the result)
        const launches = await Promise.all(
          entity.launches.map(async (launch) => {
            const lp = await strapi.services.provider.findOne({
              _id: launch.provider,
            });
            return { id: launch.launchId, provider: lp.name };
          })
        );

        const events = await Promise.all(
          entity.events.map(async (event) => {
            const ep = await strapi.services.provider.findOne({
              _id: event.provider,
            });
            return { id: event.eventId, provider: ep.name };
          })
        );

        return {
          id: entity._id,
          title: entity.title,
          url: entity.url,
          imageUrl: entity.imageUrl,
          newsSite: entity.newsSite.name,
          summary: entity.summary,
          publishedAt: entity.publishedAt,
          updatedAt: entity.updatedAt,
          featured: entity.featured,
          launches: launches,
          events: events,
        };
      })
    );

    // Set it in cache
    cache.set(launchId, entities, 3600);

    // Finally, return the response
    return entities;
  },
};
