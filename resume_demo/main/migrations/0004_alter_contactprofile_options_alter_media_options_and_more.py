# Generated by Django 4.2.4 on 2023-08-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_userprofile_is_admin"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contactprofile",
            options={
                "ordering": ["timestamp"],
                "verbose_name": "Contact Profile",
                "verbose_name_plural": "Contact Profiles",
            },
        ),
        migrations.AlterModelOptions(
            name="media",
            options={
                "ordering": ["name"],
                "verbose_name": "Media",
                "verbose_name_plural": "Media Files",
            },
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="is_admin",
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="testimonials"),
        ),
    ]