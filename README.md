# proyecto-pgy3131-django

 Proyecto con implemtenación de framework Django.

Habilitar (via PowerShell como administrador): **Set-ExecutionPolicy Unrestricted**

Nota:

Lo ideal es trabajar con la consola/bash/cmd/PowerShell de VSC (Siempre y cuando se utilice este IDLE)

# Instalación y ejecución de Django

1. **Instalar Python**

   - Descarga Python.
   - Instalar versión necesaria.
   - Nota: **SIEMPRE UTILIZAR UNA VERSIÓN DEFINIDA!!! En los pcs del Duoc puede variar.**
2. **Crear un Entorno Virtual**

   - Abrir PowerShell en Windows.
   - Navega al folder donde se necesite crear el proyecto:
     ```bash
     mkdir misProyectos (Si ha de ser necesario, ¿click derecho haters?)
     cd misProyectos
     ```
   - Crea el entorno virtual:
     ```bash
     python -m venv miEntorno
     ```
3. **Activar el Entorno Virtual**

   - ```bash
     .\miEntorno\Scripts\activate
     ```
4. **Instalar Django**

   - Actualizar pip:
     ```bash
     python -m pip install --upgrade pip
     ```
   - Crear un archivo `requirements.txt` con el contenido:
     ```text
     django>=4.0
     ```
   - Instalar los paquetes:
     ```bash
     pip install -r requirements.txt
     ```
5. **Crear un Proyecto Django**

   - En la raíz de la carpeta de proyectos:
     ```bash
     django-admin startproject miProyecto
     cd miProyecto
     ```
6. **Ejecutar el Servidor Local**

   - Dentro de la carpeta del proyecto:
     ```bash
     python manage.py runserver
     ```
   - Abrir: `http://127.0.0.1:8000/` para ver la página de inicio de Django.
7. **Crear una Aplicación en Django**

   - Dentro de la carpeta raíz del proyecto (donde está `manage.py`) ejecutar:
     ```bash
     python manage.py startapp miApp
     ```
8. **Registrar la Aplicación**

   - Abrir `settings.py` y agregar `'miApp'` a `INSTALLED_APPS`:
     ```python
     INSTALLED_APPS = [
         ...
         'miApp',
     ]
     ```
9. **Configurar Rutas**

   - En `miApp`, crear un archivo `urls.py` y agregar:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.index, name='index'),
     ]
     ```
   - En `urls.py` del proyecto (`miProyecto/urls.py`), incluír las rutas de `miApp`:
     ```python
     from django.urls import include, path

     urlpatterns = [
         path('miApp/', include('miApp.urls')),
     ]
     ```
10. **Crear una Vista**

    - En `views.py` de `miApp`, agregarr:
      ```python
      from django.http import HttpResponse

      def index(request):
          return HttpResponse("Hola, mundo!")
      ```
11. **Probar la Aplicación**

    - Ejecuta el servidor nuevamente:
      ```bash
      python manage.py runserver
      ```
    - Ejecutar via: `http://127.0.0.1:8000/miApp/` .
