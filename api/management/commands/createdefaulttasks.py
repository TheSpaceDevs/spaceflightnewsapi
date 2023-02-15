from django.core.management.base import BaseCommand, CommandError
from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask


class Command(BaseCommand):
    help = "Initialize the default periodic tasks for Celery (Beat)."

    def handle(self, *args, **kwargs):
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
                crontab=ll_launch_cron_schedule,
                name="Sync Launches",
                task="api.tasks.ll2.sync_launches",
                enabled=False,
            )

            PeriodicTask.objects.get_or_create(
                crontab=ll_event_cron_schedule,
                name="Sync Events",
                task="api.tasks.ll2.sync_events",
                enabled=False,
            )

            # SNAPI V3
            PeriodicTask.objects.get_or_create(
                interval=five_minute_schedule,
                name="Sync News Sites",
                task="api.tasks.snapi.migrate_news_sites",
                enabled=False,
            )

            PeriodicTask.objects.get_or_create(
                interval=five_minute_schedule,
                name="Sync Articles",
                task="api.tasks.snapi.migrate_articles",
                enabled=False,
            )

            PeriodicTask.objects.get_or_create(
                interval=five_minute_schedule,
                name="Sync Blogs",
                task="api.tasks.snapi.migrate_blogs",
                enabled=False,
            )

            PeriodicTask.objects.get_or_create(
                interval=five_minute_schedule,
                name="Sync Reports",
                task="api.tasks.snapi.migrate_reports",
                enabled=False,
            )

        except Exception as e:
            raise CommandError("Periodic task initalization failed.", e)
