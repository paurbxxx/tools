# Generated by Django 3.1.5 on 2022-01-19 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0022_auto_20220114_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
