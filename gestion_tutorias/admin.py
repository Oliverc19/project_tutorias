from django.contrib import admin
from .models import Persona, Estudiante, Tutor, Materia, Tutoria
from django.contrib import admin
from .models import Persona, Estudiante, Tutor, Materia, Tutoria

class EstudianteAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "persona": 
            ids_estudiantes_existentes = Estudiante.objects.values_list('persona_id', flat=True)
            kwargs["queryset"] = Persona.objects.filter(rol='EST').exclude(ci__in=ids_estudiantes_existentes)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class TutorAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "persona": 
            ids_tutores_existentes = Tutor.objects.values_list('persona_id', flat=True)
            kwargs["queryset"] = Persona.objects.filter(rol='TUT').exclude(ci__in=ids_tutores_existentes)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class TutoriaAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "estudiante":
            kwargs["queryset"] = Estudiante.objects.all()
            
        if db_field.name == "tutor":
            kwargs["queryset"] = Tutor.objects.all()
            
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Persona)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Materia)
admin.site.register(Tutoria, TutoriaAdmin) 