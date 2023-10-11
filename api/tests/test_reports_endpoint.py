import pytest

from api.models import Report


@pytest.mark.django_db
class TestReportsEndpoint:
    def test_get_all_reports(self, client, reports: list[Report]):
        response = client.get("/v4/reports/")
        assert response.status_code == 200

        data = response.json()
        assert len(data["results"]) == 10
