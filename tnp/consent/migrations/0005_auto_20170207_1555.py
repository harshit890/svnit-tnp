# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 10:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0005_job_required_data_fields'),
        ('consent', '0004_auto_20170207_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatafields',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='userdatafields',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='userconsent',
            unique_together=set([('user', 'job')]),
        ),
    ]
