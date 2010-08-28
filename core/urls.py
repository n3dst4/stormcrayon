from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('stormcrayon.core.views',
    (r'^$', 'portfolio'),
    (u'^resume/', direct_to_template, {"template":"resume.html"}, "resume"),
    (r'^about/', direct_to_template, {"template":"about.html"}, "about"),
)
