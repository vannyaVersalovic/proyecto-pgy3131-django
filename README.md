
# Proyecto PGY3131 Django

Este proyecto es una implementación del framework Django.

## Requisitos Previos

Habilitar (via PowerShell como administrador):
```powershell
Set-ExecutionPolicy Unrestricted
```

> **Nota:** Se recomienda trabajar con la consola/bash/cmd/PowerShell de Visual Studio Code (si se está utilizando este IDE).

## Consideraciones

- Asegurarse de que la versión de Python sea la correcta modificando `env\pyvenv.cfg` según sea necesario.
- La estructura principal del proyecto es la siguiente:

```plaintext
django/
└── paginaWeb/
    ├── include/
    ├── lib/
    └── Scripts/
        └── pyvenv.cfg
└── proyectoPaginaWeb/
    └── proyectoPaginaWeb/
        ├── __pycache__/
        ├── static/
        │   ├── css/
        │   ├── img/
        │   └── js/
        └── templates/
            └── proyectoPaginaWeb/
                ├── Hombre.html
                ├── Infantil.html
                ├── Inicio.html
                ├── Mujer.html
                ├── Nosotros.html
                ├── Oversize.html
                └── Videos.html
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        ├── db.sqlite3
        └── manage.py
```

## Cambios / Notas

1. Ordenamiento de diferentes archivos en sus respectivas carpetas (Imágenes, CSS y JS).
2. Creación de un entorno virtual e implementación de Django (Revisar `django/paginaWeb/env/pyvenv.cfg` para la versión y PATH de Python).
3. Creación del folder `django` que contiene el proyecto `proyectoPaginaWeb` y el entorno virtual `paginaWeb`.
4. Dentro de `proyectoPaginaWeb` se encuentra otro `proyectoPaginaWeb`. Es preferible dejarlo así para evitar errores futuros.
5. Dentro de `django/proyectoPaginaWeb/proyectoPaginaWeb` se encuentran:
   - `static`: Contiene JS, imágenes y CSS.
   - `templates`: Contiene las vistas (archivos HTML).
   - Verificar siempre `urls.py` y `views.py`. `views.py` renderiza las vistas y `urls.py` asigna las rutas.

## Instalación y Ejecución de Django

### 1. Instalar Python

