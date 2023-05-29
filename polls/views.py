from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ClientesForm
from .models import Clientes
from .models import IngresoEspacio
from .forms import EspacioForm
from datetime import date


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
    if request.method == 'GET':
         return render(request, 'registro_clientes.html', {
            'form': ClientesForm
    })
    else:
            form = ClientesForm(request.POST)    
            if form.is_valid():
                nuevo_cliente = form.save(commit=False)  
                nuevo_cliente.user = request.user
                nuevo_cliente.save()  
                return redirect('registro_clientes')
            else:
                form = ClientesForm()
                context = {'form': form}
                return render(request, 'registro_clientes.html', context)
   

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

