# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-09 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent', '0023_auto_20170605_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='caste_category',
            field=models.CharField(choices=[('OBC', 'OBC'), ('GEN', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OBC-PH', 'OBC-PH'), ('GEN-PH', 'General-PH'), ('SC-PH', 'SC-PH'), ('ST-PH', 'ST-PH')], default='GEN', max_length=6),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
