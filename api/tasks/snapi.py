"""
Tasks to support the migration of old content into this Django project.
"""
import math
from typing import List

import httpx
from celery import shared_task

from api.models import Article as ArticleModel
from api.models import Blog as BlogModel
from api.models import Event, Launch, NewsSite
from api.models import Report as ReportModel
from api.types import Article, Blog, Report

client_options = {"base_url": "https://api.spaceflightnewsapi.net/v3"}


@shared_task
def migrate_articles():
    with httpx.Client(**client_options) as client:
        count = client.get(url="/articles/count").json()

        limit = 1000
        pages = math.ceil(count / limit)
        offset = 0

        # We add 1 since range is pages - 1 by default.
        for page in range(1, pages + 1):
            params = {"_limit": limit, "_start": offset}
            response = client.get(url="/articles", params=params).json()

            for article in response:
                process_doc.delay(article, "article")

            offset = offset + 1000


@shared_task
def migrate_blogs():
    with httpx.Client(**client_options) as client:
        count = client.get(url="/blogs/count").json()

        limit = 1000
        pages = math.ceil(count / limit)
        offset = 0

        # We add 1 since range is pages - 1 by default.
        for page in range(1, pages + 1):
            params = {"_limit": limit, "_start": offset}
            response = client.get(url="/blogs", params=params).json()

            for article in response:
                process_doc.delay(article, "blog")

            offset = offset + 1000


@shared_task
def process_doc(data, type):
    # We need to check if we're saving an article or blog.
    if type == "article":
        doc = Article(**data)
        orm = ArticleModel
    elif type == "blog":
        doc = Blog(**data)
        orm = BlogModel
    else:
        raise Exception("Unknown type")

    launches: List[Launch] = []
    if len(doc.launches) > 0:
        for launch in doc.launches:
            result = Launch.objects.get(launch_id=launch.id)
            launches.append(result)

    events: List[Event] = []
    if len(doc.events) > 0:
        for event in doc.events:
            result = Event.objects.get(event_id=event.id)
            events.append(result)

    processed_doc = orm.objects.update_or_create(
        id=doc.id,
        title=doc.title,
        url=doc.url,
        image_url=doc.imageUrl,
        news_site=NewsSite.objects.get(name=doc.newsSite),
        summary=doc.summary,
        published_at=doc.publishedAt,
        updated_at=doc.updatedAt,
    )

    # Update_or_create returns a tuple with the object and a boolean (indicating whether it's a new object).
    # We only need the object.
    processed_doc[0].launches.set(launches)
    processed_doc[0].events.set(events)

    # Featured is not on the Blog type/model, so we add it later to only the articles.
    if type == "article":
        processed_doc[0].featured = doc.featured
        processed_doc[0].save()


@shared_task
def migrate_news_sites():
    with httpx.Client(**client_options) as client:
        response = client.get(url="/info").json()

        for site in response["newsSites"]:
            NewsSite.objects.update_or_create(name=site)


# Task to migrate reports. It's not that much, so we do everything in a single task.
@shared_task
def migrate_reports():
    with httpx.Client(**client_options) as client:
        count = client.get(url="/reports/count").json()

        limit = 1000
        pages = math.ceil(count / limit)
        offset = 0

        # We add 1 since range is (pages - 1) by default.
        for page in range(1, pages + 1):
            params = {"_limit": limit, "_start": offset}
            response = client.get(url="/reports", params=params).json()

            for data in response:
                report = Report(**data)
                ReportModel.objects.update_or_create(
                    id=report.id,
                    title=report.title,
                    url=report.url,
                    image_url=report.imageUrl,
                    news_site=NewsSite.objects.get(name=report.newsSite),
                    summary=report.summary,
                    published_at=report.publishedAt,
                    updated_at=report.updatedAt,
                )

            offset = offset + 1000
