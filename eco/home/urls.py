from django import views
from django.contrib import admin
from django.urls import path
from . import views
from home.views import home, contact,LOGINPAGE,RegistrationPage

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.LOGINPAGE,name="login"),
    path('register/',views.RegistrationPage,name='register')
]
if settings.DEBUG:
    urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
