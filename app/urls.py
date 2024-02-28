from django.urls import path
from . import views
from .views import lista_materiales

urlpatterns = [
    path('', views.index, name="index"),
    path('inventario/', views.inventario, name='inventario'),
    path('ventas/', views.ventas, name='ventas'),
    path('financiero/', views.financiero, name='financiero'),
    path('recursosHumanos/', views.recursosHumanos, name='recursosHumanos'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('factura/', views.factura, name='factura'),
    path('materiales/', lista_materiales, name='lista_materiales'),
    
]