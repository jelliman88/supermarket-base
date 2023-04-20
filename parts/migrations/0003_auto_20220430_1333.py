# Generated by Django 3.2.13 on 2022-04-30 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0002_auto_20220430_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='part',
            name='bike',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.bike'),
        ),
    ]