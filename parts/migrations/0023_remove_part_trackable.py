# Generated by Django 3.2.14 on 2023-02-28 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0022_part_threshold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='trackable',
        ),
    ]
