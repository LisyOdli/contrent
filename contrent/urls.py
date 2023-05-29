"""
URL configuration for contrent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('registro_ingresos/', views.registro_ingresos, name='registro_ingresos'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('home/', views.home, name='home'),
    path('registro_gastos/', views.registro_gastos, name='registro_gastos'),
    path('control_inventarios/', views.control_inventarios, name='control_inventarios'),
    path('calculo_impuestos/', views.calculo_impuestos, name='calculo_impuestos'),
    path('disponibilidad/', views.disponibilidad, name='disponibilidad'),
    path('registro_contable/', views.registro_contable, name='registro_contable'),
    path('registro_clientes/', views.registro_clientes, name='registro_clientes'),
    path('listado_clientes_reg/', views.listado_clientes_reg, name='listado_clientes_reg'),
    path('listado_clientes_act/', views.listado_clientes_act, name='listado_clientes_act'),
    path('indice_ocupacional/', views.indice_ocupacional, name='indice_ocupacional'),
    path('registro_ingreso_espacio/', views.registro_ingreso_espacio, name='registro_ingreso_espacio'),
    path('listado_ingresos_espacio/', views.listado_ingresos_espacio, name='listado_ingresos_espacio'),
    path('listado_ingresos_totales/', views.listado_ingresos_totales, name='listado_ingresos_totales')

]
