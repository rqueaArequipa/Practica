from django.contrib import admin

from .models import Pregunta, Opcion, Alumno, Nota

admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(Alumno)
admin.site.register(Nota)
