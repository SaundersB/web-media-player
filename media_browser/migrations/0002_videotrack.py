# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_browser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=100)),
                ('date_added', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('play_count', models.IntegerField()),
                ('rating', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('file_size', models.DecimalField(decimal_places=5, max_digits=20)),
            ],
        ),
    ]