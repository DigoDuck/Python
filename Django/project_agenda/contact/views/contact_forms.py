from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import

def create(req):
    context = {
        
    }
    
    return render(
        req,
        'contact/create.html',
        context
        )