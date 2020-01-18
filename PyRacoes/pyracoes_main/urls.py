from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
    path("addAnimalPage/", views.addAnimalPage, name="addAnimalPage"),
    path("editAnimalPage/", views.editAnimalPage, name="editAnimalPage"),
    path("search/", views.search, name="search"),
    path("addAnimal/", views.addAnimal, name="addAnimal"),
    path("editAnimal/", views.editAnimal, name="editAnimal")
]