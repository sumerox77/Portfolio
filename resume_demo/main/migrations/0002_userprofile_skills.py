# Generated by Django 4.2.4 on 2023-08-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="skills",
            field=models.ManyToManyField(blank=True, to="main.skill"),
        ),
    ]
