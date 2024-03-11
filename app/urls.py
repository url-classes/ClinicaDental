from django.urls import path
from . import views
from .views import lista_materiales, crear_tratamiento

urlpatterns = [
    path('', views.signin, name="index"),
    path('index/', views.index, name='index'),
    path('inventario/', views.inventario, name='inventario'),
    path('ventas/', views.lista_tratamientos, name='ventas'),
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
    path('ventas/actualizar_tratamiento/<int:idtratamientno>/', views.actualizar_tratamiento, name='actualizar_tratamiento'),
    path('ventas/borrar_tratamiento/<int:idtratamientno>/', views.borrar_tratamiento, name='borrar_tratamiento'),
]