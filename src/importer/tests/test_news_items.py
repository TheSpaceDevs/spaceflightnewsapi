"""Tests importing news items from the harvester's sources."""

from collections.abc import Iterator
from datetime import UTC, datetime
from typing import Any

import pytest
from harvester.schemas import ArticleSchema
from harvester.schemas.results import HarvestResultSchema

from api.models import Article, NewsSite
from importer.management.commands import _news_items
from importer.management.commands._news_items import fetch_news

# Like SpaceDaily's feed: whole sentences as titles, and URLs built from them.
LONG_TITLE = "A" * 283
LONG_URL = "https://spacedaily.com/" + "b" * 200 + "/"


class FakeSource:
    def __init__(self, articles: list[ArticleSchema]) -> None:
        self.articles = articles

    def harvest(self) -> HarvestResultSchema:
        return HarvestResultSchema(articles=self.articles)


@pytest.fixture
def news_site() -> Iterator[NewsSite]:
    # The importer caches news sites and authors per process; the database is rolled back after each test.
    _news_items._get_news_site.cache_clear()
    _news_items._get_author.cache_clear()
    yield NewsSite.objects.create(name="SpaceDaily")
    _news_items._get_news_site.cache_clear()
    _news_items._get_author.cache_clear()


def _article(news_site: NewsSite, title: str, url: str) -> ArticleSchema:
    return ArticleSchema(
        title=title,
        summary="A summary.",
        url=url,  # type: ignore[arg-type]
        news_site_id=news_site.pk,
        published_at=datetime(2026, 10, 27, 10, tzinfo=UTC),
        author="Space Daily Editorial Team",
        image_url="https://spacedaily.com/image.jpg",  # type: ignore[arg-type]
    )


@pytest.mark.django_db
class TestFetchNews:
    def test_long_titles_and_urls_are_imported(self, news_site: NewsSite, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(_news_items, "sources", [FakeSource([_article(news_site, LONG_TITLE, LONG_URL)])])

        fetch_news()

        article = Article.objects.get()
        assert article.title == LONG_TITLE
        assert article.url == LONG_URL

    def test_a_failing_item_does_not_stop_the_others(
        self, news_site: NewsSite, monkeypatch: pytest.MonkeyPatch, caplog: Any
    ) -> None:
        too_long = _article(news_site, "B" * 600, "https://spacedaily.com/too-long/")
        articles = [
            _article(news_site, "First", "https://spacedaily.com/first/"),
            too_long,
            _article(news_site, "Last", "https://spacedaily.com/last/"),
        ]
        monkeypatch.setattr(_news_items, "sources", [FakeSource(articles)])

        fetch_news()

        assert set(Article.objects.values_list("title", flat=True)) == {"First", "Last"}
        # Logged as an error, which Sentry reports, with the item that failed.
        errors = [record for record in caplog.records if record.levelname == "ERROR"]
        assert len(errors) == 1
        assert "https://spacedaily.com/too-long/" in errors[0].getMessage()
