
from django.shortcuts import render
from blog.data import posts

def blog(request):
    print("blog")
    
    context = {
        # 'text': 'Hello Blog',
        'posts': posts
    }
    
    return render(
        request,
        "blog/index.html",
        context)

def example(request):
    print("example")
    
    context = {
        'text': 'Hello Example'
    }
    
    return render(
        request,
        "blog/example.html",
        context)