from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q

from .models import Curso
from .models import Asignatura
from .models import Estudiante

from .forms import FormBusqueda

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

def lista_de_asignaturas(request):
    lista_asignaturas = Asignatura.objects.all()
    contexto = {
        "lista_asignaturas": lista_asignaturas,
        "equipos_de_futbol": ["Real Madrid", "Atlético de Madrid", "Barcelona"],
        "mi_nombre": "Jesús García"
    }
    return render(request, "asignaturas.html", contexto)

def lista_de_estudiantes(request):
    lista_estudiantes = Estudiante.objects.all()
    form = FormBusqueda()
    contexto = {
        "lista_estudiantes": lista_estudiantes,
        "form": form
    }
    return render(request, "estudiantes.html", contexto)

def detalle_estudiante(request, id_estudiante):
    estudiante = Estudiante.objects.get(pk=id_estudiante)
    contexto = {
        "estudiante": estudiante,
    }
    return render(request, "estudiante.html", contexto)
