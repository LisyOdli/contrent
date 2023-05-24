from django.contrib import admin
from polls.models import registro_clientes

# Register your models here.
class registro_admin(admin.ModelAdmin):
    readonly_fields = ("Creado", )
    
admin.site.register(registro_clientes, registro_admin)