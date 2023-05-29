from django.forms import ModelForm
from .models import Clientes
from django import forms
from .models import IngresoEspacio
from django.forms.widgets import SelectDateWidget

class ClientesForm(ModelForm):

    # No_de_orden = forms.IntegerField(label= 'No_de_orden', initial='')
    # Documento_identidad = forms.CharField(initial='')
    # Nombre = forms.CharField(initial='')
    # Apellidos = forms.CharField(initial='')
    # Ciudadano = forms.CharField(initial='')
    # Fecha_nacimiento = forms.DateField(initial='')
    # Estado = forms.CharField(initial='')
    # Fecha_entrada = forms.DateField(initial='')
    # Fecha_salida = forms.DateField(initial='')
    # Cantidad_noches = forms.IntegerField(initial='')
    # Objeto_arrendamiento = forms.CharField(initial='')
    # Recibo_pago = forms.IntegerField(initial='')
    # Info_registro = forms.IntegerField(initial='')
    # Ingreso_arrendamiento = forms.IntegerField(initial='')
    # Ingreso_desayuno = forms.IntegerField(initial='')
    # Ingreso_almuerzo = forms.IntegerField(initial='')
    # Ingreso_total = forms.IntegerField(initial='')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.is_bound:
    #         self.fields['No_de_orden'].initial = self.data.get('No_de_orden', '')
            

    class Meta:
        model = Clientes 
        fields = ['no_de_orden', 'documento_identidad', 'nombre', 'apellidos', 'citizenship', 'fecha_nacimiento', 
                  'estado', 'fecha_entrada', 'fecha_salida', 'cantidad_noches', 'objeto_arrendamiento', 
                  'recibo_pago', 'info_registro', 'ingreso_desayuno', 
                  'ingreso_almuerzo',  ]
        labels = {
                'no_de_orden': 'No. Orden',
                'documento_identidad': 'Documento de identidad',
                'nombre': 'Nombre',
                'apellidos': 'Apellidos',
                'citizenship': 'Ciudadania',
                'fecha_nacimiento': 'Fecha de nacimiento',
                'estado': 'Estado',
                'fecha_entrada': 'Fecha de entrada',
                'fecha_salida': 'Fecha de salida',
                'cantidad_noches': 'Cantidad de noches',
                'objeto_arrendamiento': 'Objeto de Arrendamiento',
                'recibo_pago': 'Recibo de Pago',
                'info_registro': 'Info de registro', 
                #'ingreso_alojamiento': 'Ingreso de arrendamiento', # Sale del precio de la Habitacion
                'ingreso_desayuno': 'Ingreso de desayuno',
                'ingreso_almuerzo': 'Ingreso de almuerzo',
                #'ingreso_total': 'Ingreso total', #Suma de ingreso_almuerzo + ingreso_desayuno +ingreso_alojamiento
        }
        # widgets = {
        # 'Fecha_nacimiento': SelectDateWidget(),
        # 'Fecha_entrada': SelectDateWidget(),
        # 'Fecha_salida': SelectDateWidget(),
        # }

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
      
     
