from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import

def create(req):
    if req.method == 'POST':
        print(req.method)
    
    context = {
        
    }
    
    print(req.method)
    
    return render(
        req,
        'contact/create.html',
        context
        )