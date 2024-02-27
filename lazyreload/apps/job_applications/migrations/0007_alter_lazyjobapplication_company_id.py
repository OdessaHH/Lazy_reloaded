# Generated by Django 5.0.1 on 2024-02-27 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_applications", "0006_lazyjobapplication_cover_letter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lazyjobapplication",
            name="company_id",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="job_applications.company",
            ),
        ),
    ]
