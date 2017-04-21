# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-17 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userinfo_real_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='remote_addr',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]