# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 14:08
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170727_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='partner_subtitle',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_title',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
