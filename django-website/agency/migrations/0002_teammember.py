# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('role', models.CharField(help_text='Team member company role', max_length=150)),
                ('bio', wagtail.core.fields.RichTextField(help_text='The team member bio', max_length=360)),
                ('gravatar', models.CharField(blank=True, help_text='Add your Gravatar email', max_length=150, null=True)),
                ('website', models.URLField(blank=True, help_text='Your website page URL', null=True)),
                ('github', models.URLField(blank=True, help_text='Your GitHub page URL', null=True)),
                ('stackoverflow', models.URLField(blank=True, help_text='Your Stack Overflow page URL', null=True)),
                ('twitter', models.URLField(blank=True, help_text='Your Twitter page URL', null=True)),
                ('gplus', models.URLField(blank=True, help_text='Your Google+ page URL', null=True)),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL', null=True)),
                ('linkedin', models.URLField(blank=True, help_text='Your LinkedIn page URL', null=True)),
                ('medium', models.URLField(blank=True, help_text='Your Medium page URL', null=True)),
                ('behance', models.URLField(blank=True, help_text='Your Behance page URL', null=True)),
                ('dribbble', models.URLField(blank=True, help_text='Your Dribble page URL', null=True)),
                ('flickr', models.URLField(blank=True, help_text='Your Flickr page URL', null=True)),
                ('tumblr', models.URLField(blank=True, help_text='Your Tumblr page URL', null=True)),
                ('deviantart', models.URLField(blank=True, help_text='Your DeviantArt page URL', null=True)),
                ('pinterest', models.URLField(blank=True, help_text='Your Pinterest page URL', null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='agency.AgencyPage')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
