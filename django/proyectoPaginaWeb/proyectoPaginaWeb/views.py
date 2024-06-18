# Ruta de este archvio proyectoPaginaWeb/proyectoPaginaWeb/views.py


# Estas funciones harán el renderizado para visualizar las vistas en las 
# respectivas URL (Indicadas en el README.md)
from django.shortcuts import render

def inicio(request):
    return render(request, 'proyectoPaginaWeb/Inicio.html')

def hombre(request):
    return render(request, 'proyectoPaginaWeb/Hombre.html')

def infantil(request):
    return render(request, 'proyectoPaginaWeb/Infantil.html')

def mujer(request):
    return render(request, 'proyectoPaginaWeb/Mujer.html')

def nosotros(request):
    return render(request, 'proyectoPaginaWeb/Nosotros.html')

def oversize(request):
    return render(request, 'proyectoPaginaWeb/Oversize.html')

def videos(request):
    return render(request, 'proyectoPaginaWeb/Videos.html')

def carrito(request):
    return render(request, 'proyectoPaginaWeb/carrito.html')
