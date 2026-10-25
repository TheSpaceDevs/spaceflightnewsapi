"""Tests the limits on the GraphQL endpoint."""

from typing import Any

import pytest
from django.test.client import Client
from graphql import get_introspection_query

from snapy.schema import schema


def _post(client: Client, query: str) -> tuple[int, dict[str, Any]]:
    response = client.post("/v4/graphql/", {"query": query}, content_type="application/json")
    return response.status_code, response.json()


@pytest.mark.django_db
class TestGraphQLLimits:
    @pytest.mark.parametrize(
        "query",
        [
            "{ allArticles(first: 10) { pageInfo { hasNextPage endCursor } edges { node { title } } } }",
            "{ allBlogs(first: 10) { edges { node { title newsSite { name } } } } }",
            "{ allReports(first: 10) { edges { node { title newsSite { name } } } } }",
            "{ allArticles(first: 10) { edges { node { title "
            "launches { edges { node { launchId name } } } events { edges { node { eventId name } } } } } } }",
        ],
    )
    def test_typical_queries_are_allowed(self, client: Client, query: str) -> None:
        status, body = _post(client, query)

        assert status == 200
        assert "errors" not in body

    def test_deeper_queries_are_rejected(self, client: Client) -> None:
        # Without reverse relations no valid query is this deep, but the limit guards against future schema changes,
        # as every extra level of nesting multiplies the number of database queries.
        status, body = _post(
            client, "{ allArticles(first: 10) { edges { node { launches { edges { node { launchId { a } } } } } } } }"
        )

        assert status == 400
        assert any("exceeds maximum operation depth of 6" in error["message"] for error in body["errors"])

    def test_introspection_is_allowed(self, client: Client) -> None:
        # GraphiQL and other tools load the schema with this (deeply nested) query.
        status, body = _post(client, get_introspection_query())

        assert status == 200
        assert "errors" not in body

    @pytest.mark.parametrize("type_name", ["LaunchType", "EventType", "NewsSiteType"])
    def test_no_reverse_relations(self, type_name: str) -> None:
        fields = schema.graphql_schema.type_map[type_name].fields  # type: ignore[union-attr]

        assert not {"articleSet", "blogSet", "reportSet"} & set(fields)
