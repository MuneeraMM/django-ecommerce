from django import views
from django.contrib import admin
from django.urls import path
from . import views
from home.views import home, contact,LOGINPAGE,RegistrationPage

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.LOGINPAGE,name="login"),
    path('register/',views.RegistrationPage,name='register')
]
