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
from .forms import TratamientoForm, TratamientoMaterialForm, PacienteForm, CitasForm
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
from .models import Dentista, Asistente, Paciente, Factura, Cita
from .forms import DentistaForm, AsistenteForm
from django.db.models import F, FloatField, ExpressionWrapper
from django.db import transaction
from django.db.models import Count
import json
from .models import Paciente
from .models import Material
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.db import transaction
from django.utils import timezone

import subprocess
import datetime
import os
from django.conf import settings
import logging


# Create your views here.

def index(request, context = {}):
    title = "Clinica Dental"
    total_pacientes = Paciente.objects.count()
    material = Material.objects.count()
    dentista = Dentista.objects.count()
    asistente = Asistente.objects.count()
    tratamientos = Tratamiento.objects.count()
    
    context['total_pacientes'] = total_pacientes
    context['material'] = material
    context['dentista'] = dentista
    context['asistente'] = asistente
    context['tratamiento'] = tratamientos
    #{'total_pacientes': total_pacientes, 'material': material, 'dentista': dentista, 'asistente': asistente, 'tratamiento': tratamientos}
    return render(request, 'index.html', context)


def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'layouts/pacientes.html', {'pacientes': pacientes})

def actualizar_paciente(request, idpaciente):
    paciente = Paciente.objects.get(pk=idpaciente)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('pacientes')
    return render(request, 'layouts/actualizar_paciente.html', {'form': form})

def borrar_paciente(request, idpaciente):
    paciente = Paciente.objects.get(pk=idpaciente)
    
    # Cambiar el estado a 0 en lugar de eliminar el objeto
    paciente.estado = 0
    paciente.save()
    
    # Redirigir a la lista de materiales
    return redirect('pacientes')

def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes')
    else:
        form = PacienteForm()
    return render(request, 'layouts/agregar_paciente.html', {'form': form})

