# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20170204_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='slug',
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
