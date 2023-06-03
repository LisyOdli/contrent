from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ClientesForm
from .models import Clientes, Rooms, Ciudadania, GastosArr, GastosEspacio
from .models import IngresoEspacio
from .forms import EspacioForm, GastoArrForm, GastoEspacioForm
from datetime import date
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('iniciar_sesion')
    
    
class CreateObjetoArrendamientoView(CreateView):
    model = Rooms
    template_name = 'create_objecto_arrendamiento.html'
    # form_class = ClientesForm
    fields=('habitacion','espacio',)
    # success_url = reverse_lazy('blog_dash')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objetos"] =  Rooms.objects.all()
        return context
    
class DeleteObjetoArrendamientoView(DeleteView):
    model = Rooms
    template_name = "create_objeto_arrendamiento.html"
    success_url = reverse_lazy('create_objeto_arr')
    
class DeleteCiudadanoView(DeleteView):
    model = Ciudadania
    template_name = "create_ciudadano.html"
    success_url = reverse_lazy('create_ciudadano')
    
class CreateCiudadanoView(CreateView):
    model = Ciudadania
    template_name = 'create_ciudadano.html'
    # form_class = ClientesForm
    fields=('name',)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ciudadanos"] =  Ciudadania.objects.all()
        return context
    

def update_ciudadania(request,pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        ciudadano = Ciudadania.objects.get(id = pk)
        ciudadano.name = name
        ciudadano.save()
        return redirect('create_ciudadano')
    

def update_objeto_arrendamiento(request,pk):
    if request.method == 'POST':
        habitacion = request.POST.get('habitacion')
        espacio = request.POST.get('espacio')
        objeto = Rooms.objects.get(id = pk)
        objeto.habitacion = habitacion
        objeto.espacio = espacio
        objeto.save()
        return redirect('create_objeto_arr')
    

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
    rooms = Rooms.objects.all()
    ciudadania = Ciudadania.objects.all()
    # numero_order = Clientes.objects.filter(no_de_orden__la)
    if request.method == 'GET':
         return render(request, 'registro_clientes.html', {
            'form': ClientesForm,
            'rooms':rooms,
            'ciudadanias':ciudadania
    })
    else:   
            print(request.POST)
            request.POST = request.POST.copy()
            data = request.POST
            # id_ciudadania = Ciudadania.objects.get(name = request.POST['citizenship']).id
            # id_rooms = Rooms.objects.get(name = request.POST['objeto_arrendamiento']).id
            # data['citizenship'] = id_ciudadania
            # data['objeto_arrendamiento'] = id_rooms
            
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
                   'recibo_pago', 'info_registro', 'ingreso_alojamiento','ingreso_desayuno', 
                   'ingreso_almuerzo', 'ingreso_total',]
    # fields=('no_de_orden', 'documento_identidad', 'nombre', 'apellidos','fecha_nacimiento', 
    #               'estado', 'fecha_entrada', 'fecha_salida', 'cantidad_noches', 
    #               'recibo_pago', 'info_registro', 'ingreso_desayuno', 
    #               'ingreso_almuerzo', )

    # @method_decorator(proveedor_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(AddBlogView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        # id_ciudadania = Ciudadania.objects.get(name = self.request.citizenship).id
        # id_rooms = Rooms.objects.get(name = self.request.objeto_arrendamiento).id
        # form.instance.objeto_arrendamiento= id_rooms
        # form.instance.citizenship = id_ciudadania
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["rooms"] = Rooms.objects.all()
        # context["ciudadanias"] = Ciudadania.objects.all()
        return context
  
def listado_clientes_reg(request):
    lista_clientes = Clientes.objects.all()
    return render(request, 'listado_clientes_reg.html', {'lista_clientes': lista_clientes})

def listado_clientes_act(request):
    lista_clientes = Clientes.objects.filter(fecha_salida__gte=date.today())
    return render(request, 'listado_clientes_act.html', {'lista_clientes': lista_clientes})

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
        
# def editar_cliente(request, documento_identidad):
#     clientes = Clientes.objects.get(documento_identidad = documento_identidad)

# def eliminar_cliente(request, documento_identidad):
#     clientes = Clientes.objects.get(documento_identidad = documento_identidad)
#     clientes.delete()
#     return redirect('/')

