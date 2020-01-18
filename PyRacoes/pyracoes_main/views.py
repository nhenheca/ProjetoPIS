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


def edit(request):
    return render(request, "edit.html")


def search(request):
    if request.method == 'POST':
        ration_age = request.POST['ration_age']
        ration_atrib = request.POST['ration_atrib']
        ration_type = request.POST['ration_type']
        ration_port = request.POST['ration_port']
        ration_classification = request.POST['ration_classification']
        aux = Ration.objects.all().filter(ration_age__age_name=ration_age).filter(ration_atrib__attributes_name=ration_atrib).filter(ration_type__type_name=ration_type).filter(ration_port__port_name=ration_port).filter(ration_classification__classification_name=ration_classification)
        args = {"aux": aux}
        return render(request, "home.html", args)


