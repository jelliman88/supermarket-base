# Generated by Django 3.2.13 on 2022-05-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0012_excelsheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(default=[])),
            ],
        ),
    ]