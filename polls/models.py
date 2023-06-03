from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class TimeField(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
class Rooms(TimeField):
    habitacion = models.IntegerField()
    espacio = models.IntegerField(default=0)
    # price = models.FloatField(default=0)
    # disponible = models.BooleanField(default=True)
    
    def __str__(self):
        if self.espacio > 0:
            return f'{self.habitacion} habitacion(es) y {self.espacio} espacio'
        else:
            return f'{self.habitacion} habitacion(es)'
        
    def get_absolute_url(self):
        return reverse('create_objeto_arr')
        # return reverse('blog_full', kwargs={'post_id': self.post.pk})
    
class Ciudadania(TimeField):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('create_ciudadano')
    
    
class Clientes(TimeField):
    no_de_orden = models.CharField(max_length=50)
    documento_identidad = models.CharField(max_length=125)
    nombre = models.CharField(max_length=125)
    apellidos = models.CharField(max_length=255)
    # citizenship = models.CharField(max_length=255)
    citizenship = models.ForeignKey(Ciudadania, blank=True, null=True, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=125)
    cantidad_noches = models.IntegerField()
    # objeto_arrendamiento = models.CharField(max_length=125)
    objeto_arrendamiento = models.ForeignKey(Rooms, blank=True, null=True, on_delete=models.CASCADE)
    recibo_pago = models.IntegerField()
    info_registro = models.IntegerField()
    #ingreso_alojamiento = models.FloatField(null=True, blank=True)
    ingreso_alojamiento = models.FloatField()
    ingreso_desayuno = models.FloatField(default=0)
    ingreso_almuerzo = models.FloatField(default=0)
    #ingreso_total = models.FloatField(null=True, blank=True)
    ingreso_total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
 

    
class IngresoEspacio(models.Model):
    cantidad_espacios = models.IntegerField()
    importe_cobrado = models.FloatField()
    periodo_cobrado = models.CharField(max_length = 125)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.periodo_cobrado 

class GastosArr(models.Model):
    fecha = models.DateField()
    detalle_gasto = models.CharField(max_length = 500)      
    concepto =  models.CharField(max_length = 255)
    unidad_medida = models.CharField(max_length = 125)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    importe = models.FloatField()

    def __str__(self):
        return self.concepto 

class GastosEspacio(models.Model):
    fecha = models.DateField()
    detalle_gasto = models.CharField(max_length = 500)      
    concepto =  models.CharField(max_length = 255)
    unidad_medida = models.CharField(max_length = 125)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    importe = models.FloatField()

    def __str__(self):
        return self.concepto 