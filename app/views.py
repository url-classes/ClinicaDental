from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from app.utils import user_has_permisos
from .models import Material, Usuario, TipoUsuario, Tratamiento
from django.contrib.auth.hashers import make_password
from .forms import UsuarioSignupForm
from .backends import UsuarioBackend
from .forms import UsuarioLoginForm
from .forms import TratamientoForm
from .models import Material
from .forms import MaterialForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Tratamiento
from .models import TratamientoMaterial
from io import BytesIO
from .models import Dentista, Asistente
from .forms import DentistaForm, AsistenteForm
from django.db.models import F, FloatField, ExpressionWrapper

# Create your views here.

def index(request):
    title = "Clinica Dental"
    return render(request, "index.html", {"title": title})

@user_has_permisos(permisos_requeridos=['inventario'])
def inventario(request):
    materiales = Material.objects.all()
    return render(request, 'layouts/inventario.html', {'materiales': materiales})

@user_has_permisos(permisos_requeridos=['ventas'])
def ventas(request):
    return render(request, "layouts/ventas.html")

@user_has_permisos(permisos_requeridos=['financiero'])
def financiero(request):
    if hasattr(request.user, 'dentista_iddentista'):
        tratamientos = Tratamiento.objects.all()  # Recupera todos los objetos Tratamiento
        total_tratamientos = sum(tratamiento.precio for tratamiento in tratamientos)
    
        asistentes = Asistente.objects.all()  # Recupera todos los objetos Asistente
        total_asistentes = sum(asistente.salario for asistente in asistentes)

        tratamientos_materiales = TratamientoMaterial.objects.annotate(
            detalle_tratamiento=F('tratamiento_idtratamientno__detalle'), 
            descripcion_material=F('material_idmaterial__descripcion'),  
            precio_individual_material=F('material_idmaterial__precio_individual'),
            total_material=ExpressionWrapper(
                F('cantidad_utilizada') * F('precio_individual_material'),
                output_field=FloatField()
            )  
        ).values(
            'detalle_tratamiento', 'descripcion_material', 'cantidad_utilizada', 'precio_individual_material', 'total_material'
        )
        suma_total_material = sum(item['total_material'] for item in tratamientos_materiales)
        
        total_egresos = suma_total_material + total_asistentes
        
        impuesto = 0.05 * total_tratamientos
        
        total_ingresos = total_tratamientos - impuesto
        
        ganancia = total_ingresos - suma_total_material
        
        context = {
            'tratamientos': tratamientos,
            'total_tratamientos': total_tratamientos,
            'asistentes': asistentes,
            'total_asistentes': total_asistentes,
            'tratamientos_materiales': tratamientos_materiales,
            'suma_total_material': suma_total_material,
            'total_egresos': total_egresos,
            'impuesto': impuesto,
            'total_ingresos': total_ingresos,
            'ganancia': ganancia,
        }
    
        return render(request, 'layouts/financiero.html', context)
    else:
        return HttpResponseForbidden("No tienes permiso para acceder a esta sección.")

@user_has_permisos(permisos_requeridos=['recursos'])
def recursosHumanos(request):
    if hasattr(request.user, 'dentista_iddentista'):
        return render(request, "layouts/recursosHumanos.html")
    else:
        return HttpResponseForbidden("No tienes permiso para acceder a esta sección.")
    

def factura(request, idtratamientno):
    tratamiento = get_object_or_404(Tratamiento, pk=idtratamientno)
    total = tratamiento.precio * tratamiento.cantidad_citas
    return render(request, "layouts/factura.html", {'tratamiento': tratamiento, 'total': total, 'idtratamientno': idtratamientno})


def generar_pdf(request, idtratamientno):
    tratamiento = get_object_or_404(Tratamiento, pk=idtratamientno)
    cita = tratamiento.cita_idcita
    paciente = cita.paciente_idpaciente

    # Renderiza la plantilla HTML con los datos
    html_string = render_to_string('layouts/factura.html', {'tratamiento': tratamiento, 'cita': cita, 'paciente': paciente})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="factura.pdf"'

    # Convertir HTML a PDF
    resultado_pdf = BytesIO()
    pisa_status = pisa.CreatePDF(BytesIO(html_string.encode("UTF-8")), dest=resultado_pdf)
    resultado_pdf.seek(0)
    response.write(resultado_pdf.read())
    return response

