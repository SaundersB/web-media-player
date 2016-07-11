# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_browser', '0003_auto_20160711_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiotrack',
            name='date_added',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='audiotrack',
            name='play_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='audiotrack',
            name='track_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='audiotrack',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]