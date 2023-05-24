from django.forms import ModelForm
from .models import registro_clientes

class Registro_form(ModelForm):
    class Meta:
        model = registro_clientes
        fields = ['No_orden', 'Nombre', 'Apellidos', 'Ciudadano', 'Documento_identidad', 'Objeto_arrendamiento', 'Fecha_entrada', 'Fecha_salida', 'Importe_arrendamiento', 'Importe_servicio', 'Total_ingreso', 'Recibo_pago', 'Estado']