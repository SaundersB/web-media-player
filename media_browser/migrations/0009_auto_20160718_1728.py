# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_browser', '0008_auto_20160718_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videotrack',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='videotrack',
            name='genre',
        ),
        migrations.AddField(
            model_name='videotrack',
            name='video_aspect_ratio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='videotrack',
            name='video_format',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='videotrack',
            name='video_frame_rate',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='videotrack',
            name='video_height',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='videotrack',
            name='video_width',
            field=models.CharField(max_length=50, null=True),
        ),
    ]