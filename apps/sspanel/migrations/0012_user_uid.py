# Generated by Django 3.2 on 2021-06-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0011_auto_20210504_1420"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="uid",
            field=models.UUIDField(null=True, unique=True, verbose_name="uid"),
        ),
    ]
