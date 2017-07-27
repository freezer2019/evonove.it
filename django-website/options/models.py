from django.db import models
from django.utils.translation import ugettext as _

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel


@register_setting
class WebsiteSettings(BaseSetting):
    name = models.CharField(max_length=255, help_text=_('Your company name'))
    address = models.CharField(max_length=255, help_text=_('Your company address'))
    email = models.EmailField(max_length=255, help_text=_('Your company email address'))
    phone = models.CharField(max_length=16, help_text=_('Your company phone number'))
    vat = models.CharField(max_length=16, help_text=_('Your company VAT with initial state code (i.e.: GB)'))

    github = models.URLField(help_text=_('Your GitHub page URL'))
    twitter = models.URLField(help_text=_('Your Twitter page URL'))
    facebook = models.URLField(help_text=_('Your Facebook page URL'))

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                FieldPanel('email'),
                FieldPanel('phone'),
                FieldPanel('address'),
                FieldPanel('vat'),
            ],
            heading='Company information',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [
                FieldPanel('github'),
                FieldPanel('twitter'),
                FieldPanel('facebook'),
            ],
            heading='Social media',
            classname='collapsible',
        ),
    ]


@register_setting
class AnalyticsSettings(BaseSetting):
    google_analytics = models.CharField(max_length=15, help_text=_('Google Analytics tracking ID'))
