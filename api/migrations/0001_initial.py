# Generated by Django 4.1.6 on 2023-02-16 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsSite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("url", models.URLField()),
                ("image_url", models.URLField()),
                ("summary", models.TextField(blank=True)),
                ("published_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                (
                    "news_site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.newssite"
                    ),
                ),
            ],
            options={
                "ordering": ["-published_at"],
            },
        ),
        migrations.CreateModel(
            name="Launch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("launch_id", models.UUIDField(unique=True)),
                ("name", models.CharField(max_length=250)),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.provider"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Launches",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_id", models.IntegerField()),
                ("name", models.CharField(max_length=250)),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.provider"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("url", models.URLField()),
                ("image_url", models.URLField()),
                ("summary", models.TextField()),
                ("published_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("featured", models.BooleanField(default=False)),
                ("events", models.ManyToManyField(blank=True, to="api.event")),
                ("launches", models.ManyToManyField(blank=True, to="api.launch")),
                (
                    "news_site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.newssite"
                    ),
                ),
            ],
            options={
                "ordering": ["-published_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("url", models.URLField()),
                ("image_url", models.URLField()),
                ("summary", models.TextField()),
                ("published_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("featured", models.BooleanField(default=False)),
                ("events", models.ManyToManyField(blank=True, to="api.event")),
                ("launches", models.ManyToManyField(blank=True, to="api.launch")),
                (
                    "news_site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.newssite"
                    ),
                ),
            ],
            options={
                "ordering": ["-published_at"],
                "abstract": False,
            },
        ),
    ]
