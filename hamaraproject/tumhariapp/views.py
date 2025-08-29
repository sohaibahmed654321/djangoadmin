# tumhariapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import SignUpForm, ContaactForm
from django.core.mail import send_mail
from django.conf import settings


# custom signup form

# Home view
def home(request):
    return render(request, "home.html")

# About page
def about(request):
    return render(request, "about.html")

# Contact page
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB or send email (for now just showing message)
        messages.success(request, f"Thanks {name}, your message has been received! ✅")
        return redirect("contact")

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


# def Contaact_view(request):
#     if request.method == "POST":
#         form = ContaactForm(request.POST)
#         if form.is_valid():
#             form.save()  # ✅ save in database
#             return redirect('contact')  # form submit hone ke baad redirect
#     else:
#         form = ContaactForm()
#
#     return render(request, "contact.html", {"form": form})


def Contaact_view(request):
    if request.method == "POST":
        form = ContaactForm(request.POST)
        if form.is_valid():
            contact = form.save()   # ✅ Database me save

            # ✅ Email bhejna
            subject = f"New Contact Message from {contact.name}"
            message = f"""
You have received a new contact form submission:

Name: {contact.name}
Email: {contact.email}
Message:
{contact.message}
"""
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ["sohaib@gmail.com"],  # apna email daalo jahan receive karna hai
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
    else:
        form = ContaactForm()

    return render(request, "contact.html", {"form": form})
