# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-10 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_question_next_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(),
        ),
    ]
