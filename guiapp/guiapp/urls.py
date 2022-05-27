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

    path('comienzo/clienteUs/comentario/', ListadoComentarios.as_view(template_name = "comentarios/inicio.html"),),

    path('comienzo/usuario/tiporeserva/', ListadoTiporeserva.as_view(template_name = "tiporeserva/inicio.html"), name='leer'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tiporeserva o registro 
    path('comienzo/usuario/tiporeserva/detalle/<int:pk>', TiporeservaDetalle.as_view(template_name = "tiporeserva/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tiporeserva o registro  
    path('comienzo/usuario/tiporeserva/crear', TiporeservaCrear.as_view(template_name = "tiporeserva/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tiporeservao registro de la Base de Datos 
    path('comienzo/usuario/tiporeserva/editar/<int:pk>', TiporeservaActualizar.as_view(template_name = "tiporeserva/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tiporeserva o registro de la Base de Datos 
    path('comienzo/usuario/tiporeserva/eliminar/<int:pk>', TiporeservaEliminar.as_view(), name='tiporeserva/eliminar.html'), 


    path('comienzo/clienteUs/comentarios/', ListadoComentarios.as_view(template_name = "comentarios/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un comentarios o registro 
    path('comienzo/clienteUs/comentarios/detalle/<int:pk>', ComentariosDetalle.as_view(template_name = "comentarios/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo comentarios o registro  
    path('comienzo/clienteUs/comentarios/crear', ComentariosCrear.as_view(template_name = "comentarios/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un comentarioso registro de la Base de Datos 
    path('comienzo/clienteUs/comentarios/editar/<int:pk>', ComentariosActualizar.as_view(template_name = "comentarios/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un comentarios o registro de la Base de Datos 
    path('comienzo/clienteUs/comentarios/eliminar/<int:pk>', ComentariosEliminar.as_view(), name='comentarios/eliminar.html'), 



    path('comienzo/usuario/rutas/', ListadoRutas.as_view(template_name = "rutas/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un rutas o registro 
    path('comienzo/usuario/rutas/detalle/<int:pk>', RutasDetalle.as_view(template_name = "rutas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo rutas o registro  
    path('comienzo/usuario/rutas/crear', RutasCrear.as_view(template_name = "rutas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un rutaso registro de la Base de Datos 
    path('comienzo/usuario/rutas/editar/<int:pk>', RutasActualizar.as_view(template_name = "rutas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un rutas o registro de la Base de Datos 
    path('comienzo/usuario/rutas/eliminar/<int:pk>', RutasEliminar.as_view(), name='rutas/eliminar.html'),    


    path('comienzo/usuario/tipolugar/', ListadoTipolugar.as_view(template_name = "tipolugar/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipolugar o registro 
    path('comienzo/usuario/tipolugar/detalle/<int:pk>', TipolugarDetalle.as_view(template_name = "tipolugar/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo tipolugar o registro  
    path('comienzo/usuario/tipolugar/crear', TipolugarCrear.as_view(template_name = "tipolugar/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un tipolugaro registro de la Base de Datos 
    path('comienzo/usuario/tipolugar/editar/<int:pk>', TipolugarActualizar.as_view(template_name = "tipolugar/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un tipolugar o registro de la Base de Datos 
    path('comienzo/usuario/tipolugar/eliminar/<int:pk>', TipolugarEliminar.as_view(), name='tipolugar/eliminar.html'),    
    
    

    path('comienzo/clienteUs/empresa/', ListadoEmpresa.as_view(template_name = "empresa/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un empresa o registro 
    path('comienzo/clienteUs/empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "empresa/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo empresa o registro  
    path('comienzo/clienteUs/empresa/crear', EmpresaCrear.as_view(template_name = "empresa/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un empresao registro de la Base de Datos 
    path('comienzo/clienteUs/empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "empresa/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un empresa o registro de la Base de Datos 
    path('comienzo/clienteUs/empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='empresa/eliminar.html'),
    





    path('comienzo/usuario/estadocliente/', ListadoEstadocliente.as_view(template_name = "estadocliente/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Estadocliente o registro 
    path('comienzo/usuario/estadocliente/detalle/<int:pk>', EstadoclienteDetalle.as_view(template_name = "estadocliente/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Estadocliente o registro  
    path('comienzo/usuario/estadocliente/crear', EstadoclienteCrear.as_view(template_name = "estadocliente/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Estadoclienteo registro de la Base de Datos 
    path('comienzo/usuario/estadocliente/editar/<int:pk>', EstadoclienteActualizar.as_view(template_name = "estadocliente/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Estadocliente o registro de la Base de Datos 
    path('comienzo/usuario/estadocliente/eliminar/<int:pk>', EstadoclienteEliminar.as_view(), name='estadocliente/eliminar.html'),    

    
    
    
    path('comienzo/usuario/tipodocumento/', ListadoTipodocumento.as_view(template_name = "tipodocumento/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipodocumento o registro 
    path('comienzo/usuario/tipodocumento/detalle/<int:pk>', TipodocumentoDetalle.as_view(template_name = "tipodocumento/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tipodocumento o registro  
    path('comienzo/usuario/tipodocumento/crear', TipodocumentoCrear.as_view(template_name = "tipodocumento/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipodocumentoo registro de la Base de Datos 
    path('comienzo/usuario/tipodocumento/editar/<int:pk>', TipodocumentoActualizar.as_view(template_name = "tipodocumento/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tipodocumento o registro de la Base de Datos 
    path('comienzo/usuario/tipodocumento/eliminar/<int:pk>', TipodocumentoEliminar.as_view(), name='tipodocumento/eliminar.html'),    




    path('comienzo/clienteUs/reservas/', ListadoReservas.as_view(template_name = "reservas/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Reservas o registro 
    path('comienzo/clienteUs/reservas/detalle/<int:pk>', ReservasDetalle.as_view(template_name = "reservas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Reservas o registro  
    path('comienzo/clienteUs/reservas/crear', ReservasCrear.as_view(template_name = "reservas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Reservaso registro de la Base de Datos 
    path('comienzo/clienteUs/reservas/editar/<int:pk>', ReservasActualizar.as_view(template_name = "reservas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Reservas o registro de la Base de Datos 
    path('comienzo/clienteUs/reservas/eliminar/<int:pk>', ReservasEliminar.as_view(), name='reservas/eliminar.html'),    

 

    path('comienzo/usuario/serviciotour/', ListadoServiciotour.as_view(template_name = "serviciotour/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Serviciotour o registro 
    path('comienzo/usuario/serviciotour/detalle/<int:pk>', ServiciotourDetalle.as_view(template_name = "serviciotour/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Serviciotour o registro  
    path('comienzo/usuario/serviciotour/crear', ServiciotourCrear.as_view(template_name = "serviciotour/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Serviciotouro registro de la Base de Datos 
    path('comienzo/usuario/serviciotour/editar/<int:pk>', ServiciotourActualizar.as_view(template_name = "serviciotour/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Serviciotour o registro de la Base de Datos 
    path('comienzo/usuario/serviciotour/eliminar/<int:pk>', ServiciotourEliminar.as_view(), name='serviciotour/eliminar.html'),




    path('comienzo/usuario/ofertas/', ListadoOfertas.as_view(template_name = "ofertas/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Ofertas o registro 
    path('comienzo/usuario/ofertas/detalle/<int:pk>', OfertasDetalle.as_view(template_name = "ofertas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Ofertas o registro  
    path('comienzo/usuario/ofertas/crear', OfertasCrear.as_view(template_name = "ofertas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Ofertaso registro de la Base de Datos 
    path('comienzo/usuario/ofertas/editar/<int:pk>', OfertasActualizar.as_view(template_name = "ofertas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Ofertas o registro de la Base de Datos 
    path('comienzo/usuario/ofertas/eliminar/<int:pk>', OfertasEliminar.as_view(), name='ofertas/eliminar.html'),    


    path('comienzo/usuario/lugar/', ListadoLugar.as_view(template_name = "lugar/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un lugar o registro 
    path('comienzo/usuario/lugar/detalle/<int:pk>', LugarDetalle.as_view(template_name = "lugar/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo lugar o registro  
    path('comienzo/usuario/lugar/crear', LugarCrear.as_view(template_name = "lugar/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un lugaro registro de la Base de Datos 
    path('comienzo/usuario/lugar/editar/<int:pk>', LugarActualizar.as_view(template_name = "lugar/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un lugar o registro de la Base de Datos 
    path('comienzo/usuario/lugar/eliminar/<int:pk>', LugarEliminar.as_view(), name='lugar/eliminar.html'),  




    path('comienzo/usuario/eventos/', ListadoEventos.as_view(template_name = "eventos/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Eventos o registro 
    path('comienzo/usuario/eventos/detalle/<int:pk>', EventosDetalle.as_view(template_name = "eventos/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Eventos o registro  
    path('comienzo/usuario/eventos/crear', EventosCrear.as_view(template_name = "eventos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Eventoso registro de la Base de Datos 
    path('comienzo/usuario/eventos/editar/<int:pk>', EventosActualizar.as_view(template_name = "eventos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Eventos o registro de la Base de Datos 
    path('comienzo/usuario/eventos/eliminar/<int:pk>', EventosEliminar.as_view(), name='eventos/eliminar.html'),  


    path('comienzo/clienteUs/persona/', ListadoPersona.as_view(template_name = "persona/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un persona o registro 
    path('comienzo/clienteUs/persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "persona/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo persona o registro  
    path('comienzo/clienteUs/persona/crear', PersonaCrear.as_view(template_name = "persona/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un personao registro de la Base de Datos 
    path('comienzo/clienteUs/persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "persona/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un persona o registro de la Base de Datos 
    path('comienzo/clienteUs/persona/eliminar/<int:pk>', PersonaEliminar.as_view(), name='persona/eliminar.html'),    
]


    

    

   



    
