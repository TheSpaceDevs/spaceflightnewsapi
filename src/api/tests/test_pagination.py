"""Tests the cached count of the list endpoints' pagination."""

import pytest
from django.db import connection
from django.test.client import Client
from django.test.utils import CaptureQueriesContext

from api.models import Article, NewsSite
from api.utils.pagination import CustomLimitOffsetPagination


def _count_queries(client: Client, url: str) -> tuple[int, int]:
    """Returns the response's count and the number of COUNT queries it took."""
    with CaptureQueriesContext(connection) as ctx:
        response = client.get(url)
    assert response.status_code == 200
    return response.json()["count"], sum("COUNT(*)" in q["sql"] for q in ctx.captured_queries)


@pytest.mark.django_db
class TestCachedCount:
    def test_count_is_reused_across_pages(self, client: Client, articles: list[Article]) -> None:
        count, queries = _count_queries(client, "/v4/articles/?limit=5&offset=0")
        assert queries == 1

        for offset in (5, 10, 15):
            assert _count_queries(client, f"/v4/articles/?limit=5&offset={offset}") == (count, 0)

    def test_count_ignores_ordering(self, client: Client, articles: list[Article]) -> None:
        count, _ = _count_queries(client, "/v4/articles/")
        assert _count_queries(client, "/v4/articles/?ordering=updated_at") == (count, 0)

    def test_count_is_per_filter(self, client: Client, articles: list[Article]) -> None:
        total, _ = _count_queries(client, "/v4/articles/")
        filtered, queries = _count_queries(client, "/v4/articles/?title_contains=specific")

        assert queries == 1
        assert filtered == 1
        assert total > filtered

    def test_count_is_per_endpoint(self, client: Client, articles: list[Article]) -> None:
        articles_count, _ = _count_queries(client, "/v4/articles/")
        blogs_count, queries = _count_queries(client, "/v4/blogs/")

        assert queries == 1
        assert blogs_count == 0
        assert articles_count > 0

    def test_empty_queryset(self) -> None:
        assert CustomLimitOffsetPagination().get_count(NewsSite.objects.none()) == 0

    def test_list(self) -> None:
        assert CustomLimitOffsetPagination().get_count([1, 2, 3]) == 3
