from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.decorators.cache import cache_page

cache_timeout = 60 * 15 # seconds

urlpatterns = patterns('stormcrayon.core.views',
    (r'^$', 'portfolio'),
    url(u'^resume/', cache_page(direct_to_template, cache_timeout), {"template":"resume.html", "extra_context": {"nav_active": "resume"}}, name="resume"),
    url(r'^about/', cache_page(direct_to_template, cache_timeout), {"template":"about.html", "extra_context": {"nav_active": "about"}}, name="about"),
    (r'^thanks/', cache_page(direct_to_template, cache_timeout), {"template":"thanks.html", "extra_context": {"nav_active": "contact"}}),
    (r'^contact/', "contact"),
    #(r'^frame/$', direct_to_template, {
    #    "template":"frame.html",
    #    "extra_context": {
    #        "url": "http://google.com"
    #    }}),
    (r'^frame/(?P<id>.*)', "frame"),
)
