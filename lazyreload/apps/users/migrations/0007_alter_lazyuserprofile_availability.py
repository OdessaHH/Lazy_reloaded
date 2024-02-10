# Generated by Django 5.0.1 on 2024-02-10 00:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_lazyuserprofile_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lazyuserprofile",
            name="availability",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 2, 10, 0, 27, 47, 725098, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Earliest Start Date",
            ),
        ),
    ]
