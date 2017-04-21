# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-09 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20161108_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingsignup',
            name='description',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pendingsignup',
            name='real_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pendingsignup',
            name='remote_addr',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pendingsignup',
            name='student_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]