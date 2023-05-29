from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ClientesForm
from .models import Clientes, Rooms, Ciudadania
from .models import IngresoEspacio
from .forms import EspacioForm
from datetime import date
from django.views.generic import CreateView


# Create your views here.

def home(request):
    return render(request, 'home.html')

def registro_gastos(request):
    return render(request, 'registro_gastos.html')

def control_inventarios(request):
    return render(request, 'control_inventarios.html')

def calculo_impuestos(request):
    return render(request, 'calculo_impuestos.html')

def disponibilidad(request):
    return render(request, 'disponibilidad.html')

def registro_contable(request):
    return render(request, 'registro_contable.html')

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('registro_clientes')
            except IntegrityError:
                return render(request, 'registrarse.html', {
                'form': UserCreationForm,
                "error": 'El usuario ya existe'
                })
        return render(request, 'registrarse.html', {
                'form': UserCreationForm,
                "error": 'Las contraseñas no coinciden'
       })

def registro_ingresos(request):
    return render(request, 'registro_ingresos.html')

def registro_clientes(request):
    rooms = Rooms.objects.filter(disponible = True)
    ciudadania = Ciudadania.objects.all()
    # numero_order = Clientes.objects.filter(no_de_orden__la)
    if request.method == 'GET':
         return render(request, 'registro_clientes.html', {
            'form': ClientesForm,
            'rooms':rooms,
            'ciudadanias':ciudadania
    })
    else:   
            request.POST = request.POST.copy()
            data = request.POST
            id_ciudadania = Ciudadania.objects.get(name = request.POST['citizenship']).id
            id_rooms = Rooms.objects.get(name = request.POST['objeto_arrendamiento']).id
            data['citizenship'] = id_ciudadania
            data['objeto_arrendamiento'] = id_rooms
            
            form = ClientesForm(data)    
            print('Form',form)
            print('Data',data)
            
            if form.is_valid():
                nuevo_cliente = form.save(commit=False)  
                nuevo_cliente.user = request.user
                nuevo_cliente.save()  
                return redirect('registro_clientes')
            else:
                form = ClientesForm()
                context = {'form': form}
                return render(request, 'registro_clientes.html', context)
            
            
class RegistroIngresoView(CreateView):
    model = Clientes
    template_name = 'registro_clientes.html'
    form_class = ClientesForm
    fields=['no_de_orden', 'documento_identidad', 'nombre', 'apellidos', 'citizenship', 'fecha_nacimiento', 
                   'estado', 'fecha_entrada', 'fecha_salida', 'cantidad_noches', 'objeto_arrendamiento', 
                   'recibo_pago', 'info_registro', 'ingreso_desayuno', 
                   'ingreso_almuerzo', ]
    # fields=('no_de_orden', 'documento_identidad', 'nombre', 'apellidos','fecha_nacimiento', 
    #               'estado', 'fecha_entrada', 'fecha_salida', 'cantidad_noches', 
    #               'recibo_pago', 'info_registro', 'ingreso_desayuno', 
    #               'ingreso_almuerzo', )

    # @method_decorator(proveedor_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(AddBlogView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        id_ciudadania = Ciudadania.objects.get(name = self.request.citizenship).id
        id_rooms = Rooms.objects.get(name = self.request.objeto_arrendamiento).id
        form.instance.objeto_arrendamiento= id_rooms
        form.instance.citizenship = id_ciudadania
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Rooms.objects.all()
        context["ciudadanias"] = Ciudadania.objects.all()
        return context
   

def listado_clientes_reg(request):
    lista_clientes = Clientes.objects.all()
    return render(request, 'listado_clientes_reg.html', {'lista_clientes': lista_clientes})



def listado_clientes_act(request):
    lista_clientes = Clientes.objects.filter(Fecha_salida__gte=date.today())
    return render(request, 'listado_clientes_reg.html', {'lista_clientes': lista_clientes})


def indice_ocupacional(request):
    return render(request, 'indice_ocupacional.html')

def registro_ingreso_espacio(request):
    if request.method == 'GET':
         return render(request, 'registro_ingreso_espacio.html', {
            'form': EspacioForm
    })
    else:
            formespacio = EspacioForm(request.POST)    
            if  formespacio.is_valid():
                nuevo_espacio = formespacio.save(commit=False)  
                nuevo_espacio.user = request.user
                nuevo_espacio.save()  
               
                return redirect('registro_ingreso_espacio')            
            else:
                formespacio = ClientesForm()
                context = {'formespacio': formespacio}
                
                return render(request, 'registro_ingreso_espacio.html', context)
 

def listado_ingresos_espacio(request):    
    lista_espacio = IngresoEspacio.objects.all()
    return render(request, 'listado_ingresos_espacio.html', {'lista_espacio': lista_espacio})

def listado_ingresos_totales(request):
    return render(request, 'listado_ingresos_totales.html')
    
def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {
            'form': AuthenticationForm,
            'error': 'El usuario o la contraseña es incorrecta'
            })   
        else:
            login(request,user)
            return redirect('home')

