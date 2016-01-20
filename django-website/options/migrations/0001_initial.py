# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your company name', max_length=255)),
                ('email', models.EmailField(help_text='Your company email address', max_length=255)),
                ('phone', models.CharField(help_text='Your company phone number', max_length=16)),
                ('vat', models.CharField(help_text='Your company VAT with initial state code (i.e.: GB)', max_length=16)),
                ('github', models.URLField(help_text='Your GitHub page URL')),
                ('twitter', models.URLField(help_text='Your Twitter page URL')),
                ('facebook', models.URLField(help_text='Your Facebook page URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