def gasto_arren(request):
    if request.method == 'GET':
         return render(request, 'gasto_arren.html', {
            'form': GastosArr
    })
    else:
            formgasto = GastoArrForm(request.POST)    
            if  formgasto.is_valid():
                nuevo_gasto = formgasto.save(commit=False)  
                nuevo_gasto.user = request.user
                nuevo_gasto.save()  
               
                return redirect('gasto_arren')            
            else:
                formgasto = GastoArrForm()
                context = {'formgasto': formgasto}
                
                return render(request, 'gasto_arren.html', context)
 
def gasto_espacio(request):
    if request.method == 'GET':
        return render(request, 'gasto_espacio.html', {
            'form': GastosEspacio
         })
    else:
            formgasto = GastoEspacioForm(request.POST)    
            if  formgasto.is_valid():
                nuevo_gasto = formgasto.save(commit=False)  
                nuevo_gasto.user = request.user
                nuevo_gasto.save()  
               
                return redirect('gasto_espacio')            
            else:
                formgasto = GastoEspacioForm()
                context = {'formgasto': formgasto}
                
                return render(request, 'gasto_espacio.html', context)

def listado_gastos_esp(request):
    gastos_esp = GastosEspacio.objects.all()
    return render(request, 'listado_gastos_esp.html', {'gastos_esp': gastos_esp})

def listado_gastos_arren(request):
    gastos_arren = GastosArr.objects.all()
    return render(request, 'listado_gastos_arren.html', {'gastos_arren': gastos_arren})

def eliminar_cliente(request, documento_identidad):
    cliente = get_object_or_404(Clientes, documento_identidad=documento_identidad)
    if request.method == 'POST':
        clientes = Clientes.objects.get(documento_identidad=documento_identidad)
        clientes.delete()
        return redirect('listado_clientes_reg')
    else:
        return render(request, 'confirmar_eliminar_cliente.html', {'cliente': cliente})

def edicion_cliente(request, documento_identidad):
    # Obtener el objeto Clientes correspondiente al documento de identidad
    clientes_edit = Clientes.objects.get(documento_identidad=documento_identidad)

    if request.method == 'POST':
        # Crear un formulario con los datos enviados en la solicitud POST
        form = ClientesForm(request.POST, instance=clientes_edit)
        if form.is_valid():
            # Si el formulario es válido, guardar los cambios en la base de datos
            form.save()
            # Redirigir al usuario a la página de detalles del cliente actualizado
            return redirect('detalles_cliente', documento_identidad=documento_identidad)
    else:
        # Si la solicitud no es POST, renderizar el formulario con los datos actuales del cliente
        form = ClientesForm(instance=clientes_edit)

    return render(request, 'editar_cliente.html', {'form': form, 'clientes_edit': clientes_edit})

def editar_cliente(request, documento_identidad):
                         
    clientes_edit = Clientes.objects.get(documento_identidad=documento_identidad)
    form = ClientesForm(initial={
        'no_de_orden': clientes_edit.no_de_orden,
        'nombre': clientes_edit.nombre,
        'apellidos': clientes_edit.apellidos,
        'documento_identidad': clientes_edit.documento_identidad,
        'citizenship': clientes_edit.citizenship,
        'fecha_nacimiento': clientes_edit.fecha_nacimiento,
        'estado': clientes_edit.estado,
        'fecha_entrada': clientes_edit.fecha_entrada,
        'cantidad_noches': clientes_edit.cantidad_noches,
        'fecha_salida': clientes_edit.fecha_salida,
        'objeto_arrendamiento': clientes_edit.objeto_arrendamiento,
        'recibo_pago': clientes_edit.recibo_pago,
        'info_registro': clientes_edit.info_registro,
        'ingreso_alojamiento': clientes_edit.ingreso_alojamiento,
        'ingreso_desayuno': clientes_edit.ingreso_desayuno,
        'ingreso_almuerzo': clientes_edit.ingreso_almuerzo,
        'ingreso_total': clientes_edit.ingreso_total
    })
    
    return render(request, 'listado_clientes_reg', {'form': form, 'clientes_edit': clientes_edit})

# def listado_clientes_reg(request):
#     query = request.GET.get('q')
#     if query:
#         clientes = Clientes.objects.filter(documento_identidad__icontains=query)
#     else:
#         clientes = Clientes.objects.all()
#     return render(request, 'listado_clientes_reg.html', {'clientes': clientes, 'query': query})