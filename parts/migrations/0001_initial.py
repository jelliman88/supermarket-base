# Generated by Django 3.2.13 on 2022-04-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('serial', models.IntegerField(blank=True, null=True)),
                ('bike', models.TextField(blank=True, max_length=50)),
            ],
        ),
    ]
