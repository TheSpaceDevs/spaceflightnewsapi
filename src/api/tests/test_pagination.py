"""Tests the list endpoints' pagination: the cached count and the maximum offset."""

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


@pytest.mark.django_db
class TestMaxOffset:
    @pytest.fixture(autouse=True)
    def small_max_offset(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(CustomLimitOffsetPagination, "max_offset", 20)

    def test_max_offset_is_allowed(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?limit=5&offset=20")

        assert response.status_code == 200
        assert len(response.json()["results"]) == 5

    @pytest.mark.parametrize("endpoint", ["articles", "blogs", "reports"])
    def test_larger_offset_is_rejected(self, client: Client, endpoint: str) -> None:
        response = client.get(f"/v4/{endpoint}/?offset=21")

        assert response.status_code == 400
        assert "published_at_lt" in response.json()["offset"][0]

    def test_next_link_stops_at_max_offset(self, client: Client, articles: list[Article]) -> None:
        assert client.get("/v4/articles/?limit=5&offset=15").json()["next"].endswith("offset=20")
        assert client.get("/v4/articles/?limit=5&offset=20").json()["next"] is None

    def test_count_is_unchanged(self, client: Client, articles: list[Article]) -> None:
        # The count still reflects all results, also those beyond the maximum offset.
        assert client.get("/v4/articles/?limit=5&offset=20").json()["count"] > 25
