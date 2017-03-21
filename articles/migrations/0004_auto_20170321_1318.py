# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 18:18
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20170317_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='first_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='lead_photo',
        ),
        migrations.RemoveField(
            model_name='image',
            name='path',
        ),
        migrations.RemoveField(
            model_name='image',
            name='slug',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to=articles.models.upload_image_to),
        ),
    ]
