from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('shop/', views.shop , name = 'shop'),
    path('contact/', views.contact , name = 'contact'),
    path('cart/', views.cart , name = 'cart'),
    path('login_signup/', views.login_signup , name = 'login_signup')
    
]