# Generated by Django 4.2.3 on 2023-07-28 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=5)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2023, 7, 28, 20, 24, 24, 870659))),
            ],
        ),
    ]
