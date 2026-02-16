
from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404

def blog(request):
    
    context = {
        # 'text': 'Hello Blog',
        'posts': posts
    }
    
    return render(
        request,
        "blog/index.html",
        context)
    
def post(req: HttpRequest, post_id: int):
    found_post: dict[str, Any ] | None = None
    
    for post  in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post  is None:
        raise Http404('post not exist')
    
    context = {
        # 'text': 'Hello Blog',
        'post': found_post,
        'title': found_post['title']  + ' - '
    }
    
    return render(
        req,
        "blog/post.html",
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