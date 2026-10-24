"""Tests the admin pages that have custom behaviour."""

from uuid import uuid4

import pytest
from django.test.client import Client

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
