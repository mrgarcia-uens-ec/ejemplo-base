from django.contrib import admin

from .models import Estudiante
from .models import Curso

admin.site.register(Estudiante)
admin.site.register(Curso)
