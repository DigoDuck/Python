from django.shortcuts import render

def home(request):
    print("Home")
    return render(
        request,
        'home/index.html',
        {
            'text': 'We are at home'
        }
    )