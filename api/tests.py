from rest_framework.test import APITestCase
from django.conf import settings

from api.models import NewsSite


# Create your tests here.
class TestInfoEndpoint(APITestCase):
    def setUp(self):
        for site in range(5):
            NewsSite.objects.create(name=f"Site {site}")

    def test_version(self):
        response = self.client.get('/v4/info/')
        version = response.json()['version']

        assert response.status_code == 200
        assert version == settings.VERSION

    def test_news_sites(self):
        response = self.client.get('/v4/info/')
        news_sites = response.json()['news_sites']

        assert response.status_code == 200
        assert isinstance(news_sites, list)
        assert len(news_sites) == 5
