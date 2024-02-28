from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Material, Usuario, TipoUsuario
from django.contrib.auth.hashers import make_password

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
        # Aquí debes pasar tu formulario personalizado si tienes uno
        return render(request, "layouts/signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Asumimos que TipoUsuario ya está definido, por ejemplo, "Usuario Regular"
                tipo_usuario = TipoUsuario.objects.get(descripcion="Usuario Regular")
                
                usuario = Usuario(
                    nombre_usuario=request.POST["username"],
                    password=make_password(request.POST["password1"]),
                    tipo_usuario_idtipo_usuario=tipo_usuario,
                    # Asegúrate de asignar los demás campos necesarios, como dentista_iddentista si es requerido
                )
                usuario.save()
                
                # login(request, user)  # La función login requiere un objeto User de Django. Considera crear una sesión manualmente o adaptar tu modelo Usuario.
                return redirect("index")
            except IntegrityError:
                return render(request, "layouts/signup.html", {"error": "El usuario ya existe"})
        else:
            return render(request, "layouts/signup.html", {"error": "Las contraseñas no coinciden"})


def signin(request):
    if request.method == "GET":
        return render(request, "layouts/login.html", {"form": AuthenticationForm})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        # Aquí necesitas implementar tu propia lógica de autenticación basada en tu modelo Usuario
        usuario = Usuario.objects.filter(nombre_usuario=username).first()
        if usuario and usuario.check_password(password):  # Necesitarás implementar check_password en tu modelo Usuario
            # login(request, user)  # Considera crear una sesión manualmente o adaptar tu modelo Usuario.
            return redirect('index')
        else:
            return render(request, "layouts/login.html", {"form": AuthenticationForm, "error": "El usuario o la contraseña es incorrecta"})
        
def lista_materiales(request):
    materiales = Material.objects.all()  # Realiza la consulta a la base de datos
    return render(request, 'layouts/inventario.html', {'materiales': materiales})

        
