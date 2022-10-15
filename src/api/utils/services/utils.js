'use strict';

/**
 * utils service.
 */

module.exports = () => ({
  sanitizeEntity(item) {
    console.log(item)
    const sanitizedItem = {
      id: item.id,
      title: item.title,
      url: item.url,
      imageUrl: item.imageUrl,
      newsSite: item.news_site.name,
      summary: item.summary,
      publishedAt: item.published,
      updatedAt: item.updatedAt,
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
  }
});
