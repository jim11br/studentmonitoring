# Generated by Django 4.2.6 on 2024-03-05 05:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0016_remove_status_time_stam_status_time_stamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="status",
            name="time_stamp",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
