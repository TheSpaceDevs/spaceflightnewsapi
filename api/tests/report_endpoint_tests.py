from rest_framework.test import APITestCase

from api.models import NewsSite, Report


class ReportEndpointTests(APITestCase):
    def setUp(self):
        news_site_test_com = NewsSite.objects.create(name="test.com")
        news_site_example_com = NewsSite.objects.create(name="example.com")

        self.report_test_com = Report.objects.create(
            title="Test Report Not Example",
            url="https://www.test.com/report",
            image_url="https://www.test.com/report_image.jpg",
            summary="Test summary not example",
            published_at="2021-01-01T00:00:00Z",
            updated_at="2021-01-05T00:00:00Z",
            news_site=news_site_test_com,
        )

        self.report_example_com = Report.objects.create(
            title="Test Report Example",
            url="https://www.example.com/report",
            image_url="https://www.example.com/report_image.jpg",
            summary="Test summary example",
            published_at="2021-02-01T00:00:00Z",
            updated_at="2021-02-05T00:00:00Z",
            news_site=news_site_example_com,
        )

    def test_report_endpoint(self):
        response = self.client.get("/v4/reports/")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)

    def test_title_contains(self):
        response = self.client.get("/v4/reports/?title_contains=Not")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 1)

    def test_title_contains_all(self):
        response = self.client.get("/v4/reports/?title_contains_all=Test")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)

    def test_summary_contains(self):
        response = self.client.get("/v4/reports/?summary_contains=not")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 1)

    def test_summary_contains_all(self):
        response = self.client.get("/v4/reports/?summary_contains_all=Test, example")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)

    def test_published_at__gt(self):
        response = self.client.get("/v4/reports/?published_at_gt=2021-01-01T00:00:00Z")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 1)

    def test_published_at__gte(self):
        response = self.client.get("/v4/reports/?published_at_gte=2021-01-01T00:00:00Z")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)

    def test_published_at__lt(self):
        response = self.client.get("/v4/reports/?published_at_lt=2021-02-01T00:00:00Z")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 1)

    def test_published_at__lte(self):
        response = self.client.get("/v4/reports/?published_at_lte=2021-02-01T00:00:00Z")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)

    def test_updated_at__gt(self):
        response = self.client.get("/v4/reports/?updated_at_gt=2021-01-05T00:00:00Z")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 1)

    def test_updated_at__gte(self):
        response = self.client.get("/v4/reports/?updated_at_gte=2021-01-05T00:00:00Z")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)

    def test_updated_at__lt(self):
        response = self.client.get("/v4/reports/?updated_at_lt=2021-02-05T00:00:00Z")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 1)

    def test_updated_at__lte(self):
        response = self.client.get("/v4/reports/?updated_at_lte=2021-02-05T00:00:00Z")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)
