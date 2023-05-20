from django.contrib import admin
from django.urls import path 
from web_app import views

urlpatterns = [
    path("", views.index, name='web_app'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("signup", views.handelsignup, name="handelsignup"),
    path("login", views.handellogin, name='handellogin'),
    path("logout", views.handellogout, name='handellogout'),
]