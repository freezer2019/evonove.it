from django.views.generic import TemplateView

from wagtail.wagtailcore.models import Page


class UserSitemapView(TemplateView):
    template_name = 'user_sitemap.html'

    def get_context_data(self, **kwargs):
        context = super(UserSitemapView, self).get_context_data(**kwargs)
        root_page = Page.objects.get(slug='root')
        context['live_pages'] = Page.objects.live().descendant_of(root_page)
        return context
