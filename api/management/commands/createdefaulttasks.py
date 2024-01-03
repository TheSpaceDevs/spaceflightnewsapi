from typing import Any

from django.core.management.base import BaseCommand, CommandError
from django_celery_beat.models import (  # type: ignore
    CrontabSchedule,
    IntervalSchedule,
    PeriodicTask,
)


class Command(BaseCommand):
    help = "Initialize the default periodic tasks for Celery (Beat)."

    def handle(self, *args: Any, **kwargs: Any) -> None:
        try:
            # Schedules
            five_minute_schedule, _ = IntervalSchedule.objects.get_or_create(
                every=5,
                period=IntervalSchedule.MINUTES,
            )
            ll_launch_cron_schedule, _ = CrontabSchedule.objects.get_or_create(
                minute="0",
                hour="5",
                day_of_week="*",
                day_of_month="*",
                month_of_year="*",
            )
            ll_event_cron_schedule, _ = CrontabSchedule.objects.get_or_create(
                minute="15",
                hour="5",
                day_of_week="*",
                day_of_month="*",
                month_of_year="*",
            )

            # Tasks
            # LL
            PeriodicTask.objects.get_or_create(
                name="Sync Launches",
                defaults={
                    "crontab": ll_launch_cron_schedule,
                    "task": "Sync Launches",
                    "enabled": False,
                },
            )

            PeriodicTask.objects.get_or_create(
                name="Sync Events",
                defaults={
                    "crontab": ll_event_cron_schedule,
                    "task": "Sync Events",
                    "enabled": False,
                },
            )
        except Exception as e:
            raise CommandError("Periodic task initialization failed.", e)
