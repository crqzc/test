# Generated by Django 2.1.1 on 2018-10-09 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20181009_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 21, 34, 43, 75677), verbose_name='创建时间'),
        ),
    ]