# Generated by Django 3.2.14 on 2023-02-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0025_auto_20230228_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
    ]
