# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api', '0004_auto_20171013_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantdb',
            name='geocode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
