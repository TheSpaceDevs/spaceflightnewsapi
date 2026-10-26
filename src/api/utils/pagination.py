import hashlib
from collections.abc import Sequence
from typing import Any

from django.core.cache import cache
from django.core.exceptions import EmptyResultSet
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.request import Request


class CustomLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 500
    # The count is the same for every page of a filter combination, while the cache middleware stores each page
    # (offset, limit, request headers) separately. Caching it on its own saves a COUNT(*) for every other page.
    count_cache_timeout = 300
    # The database reads and skips every row before the offset, so deep pages get slower the further they are.
    max_offset = 10_000
    offset_query_description = (
        f"The initial index from which to return the results, at most {max_offset:,}. To go further back, filter on "
        f"`published_at_lt` with the `published_at` of the last result instead."
    )

    def get_offset(self, request: Request) -> int:
        offset = super().get_offset(request)
        if offset > self.max_offset:
            raise ValidationError(
                {
                    self.offset_query_param: [
                        f"The offset can be at most {self.max_offset}. To go further back, filter on `published_at_lt` "
                        f"with the `published_at` of the last result instead."
                    ]
                }
            )
        return offset

    def get_next_link(self) -> str | None:
        # Don't link to a page beyond the maximum offset, which would be rejected.
        if self.offset is not None and self.limit is not None and self.offset + self.limit > self.max_offset:
            return None
        return super().get_next_link()

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
