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
from principal.views import TiporeservaActualizar, TiporeservaCrear, TiporeservaDetalle, TiporeservaEliminar, ListadoTiporeserva, formulario, contactar, indexprincipal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/', formulario),
    path('contactar/', contactar),
    path('indexprincipal/', indexprincipal),
        path('Tiporeserva/', ListadoTiporeserva.as_view(template_name = "Tiporeserva/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tiporeserva o registro 
    path('Tiporeserva/detalle/<int:pk>', TiporeservaDetalle.as_view(template_name = "Tiporeserva/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tiporeserva o registro  
    path('Tiporeserva/crear', TiporeservaCrear.as_view(template_name = "Tiporeserva/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tiporeservao registro de la Base de Datos 
    path('Tiporeserva/editar/<int:pk>', TiporeservaActualizar.as_view(template_name = "Tiporeserva/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tiporeserva o registro de la Base de Datos 
    path('Tiporeserva/eliminar/<int:pk>', TiporeservaEliminar.as_view(), name='Tiporeserva/eliminar.html'), 

    ]
