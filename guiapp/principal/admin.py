from django.contrib import admin
from principal.models import Comentarios
from principal.models import Empresa

from principal.models import Eventos
from principal.models import Lugar
from principal.models import Ofertas
from principal.models import Persona
from principal.models import Reservas
from principal.models import Rutas
from principal.models import Serviciotour
from principal.models import Tipodocumento
from principal.models import Tipoeventos
from principal.models import Tipolugar
from principal.models import Tiporeserva
# Register your models here.
admin.site.register(Comentarios)
admin.site.register(Empresa)

admin.site.register(Eventos)
admin.site.register(Lugar)
admin.site.register(Ofertas)
admin.site.register(Persona)
admin.site.register(Reservas)
admin.site.register(Rutas)
admin.site.register(Serviciotour)
admin.site.register(Tipodocumento)
admin.site.register(Tipolugar)
admin.site.register(Tiporeserva)
