# Generated by Django 5.0.1 on 2024-03-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flat_applications", "0011_alter_lazyflatapplication_additional_notes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lazyflatapplication",
            name="additional_notes",
            field=models.TextField(blank=True),
        ),
    ]
