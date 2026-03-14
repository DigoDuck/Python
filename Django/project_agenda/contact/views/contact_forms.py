from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =(
            'first_name', 'last_name', 'phone',
        )

def create(req):    
    if req.method == 'POST':
        context = {
            'form' : ContactForm(req.POST)
        }
    
        return render(
        req,
        'contact/create.html',
        context
        )
    
    context = {
            'form' : ContactForm()
    }
    
    return render(
        req,
        'contact/create.html',
        context
        )