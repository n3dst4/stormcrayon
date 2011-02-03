from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import FeaturedLink
from django.utils.translation import ugettext as _

class FeaturedLinkPlugin(CMSPluginBase):
    model = FeaturedLink
    name = _("Featured link")
    render_template = "featured_link.html"
    readonly_fields = ("description_html", "slug")
    
    def render(self, context, instance, placeholder):
        context.update({
            "link": instance,
            "placeholder": placeholder
        })
        return context
    
plugin_pool.register_plugin(FeaturedLinkPlugin)