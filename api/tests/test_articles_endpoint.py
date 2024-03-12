"""This module tests both articles and the blogs endpoints.
Most code is shared between the two.
"""

import pytest
from django.test.client import Client

from api.models import Article, Event, Launch, NewsSite


@pytest.mark.django_db
class TestArticlesEndpoint:
    def test_get_articles(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/")
        assert response.status_code == 200

        data = response.json()

        assert all(article["title"] in [article.title for article in articles] for article in data["results"])
        assert all(
            article["news_site"] in [fixture_article.news_site.name for fixture_article in articles]
            for article in data["results"]
        )
        assert len(data["results"]) == 10

    def test_get_single_article(self, client: Client, articles: list[Article]) -> None:
        response = client.get(f"/v4/articles/{articles[0].id}/")
        assert response.status_code == 200

        data = response.json()

        assert data["title"] == articles[0].title
        assert data["news_site"] == articles[0].news_site.name

    def test_limit_articles(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?limit=5")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 5

    def test_get_all_articles_with_launches(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?has_launch=true")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 2

    def test_get_all_articles_with_events(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?has_event=true")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 2

    def test_get_articles_with_launch(self, client: Client, articles: list[Article], launches: list[Launch]) -> None:
        response = client.get(f"/v4/articles/?launch={launches[0].launch_id}")
        assert response.status_code == 200

        data = response.json()
        assert data["results"][0]["title"] == articles[100].title
        assert data["results"][0]["launches"][0]["launch_id"] == str(launches[0].launch_id)
        assert data["results"][0]["launches"][0]["provider"] == launches[0].provider.name
        assert len(data["results"]) == 1

    def test_get_articles_with_event(self, client: Client, articles: list[Article], events: list[Event]) -> None:
        article_with_event = [article for article in articles if article.title == "Article with Event 1"][0]
        response = client.get(f"/v4/articles/?event={events[0].event_id}")
        assert response.status_code == 200

        data = response.json()
        assert data["results"][0]["title"] == article_with_event.title
        assert data["results"][0]["events"][0]["event_id"] == events[0].event_id
        assert data["results"][0]["events"][0]["provider"] == events[0].provider.name
        assert len(data["results"]) == 1

    def test_get_articles_by_news_site(
        self, client: Client, articles: list[Article], news_sites: list[NewsSite]
    ) -> None:
        filtered_articles = [article for article in articles if article.news_site.name == news_sites[0].name]

        response = client.get(f"/v4/articles/?news_site={news_sites[0].name}")
        assert response.status_code == 200

        data = response.json()
        assert data["results"][0]["title"] == filtered_articles[0].title
        assert data["results"][0]["news_site"] == news_sites[0].name
        assert len(data["results"]) == len(filtered_articles)

    def test_get_articles_by_multiple_news_sites(
        self, client: Client, articles: list[Article], news_sites: list[NewsSite]
    ) -> None:
        filtered_articles = [
            article for article in articles if article.news_site.name in [news_sites[0].name, news_sites[1].name]
        ]

        response = client.get(f"/v4/articles/?news_site={news_sites[0].name},{news_sites[1].name}&limit=100")
        assert response.status_code == 200

        data = response.json()
        assert len(data["results"]) == len(filtered_articles)
        assert all(article["title"] in [article.title for article in filtered_articles] for article in data["results"])

    def test_get_articles_with_offset(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?offset=5")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 10

    def test_get_articles_with_limit(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?limit=5")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 5

    def test_get_articles_with_ordering(self, client: Client, articles: list[Article]) -> None:
        sorted_data = sorted(articles, key=lambda article: article.published_at, reverse=True)

        response = client.get("/v4/articles/?ordering=-published_at")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == sorted_data[0].title

    def test_get_articles_published_at_greater_then(self, client: Client, articles: list[Article]) -> None:
        articles_in_the_future = list(
            filter(
                lambda article: article.title.startswith("Article in the future"),
                articles,
            )
        )

        response = client.get("/v4/articles/?published_at_gt=2040-10-01")
        assert response.status_code == 200

        data = response.json()

        assert all(
            article["title"] in [article.title for article in articles_in_the_future] for article in data["results"]
        )
        assert len(data["results"]) == 2

    def test_get_articles_published_at_lower_then(self, client: Client, articles: list[Article]) -> None:
        articles_in_the_past = list(
            filter(
                lambda article: article.title.startswith("Article in the past"),
                articles,
            )
        )

        response = client.get("/v4/articles/?published_at_lt=2001-01-01")
        assert response.status_code == 200

        data = response.json()

        assert all(
            article["title"] in [article.title for article in articles_in_the_past] for article in data["results"]
        )
        assert len(data["results"]) == 2

    def test_get_article_search_articles(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?search=title")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Article with specific title"
        assert len(data["results"]) == 1

    def test_get_articles_search_summary(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?search=title")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["summary"] == "Description of an article with a specific title"
        assert len(data["results"]) == 1

    def test_get_articles_title_contains(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?title_contains=Article with specific")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Article with specific title"
        assert len(data["results"]) == 1

    def test_get_articles_title_contains_one(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?title_contains_one=SpaceX, specific")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Article with specific title"
        assert len(data["results"]) == 2

    def test_get_articles_title_contains_all(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?title_contains_all=specific, with, title")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Article with specific title"
        assert len(data["results"]) == 1

    def test_get_articles_summary_contains(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?summary_contains=specific")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Article with specific title"
        assert len(data["results"]) == 1

    def test_get_articles_summary_contains_one(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?summary_contains_one=SpaceX, specific")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Article with specific title"
        assert len(data["results"]) == 2

    def test_get_articles_summary_contains_all(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?summary_contains_all=specific, with, title")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Article with specific title"
        assert len(data["results"]) == 1

    def test_soft_deleted(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?title_contains=Deleted")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 0

    def test_news_site_exclude(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?news_site_exclude=SpaceNews")
        assert response.status_code == 200

        data = response.json()

        assert all(article["news_site"] != "SpaceNews" for article in data["results"])

    def test_news_site_exclude_multiple(self, client: Client, articles: list[Article]) -> None:
        response = client.get("/v4/articles/?news_site_exclude=SpaceNews,SpaceFlightNow")
        assert response.status_code == 200

        data = response.json()

        assert all(article["news_site"] not in ["SpaceNews", "SpaceFlightNow"] for article in data["results"])
