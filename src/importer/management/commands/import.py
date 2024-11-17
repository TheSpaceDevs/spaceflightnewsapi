from django.core.management.base import BaseCommand, CommandParser

from importer.management.commands._launch_events import fetch_events, fetch_launches
from importer.management.commands._news_items import fetch_news


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--launches", action="store_true", help="Fetch launches")
        parser.add_argument("--events", action="store_true", help="Fetch events")
        parser.add_argument("--news", action="store_true", help="Fetch news")

    def handle(self, *args: tuple[str], **options: dict[str, str | bool]) -> None:
        if options["news"]:
            fetch_news()

        if options["launches"]:
            fetch_launches()

        if options["events"]:
            fetch_events()
