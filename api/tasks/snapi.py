"""
Tasks to support the migration of old content into this Django project.
"""
import math

import httpx
from celery import shared_task

from api.models import NewsSite
from api.serializers.v3 import ArticleV3Serializer, BlogV3Serializer, ReportV3Serializer

client_options = {"base_url": "https://api.spaceflightnewsapi.net/v3"}


@shared_task(name="Sync Articles")
def sync_articles() -> None:
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
                v3_article = ArticleV3Serializer(data=article)
                v3_article.is_valid(raise_exception=True)

                v3_article.save()

            offset = offset + 1000


@shared_task(name="Sync Blogs")
def sync_blogs() -> None:
    with httpx.Client(**client_options) as client:
        count = client.get(url="/blogs/count").json()

        limit = 1000
        pages = math.ceil(count / limit)
        offset = 0

        # We add 1 since range is pages - 1 by default.
        for page in range(1, pages + 1):
            params = {"_limit": limit, "_start": offset}
            response = client.get(url="/blogs", params=params).json()

            for blog in response:
                v3_blog = BlogV3Serializer(data=blog)
                v3_blog.is_valid(raise_exception=True)

                v3_blog.save()

            offset = offset + 1000


@shared_task(name="Sync News Sites")
def sync_news_sites() -> None:
    with httpx.Client(**client_options) as client:
        response = client.get(url="/info").json()

        for site in response["newsSites"]:
            NewsSite.objects.update_or_create(name=site)


# Task to migrate reports. It's not that much, so we do everything in a single task.
@shared_task(name="Sync Reports")
def sync_reports() -> None:
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
                report = ReportV3Serializer(data=data)
                report.is_valid(raise_exception=True)
                report.save()

            offset = offset + 1000
