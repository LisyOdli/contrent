from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TimeField(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
class Rooms(TimeField):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Ciudadania(TimeField):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Clientes(TimeField):
    no_de_orden = models.CharField(max_length=50)
    documento_identidad = models.CharField(max_length=125)
    nombre = models.CharField(max_length=125)
    apellidos = models.CharField(max_length=255)
    citizenship = models.ForeignKey(Ciudadania, blank=True, null=True, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=125)
    cantidad_noches = models.IntegerField()
    objeto_arrendamiento = models.ForeignKey(Rooms, blank=True, null=True, on_delete=models.CASCADE)
    recibo_pago = models.IntegerField()
    info_registro = models.IntegerField()
    ingreso_alojamiento = models.FloatField(null=True, blank=True)
    ingreso_desayuno = models.FloatField(default=0)
    ingreso_almuerzo = models.FloatField(default=0)
    ingreso_total = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
 

    
class IngresoEspacio(models.Model):
    Cantidad_espacios = models.IntegerField()
    Importe_cobrado = models.FloatField()
    Periodo_cobrado = models.CharField(max_length = 125)
    Fecha = models.DateField(auto_now_add=True)
    

