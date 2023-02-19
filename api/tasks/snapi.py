"""
Tasks to support the migration of old content into this Django project.
"""
import math
from typing import List

import django.db
import httpx
import rest_framework.exceptions
from celery import shared_task

from api.models import Article, Event, Launch, NewsSite
from api.models import Report as ReportModel
from api.serializers.v3 import ArticleV3Serializer
from api.types import Report

client_options = {"base_url": "https://api.spaceflightnewsapi.net/v3"}


@shared_task(name="Sync Articles")
def sync_articles():
    with httpx.Client(**client_options) as client:
        count = client.get(url="/articles/count").json()

        limit = 1000
        pages = math.ceil(count / limit)
        offset = 0

        # We add 1 since range is pages - 1 by default.
        for page in range(1, pages + 1):
            params = {"_limit": limit, "_start": offset}
            response = client.get(url="/articles", params=params).json()

            articles: List[Article] = []
            for article in response:
                try:
                    serializer = ArticleV3Serializer(data=article)
                    serializer.is_valid(raise_exception=True)
                    articles.append(serializer.save())

                    Article.objects.bulk_create(articles)
                except rest_framework.exceptions.ValidationError as e:
                    print(f"Error with article: {article}", e)
                except django.db.utils.IntegrityError as e:
                    print(f"Error with article: {article}", e)
                except Launch.DoesNotExist as e:
                    print(f"Error with article: {article}", e)
                except Event.DoesNotExist as e:
                    print(f"Error with article: {article}", e)
                except django.db.utils.DataError as e:
                    print(f"Error with article: {article}", e)

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
