from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contact.models import Contact

def index(req):
    contacts = Contact.objects.all() \
        .filter(show=True)
    
    context = {
        'contacts': contacts,
        'site_title': 'Contacts -'
    }
    
    return render(
        req,
        'contact/index.html',
        context
    )
    
def contact(req, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    contact_name = f'{single_contact.first_name} {single_contact.last_name}  -'
    
    if single_contact is None:
        raise Http404
    
    context = {
        'contact': single_contact,
        'site_title': contact_name
    }
    
    return render(
        req,
        'contact/contact.html',
        context
    )
    
