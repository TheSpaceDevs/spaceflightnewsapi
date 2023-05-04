import random
from datetime import timedelta

from django.utils import timezone
from rest_framework.test import APITestCase

from api.models import Article, NewsSite


class TestArticleEndpoint(APITestCase):
    def setUp(self):
        for site in range(5):
            news_site = NewsSite.objects.create(name=f"Site {site}")

            # Create 10 articles for each news site
            for index, article in enumerate(range(10)):
                # Create a random date between now and 10 days
                start_date = timezone.now()
                end_date = start_date + timedelta(days=10)
                random_date = start_date + (end_date - start_date) * random.random()

                Article.objects.create(
                    title=f"Article {index}",
                    url=f"https://example.com/article/{news_site.id}/{index}",
                    published_at=random_date,
                    updated_at=random_date,
                    news_site_id=news_site.id,
                )

    def test_all_articles(self):
        response = self.client.get("/v4/articles/")
        articles = response.json()["results"]

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(articles), 10)

    def test_all_articles_with_limit(self):
        response = self.client.get("/v4/articles/?limit=5")
        articles = response.json()["results"]

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(articles), 5)

    def test_all_articles_with_offset(self):
        response_all = self.client.get("/v4/articles/")
        articles_all = response_all.json()["results"]
        response = self.client.get("/v4/articles/?offset=5")
        articles = response.json()["results"]

        self.assertEquals(response.status_code, 200)
        self.assertEquals(articles[0]["id"], articles_all[5]["id"])

    def test_all_articles_with_sort(self):
        response = self.client.get("/v4/articles/?sort=updated_at")
        articles = response.json()["results"]

        self.assertEquals(response.status_code, 200)
        self.assertGreater(articles[0]["updated_at"], articles[1]["updated_at"])

    def test_all_articles_per_news_site(self):
        response = self.client.get("/v4/articles/?news_site=Site 1")
        articles = response.json()["results"]

        self.assertEquals(response.status_code, 200)
        self.assertTrue(all(article["news_site"] == "Site 1" for article in articles))