def enviar_factura_email(request, idtratamientno):
    if request.method == 'POST':
        tratamiento = get_object_or_404(Tratamiento, pk=idtratamientno)
        cita = tratamiento.cita_idcita
        paciente = cita.paciente_idpaciente
        
        # Generar el contexto para tu plantilla
        context = {
            'tratamiento': tratamiento,
            'cita': cita,
            'paciente': paciente,
            'idtratamientno': idtratamientno,
        }

        # Renderizar la plantilla HTML con el contexto
        html_string = render_to_string('layouts/factura.html', context)
        
        # Convertir HTML a PDF
        resultado_pdf = BytesIO()
        pisa_status = pisa.CreatePDF(BytesIO(html_string.encode("UTF-8")), dest=resultado_pdf)
        resultado_pdf.seek(0)

        # Configura el correo electrónico
        email = EmailMessage(
            'Tu Factura de la Clínica Dental',  # Asunto
            'Aquí está tu factura adjunta.',  # Mensaje
            'especialidadeslapaz1@gmail.com',  # Email de origen
            ['paciente.correo_electronico'],  # Destinatario de prueba
            reply_to=['especialidadeslapaz1@gmail.com'],  # Opcional
        )
        email.attach('factura.pdf', resultado_pdf.getvalue(), 'application/pdf')  # Adjunta el PDF
        email.send()

        # Redirecciona a una página de confirmación o vuelve a la lista de tratamientos, por ejemplo
        return redirect('confirmacion_factura')
    else:
        # Si el método no es POST, puedes redireccionar a otra página o mostrar un mensaje de error
        return HttpResponse("Método no permitido", status=405)

def confirmacion_factura(request):
    return render(request, 'layouts/confirmacion_factura.html')

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
                # Establece la sesión para el usuario autenticado
                login(request, usuario)
                return redirect('index')
            else:
                return render(request, "layouts/login.html", {"form": form, "error": "Error de autenticación."})
        else:
            return render(request, "layouts/login.html", {"form": form})

def crear_tratamiento(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ventas")
    else:
        form = TratamientoForm()
    return render(request, 'layouts/tratamiento.html', {'form': form})

def lista_tratamientos(request):
    tratamientos = Tratamiento.objects.all()  # Recupera todos los objetos Tratamiento
    return render(request, 'layouts/ventas.html', {'tratamientos': tratamientos})

        
def agregar_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_materiales')
    else:
        form = MaterialForm()
    return render(request, 'layouts/agregar_material.html', {'form': form})

def borrar_material(request, idmaterial):
    material = Material.objects.get(pk=idmaterial)
    material.delete()
    return redirect('lista_materiales')

def actualizar_material(request, idmaterial):
    material = Material.objects.get(pk=idmaterial)
    form = MaterialForm(request.POST or None, instance=material)
    if form.is_valid():
        form.save()
        return redirect('lista_materiales')
    return render(request, 'layouts/actualizar_material.html', {'form': form})

def buscar_material(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion', '')
        material = Material.objects.filter(descripcion=descripcion).first()
        return render(request, 'layouts/resultado_busqueda.html', {'material': material})
    return render(request, 'layouts/buscar_material.html')


def lista_materiales(request):
    materiales = Material.objects.all()
    return render(request, 'layouts/lista_materiales.html', {'materiales': materiales})

def borrar_tratamiento(request, idtratamientno):
    tratamiento = Tratamiento.objects.get(pk=idtratamientno)
    tratamiento.delete()
    return redirect('ventas')

def actualizar_tratamiento(request, idtratamientno):
    if idtratamientno:
        tratamiento = get_object_or_404(Tratamiento, pk=idtratamientno)
    else:
        tratamiento = None
    form = TratamientoForm(request.POST or None, instance=tratamiento)
    if form.is_valid():
        form.save()
        return redirect('ventas')
    return render(request, 'layouts/actualizar_tratamiento.html', {'form': form})

# Funciones para Dentistas

def listar_dentistas(request):
    dentistas = Dentista.objects.all()
    return render(request, 'layouts/listar_dentistas.html', {'dentistas': dentistas})

def agregar_dentista(request):
    if request.method == 'POST':
        form = DentistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dentistas')  # Asegúrate de reemplazar esto con el nombre de tu URL
    else:
        form = DentistaForm()
    return render(request, 'layouts/agregar_dentistas.html', {'form': form})

def eliminar_dentista(request, iddentista):
    dentista = Dentista.objects.get(pk=iddentista)
    dentista.delete()
    return redirect('listar_dentistas')

def actualizar_dentista(request, iddentista):
    if iddentista:
        dentista = get_object_or_404(Dentista, pk=iddentista)
    else:
        dentista = None
    form = DentistaForm(request.POST or None, instance=dentista)
    if form.is_valid():
        form.save()
        return redirect('listar_dentistas')
    return render(request, 'layouts/actualizar_dentista.html', {'form': form})

# Funciones para Asistentes
def listar_asistentes(request):
    asistentes = Asistente.objects.all()
    return render(request, 'layouts/listar_asistentes.html', {'asistentes': asistentes})

def agregar_asistente(request):
    if request.method == 'POST':
        form = AsistenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_asistentes')  # Asegúrate de reemplazar esto con el nombre de tu URL
    else:
        form = AsistenteForm()
    return render(request, 'layouts/agregar_asistentes.html', {'form': form})

def eliminar_asistente(request, idasistente):
    asistente = Asistente.objects.get(pk=idasistente)
    asistente.delete()
    return redirect('listar_asistentes')

def actualizar_asistente(request, idasistente):
    if idasistente:
        asistente = get_object_or_404(Asistente, pk=idasistente)
    else:
        asistente = None
    form = AsistenteForm(request.POST or None, instance=asistente)
    if form.is_valid():
        form.save()
        return redirect('listar_asistentes')
    return render(request, 'layouts/actualizar_asistente.html', {'form': form})