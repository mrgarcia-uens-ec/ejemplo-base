from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hola", views.index, name="index"),
    path("adios", views.adios, name="adios"),
    path("mostrarhtml", views.mostrarhtml, name="mostrarhtml")
]