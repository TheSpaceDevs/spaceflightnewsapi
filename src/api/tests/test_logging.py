"""Tests that server errors are logged to stdout, where the container logs pick them up."""

import os
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[2]

# Makes the articles endpoint crash and requests it, without touching the database.
SCRIPT = """
import django
django.setup()

from django.test import Client
from api.views import ArticleViewSet

def crash(*args, **kwargs):
    raise RuntimeError("boom from the articles endpoint")

ArticleViewSet.list = crash
response = Client(raise_request_exception=False).get("/v4/articles/")
print(f"status={response.status_code}")
response = Client(raise_request_exception=False).get("/v4/does-not-exist/")
print(f"status={response.status_code}")
"""


def _run() -> subprocess.CompletedProcess[str]:
    env = {**os.environ, "DJANGO_SETTINGS_MODULE": "snapy.settings", "DEBUG": "false", "ENABLE_CACHE": "false"}
    return subprocess.run([sys.executable, "-c", SCRIPT], cwd=SRC, env=env, capture_output=True, text=True, timeout=60)


def test_server_errors_are_logged_to_stdout() -> None:
    result = _run()

    assert "status=500" in result.stdout, result.stderr
    assert "Internal Server Error: /v4/articles/" in result.stdout
    assert "Traceback (most recent call last):" in result.stdout
    assert "RuntimeError: boom from the articles endpoint" in result.stdout


def test_not_found_is_not_logged() -> None:
    result = _run()

    assert "status=404" in result.stdout, result.stderr
    assert "Not Found: /v4/does-not-exist/" not in result.stdout + result.stderr
