from django.urls import path
from . import views
from .views import lista_materiales, crear_tratamiento, agregar_paciente

urlpatterns = [
    path('', views.signin, name="index"),
    path('index/', views.index, name='index'),
    path('inventario/', views.inventario, name='inventario'),
    path('ventas/', views.lista_tratamientos, name='ventas'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('pacientes/actualizar_paciente/<int:idpaciente>/', views.actualizar_paciente, name='actualizar_paciente'),
    path('pacientes/borrar_paciente/<int:idpaciente>/', views.borrar_paciente, name='borrar_paciente'),
    path('paciente/', agregar_paciente, name='agregar_paciente'),
    path('financiero/', views.financiero, name='financiero'),
    path('recursosHumanos/', views.recursosHumanos, name='recursosHumanos'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('factura/<int:idtratamientno>/', views.factura, name='factura'),
    path('tratamiento/', crear_tratamiento, name='crear_tratamiento'),
    path('inventario/agregar_material/', views.agregar_material, name='agregar_material'),
    path('inventario/borrar_material/<int:idmaterial>/', views.borrar_material, name='borrar_material'),
    path('inventario/actualizar_material/<int:idmaterial>/', views.actualizar_material, name='actualizar_material'),
    path('inventario/listaMateriales/', views.lista_materiales, name='lista_materiales'),
    path('inventario/buscar_material/', views.buscar_material, name='buscar_material'),
    path('inventario/resultado/', views.buscar_material, name='resultado_busqueda'),
    path('ventas/actualizar_tratamiento/<int:idtratamientno>/', views.actualizar_tratamiento, name='actualizar_tratamiento'),
    path('ventas/borrar_tratamiento/<int:idtratamientno>/', views.borrar_tratamiento, name='borrar_tratamiento'),
    path('enviar-factura/<int:idtratamientno>/', views.enviar_factura_email, name='enviar_factura_email'),
    path('confirmacion-factura/', views.confirmacion_factura, name='confirmacion_factura'),
    
    path('recursosHumanos/dentistas/', views.listar_dentistas, name='listar_dentistas'),
    path('recursosHumanos/dentistas/listar_dentistas/', views.listar_dentistas, name='listas_dentistas'),
    path('recursosHumanos/dentistas/agregar_dentista/', views.agregar_dentista, name='agregar_dentista'),
    path('recursosHumanos/eliminar_dentista/<int:iddentista>/', views.eliminar_dentista, name='eliminar_dentista'),
    path('recursosHumanos/actualizar_dentista/<int:iddentista>/', views.actualizar_dentista, name='actualizar_dentista'),

    path('recursosHumanosasistentes/', views.listar_asistentes, name='listar_asistentes'),
    path('recursosHumanos/asistente/listar_asistente/', views.listar_asistentes, name='listar_asistentes'),
    path('recursosHumanos/asistente/agregar_asistente/', views.agregar_asistente, name='agregar_asistente'),
    path('recursosHumanos/asistentes/<int:idasistente>/eliminar/', views.eliminar_asistente, name='eliminar_asistente'),
    path('recursosHumanos/actualizar_asistente/<int:idasistente>/', views.actualizar_asistente, name='actualizar_asistente'),
    
    path('ventas/<int:idtratamientno>/agregar_material', views.agregar_tratamiento_material, name='agregar_tratamiento_material'),
    path('ventas/<int:idtratamientno>/agregar_fecha_material/', views.guardar_fecha, name='guardar_fecha_material'),
    
    path('bussines-inteligence/', views.bussines, name='bussines'),

        
    path('citas', views.citas, name='citas'),     
    path('citas/agregar_citas/', views.agregar_cita, name='agregar_citas'),
    path('citas/actualizar_cita/<int:idcita>/', views.actualizar_cita, name='actualizar_cita'),
    path('citas/eliminar_cita/<int:idcita>/', views.eliminar_cita, name='eliminar_cita'),

    path('error/', views.error, name='error'),
]
