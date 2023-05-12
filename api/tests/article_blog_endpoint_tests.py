from uuid import uuid4

from rest_framework.test import APITestCase

from api.models import Article, Event, Launch, NewsSite, Provider


class TestArticleAndBlogEndpoints(APITestCase):
    def setUp(self):
        # Create a provider including a launch
        provider = Provider.objects.create(name="Launch Library 2")
        self.launch = Launch.objects.create(
            launch_id=uuid4(),
            name="Launch 1",
            provider=provider,
        )

        self.event = Event.objects.create(
            event_id=1,
            name="Event 1",
            provider=provider,
        )

        # Create a news site
        news_site_test_com = NewsSite.objects.create(name="test.com")
        news_site_example_com = NewsSite.objects.create(name="example.com")

        # Create an article
        self.article_with_launch = Article.objects.create(
            title="Test Article with Launch",
            url="https://www.test.com/launch",
            image_url="https://www.test.com/launch_image.jpg",
            summary="Test summary with launch",
            news_site=news_site_test_com,
            published_at="2021-01-01T00:00:00Z",
            updated_at="2021-01-05T00:00:00Z",
        )
        self.article_with_launch.launches.add(self.launch)

        self.article_with_event = Article.objects.create(
            title="Test Article with Event",
            url="https://www.test.com/event",
            image_url="https://www.test.com/event_image.jpg",
            summary="Test summary with event",
            news_site=news_site_test_com,
            published_at="2021-02-01T00:00:00Z",
            updated_at="2021-02-05T00:00:00Z",
        )
        self.article_with_event.events.add(self.event)

        self.article_without_launch_and_event = Article.objects.create(
            title="Test Article without Launch",
            url="https://www.example.com",
            image_url="https://www.example.com/image.jpg",
            summary="Test summary without launch",
            news_site=news_site_example_com,
            published_at="2021-03-01T00:00:00Z",
            updated_at="2021-03-05T00:00:00Z",
        )

    def test_get_all_articles(self):
        response = self.client.get("/v4/articles/")
        articles = response.json()["results"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 3)

    def test_all_articles_with_launch(self):
        response = self.client.get("/v4/articles/?has_launch=true")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 1)

    def test_all_articles_with_event(self):
        response = self.client.get("/v4/articles/?has_event=true")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 1)

    def test_all_articles_with_a_specific_launch(self):
        response = self.client.get(f"/v4/articles/?launch={self.launch.launch_id}")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]["title"], self.article_with_launch.title)

    def test_all_articles_with_a_specific_event(self):
        response = self.client.get(f"/v4/articles/?event={self.event.event_id}")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]["title"], self.article_with_event.title)

    def test_all_articles_with_a_specific_news_site(self):
        response = self.client.get(
            f"/v4/articles/?news_site={self.article_with_launch.news_site.name}"
        )
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 2)

    def test_published_at__gt(self):
        response = self.client.get(
            "/v4/articles/?published_at__gt=2021-01-01T00:00:00Z"
        )
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 2)

    def test_published_at__gte(self):
        response = self.client.get(
            "/v4/articles/?published_at__gte=2021-01-01T00:00:00Z"
        )
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 3)

    def test_published_at__lt(self):
        response = self.client.get(
            "/v4/articles/?published_at__lt=2021-02-01T00:00:00Z"
        )
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 1)

    def test_published_at__lte(self):
        response = self.client.get(
            "/v4/articles/?published_at__lte=2021-02-01T00:00:00Z"
        )
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 2)

    def test_updated_at__gt(self):
        response = self.client.get("/v4/articles/?updated_at__gt=2021-01-05T00:00:00Z")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 2)

    def test_updated_at__gte(self):
        response = self.client.get("/v4/articles/?updated_at__gte=2021-01-01T00:00:00Z")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 3)

    def test_updated_at__lt(self):
        response = self.client.get("/v4/articles/?updated_at__lt=2021-03-05T00:00:00Z")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 2)

    #
    def test_updated_at__lte(self):
        response = self.client.get("/v4/articles/?updated_at__lte=2021-03-05T00:00:00Z")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 3)

    def test_title_contains(self):
        response = self.client.get("/v4/articles/?title_contains=Article")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 3)

    def test_title_contains_all(self):
        response = self.client.get("/v4/articles/?title_contains_all=Article, Launch")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 2)

    def test_summary_contains(self):
        response = self.client.get("/v4/articles/?summary_contains=summary")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 3)

    def test_summary_contains_all(self):
        response = self.client.get("/v4/articles/?summary_contains_all=summary, launch")
        articles = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(articles), 2)
