from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.landing_page),
    path('news/', views.news_page),
    path('forum/', views.forum_page),
    path('login/', views.login_page),
    path('signup/', views.signup_page),
    path('classpage/', views.class_page),
    path('patient-sign-up/', views.patient_sign_up_page),
    path('doctor-sign-up/', views.doctor_sign_up_page),
    path('clinic-sign-up/', views.clinic_sign_up_page),
]
