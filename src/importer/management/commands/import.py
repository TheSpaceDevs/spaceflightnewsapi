from django.core.management.base import BaseCommand
from harvester import sources


class Command(BaseCommand):
    def handle(self, *args: tuple[str], **options: dict[str, str | bool]) -> None:
        for source in sources:
            try:
                data = source.harvest()

                print(data)
            except Exception as e:
                print(f"Error: {e}")
