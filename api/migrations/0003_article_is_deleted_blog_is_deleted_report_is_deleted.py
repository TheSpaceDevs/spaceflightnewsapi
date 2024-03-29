# Generated by Django 4.2.7 on 2023-11-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_article_options_alter_blog_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="blog",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="report",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
