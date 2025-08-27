from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Hamara Project 🚀")

urlpatterns = [
    path('', home, name='home'),
]
