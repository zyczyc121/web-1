# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-29 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0017_auto_20160922_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='sponsor_en',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='competition',
            name='sponsor',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
