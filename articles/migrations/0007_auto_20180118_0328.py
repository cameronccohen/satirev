# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-18 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_mostread'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Section',
            new_name='section',
        ),
    ]
