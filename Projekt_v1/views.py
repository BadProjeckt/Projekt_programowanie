from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def landing_page(request):
    return render(request, 'home.html',{'name': 'home'})

def news_page(request):
    return render(request, 'news.html',{'name': 'news'})

def forum_page(request):
    return render(request, 'forum.html',{'name': 'forum'})

def login_page(request):
    return render(request, 'forum.html',{'name': 'login'})

