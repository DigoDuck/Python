from django.shortcuts import render
from contact.models import Contact

def index(req):
    contacts = Contact.objects.all() \
        .filter(show=True)
    
    context = {
        'contacts': contacts
    }
    
    return render(
        req,
        'contact/index.html',
        context
    )