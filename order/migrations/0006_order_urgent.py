# Generated by Django 3.2.13 on 2023-03-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_current_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
    ]
