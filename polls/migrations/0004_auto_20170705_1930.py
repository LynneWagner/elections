# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-05 23:30
from __future__ import unicode_literals
import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170704_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_Date',
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
