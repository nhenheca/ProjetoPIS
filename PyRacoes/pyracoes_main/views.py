from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import  authenticate
from .models import User, Animal,Ration
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")


def signup(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect(home)
    return render(request, 'signup.html', {'form': form})
    #return render(request, "signup.html")


def login(request):
    return render(request, "login.html")


def home(request):
    rations = Ration.objects.all()
    args = {"rations": rations}
    return render(request, "home.html", args)