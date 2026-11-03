"""Settings shared by all tests."""

from typing import Any

import pytest


@pytest.fixture(autouse=True)
def local_static_files(settings: Any) -> None:
    # Pages that render `{% static %}`, like the admin, would otherwise build their URLs with the S3 storage, which
    # needs a bucket name. Dependabot's pull requests don't get the repository's secrets, so the bucket name is empty
    # there and those tests failed.
    settings.STORAGES = {
        **settings.STORAGES,
        "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
    }
