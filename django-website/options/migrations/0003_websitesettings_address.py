# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0002_analyticssettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesettings',
            name='address',
            field=models.CharField(default='', help_text='Your company address', max_length=255),
            preserve_default=False,
        ),
    ]
