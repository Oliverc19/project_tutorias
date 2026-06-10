from django import forms
from .models import Materia, Tutoria, Tutor, Estudiante, Persona

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'codigo']

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['ci', 'nombre', 'paterno', 'materno', 'email', 'rol']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['persona', 'carrera', 'codigo_estudiante']

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['persona', 'especialidad', 'cubiculo']

class TutoriaForm(forms.ModelForm):
    class Meta:
        model = Tutoria
        fields = ['tutor', 'estudiante', 'materia', 'fecha_hora']

