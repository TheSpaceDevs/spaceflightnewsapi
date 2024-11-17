from django.core.management.base import BaseCommand

from importer.management.commands._news_items import fetch_news


class Command(BaseCommand):
    def handle(self, *args: tuple[str], **options: dict[str, str | bool]) -> None:
        fetch_news()
