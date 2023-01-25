from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page), #nie ma 
    path('forum/', views.forum_page), #nie ma
    path('signup/', views.signup_page), #zbedne
    path('classpage/', views.class_page, name='class'),
    path('patient-sign-up/', views.patient_sign_up_page, name='patient'),
    path('doctor-sign-up/', views.doctor_sign_up_page, name='doctor'),
    path('clinic-sign-up/', views.clinic_sign_up_page, name='clinic'),
    path('login/', views.login_page, name='login'),
    path('logout_user', views.logout_user, name = 'logout'),
    path('news/', views.news_page, name='news'),
    path('calendar/', views.calendar_page, name='calendar'), #Na tym sie poddaje
]
