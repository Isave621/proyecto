"""guiapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from principal.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/', formulario),
    path('contactar/', contactar),
    path('indexprincipal/', indexprincipal),
    path('tiporeserva/', ListadoTiporeserva.as_view(template_name = "tiporeserva/inicio.html"), name='leer'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tiporeserva o registro 
    path('tiporeserva/detalle/<int:pk>', TiporeservaDetalle.as_view(template_name = "tiporeserva/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tiporeserva o registro  
    path('tiporeserva/crear', TiporeservaCrear.as_view(template_name = "tiporeserva/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tiporeservao registro de la Base de Datos 
    path('tiporeserva/editar/<int:pk>', TiporeservaActualizar.as_view(template_name = "tiporeserva/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tiporeserva o registro de la Base de Datos 
    path('tiporeserva/eliminar/<int:pk>', TiporeservaEliminar.as_view(), name='tiporeserva/eliminar.html'), 


    path('comentarios/', ListadoComentarios.as_view(template_name = "comentarios/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un comentarios o registro 
    path('comentarios/detalle/<int:pk>', ComentariosDetalle.as_view(template_name = "comentarios/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo comentarios o registro  
    path('comentarios/crear', ComentariosCrear.as_view(template_name = "comentarios/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un comentarioso registro de la Base de Datos 
    path('comentarios/editar/<int:pk>', ComentariosActualizar.as_view(template_name = "comentarios/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un comentarios o registro de la Base de Datos 
    path('comentarios/eliminar/<int:pk>', ComentariosEliminar.as_view(), name='comentarios/eliminar.html'), 



    path('rutas/', ListadoRutas.as_view(template_name = "rutas/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un rutas o registro 
    path('rutas/detalle/<int:pk>', RutasDetalle.as_view(template_name = "rutas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo rutas o registro  
    path('rutas/crear', RutasCrear.as_view(template_name = "rutas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un rutaso registro de la Base de Datos 
    path('rutas/editar/<int:pk>', RutasActualizar.as_view(template_name = "rutas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un rutas o registro de la Base de Datos 
    path('rutas/eliminar/<int:pk>', RutasEliminar.as_view(), name='rutas/eliminar.html'),    
]
   



    
