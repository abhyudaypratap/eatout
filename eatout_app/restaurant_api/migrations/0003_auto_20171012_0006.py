# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api', '0002_restaurantreviews_reviewscomments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantreviews',
            old_name='google_rating',
            new_name='user_rating',
        ),
        migrations.AddField(
            model_name='restaurantdb',
            name='contact',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='restaurantdb',
            name='user_rated',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='restaurantdb',
            name='visted',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='restaurantreviews',
            name='reviews',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='reviewscomments',
            name='comments',
            field=models.CharField(max_length=3000),
        ),
    ]
