# Generated by Django 2.1.1 on 2018-10-10 02:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20181009_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 10, 5, 26, 831531), verbose_name='创建时间'),
        ),
    ]