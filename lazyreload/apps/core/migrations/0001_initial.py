# Generated by Django 5.0.1 on 2024-02-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AiSettings",
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
                ("ai_setting_name", models.CharField(default="new", max_length=60)),
                (
                    "favorite",
                    models.BooleanField(
                        default=False, verbose_name="Saved as Favorite"
                    ),
                ),
                (
                    "temperature",
                    models.FloatField(default=0.5, verbose_name="Rational/Creative"),
                ),
                (
                    "word_count",
                    models.IntegerField(
                        default=320, verbose_name="How long should the letter be"
                    ),
                ),
                (
                    "quality",
                    models.CharField(
                        blank=True,
                        choices=[("low", "Low"), ("high", "High")],
                        default="high",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
