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
from re import template
from django.contrib import admin
from django.urls import path
from principal.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/', formulario),
    path('contactar/', contactar),
    path('indexprincipal/', indexprincipal),
    path('inicio/', inicio),
    path('comienzo/', comienzo),
    path('comienzo/usuario/', usuario),
    path('comienzo/clienteUs/', clienteUs),
    path('comienzo/usuario/treserva/', ListadoTiporeserva.as_view(template_name = "tiporeserva/inicio.html"),),
    path('comienzo/clienteUs/comentario/', ListadoComentarios.as_view(template_name = "comentarios/inicio.html"),),

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


    path('tipolugar/', ListadoTipolugar.as_view(template_name = "tipolugar/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipolugar o registro 
    path('tipolugar/detalle/<int:pk>', TipolugarDetalle.as_view(template_name = "tipolugar/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo tipolugar o registro  
    path('tipolugar/crear', TipolugarCrear.as_view(template_name = "tipolugar/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un tipolugaro registro de la Base de Datos 
    path('tipolugar/editar/<int:pk>', TipolugarActualizar.as_view(template_name = "tipolugar/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un tipolugar o registro de la Base de Datos 
    path('tipolugar/eliminar/<int:pk>', TipolugarEliminar.as_view(), name='tipolugar/eliminar.html'),    
    
    

    path('empresa/', ListadoEmpresa.as_view(template_name = "empresa/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un empresa o registro 
    path('empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "empresa/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo empresa o registro  
    path('empresa/crear', EmpresaCrear.as_view(template_name = "empresa/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un empresao registro de la Base de Datos 
    path('empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "empresa/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un empresa o registro de la Base de Datos 
    path('empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='empresa/eliminar.html'),
    





    path('estadocliente/', ListadoEstadocliente.as_view(template_name = "estadocliente/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Estadocliente o registro 
    path('estadocliente/detalle/<int:pk>', EstadoclienteDetalle.as_view(template_name = "estadocliente/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Estadocliente o registro  
    path('estadocliente/crear', EstadoclienteCrear.as_view(template_name = "estadocliente/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Estadoclienteo registro de la Base de Datos 
    path('estadocliente/editar/<int:pk>', EstadoclienteActualizar.as_view(template_name = "estadocliente/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Estadocliente o registro de la Base de Datos 
    path('estadocliente/eliminar/<int:pk>', EstadoclienteEliminar.as_view(), name='estadocliente/eliminar.html'),    

    
    
    
    path('tipodocumento/', ListadoTipodocumento.as_view(template_name = "tipodocumento/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipodocumento o registro 
    path('tipodocumento/detalle/<int:pk>', TipodocumentoDetalle.as_view(template_name = "tipodocumento/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tipodocumento o registro  
    path('tipodocumento/crear', TipodocumentoCrear.as_view(template_name = "tipodocumento/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipodocumentoo registro de la Base de Datos 
    path('tipodocumento/editar/<int:pk>', TipodocumentoActualizar.as_view(template_name = "tipodocumento/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tipodocumento o registro de la Base de Datos 
    path('tipodocumento/eliminar/<int:pk>', TipodocumentoEliminar.as_view(), name='tipodocumento/eliminar.html'),    




    path('reservas/', ListadoReservas.as_view(template_name = "reservas/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Reservas o registro 
    path('reservas/detalle/<int:pk>', ReservasDetalle.as_view(template_name = "reservas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Reservas o registro  
    path('reservas/crear', ReservasCrear.as_view(template_name = "reservas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Reservaso registro de la Base de Datos 
    path('reservas/editar/<int:pk>', ReservasActualizar.as_view(template_name = "reservas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Reservas o registro de la Base de Datos 
    path('reservas/eliminar/<int:pk>', ReservasEliminar.as_view(), name='reservas/eliminar.html'),    

 

   #path('Serviciotour/', ListadoServiciotour.as_view(template_name = "Serviciotour/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Serviciotour o registro 
    #path('Serviciotour/detalle/<int:pk>', ServiciotourDetalle.as_view(template_name = "Serviciotour/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Serviciotour o registro  
    #path('Serviciotour/crear', ServiciotourCrear.as_view(template_name = "Serviciotour/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Serviciotouro registro de la Base de Datos 
    #path('Serviciotour/editar/<int:pk>', ServiciotourActualizar.as_view(template_name = "Serviciotour/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Serviciotour o registro de la Base de Datos 
    #path('Serviciotour/eliminar/<int:pk>', ServiciotourEliminar.as_view(), name='Serviciotour/eliminar.html'),
]


    

    

   



    
