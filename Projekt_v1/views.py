from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def landing_page(request):
    return render(request, 'home.html',{'name': 'home'})

def forum_page(request):
    return render(request, 'forum.html',{'name': 'forum'})

def signup_page(request):
    return render(request, 'signup.html',{'name': 'signup'})

def class_page(request):
    return render(request, 'class-page.html',{'name': 'class'})

def news_page(request):
    return render(request, 'news-page.html',{'name': 'news'})

def calendar_page(request):
    return render(request, 'calendar-page.html',{'name': 'calendar'})

def login_page(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('news')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'login-page.html', {})

def logout_user(request):
    logout (request)
    return redirect('news')

def patient_sign_up_page(request):
    return render(request, 'patient-sign-up-page.html',{'name': 'patient'})

def doctor_sign_up_page(request):
    return render(request, 'doctor-sign-up-page.html',{'name': 'doctor'})

def clinic_sign_up_page(request):
    return render(request, 'clinic-sign-up-page.html',{'name': 'clinic'})