- Descarga Python desde su [sitio oficial](https://www.python.org/downloads/).
- Instalar la versión necesaria.
- **Nota:** Utilizar siempre una versión definida, especialmente en los PCs del Duoc.

### 2. Crear un Entorno Virtual

- Abrir PowerShell en Windows y navegar al folder donde se creará el proyecto:
  ```bash
  mkdir misProyectos
  cd misProyectos
  ```
- Crear el entorno virtual:
  ```bash
  python -m venv miEntorno
  ```

### 3. Activar el Entorno Virtual

- Activar el entorno virtual:
  ```bash
  .\miEntorno\Scripts ctivate
  ```

### 4. Instalar Django

- Actualizar pip:
  ```bash
  python -m pip install --upgrade pip
  ```
- Crear un archivo `requirements.txt` con el siguiente contenido:
  ```text
  django>=4.0
  ```
- Instalar los paquetes:
  ```bash
  pip install -r requirements.txt
  ```
  Alternativamente, usar:
  ```bash
  pip install django
  ```

### 5. Crear un Proyecto Django

- En la raíz de la carpeta de proyectos:
  ```bash
  django-admin startproject miProyecto
  cd miProyecto
  ```

### 6. Ejecutar el Servidor Local

- Dentro de la carpeta del proyecto:
  ```bash
  python manage.py runserver
  ```
- Abrir: `http://127.0.0.1:8000/` para ver la página de inicio de Django.

### 7. Crear una Aplicación en Django

- Dentro de la carpeta raíz del proyecto (donde está `manage.py`) ejecutar:
  ```bash
  python manage.py startapp miApp
  ```

### 8. Registrar la Aplicación

- Abrir `settings.py` y agregar `'miApp'` a `INSTALLED_APPS`:
  ```python
  INSTALLED_APPS = [
      ...
      'miApp',
  ]
  ```

### 9. Configurar Rutas

- En `miApp`, crear un archivo `urls.py` y agregar:
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```
- En `urls.py` del proyecto (`miProyecto/urls.py`), incluir las rutas de `miApp`:
  ```python
  from django.urls import include, path

  urlpatterns = [
      path('miApp/', include('miApp.urls')),
  ]
  ```

### 10. Crear una Vista

- En `views.py` de `miApp`, agregar:
  ```python
  from django.http import HttpResponse

  def index(request):
      return HttpResponse("Hola, mundo!")
  ```

### 11. Probar la Aplicación

- Ejecutar el servidor nuevamente:
  ```bash
  python manage.py runserver
  ```
- Navegar a `http://127.0.0.1:8000/miApp/` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

La estructura del proyecto Django es crucial para una buena organización y mantenimiento. A continuación, se detalla la estructura típica del proyecto:

### Directorio Principal: `django/paginaWeb/`

- `include/`: Contiene archivos de configuración del entorno virtual.
- `lib/`: Contiene las bibliotecas instaladas en el entorno virtual.
- `Scripts/`: Contiene los scripts ejecutables del entorno virtual.
- `pyvenv.cfg`: Archivo de configuración del entorno virtual.

### Directorio del Proyecto: `django/proyectoPaginaWeb/`

#### Subdirectorio del Proyecto: `django/proyectoPaginaWeb/proyectoPaginaWeb/`

- `__pycache__/`: Contiene archivos caché generados por Python.
- `static/`: Carpeta para archivos estáticos.
  - `css/`: Archivos CSS.
  - `img/`: Imágenes.
  - `js/`: Archivos JavaScript.
- `templates/`: Carpeta para plantillas HTML.
  - `proyectoPaginaWeb/`: Contiene las vistas específicas del proyecto.
    - `Hombre.html`
    - `Infantil.html`
    - `Inicio.html`
    - `Mujer.html`
    - `Nosotros.html`
    - `Oversize.html`
    - `Videos.html`
- `__init__.py`: Archivo para indicar que el directorio es un módulo de Python.
- `asgi.py`: Configuración para el servidor ASGI.
- `settings.py`: Configuraciones del proyecto Django.
- `urls.py`: Definición de las rutas del proyecto.
- `wsgi.py`: Configuración para el servidor WSGI.
- `db.sqlite3`: Base de datos SQLite.
- `manage.py`: Herramienta de línea de comandos para interactuar con el proyecto Django.

## Buenas Prácticas

### Uso de Entornos Virtuales

El uso de entornos virtuales es una práctica recomendada para mantener las dependencias del proyecto aisladas y evitar conflictos con otras aplicaciones. Siempre activar el entorno virtual antes de trabajar en el proyecto.

### Mantenimiento de Archivos Estáticos

Organizar los archivos estáticos (CSS, JS, imágenes) dentro de la carpeta `static` para una mejor gestión y acceso.

### Organización de Plantillas

Colocar las plantillas HTML dentro de la carpeta `templates` siguiendo una estructura coherente que facilite la navegación y el mantenimiento.

### Verificación de Archivos Clave

- `urls.py`: Asegurarse de que todas las rutas estén correctamente definidas y que incluyan las aplicaciones necesarias.
- `views.py`: Verificar que las vistas están correctamente implementadas y renderizan las plantillas adecuadas.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. **Fork el repositorio**.
2. **Clona tu fork**:
   ```bash
   git clone https://github.com/tu-usuario/proyecto-pgy3131-django.git
   ```
3. **Crea una rama** para tu característica o corrección:
   ```bash
   git checkout -b nombre-de-la-rama
   ```
4. **Realiza tus cambios** y realiza commits descriptivos:
   ```bash
   git commit -m "Descripción de los cambios"
   ```
5. **Envía tus cambios** al repositorio remoto:
   ```bash
   git push origin nombre-de-la-rama
   ```
6. **Crea un Pull Request** en GitHub.

## Contacto

Para cualquier duda o consulta, puedes contactarnos a través del correo [correo@ejemplo.com](mailto:correo@ejemplo.com).

---

¡Gracias por tu interés en contribuir a este proyecto!
