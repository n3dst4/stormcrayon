from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('stormcrayon.core.views',
    (r'^$', 'portfolio'),
    (u'^resume/', direct_to_template, {"template":"resume.html", "extra_context": {"nav_active": "resume"}}, "resume"),
    (r'^about/', direct_to_template, {"template":"about.html", "extra_context": {"nav_active": "about"}}, "about"),
    (r'^thanks/', direct_to_template, {"template":"thanks.html", "extra_context": {"nav_active": "contact"}}, "thanks"),
    (r'^contact/', "contact"),
)
