'use strict';

/**
 * `utils` service.
 */

module.exports = {
  sanitizeArticleBlog: (item => {
    return {
      id: item.id,
      title: item.title,
      url: item.url,
      imageUrl: item.imageUrl,
      newsSite: item.newsSite.name,
      summary: item.summary,
      publishedAt: item.publishedAt,
      updatedAt: item.updatedAt,
      featured: item.featured,
      launches: item.launches.map(launch => {
        return {
          id: launch.launchId,
          provider: launch.provider.name
        }
      }),
      events: item.events.map(event => {
        return {
          id: event.eventId,
          provider: event.provider.name
        }
      }),
    };
  })
};
