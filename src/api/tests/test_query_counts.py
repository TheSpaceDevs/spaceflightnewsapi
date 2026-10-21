"""Guards against N+1 queries on the list endpoints.
The number of queries should not grow with the number of related launches and events.
"""

from uuid import uuid4

import pytest
from django.test.client import Client

from api.models import Article, Author, Blog, Event, Launch, NewsSite, Provider, Socials

NUMBER_OF_ITEMS = 20

# count, items (+ news_site), launches (+ provider), events (+ provider), authors (+ socials)
MAX_LIST_QUERIES = 5


@pytest.fixture
def news_items_with_relations() -> None:
    news_site = NewsSite.objects.create(name="News Site")
    socials = Socials.objects.create(name="Author socials")
    author = Author.objects.create(name="Author", socials=socials)

    for model in (Article, Blog):
        for i in range(NUMBER_OF_ITEMS):
            # A new provider per relation makes sure every provider would be a separate query without prefetching.
            launch = Launch.objects.create(
                launch_id=uuid4(),
                name=f"Launch {i}",
                provider=Provider.objects.create(name=f"Launch provider {i}"),
            )
            event = Event.objects.create(
                event_id=i,
                name=f"Event {i}",
                provider=Provider.objects.create(name=f"Event provider {i}"),
            )
            item = model.objects.create(
                title=f"{model.__name__} {i}",
                summary=f"Summary {i}",
                url=f"https://example.com/{model.__name__}/{i}",
                image_url=f"https://example.com/{i}.png",
                news_site=news_site,
                published_at="2021-01-01T00:00:00Z",
            )
            item.launches.add(launch)
            item.events.add(event)
            item.authors.add(author)


@pytest.mark.django_db
@pytest.mark.usefixtures("news_items_with_relations")
class TestListQueryCounts:
    @pytest.mark.parametrize("endpoint", ["articles", "blogs"])
    def test_list_query_count_is_constant(self, client: Client, django_assert_max_num_queries, endpoint: str) -> None:
        with django_assert_max_num_queries(MAX_LIST_QUERIES):
            response = client.get(f"/v4/{endpoint}/?limit={NUMBER_OF_ITEMS}")

        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == NUMBER_OF_ITEMS
        assert all(launch["provider"].startswith("Launch provider") for r in results for launch in r["launches"])
        assert all(event["provider"].startswith("Event provider") for r in results for event in r["events"])

    @pytest.mark.parametrize("field", ["allArticles", "allBlogs"])
    def test_graphql_query_count_is_constant(self, client: Client, django_assert_max_num_queries, field: str) -> None:
        query = (
            f"{{ {field}(first: {NUMBER_OF_ITEMS}) {{ edges {{ node {{ title "
            "launches { edges { node { launchId } } } "
            "events { edges { node { eventId } } } "
            "} } } }"
        )

        with django_assert_max_num_queries(MAX_LIST_QUERIES):
            response = client.post("/v4/graphql/", {"query": query}, content_type="application/json")

        assert response.status_code == 200
        body = response.json()
        assert "errors" not in body
        assert len(body["data"][field]["edges"]) == NUMBER_OF_ITEMS
