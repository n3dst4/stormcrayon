from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('stormcrayon.core.views',
    (r'^$', 'portfolio'),
    url(u'^resume/', direct_to_template, {"template":"resume.html", "extra_context": {"nav_active": "resume"}}, name="resume"),
    url(r'^about/', direct_to_template, {"template":"about.html", "extra_context": {"nav_active": "about"}}, name="about"),
    (r'^thanks/', direct_to_template, {"template":"thanks.html", "extra_context": {"nav_active": "contact"}}),
    (r'^contact/', "contact"),
    #(r'^frame/$', direct_to_template, {
    #    "template":"frame.html",
    #    "extra_context": {
    #        "url": "http://google.com"
    #    }}),
    (r'^frame/(?P<id>.*)', "frame"),
)
