from django.forms import ModelForm
from .models import Clientes
from django import forms
from .models import IngresoEspacio
from django.forms.widgets import SelectDateWidget

class ClientesForm(ModelForm):

    No_de_orden = forms.IntegerField(label= 'No_de_orden', initial='')
    Documento_identidad = forms.CharField(initial='')
    Nombre = forms.CharField(initial='')
    Apellidos = forms.CharField(initial='')
    Ciudadano = forms.CharField(initial='')
    Fecha_nacimiento = forms.DateField(initial='')
    Estado = forms.CharField(initial='')
    Fecha_entrada = forms.DateField(initial='')
    Fecha_salida = forms.DateField(initial='')
    Cantidad_noches = forms.IntegerField(initial='')
    Objeto_arrendamiento = forms.CharField(initial='')
    Recibo_pago = forms.IntegerField(initial='')
    Info_registro = forms.IntegerField(initial='')
    Ingreso_arrendamiento = forms.IntegerField(initial='')
    Ingreso_desayuno = forms.IntegerField(initial='')
    Ingreso_almuerzo = forms.IntegerField(initial='')
    Ingreso_total = forms.IntegerField(initial='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound:
            self.fields['No_de_orden'].initial = self.data.get('No_de_orden', '')
            

    class Meta:
        model = Clientes 
        fields = ['No_de_orden', 'Documento_identidad', 'Nombre', 'Apellidos', 'Ciudadano', 'Fecha_nacimiento', 
                  'Estado', 'Fecha_entrada', 'Fecha_salida', 'Cantidad_noches', 'Objeto_arrendamiento', 
                  'Recibo_pago', 'Info_registro', 'Ingreso_arrendamiento', 'Ingreso_desayuno', 
                  'Ingreso_almuerzo', 'Ingreso_total' ]
        labels = {
                'No_de_orden': 'No. Orden',
                'Documento_identidad': 'Documento de identidad',
                'Nombre': 'Nombre',
                'Apellidos': 'Apellidos',
                'Ciudadano': 'Ciudadano',
                'Fecha_nacimiento': 'Fecha de nacimiento',
                'Estado': 'Estado',
                'Fecha_entrada': 'Fecha de entrada',
                'Fecha_salida': 'Fecha de salida',
                'Cantidad_noches': 'Cantidad de noches',
                'Objeto_arrendamiento': 'Objeto de arrendamiento',
                'Recibo_pago': 'Recibo de pago',
                'Info_registro': 'Info de registro',
                'Ingreso_arrendamiento': 'Ingreso de arrendamiento',
                'Ingreso_desayuno': 'Ingreso de desayuno',
                'Ingreso_almuerzo': 'Ingreso de almuerzo',
                'Ingreso_total': 'Ingreso total',
        }
        widgets = {
        'Fecha_nacimiento': SelectDateWidget(),
        'Fecha_entrada': SelectDateWidget(),
        'Fecha_salida': SelectDateWidget(),
        }

class EspacioForm(ModelForm):
    Cantidad_espacios = forms.IntegerField()
    Importe_cobrado = forms.FloatField()
    Periodo_cobrado = forms.CharField()
    

    class Meta:
        model = IngresoEspacio
        fields = ['Cantidad_espacios', 'Importe_cobrado', 'Periodo_cobrado']
        labels = {
                'Cantidad_espacios': 'Cantidad de espacios',
                'Importe_cobrado': 'Importe cobrado',
                'Periodo_cobrado': 'Periodo cobrado',
                }
      
     
