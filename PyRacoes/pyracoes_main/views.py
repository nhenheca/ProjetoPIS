from django.shortcuts import render
from .models import User, Animal,Ration
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")


def main(request):
    rations = Ration.objects.all()
    args = {"rations": rations}
    return render(request, "main.html", args)