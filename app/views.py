from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Material, Usuario, TipoUsuario
from django.contrib.auth.hashers import make_password
from .forms import UsuarioSignupForm
from .backends import UsuarioBackend
from .forms import UsuarioLoginForm


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

def factura(request):
    return render(request, "layouts/factura.html")


def signup(request):
    if request.method == "GET":
        return render(request, "layouts/signup.html", {"form": UsuarioSignupForm()})
    else:
        form = UsuarioSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "layouts/signup.html", {"form": form})


def signin(request):
    if request.method == "GET":
        form = UsuarioLoginForm()
        return render(request, "layouts/login.html", {"form": form})
    else:
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            # Se usa el backend personalizado para autenticar al usuario
            backend = UsuarioBackend()
            usuario = backend.authenticate(request, username=form.cleaned_data['nombre_usuario'], password=form.cleaned_data['password'])
            if usuario:
                return redirect('index')
            else:
                return render(request, "layouts/login.html", {"form": form, "error": "Error de autenticación."})
        else:
            return render(request, "layouts/login.html", {"form": form})
        
def lista_materiales(request):
    materiales = Material.objects.all()  # Realiza la consulta a la base de datos
    return render(request, 'layouts/inventario.html', {'materiales': materiales})

        
