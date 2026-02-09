
from django.shortcuts import render


def blog(request):
    print("blog")
    
    context = {
        'text': 'Hello Blog',
        'title': 'Blog - ',
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