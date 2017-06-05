# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-05 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent', '0022_auto_20170531_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='caste_category',
            field=models.CharField(choices=[('OBC', 'OBC'), ('GEN', 'General/Open'), ('SC', 'SC'), ('ST', 'ST'), ('OBC-PH', 'OBC Physically Handicapped'), ('GEN-PH', 'General Physically Handicapped'), ('SC-PH', 'SC Physically Handicapped'), ('ST-PH', 'ST Physically Handicapped')], default='GEN', max_length=6),
        ),
    ]