from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('shop/', views.shop , name = 'shop'),
    path('contact/', views.shop , name = 'contact')
    
]