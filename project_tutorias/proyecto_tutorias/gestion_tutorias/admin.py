from django.contrib import admin
from .models import Persona, Estudiante, Tutor, Materia, Tutoria

# Registramos los modelos de forma normal
admin.site.register(Persona)
admin.site.register(Estudiante)
admin.site.register(Tutor)
admin.site.register(Materia)
admin.site.register(Tutoria)
