from django.http import HttpResponse
from django.shortcuts import render_to_response
from stormcrayon.core.models import FeaturedLink

from django.db import connection


def portfolio(request):
    site_links = FeaturedLink.objects.filter(category="sites", live=True) #[:3]
    other_links = FeaturedLink.objects.filter(category="other", live=True) #[:3]
    raise "hell"
    return render_to_response('portfolio.html', {
        'sites': site_links,
        'other': other_links,
        'queries': connection.queries,
    })
    
    
    