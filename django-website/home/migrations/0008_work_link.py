# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20160616_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='link',
            field=models.URLField(blank=True, help_text='Project link', null=True),
        ),
    ]
