from django.urls import path
from . import views
from .views import lista_materiales, crear_tratamiento

urlpatterns = [
    path('', views.index, name="index"),
    path('inventario/', views.inventario, name='inventario'),
    path('ventas/', views.lista_tratamientos, name='ventas'),
    path('financiero/', views.financiero, name='financiero'),
    path('recursosHumanos/', views.recursosHumanos, name='recursosHumanos'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('factura/', views.factura, name='factura'),
    path('materiales/', lista_materiales, name='lista_materiales'),
    path('tratamiento/', crear_tratamiento, name='crear_tratamiento'),
    path('agregar_material/', views.agregar_material, name='agregar_terial'),
    path('borrar_material/<int:idmaterial>/', views.borrar_material, name='borrar_material'),
    path('actualizar_material/<int:idmaterial>/', views.actualizar_material, name='actualizar_material'),
    path('listaMateriales ', views.lista_materiales, name='lista_materiales')
]