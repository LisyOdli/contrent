from django.db import models

# Create your models here.

class contrent(models.Model):
    No_de_orden = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=125)
    Apellidos = models.CharField(max_length=255)
    Pasaporte = models.CharField(max_length=125)
    



    def _str_(self) -> str:
        return self.Nombre, self.Apellidos, self.Pasaporte, self.No_de_orden