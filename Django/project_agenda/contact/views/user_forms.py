from django.shortcuts import render, redirect
from django.contrib import auth, messages
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(req):
    form = RegisterForm()
    
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        
        if form.is_valid():
            form.save()
            messages.success(req, 'Usuário Registado')
            return redirect('contact:login')
    
    return render(
        req,
        'contact/register.html',
        {
            'form': form,
        }
    )
    
def login_view(req):
    form = AuthenticationForm(req)

    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(req, user)
            messages.success(req, 'Logado com sucesso')
            return redirect('contact:index')
        messages.error(req, 'Invalid Login')
    
    return render(
        req,
        'contact/login.html',
        {
            'form': form,
        }
    )
    
@login_required(login_url='contact:login')
def user_update(req):
    form = RegisterUpdateForm(instance=req.user)
    
    if req.method != 'POST':
        return render(
            req,
            'contact/register.html',
            {
                'form': form,
            }
        )
    form = RegisterUpdateForm(data=req.POST, instance=req.user)
    
    if not form.is_valid():
        return render(
            req,
            'contact/register.html',
            {
                'form': form,
            }
        )
        
    form.save()
    return redirect('contact:login')

@login_required(login_url='contact:login')
def logout_view(req):
    auth.logout(req)
    return redirect('contact:login')