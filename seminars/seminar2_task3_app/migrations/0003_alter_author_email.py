# Generated by Django 4.2.3 on 2023-08-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2_task3_app', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
