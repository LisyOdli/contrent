from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.db import models
from .forms import Registro_form
from .models import registro_clientes

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registrarse(request):

    if request.method == 'GET':
        print('enviando formulario')

        return render(request, 'registrarse.html', {
        'form': UserCreationForm
    })

    else:
        if request.POST['password1'] == request.POST['password2']:
            #register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
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

def listado_clientes(request):
     listado = registro_clientes.objects.all()
     return render(request, 'listado_clientes.html', {'listado': listado})


def registro_clientes(request):

    if request.method == 'GET':
         return render(request, 'registro_clientes.html',{
        'form': Registro_form   
         }) 
    else:
        try:
            form = Registro_form(request.POST)
            nuevo_registro = form.save(commit=False)
            nuevo_registro.user = request.user
            nuevo_registro.save() 
            return redirect('registro_clientes')
        except ValueError:
            return render(request, 'registro_clientes.html',{
            'form': Registro_form, 
            'error': 'Por favor ingrese datos validos'  
            }) 
        
def obt_list_clientes(request):
    return render(request, 'obt_list_clientes.html')        

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
     if request.method == 'GET':
        return render(request, 'iniciar_sesion.html',{
        'form': AuthenticationForm
    })
     else:
          user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
          if user is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'El nombre de usuario o la contraseña son incorrectas'
            })
          else: 
              login(request, user)
              return redirect('registro_clientes')
        
    
    