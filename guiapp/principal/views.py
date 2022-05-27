from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse 

# librerias del crud
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms


# Create your views here.

def inicio(request):
    return HttpResponse ("<h1>Bienvenido a Tu Destino</h1>")

def comienzo(request):
    return render (request,'paginas/base.html')
    
def usuario(request):
    return render (request,'paginas/admin.html')

def clienteUs(request):
    return render (request,'paginas/cliente.html')










def formulario(request):
    return render (request, "formularioContacto.html")

def indexprincipal(request):
    return render (request, "index.html")



def contactar(request):
    if request.method == "POST":
        asunto = request.POST ["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["jhornym8@gmail.co"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render (request, "contactoExitoso.html")
    return render (request, "formulario.html")


#
class ListadoTiporeserva(ListView):
    model = Tiporeserva
    
    
class TiporeservaCrear(SuccessMessageMixin, CreateView):
    model =Tiporeserva
    form = Tiporeserva
    fields = "__all__"
    success_message ='Tiporeserva creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class TiporeservaDetalle (DetailView):
    model =Tiporeserva

class  TiporeservaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tiporeserva
    form = Tiporeserva
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tiporeserva Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class TiporeservaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tiporeserva 
    form = Tiporeserva
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tiporeserva Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

#
class ListadoComentarios(ListView):
    model =  Comentarios
    
    
class  ComentariosCrear(SuccessMessageMixin, CreateView):
    model = Comentarios
    form =  Comentarios
    fields = "__all__"
    success_message =' Comentarios creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class  ComentariosDetalle (DetailView):
    model = Comentarios

class   ComentariosActualizar(SuccessMessageMixin,UpdateView):
    model =   Comentarios
    form =  Comentarios
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = ' Comentarios Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class  ComentariosEliminar(SuccessMessageMixin, DeleteView): 
    model =  Comentarios 
    form =  Comentarios
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = ' Comentarios Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'



#
class ListadoRutas(ListView):
    model = Rutas
    
    
class  RutasCrear(SuccessMessageMixin, CreateView):
    model = Rutas
    form =  Rutas
    fields = "__all__"
    success_message =' Rutas creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class  RutasDetalle (DetailView):
    model = Rutas

class   RutasActualizar(SuccessMessageMixin,UpdateView):
    model =   Rutas
    form =  Rutas
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = ' Rutas Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class  RutasEliminar(SuccessMessageMixin, DeleteView): 
    model =  Rutas
    form =  Rutas
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = ' Rutas Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

#

class ListadoTipolugar(ListView):
    model = Tipolugar
    
    
class TipolugarCrear(SuccessMessageMixin, CreateView):
    model =Tipolugar
    form = Tipolugar
    fields = "__all__"
    success_message ='Tipolugar creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class TipolugarDetalle (DetailView):
    model =Tipolugar

class  TipolugarActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipolugar
    form = Tipolugar
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipolugar Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class TipolugarEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipolugar 
    form = Tipolugar
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipolugar Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

# 

class ListadoEmpresa(ListView):
    model = Empresa
    
    
class EmpresaCrear(SuccessMessageMixin, CreateView):
    model =Empresa
    form = Empresa
    fields = "__all__"
    success_message ='Empresa creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class EmpresaDetalle (DetailView):
    model =Empresa

class  EmpresaActualizar(SuccessMessageMixin,UpdateView):
    model =  Empresa
    form = Empresa
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Empresa Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class EmpresaEliminar(SuccessMessageMixin, DeleteView): 
    model = Empresa 
    form = Empresa
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Empresa Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'




#
class ListadoEstadocliente(ListView):
    model = Estadocliente
    
    
class EstadoclienteCrear(SuccessMessageMixin, CreateView):
    model =Estadocliente
    form = Estadocliente
    fields = "__all__"
    success_message ='Estadocliente creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class EstadoclienteDetalle (DetailView):
    model =Estadocliente

class  EstadoclienteActualizar(SuccessMessageMixin,UpdateView):
    model =  Estadocliente
    form = Estadocliente
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Estadocliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class EstadoclienteEliminar(SuccessMessageMixin, DeleteView): 
    model = Estadocliente 
    form = Estadocliente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Estadocliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'



#
class ListadoTipodocumento(ListView):
    model = Tipodocumento
    
    
class TipodocumentoCrear(SuccessMessageMixin, CreateView):
    model =Tipodocumento
    form = Tipodocumento
    fields = "__all__"
    success_message ='Tipodocumento creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class TipodocumentoDetalle (DetailView):
    model =Tipodocumento

class  TipodocumentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipodocumento
    form = Tipodocumento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipodocumento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class TipodocumentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipodocumento 
    form = Tipodocumento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipodocumento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'




#
class ListadoReservas(ListView):
    model = Reservas
    
    
class ReservasCrear(SuccessMessageMixin, CreateView):
    model =Reservas
    form = Reservas
    fields = "__all__"
    success_message ='Reservas creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ReservasDetalle (DetailView):
    model =Reservas

class  ReservasActualizar(SuccessMessageMixin,UpdateView):
    model =  Reservas
    form = Reservas
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Reservas Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class ReservasEliminar(SuccessMessageMixin, DeleteView): 
    model = Reservas 
    form = Reservas
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Reservas Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
       


#
 

 


    