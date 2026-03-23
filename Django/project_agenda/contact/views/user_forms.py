from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm

def register(req):
    form = RegisterForm()
    
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        
        if form.is_valid():
            form.save()
            messages.success(req, 'Usuário Registado')
            return redirect('contact:index')
    
    return render(
        req,
        'contact/register.html',
        {
            'form': form,
        }
    )