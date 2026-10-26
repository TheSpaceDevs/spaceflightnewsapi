"""Tests the admin pages that have custom behaviour."""

from typing import Any
from uuid import uuid4

import pytest
from django.db import connection
from django.test.client import Client
from django.test.utils import CaptureQueriesContext

from api.models import Article, Author, Blog, Event, Launch, NewsSite, Provider

FILTERS = ["launches", "events", "authors"]


@pytest.fixture
def related_items() -> dict[str, list]:
    """Two news items per model, each linked to its own launch, event and author."""
    provider = Provider.objects.create(name="Launch Library 2")
    news_site = NewsSite.objects.create(name="News Site")
    related: dict[str, list] = {"launches": [], "events": [], "authors": [], "articles": [], "blogs": []}

    for i in range(2):
        related["launches"].append(Launch.objects.create(launch_id=uuid4(), name=f"Launch {i}", provider=provider))
        related["events"].append(Event.objects.create(event_id=i, name=f"Event {i}", provider=provider))
        related["authors"].append(Author.objects.create(name=f"Author {i}"))

    for model, key in ((Article, "articles"), (Blog, "blogs")):
        for i in range(2):
            item = model.objects.create(
                title=f"{model.__name__} {i}",
                summary=f"Summary {i}",
                url=f"https://example.com/{key}/{i}",
                image_url=f"https://example.com/{i}.png",
                news_site=news_site,
                published_at="2021-01-01T00:00:00Z",
            )
            item.launches.add(related["launches"][i])
            item.events.add(related["events"][i])
            item.authors.add(related["authors"][i])
            related[key].append(item)

    return related


@pytest.mark.django_db
class TestNewsItemAdminFilters:
    @pytest.mark.parametrize("model", ["article", "blog"])
    @pytest.mark.parametrize("relation", FILTERS)
    def test_filter_on_related_item(
        self, admin_client: Client, related_items: dict[str, list], model: str, relation: str
    ) -> None:
        selected = related_items[relation][1]

        response = admin_client.get(f"/admin/api/{model}/", {f"{relation}__id__exact": selected.pk})

        assert response.status_code == 200
        assert list(response.context["cl"].result_list) == [related_items[f"{model}s"][1]]
        # The selected item is shown as the filter's current choice.
        assert str(selected) in response.content.decode()


def _create_news_items(model: type[Article] | type[Blog], count: int, author_name: str = "Author") -> None:
    """Creates news items that each have their own launch, event and two authors."""
    provider, _ = Provider.objects.get_or_create(name="Launch Library 2")
    news_site, _ = NewsSite.objects.get_or_create(name="News Site")
    start = model.objects.count()

    for i in range(start, start + count):
        item = model.objects.create(
            title=f"{model.__name__} {i}",
            summary=f"Summary {i}",
            url=f"https://example.com/{model.__name__}/{i}",
            image_url=f"https://example.com/{i}.png",
            news_site=news_site,
            published_at="2021-01-01T00:00:00Z",
        )
        item.launches.add(Launch.objects.create(launch_id=uuid4(), name=f"Launch {i}", provider=provider))
        item.events.add(
            Event.objects.create(event_id=1000 * len(model.__name__) + i, name=f"Event {i}", provider=provider)
        )
        item.authors.add(Author.objects.create(name=f"{author_name} {i}"), Author.objects.create(name=f"Co-author {i}"))


@pytest.mark.django_db
@pytest.mark.parametrize("model", [Article, Blog])
class TestNewsItemAdminChangelist:
    def test_query_count_does_not_grow_with_rows(
        self, admin_client: Client, django_assert_num_queries: Any, model: type[Article] | type[Blog]
    ) -> None:
        url = f"/admin/api/{model._meta.model_name}/"
        _create_news_items(model, 2)
        with CaptureQueriesContext(connection) as few:
            assert admin_client.get(url).status_code == 200

        _create_news_items(model, 20)
        with django_assert_num_queries(len(few.captured_queries)):
            assert admin_client.get(url).status_code == 200

    def test_author_names_are_escaped(self, admin_client: Client, model: type[Article] | type[Blog]) -> None:
        _create_news_items(model, 1, author_name="<script>alert(1)</script>")

        content = admin_client.get(f"/admin/api/{model._meta.model_name}/").content.decode()

        assert "<script>alert(1)</script>" not in content
        assert "&lt;script&gt;alert(1)&lt;/script&gt; 0" in content
