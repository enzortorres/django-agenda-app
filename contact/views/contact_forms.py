from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib import messages
from contact.forms import ContactForm
from contact.models import Contact

def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        
        context = {
            'form': form,
            'form_action': form_action, 
            'site_title': 'Contacts - ',
            'subtitle': 'Create Contact',
        }
        
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contact created')
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(),
        'form_action': form_action, 
        'site_title': 'Contacts - ',
        'subtitle': 'Create Contact',
    }
        
    return render(request, 'contact/create.html', context)

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        
        context = {
            'form': form,
            'site_title': 'Contacts - ',
            'form_action': form_action,
            'subtitle': 'Update Contact',
        }
        
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contact updated')
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action, 
        'site_title': 'Contacts - ',
        'subtitle': 'Update Contact',
    }
        
    return render(request, 'contact/create.html', context)

def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    
    confirmation = request.POST.get('confirmation', 'no')
    print('confirmation: ', confirmation)
    
    if confirmation == 'yes':
        contact.delete()
        messages.success(request, 'Contact deleted')
        return redirect('contact:index')
    
    return render(request, 'contact/contact.html', {'contact': contact, 'confirmation': confirmation})