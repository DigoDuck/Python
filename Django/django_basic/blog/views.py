
from django.shortcuts import render


def blog(request):
    print("blog")
    return render(
        request,
        "blog/index.html")

def example(request):
    print("blog1")
    return render(
        request,
        "blog/example.html")