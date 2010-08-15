from django.conf.urls.defaults import *

urlpatterns = patterns('stormcrayon.core.views',
    (r'^$', 'frontpage'),
)
