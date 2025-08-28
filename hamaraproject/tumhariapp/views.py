# tumhariapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import SignUpForm  # custom signup form

# Home view
def home(request):
    return render(request, "home.html")

# About page
def about(request):
    return render(request, "about.html")

# Contact page
def contact(request):
    return render(request, "contact.html")

# Signup view
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "😄 Account created successfully! You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"😄 Welcome back, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "⚠️ Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

# Logout view
def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")
