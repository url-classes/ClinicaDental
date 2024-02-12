from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def index(request):
    title = "Clinica Dental"
    return render(request, "index.html", {"title": title})


def inventario(request):
    return render(request, "layouts/inventario.html")


def ventas(request):
    return render(request, "layouts/ventas.html")


def financiero(request):
    return render(request, "layouts/financiero.html")


def recursosHumanos(request):
    return render(request, "layouts/recursosHumanos.html")


def signup(request):

    if request.method == "GET":
        return render(request, "layouts/signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("index")
            except IntegrityError:
                return render(
                    request,
                    "layouts/signup.html",
                    {
                        "form": UserCreationForm,
                        "error": "El usuario ya existe",
                    },
                )
        return render(
            request,
            "layouts/signup.html",
            {"form": UserCreationForm, "error": "Las contrasenas no coinciden"},
        )


def signin(request):
    if request.method == "GET":
        return render(request, "layouts/login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "layouts/login.html",
                {
                    "form": AuthenticationForm,
                    "error": "El usuario o la constrasena es incorrecta",
                },
            )
        else:
            login(request, user)
            return redirect('index')

        
