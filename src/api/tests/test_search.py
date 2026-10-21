"""Tests the `search` parameter shared by the articles, blogs and reports endpoints."""

import pytest
from django.test.client import Client

from api.models import Article, Blog, NewsSite, Report


@pytest.fixture
def searchable_items() -> None:
    nasa = NewsSite.objects.create(name="NASA")
    esa = NewsSite.objects.create(name="ESA")

    for model in (Article, Blog, Report):
        for i, (title, summary, news_site) in enumerate(
            [
                ("Starship flight test", "SpaceX launches Starship", esa),
                ("Artemis update", "A summary about the Moon", nasa),
                ("Crew rotation", "Starliner docks with the station", nasa),
                ("Deleted Starship item", "Should never show up", nasa),
            ]
        ):
            model.objects.create(
                title=title,
                summary=summary,
                url=f"https://example.com/{model.__name__}/{i}",
                image_url=f"https://example.com/{i}.png",
                news_site=news_site,
                published_at="2021-01-01T00:00:00Z",
                is_deleted=title.startswith("Deleted"),
            )


def _titles(client: Client, endpoint: str, search: str) -> set[str]:
    response = client.get(f"/v4/{endpoint}/", {"search": search})
    assert response.status_code == 200
    return {item["title"] for item in response.json()["results"]}


@pytest.mark.django_db
@pytest.mark.usefixtures("searchable_items")
@pytest.mark.parametrize("endpoint", ["articles", "blogs", "reports"])
class TestSearch:
    def test_matches_title_case_insensitive(self, client: Client, endpoint: str) -> None:
        assert _titles(client, endpoint, "starship") == {"Starship flight test"}

    def test_matches_summary(self, client: Client, endpoint: str) -> None:
        assert _titles(client, endpoint, "moon") == {"Artemis update"}

    def test_matches_news_site_name(self, client: Client, endpoint: str) -> None:
        assert _titles(client, endpoint, "nas") == {"Artemis update", "Crew rotation"}

    def test_matches_news_site_only(self, client: Client, endpoint: str) -> None:
        # "esa" only appears in a news site name, never in a title or summary.
        assert _titles(client, endpoint, "esa") == {"Starship flight test"}

    def test_all_terms_must_match(self, client: Client, endpoint: str) -> None:
        assert _titles(client, endpoint, "starliner nasa") == {"Crew rotation"}
        assert _titles(client, endpoint, "starliner esa") == set()

    def test_no_match(self, client: Client, endpoint: str) -> None:
        assert _titles(client, endpoint, "xyzzy") == set()
