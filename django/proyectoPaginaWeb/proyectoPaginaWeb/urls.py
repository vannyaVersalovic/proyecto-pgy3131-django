"""
URL configuration for proyectoPaginaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Ruta actual proyectoPaginaWeb/proyectoPaginaWeb/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('hombre/', views.hombre, name='hombre'),
    path('infantil/', views.infantil, name='infantil'),
    path('mujer/', views.mujer, name='mujer'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('oversize/', views.oversize, name='oversize'),
    path('videos/', views.videos, name='videos'),
    path('carrito/', views.carrito, name='carrito')
]
