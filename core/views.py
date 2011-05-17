from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404 

from django.shortcuts import render_to_response
from stormcrayon.core.models import FeaturedLink

from django.db import connection
from django import forms
from django.template import RequestContext
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


#@cache_page(60 * 15)
#@vary_on_cookie
#def portfolio(request):
#    xlinks = FeaturedLink.objects.filter(live=True)
#    return render_to_response('portfolio.html', RequestContext(request, {
#        'xlinks': xlinks,
#        "nav_active": "portfolio"
#    }))
    
    
#@cache_page(60 * 15)
#@vary_on_cookie
#def primple(request):
#    return render_to_response("portfolio.html")

    
@cache_page(60 * 15)
@vary_on_cookie
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = ("Sender's alleged email address: " + form.cleaned_data['sender']
                + "\n\n"
                + (form.cleaned_data['message'] or "The sender did not include a message.")
                + "\n\n")
            if form.cleaned_data['interest_web_design']:
                message += "Interested in web design\n"
            if form.cleaned_data['interest_other_development']:
                message += "Interested in other development\n"
            if form.cleaned_data['interest_graphic_design']:
                message += "Interested in graphic design\n"
            send_mail('Website contact', message, 'Website contact <neil.decarteret@gmail.com>',
                ['neil.decarteret@gmail.com'], fail_silently=False)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render_to_response('contact.html', RequestContext(request, {
        'form': form,
        "nav_active": "contact"
    }))


class ContactForm(forms.Form):
    message = forms.CharField(required=False, widget=forms.Textarea, label="Message", initial="")
    sender = forms.EmailField(required=True)
    interest_web_design = forms.BooleanField(required=False, label="Web design")
    interest_other_development = forms.BooleanField(required=False, label="Other development")
    interest_graphic_design = forms.BooleanField(required=False, label="Graphic design")
    
    
    
@cache_page(60 * 15)    
def frame(request, id):
    try:
        link = FeaturedLink.objects.filter(live=True, slug=id)[0]
    except:
        raise Http404
    return render_to_response('frame.html', {
        "url": link.address,
        "link": link,
        "id": id
    })


def error(request):
    raise Exception("This is a test error")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    