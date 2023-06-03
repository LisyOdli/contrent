from django.contrib import admin
from polls.models import Clientes, Rooms, Ciudadania, IngresoEspacio

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Rooms)
admin.site.register(Ciudadania)
admin.site.register(IngresoEspacio)