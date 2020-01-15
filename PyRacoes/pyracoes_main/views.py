from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from .models import User, Animal, Ration, Attributes
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
    atribs = Attributes.objects.all()
    args = {"atribs": atribs}
    if request.user.id == None:
        return render(request, "deny.html")
    else:
        return render(request, "home.html", args)


def logout(request):
    auth_logout(request)
    return render(request, "index.html")


def search(request):
    if request.method == 'POST':
        age = request.POST['age']
        atrib = request.POST['atrib']
        type = request.POST['type']
        port = request.POST['port']
        classification = request.POST['classification']
        aux = Entry.objects.filter(ration_age=age, ration_atrib=atrib, ration_type=type, ration_port=port, ration_classification=classification)
        args = {"aux": aux}
        return render(request, "home.html", args)
