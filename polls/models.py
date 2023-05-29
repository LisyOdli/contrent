from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clientes(models.Model):
    No_de_orden = models.CharField(max_length=50)
    Documento_identidad = models.CharField(max_length=125)
    Nombre = models.CharField(max_length=125)
    Apellidos = models.CharField(max_length=255)
    Ciudadano = models.CharField(max_length=125)
    Fecha_nacimiento = models.DateField()
    Estado = models.CharField(max_length=125)
    Fecha_entrada = models.DateField()
    Fecha_salida = models.DateField()
    Cantidad_noches = models.IntegerField()
    Objeto_arrendamiento = models.CharField(max_length=125)
    Recibo_pago = models.IntegerField()
    Info_registro = models.IntegerField()
    Ingreso_arrendamiento = models.FloatField()
    Ingreso_desayuno = models.FloatField()
    Ingreso_almuerzo = models.FloatField()
    Ingreso_total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    
class IngresoEspacio(models.Model):
    Cantidad_espacios = models.IntegerField()
    Importe_cobrado = models.FloatField()
    Periodo_cobrado = models.CharField(max_length = 125)
    Fecha = models.DateField(auto_now_add=True)
