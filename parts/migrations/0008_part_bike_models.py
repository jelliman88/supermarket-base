# Generated by Django 3.2.13 on 2022-05-03 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_alter_part_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='bike_models',
            field=models.JSONField(default=[]),
        ),
    ]