def bussines(request):
    asistentes_tratamientos = Tratamiento.objects.values('asistente_idasistente_id__nombre', 'asistente_idasistente_id__salario').annotate(total_tratamientos=Count('idtratamientno')).order_by('asistente_idasistente_id')
    
    # Crear listas para los labels, datos, salarios y bonificaciones
    labels = [item['asistente_idasistente_id__nombre'] for item in asistentes_tratamientos]
    data = [item['total_tratamientos'] for item in asistentes_tratamientos]
    salarios = [item['asistente_idasistente_id__salario'] for item in asistentes_tratamientos]
    bonificaciones = [100 * count if count >= 5 else 0 for count in data]  # 100 dólares por cada tratamiento a partir del quinto

    # Convertir a JSON para uso seguro en JavaScript
    context = {
        'labels_json': json.dumps(labels),
        'data_json': json.dumps(data),
        'salarios_json': json.dumps(salarios),
        'bonificaciones_json': json.dumps(bonificaciones),
    }
    return render(request, 'layouts/bussines.html', context)


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
            cantidad_material=F('material_idmaterial__cantidad'),  
            precio_individual_material=F('material_idmaterial__precio_individual'),
            total_material=ExpressionWrapper(
                F('cantidad_utilizada') * F('precio_individual_material'),
                output_field=FloatField()
            ),
            cantidad_material_despues=ExpressionWrapper(
                F('material_idmaterial__cantidad') - F('cantidad_utilizada'),
                output_field=FloatField()
            )  
        ).values(
            'detalle_tratamiento', 'descripcion_material', 'cantidad_material', 'cantidad_utilizada', 'cantidad_antes', 'cantidad_despues', 'fecha_transaccion', 'precio_individual_material', 'total_material', 'cantidad_material_despues'
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
    
def error(request):
    return render(request, 'layouts/error.html')

def factura(request, idtratamientno):
    tratamiento = get_object_or_404(Tratamiento, pk=idtratamientno)
    cita = tratamiento.cita_idcita
    paciente = cita.paciente_idpaciente
    
    try:
        with transaction.atomic():
            # Calcula el total basado en el tratamiento
            total = tratamiento.precio * tratamiento.cantidad_citas
            
            # Busca si ya existe una factura asociada al tratamiento
            factura = Factura.objects.filter(tratamiento_idtratamientno=tratamiento).first()
            
            if not factura:
                # Si no existe factura se crea
                factura = Factura.objects.create(
                    detalle=tratamiento.detalle,  
                    cantidad_servicios=tratamiento.cantidad_citas,
                    fecha=timezone.now(),  
                    total=total,
                    tratamiento_idtratamientno=tratamiento
                )
            else:
                # Si ya existe se actualiza el total
                factura.total = total
                factura.save()
            
            # Prepara el contexto para la plantilla
            context = {
                'tratamiento': tratamiento,
                'total': factura.total,
                'idtratamientno': idtratamientno,
                'paciente': paciente,
            }
        
        # Renderiza la plantilla con el contexto
        return render(request, "layouts/factura.html", context)
    
    except Exception as e:
        # Maneja cualquier error que ocurra durante la transacción
        context = {
            'error': 'Ocurrió un error al procesar la factura. Por favor, intenta nuevamente.',
            'detalle_error': str(e),
        }
        return render(request, "layouts/error.html", context)

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
        # Asegurándonos de que el correo electrónico del paciente es válido
        if paciente.correo_electronico and '@' in paciente.correo_electronico:
            email = EmailMessage(
                'Tu Factura de la Clínica Dental',  # Asunto
                'Aquí está tu factura adjunta.',  # Mensaje
                'especialidadeslapaz1@gmail.com',  # Email de origen
                [paciente.correo_electronico],  # Correo del destinatario
                reply_to=['especialidadeslapaz1@gmail.com'],  # Opcional
            )
            email.attach('factura.pdf', resultado_pdf.getvalue(), 'application/pdf')  # Adjunta el PDF
            email.send()

            # Redirecciona a una página de confirmación
            return redirect('confirmacion_factura')
        else:
            return HttpResponse("La dirección de correo electrónico del paciente no es válida", status=400)
    else:
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
    tratamientos = Tratamiento.objects.filter(estado=1)
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
    # Obtener la instancia de Material
    material = Material.objects.get(pk=idmaterial)
    
    # Cambiar el estado a 0 en lugar de eliminar el objeto
    material.estado = 0
    material.save()
    
    # Redirigir a la lista de materiales
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
    materiales = Material.objects.filter(estado=1)
    return render(request, 'layouts/lista_materiales.html', {'materiales': materiales})

def borrar_tratamiento(request, idtratamientno):
    # Obtener la instancia de Tratamiento
    tratamiento = Tratamiento.objects.get(pk=idtratamientno)
    
    # Cambiar el estado a 0 en lugar de eliminar el objeto
    tratamiento.estado = 0
    tratamiento.save()
    
    # Redirigir a la vista de ventas
    return redirect('ventas')

def agregar_tratamiento_material(request, idtratamientno):
    if request.method == 'POST':
        form = TratamientoMaterialForm(request.POST)
        if form.is_valid():
            tratamiento = get_object_or_404(Tratamiento, pk=idtratamientno)
            fecha_transaccion = request.POST.get("fecha_transaccion")
            logger = logging.getLogger(__name__)
            try:
                with transaction.atomic():
                    logger.error("Intentando insertar datos en la tabla TratamientoMaterial.")
                    for material in Material.objects.all():
                        material_seleccionado = form.cleaned_data.get(f'material_seleccionado_{material.idmaterial}', False)
                        cantidad_utilizada = form.cleaned_data.get(f'cantidad_{material.idmaterial}', 0)

                        if material_seleccionado and cantidad_utilizada > 0:
                            tratamiento_material = TratamientoMaterial.objects.create(
                                tratamiento_idtratamientno=tratamiento, 
                                material_idmaterial=material,  
                                cantidad_utilizada=cantidad_utilizada, 
                                cantidad_antes=material.cantidad,
                                cantidad_despues=material.cantidad - cantidad_utilizada, 
                                fecha_transaccion=fecha_transaccion
                            )


                            # if not created:
                            #     pass
                            #     tratamiento_material.cantidad_utilizada = cantidad_utilizada
                            #     tratamiento_material.cantidad_antes = material.cantidad
                            #     tratamiento_material.cantidad_despues = material.cantidad - cantidad_utilizada
                            #     tratamiento_material.fecha_transaccion = fecha_transaccion
                            #     tratamiento_material.save()

                            # material.cantidad = tratamiento_material.cantidad_despues
                            # material.save()

                    # Registrar en la bitácora como exitosa si no hubo excepción
                    registrar_bitacora(
                        numero_transaccion=tratamiento.idtratamientno,
                        tipo_transaccion='Agregar tratamiento material',
                        estado='Exitosa',
                        fecha_transaccion=fecha_transaccion
                    )

                return redirect('ventas')

            except Exception as e:
                if 'tratamiento_material' in locals():
                    tratamiento_material.delete()
                
                # Registrar en la bitácora como fallida si hubo excepción
                registrar_bitacora(
                    numero_transaccion=tratamiento.idtratamientno,
                    tipo_transaccion='Agregar tratamiento material',
                    estado='Fallida',
                    fecha_transaccion=fecha_transaccion
                )

                context = {
                    'error': 'Ocurrió un error al procesar el tratamiento y actualizar el inventario.',
                    'detalle_error': str(e),
                }
                logger.error(f"Transacción fallida: {str(e)}")
                return render(request, 'layouts/error.html', context)
        
        else:
            # Manejar el caso donde el formulario no es válido
            context = {'form': form, 'error': 'Formulario inválido. Por favor, revisa los datos ingresados.'}
            return render(request, 'layouts/agregar_tratamiento_material.html', context)

    else:
        form = TratamientoMaterialForm()

    return render(request, 'layouts/agregar_tratamiento_material.html', {'form': form})

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
    dentistas = Dentista.objects.filter(estado=1)
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
    # Obtener la instancia de Dentista
    dentista = Dentista.objects.get(pk=iddentista)
    
    # Cambiar el estado a 0 en lugar de eliminar el objeto
    dentista.estado = 0
    dentista.save()
    
    # Redirigir a la lista de dentistas
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
    asistentes = Asistente.objects.filter(estado=1)
    return render(request, 'layouts/listar_asistentes.html', {'asistentes': asistentes})

def agregar_asistente(request):
    if request.method == 'POST':
        form = AsistenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_asistentes')  
    else:
        form = AsistenteForm()
    return render(request, 'layouts/agregar_asistentes.html', {'form': form})

def eliminar_asistente(request, idasistente):
    # Obtener la instancia del Asistente
    asistente = Asistente.objects.get(pk=idasistente)
    
    # Cambiar el estado a 0 para marcar el asistente como inactivo
    asistente.estado = 0
    asistente.save()
    
    # Redirigir a la lista de asistentes
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

def guardar_fecha(request, idtratamientno):
    # Si es POST, se procesa el formulario
    if request.method == "POST":
        fecha_transaccion = request.POST.get("fecha_transaccion")
        tratamiento = get_object_or_404(Tratamiento, pk=idtratamientno)

        TratamientoMaterial.objects.create(
            tratamiento_idtratamientno=tratamiento,
            fecha_transaccion=fecha_transaccion,
            # Configura otros campos según sea necesario
        )

        # Redirige después de guardar la fecha
        return redirect('ventas')
    else:
        return render(request, 'layouts/seleccionar_fecha.html', {'idtratamientno': idtratamientno})
    
def citas(request):
    citas = Cita.objects.filter(estado=1)  # Fetch all cita objects
    citas_data = serialize('json', citas)  # Serialize the queryset to JSON
    #print("Serialized data:", citas_data)

    # Create a context dictionary to pass both the queryset and the serialized data
    context = {
        'citas': citas,          # Pass the queryset (optional if only needed serialized)
        'citas_json': citas_data # Serialized JSON data for JavaScript usage
    }

    # Render the response with the context
    return render(request, 'layouts/citas.html', context)

def agregar_cita(request):
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cita ha sido agregada con éxito.')
            return redirect('citas')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CitasForm()
    return render(request, 'layouts/agregar_citas.html', {'form': form})

def eliminar_cita(request, idcita):
    # Obtener la instancia de Cita
    cita = Cita.objects.get(pk=idcita)
    
    # Cambiar el estado a 0 en lugar de eliminar el objeto
    cita.estado = 0
    cita.save()
    
    # Redirigir a la lista de citas
    return redirect('citas')

def actualizar_cita(request, idcita):
    if idcita:
        cita = get_object_or_404(Cita, pk=idcita)
    else:
        cita = None
    form = CitasForm(request.POST or None, instance=cita)
    if form.is_valid():
        form.save()
        return redirect('citas')
    return render(request, 'layouts/agregar_citas.html', {'form': form})


def db_backup(request):
    usr = "root"
    password = "root"
    host = "localhost"
    database = "clinica_dental"
    file_path = "D:backup_clinicadental.sql"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#    file_name = f"clinicadental_backup_{timestamp}.sql"
    command = f"mariadb-dump -h{host} -u{usr} -p{password} --add-drop-database -B {database} > {file_path}"
    try:
        subprocess.run(command, shell=True)
        messages.success(request,"Backup exitoso")
    except:
        messages.error(request, "Error al realizar el backup")
        return render(request, 'layouts/error.html')
    return redirect('index')

@user_has_permisos(permisos_requeridos=["financiero"])
def db_restore(request):
    usr = "root"
    password = "root"
    host = "localhost"
    file_path = "E:backup_clinicadental.sql"

    command = f"mariadb -h{host} -u{usr} -p{password} < {file_path}"
    try:
        subprocess.run(command, shell=True)
        messages.success(request, "Restauracion exitosa")
    except:
        messages.error(request, "Error al realizar backup")
        return render(request, 'layouts/error.html')
    return redirect('index')

def descargar_bitacora(request):
    # Ruta del archivo de bitácora
    file_path = os.path.join(settings.BASE_DIR, 'Documentacion', 'bitacora.txt')

    # Intentar abrir el archivo y leer su contenido
    try:
        with open(file_path, 'r') as file:
            bitacora_contenido = file.read()
    except FileNotFoundError:
        # Manejar el caso en que el archivo no exista
        bitacora_contenido = "No se encontró ninguna bitácora."

    # Crear una respuesta HTTP con el contenido del archivo
    response = HttpResponse(bitacora_contenido, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="bitacora.txt"'
    
    return response

def obtener_siguiente_id():
    file_path = os.path.join(settings.BASE_DIR, 'Documentacion', 'bitacora.txt')
    if not os.path.exists(file_path):
        return 1

    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("ID de transacción:"):
                count += 1
    return count + 1

def registrar_bitacora(numero_transaccion, tipo_transaccion, estado, fecha_transaccion, cantidad_antes=None, cantidad_despues=None):
    folder_path = os.path.join(settings.BASE_DIR, 'Documentacion')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    archivo_bitacora = os.path.join(folder_path, 'bitacora.txt')

    # Obtener el siguiente ID de transacción
    id_transaccion = obtener_siguiente_id()

    # Crear una nueva entrada de bitácora
    nueva_entrada = (
        f"Numero de Transaccion: {numero_transaccion}\n"
        f"ID de transacción: {id_transaccion}\n"
        f"Tipo de Transaccion: {tipo_transaccion}\n"
        f"Estado: {estado}\n"
        f"Fecha de Transaccion: {fecha_transaccion}\n"
        "--------------------------\n"
    )

    # Agregar la entrada al archivo
    with open(archivo_bitacora, 'a') as file:
        file.write(nueva_entrada)