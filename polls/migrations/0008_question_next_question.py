# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-10 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20170709_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='next_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]