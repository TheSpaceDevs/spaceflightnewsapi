from django.conf import settings
from rest_framework.test import APITestCase

from api.models import NewsSite


class TestInfoEndpoint(APITestCase):
    def setUp(self):
        for site in range(5):
            NewsSite.objects.create(name=f"Site {site}")

    def test_version(self):
        response = self.client.get("/v4/info/")
        version = response.json()["version"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(version, settings.VERSION)

    def test_news_sites(self):
        response = self.client.get("/v4/info/")
        news_sites = response.json()["news_sites"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(news_sites), 5)
