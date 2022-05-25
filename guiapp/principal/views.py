from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

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
 


    