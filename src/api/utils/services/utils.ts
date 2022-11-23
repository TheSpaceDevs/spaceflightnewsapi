/**
 * utils service
 */

export default () => ({
  articleSerializer(item) {
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
      launches: item.launches,
      events: item.events
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
