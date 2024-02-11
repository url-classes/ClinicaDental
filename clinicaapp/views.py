from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def index(request):
    title = 'Clinica Dental'
    return render(request, 'index.html', {
        'title': title
    })


def inventario(request):
    return render(request, 'layouts/inventario.html')

def ventas(request):
    return render(request, 'layouts/ventas.html')

def financiero(request):
    return render(request, 'layouts/financiero.html')

def recursosHumanos(request):
    return render(request, 'layouts/recursosHumanos.html')