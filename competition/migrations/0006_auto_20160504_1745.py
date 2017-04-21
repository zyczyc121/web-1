# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 17:45
from __future__ import unicode_literals

import competition.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0005_competition_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='max_team_size',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='competition',
            name='banner',
            field=models.ImageField(blank=True, upload_to=competition.models.resource_file_name),
        ),
        migrations.AlterField(
            model_name='competition',
            name='evaluation',
            field=models.CharField(choices=[('AUC', 'Area Under ROC Curve'), ('RMSE', 'Root of Mean Square Error'), ('PRECISION', 'Precision'), ('RECALL', 'Recall'), ('ACCURACY', 'Accuracy'), ('MAP', 'Mean Average Precision'), ('NDCG', 'Normalized Discounted Cumulative Gain')], max_length=10),
        ),
        migrations.AlterField(
            model_name='competition',
            name='logo',
            field=models.ImageField(blank=True, upload_to=competition.models.resource_file_name),
        ),
    ]