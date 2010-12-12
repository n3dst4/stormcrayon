from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404 

from django.shortcuts import render_to_response
from stormcrayon.core.models import FeaturedLink

from django.db import connection
from django import forms
from django.template import RequestContext
from django.core.mail import send_mail



def portfolio(request):
    links = FeaturedLink.objects.filter(live=True)
    return render_to_response('portfolio.html', {
        'links': links,
        "nav_active": "portfolio"
    })
    
    
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
    
    
    
    
def frame(request, id):
    try:
        url = FeaturedLink.objects.filter(live=True, id=id)[0].address
    except:
        raise Http404
    return render_to_response('frame.html', {
        "url": url,
        "id": id
    })
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    