from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def landing_page(request):
    return render(request, 'home.html',{'name': 'home'})

def news_page(request):
    return render(request, 'news.html',{'name': 'news'})

def forum_page(request):
    return render(request, 'forum.html',{'name': 'forum'})

def signup_page(request):
    return render(request, 'signup.html',{'name': 'signup'})

def class_page(request):
    return render(request, 'class-page.html',{'name': 'class'})

def patient_sign_up_page(request):
    return render(request, 'patient-sign-up-page.html',{'name': 'patient'})

def doctor_sign_up_page(request):
    return render(request, 'doctor-sign-up-page.html',{'name': 'doctor'})

def clinic_sign_up_page(request):
    return render(request, 'clinic-sign-up-page.html',{'name': 'clinic'})

def login_page(request):
    return render(request, 'login-page.html',{'name': 'login'})

