# Generated by Django 3.2.14 on 2023-02-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_json_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
