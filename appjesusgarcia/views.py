from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso

def index(request):
    return HttpResponse("Hola")

def adios(request):
    return HttpResponse("Adiós")

def mostrarhtml(request):
    lista_cursos = Curso.objects.all()
    contexto = {
        "lista_cursos": lista_cursos
    }
    return render(request, "cursos.html", contexto)


# Esto es un cambio

