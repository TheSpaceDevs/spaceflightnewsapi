import hashlib
from collections.abc import Sequence
from typing import Any

from django.core.cache import cache
from django.core.exceptions import EmptyResultSet
from django.db.models import QuerySet
from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 500
    # The count is the same for every page of a filter combination, while the cache middleware stores each page
    # (offset, limit, request headers) separately. Caching it on its own saves a COUNT(*) for every other page.
    count_cache_timeout = 300

    def get_count(self, queryset: QuerySet[Any] | Sequence[Any]) -> int:
        if not isinstance(queryset, QuerySet):
            return super().get_count(queryset)

        try:
            # Ordering doesn't affect the count, so leave it out of the key.
            sql, params = queryset.order_by().query.sql_with_params()
        except EmptyResultSet:
            return 0

        key = "pagination-count:" + hashlib.sha256(f"{sql}{params!r}".encode()).hexdigest()
        count = cache.get(key)
        if count is None:
            count = super().get_count(queryset)
            cache.set(key, count, self.count_cache_timeout)

        return count
