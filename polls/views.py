from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    return HttpResponse("Hola Mundo :D creamos nuestra primera vista")

def autenticar(request):
    return render(request, "autentication.html")