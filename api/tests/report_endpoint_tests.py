from rest_framework.test import APITestCase

from api.models import NewsSite, Report


class ReportEndpointTests(APITestCase):
    def setUp(self):
        news_site_test_com = NewsSite.objects.create(name="test.com")
        news_site_example_com = NewsSite.objects.create(name="example.com")

        self.report_test_com = Report.objects.create(
            title="Test Report Test",
            url="https://www.test.com/report",
            image_url="https://www.test.com/report_image.jpg",
            summary="Test summary",
            published_at="2021-01-01T00:00:00Z",
            updated_at="2021-01-05T00:00:00Z",
            news_site=news_site_test_com,
        )

        self.report_example_com = Report.objects.create(
            title="Test Report Example",
            url="https://www.example.com/report",
            image_url="https://www.example.com/report_image.jpg",
            summary="Test summary",
            published_at="2021-02-01T00:00:00Z",
            updated_at="2021-02-05T00:00:00Z",
            news_site=news_site_example_com,
        )

    def test_report_endpoint(self):
        response = self.client.get("/v4/reports/")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)

    def test_summary_filter(self):
        response = self.client.get("/v4/reports/?summary=Test summary")
        reports = response.json()["results"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(reports), 2)
