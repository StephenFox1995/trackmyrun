# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170427_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='distance',
            field=models.FloatField(default=0, verbose_name='length'),
        ),
    ]
