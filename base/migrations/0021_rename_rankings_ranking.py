# Generated by Django 4.2.6 on 2024-03-05 13:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0020_rankings"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Rankings",
            new_name="Ranking",
        ),
    ]
