"""Tests the database settings that production depends on."""

from typing import Any

import pytest
from django import forms
from django.db import connection

from api.models import NewsSite


@pytest.mark.django_db
def test_form_choices_do_not_use_server_side_cursors(monkeypatch: pytest.MonkeyPatch) -> None:
    # Production connects through PgBouncer in transaction mode, where a named (server-side) cursor can be declared
    # on one Postgres connection and fetched from on another, failing with InvalidCursorName. Django's form fields use
    # `.iterator()` for their choices, so this broke the admin's change pages at random.
    NewsSite.objects.create(name="ESA")
    named_cursors: list[Any] = []
    chunked_cursor = connection.chunked_cursor

    def spy() -> Any:
        named_cursors.append(True)
        return chunked_cursor()

    monkeypatch.setattr(connection, "chunked_cursor", spy)

    # The same choices the admin's select widgets render.
    widget = forms.ModelChoiceField(queryset=NewsSite.objects.all()).widget
    labels = [label for _, label in widget.choices]

    assert labels == ["---------", "ESA"]
    assert named_cursors == []
