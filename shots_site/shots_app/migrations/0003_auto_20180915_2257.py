# Generated by Django 2.1.1 on 2018-09-16 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots_app', '0002_auto_20180915_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkinggame',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 15, 22, 57, 48, 316012), verbose_name='date created'),
        ),
    ]