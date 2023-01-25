"""
Tasks to support the migration of old content into this Django project.
"""
import math
from typing import List

import httpx
from celery import shared_task

from api.models import Article as ArticleModel
from api.models import Event, Launch, NewsSite
from api.types import Article


@shared_task
def migrate_articles():
    count = httpx.get("https://api.spaceflightnewsapi.net/v3/articles/count").json()

    limit = 1000
    pages = math.ceil(count / limit)
    offset = 0

    # We add 1 since range is pages - 1 by default.
    for page in range(1, pages + 1):
        response = httpx.get(
            f"https://api.spaceflightnewsapi.net/v3/articles?_limit={limit}&_start={offset}"
        ).json()

        for article in response:
            process_articles.delay(article)

        offset = offset + 1000


@shared_task
def process_articles(data):
    article = Article(**data)

    launches: List[Launch] = []
    if len(article.launches) > 0:
        for launch in article.launches:
            result = Launch.objects.get(launch_id=launch.id)
            launches.append(result)

    events: List[Event] = []
    if len(article.events) > 0:
        for event in article.events:
            result = Event.objects.get(event_id=event.id)
            events.append(result)

    processed_article = ArticleModel.objects.update_or_create(
        title=article.title,
        url=article.url,
        image_url=article.imageUrl,
        news_site=NewsSite.objects.get(name=article.newsSite),
        summary=article.summary,
        published_at=article.publishedAt,
        updated_at=article.updatedAt,
        featured=article.featured,
    )

    # Update_or_create returns a tuple with the object and a boolean (indicating whether it's a new object.
    # We only need the object.
    processed_article[0].launches.set(launches)
    processed_article[0].events.set(events)


@shared_task
def migrate_news_sites():
    response = httpx.get("https://api.spaceflightnewsapi.net/v3/info").json()

    for site in response["newsSites"]:
        new_site_entry = NewsSite(name=site)
        new_site_entry.save()
