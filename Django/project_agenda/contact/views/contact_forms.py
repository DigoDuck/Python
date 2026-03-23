from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from contact.models import Contact
from django.urls import reverse

def create(req):
    form_action = reverse('contact:create')
    
    if req.method == 'POST':
        form =  ContactForm(req.POST)
        
        context = {
            'form' : form,
            'form_action': form_action,
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(
        req,
        'contact/create.html',
        context
        )
    
    context = {
            'form' : ContactForm(),
            'form_action': form_action,
        }
    
    return render(
        req,
        'contact/create.html',
        context
        )
    
    
def update(req, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if req.method == 'POST':
        form =  ContactForm(req.POST, instance=contact)
        
        context = {
            'form' : form,
            'form_action': form_action,
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(
        req,
        'contact/create.html',
        context
        )
    
    context = {
            'form' : ContactForm(instance=contact),
            'form_action': form_action,
        }
    
    return render(
        req,
        'contact/create.html',
        context
        )