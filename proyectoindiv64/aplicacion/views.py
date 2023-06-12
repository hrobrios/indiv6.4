from django.shortcuts import render
from . models import Usuarios
from .forms import aplicacionForm


def index_aplicacion(request):
    return render(request,"crear.html") 


def crear_aplicacion(request):
    form = aplicacionForm()

    if request.method == "POST":
        nombre = request.POST["nombre"]
        clave = request.POST["clave"]
        Usuarios.objects.create(name=nombre, clave=clave)


    context = { "form":form

    }


    return render(request,"crear.html", context)