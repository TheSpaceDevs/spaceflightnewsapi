from collections.abc import Callable

from django.http import HttpRequest, HttpResponse


class NormalizeJSONAcceptMiddleware:
    """Gives every request that can only be answered with JSON the same `Accept` header.

    DRF renders both JSON and the browsable HTML API, so it sets `Vary: Accept` and the cache middleware stores a
    response per `Accept` header. Without this, `*/*`, `application/json`, axios' `application/json, text/plain, */*`
    and so on each got their own cache entry. Headers that allow HTML, or only allow types we don't serve (which DRF
    answers with a 406), are left alone.
    """

    JSON_RANGES = ("application/json", "application/*", "*/*")
    HTML_RANGES = ("text/html", "text/*")

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        accept = request.META.get("HTTP_ACCEPT", "")
        allows_html = any(media_range in accept for media_range in self.HTML_RANGES)
        allows_json = not accept.strip() or any(media_range in accept for media_range in self.JSON_RANGES)

        if allows_json and not allows_html:
            request.META["HTTP_ACCEPT"] = "application/json"

        return self.get_response(request)
