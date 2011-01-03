from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.decorators.cache import cache_page

cache_timeout = 60 * 15 # seconds

urlpatterns = patterns('stormcrayon.core.views',
    (r'^thanks/', cache_page(direct_to_template, cache_timeout), {"template":"thanks.html", "extra_context": {"nav_active": "contact"}}),
    (r'^contact/', "contact"),
    #(r'^portfolio/', "portfolio"),
    (r'^frame/(?P<id>.*)', "frame"),
    (r'^error/', "error"),
    (r'^$', 'portfolio'),
    
)

