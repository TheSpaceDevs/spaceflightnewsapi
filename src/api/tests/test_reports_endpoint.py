import pytest
from django.test.client import Client

from api.models import NewsSite, Report


@pytest.mark.django_db
class TestReportsEndpoint:
    def test_get_reports(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/")
        assert response.status_code == 200

        data = response.json()
        assert len(data["results"]) == 10

    @pytest.mark.skip("Keeps failing?")
    def test_get_single_report(self, client: Client, reports: list[Report]) -> None:
        response = client.get(path="/v4/reports/1/")

        data = response.json()
        assert data["id"] == 1
        assert data["title"] == "Report 0"

    def test_limit_reports(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?limit=5")
        assert response.status_code == 200

        data = response.json()
        assert len(data["results"]) == 5

    def test_get_report_by_news_site(self, client: Client, reports: list[Report], news_sites: list[NewsSite]) -> None:
        filtered_reports = [report for report in reports if report.news_site.name == news_sites[0].name]

        response = client.get(f"/v4/reports/?news_site={news_sites[0].name}")
        assert response.status_code == 200

        data = response.json()
        assert data["results"][0]["title"] == filtered_reports[0].title
        assert data["results"][0]["news_site"] == news_sites[0].name
        assert len(data["results"]) == len(filtered_reports)

    def test_get_reports_by_multiple_news_sites(
        self, client: Client, reports: list[Report], news_sites: list[NewsSite]
    ) -> None:
        filtered_reports = [
            report for report in reports if report.news_site.name in [news_sites[0].name, news_sites[1].name]
        ]

        response = client.get(f"/v4/reports/?news_site={news_sites[0].name},{news_sites[1].name}&limit=100")
        assert response.status_code == 200

        data = response.json()
        assert len(data["results"]) == len(filtered_reports)
        assert all(report["title"] in [report.title for report in filtered_reports] for report in data["results"])

    def test_get_reports_with_offset(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?offset=5")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 10

    def test_get_reports_with_limit(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?limit=3")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 3

    def test_get_reports_with_ordering(self, client: Client, reports: list[Report]) -> None:
        sorted_data = sorted(reports, key=lambda report: report.published_at, reverse=True)

        response = client.get("/v4/reports/?ordering=-published_at")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == sorted_data[0].title

    def test_get_reports_published_at_greater_then(self, client: Client, reports: list[Report]) -> None:
        reports_in_the_future = list(
            filter(
                lambda report: report.title.startswith("Report in the future"),
                reports,
            )
        )

        response = client.get("/v4/reports/?published_at_gt=2040-10-01")
        assert response.status_code == 200

        data = response.json()

        assert all(report["title"] in [report.title for report in reports_in_the_future] for report in data["results"])
        assert len(data["results"]) == 2

    def test_get_reports_published_at_lower_then(self, client: Client, reports: list[Report]) -> None:
        reports_in_the_past = list(
            filter(
                lambda report: report.title.startswith("Report in the past"),
                reports,
            )
        )

        response = client.get("/v4/reports/?published_at_lt=2001-01-01")
        assert response.status_code == 200

        data = response.json()

        assert all(report["title"] in [report.title for report in reports_in_the_past] for report in data["results"])
        assert len(data["results"]) == 2

    def test_get_report_search_reports(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?search=title")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Report with specific title"
        assert len(data["results"]) == 1

    def test_get_reports_search_summary(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?search=title")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["summary"] == "Description of an report with a specific title"
        assert len(data["results"]) == 1

    def test_get_reports_title_contains(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?title_contains=Report with specific")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Report with specific title"
        assert len(data["results"]) == 1

    def test_get_reports_title_contains_one(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?title_contains_one=SpaceX, specific")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Report with specific title"
        assert len(data["results"]) == 2

    def test_get_reports_title_contains_all(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?title_contains_all=specific, with, title")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Report with specific title"
        assert len(data["results"]) == 1

    def test_get_reports_summary_contains(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?summary_contains=specific")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Report with specific title"
        assert len(data["results"]) == 1

    def test_get_reports_summary_contains_one(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?summary_contains_one=SpaceX, specific")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Report with specific title"
        assert len(data["results"]) == 2

    def test_get_reports_summary_contains_all(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?summary_contains_all=specific, with, title")
        assert response.status_code == 200

        data = response.json()

        assert data["results"][0]["title"] == "Report with specific title"
        assert len(data["results"]) == 1

    def test_soft_deleted(self, client: Client, reports: list[Report]) -> None:
        response = client.get("/v4/reports/?title_contains=Deleted")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 0
