# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 08:32
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api', '0003_auto_20171012_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantdb',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantreviews',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewscomments',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurantdb',
            name='geocode',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
