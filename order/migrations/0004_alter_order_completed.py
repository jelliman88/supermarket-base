# Generated by Django 3.2.14 on 2023-02-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='completed',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]