# Generated by Django 4.1.2 on 2022-10-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="description",
            field=models.TextField(max_length=2000),
        ),
    ]