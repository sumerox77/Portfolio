# Generated by Django 4.2.4 on 2023-08-24 12:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_certificate_credential_id_certificate_credential_url_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="certificate",
            name="date",
        ),
    ]
