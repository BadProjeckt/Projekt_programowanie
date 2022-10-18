from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.landing_page),
    path('news/', views.news_page),
    path('forum/', views.forum_page),
    path('login/', views.login_page),
    path('signup/', views.signup_page),
]
