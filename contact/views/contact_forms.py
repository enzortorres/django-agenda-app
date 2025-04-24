from django.shortcuts import render

from contact.models import Contact
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST),
            'site_title': 'Contacts - ',
        }
        
        return render(request, 'contact/create.html', context)
        

    context = {
        'form': ContactForm(),
        'site_title': 'Contacts - ',
    }
        
    return render(request, 'contact/create.html', context)
    
    