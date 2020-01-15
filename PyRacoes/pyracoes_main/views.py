from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from .models import User, Animal, Ration
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "index.html")


def signup(request):
    auth_logout(request)
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect("home")
    return render(request, 'signup.html', {'form': form})
    # return render(request, "signup.html")


def login(request):
    password = request.POST.get('password')
    username = request.POST.get('username')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect("home")
    else:
        return render(request, "login.html")


def home(request):
    rations = Ration.objects.all()
    args = {"rations": rations}
    if request.user.id == None:
        return render(request, "deny.html")
    else:
        return render(request, "home.html", args)


def logout(request):
    auth_logout(request)
    return render(request, "index.html")


def search(request):
    if request.method == 'POST':
        if form.is_valid():
            age = form.cleaned_data.get('age')
            atrib = form.cleaned_data.get('atrib')
            type = form.cleaned_data.get('type')
            port = form.cleaned_data.get('port')
            classification = form.cleaned_data.get('classification')
            Entry.objects.filter(ration_age=age, ration_atrib=atrib, ration_type=type, ration_port=port, ration_classification=classification)
    return render(request, "index.html")
