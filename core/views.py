from django.http import HttpResponse
from django.shortcuts import render_to_response
from stormcrayon.core.models import FeaturedLink


def portfolio(request):
    site_links = FeaturedLink.objects.filter(category="sites")[:3]
    other_links = FeaturedLink.objects.filter(category="other")[:3]
    return render_to_response('portfolio.html', {
        'sites': site_links,
        'other': other_links,
    })
    
    
    