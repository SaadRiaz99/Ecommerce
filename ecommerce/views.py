from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . import models


def home(request):
    return render(request, 'home.html')


def shop(request):
    return render(request, 'shop.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        txt_message = request.POST.get("message")
        contact.object.create(
            name = name , 
            email = email ,
            message = txt_message)
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")
        
    return render(request, 'contact.html')


def cart(request):
    return render(request, 'cart.html')


def login_signup(request):
    if request.method == "POST":
        form_type = request.POST.get('form_type')

        # LOGIN
        if form_type == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')   
            else:
                messages.error(request, "Invalid username or password")

        # SIGNUP
        elif form_type == 'signup':
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")

            if password != confirm_password:
                messages.error(request, "Passwords do not match")

            elif User.objects.filter(username=username).exists():   
                messages.error(request, "Username already exists")

            else:
                new_user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                login(request, new_user)   
                return redirect("home")

    return render(request, 'form.html')