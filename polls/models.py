from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class registro_clientes(models.Model):
    No_orden = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=125)
    Apellidos = models.CharField(max_length=255)
    Ciudadano = models.CharField(max_length=125)
    Documento_identidad = models.CharField(max_length=125)
    Objeto_arrendamiento = models.CharField(max_length=125)
    Fecha_entrada = models.DateField(auto_now=False, auto_now_add=False)
    Fecha_salida = models.DateField(auto_now=False, auto_now_add=False)
    Importe_arrendamiento = models.FloatField()
    Importe_servicio = models.FloatField()
    Total_ingreso = models.FloatField()
    Recibo_pago = models.IntegerField()
    Estado = models.CharField(max_length=50)
    Creado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombre