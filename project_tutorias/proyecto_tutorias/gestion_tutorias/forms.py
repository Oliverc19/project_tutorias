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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ids_existentes = Estudiante.objects.values_list('persona__ci', flat=True)
        self.fields['persona'].queryset = Persona.objects.filter(rol='EST').exclude(ci__in=ids_existentes)
    class Meta:
        model = Estudiante
        fields = '__all__'

class TutorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ids_existentes = Tutor.objects.values_list('persona__ci', flat=True)
        self.fields['persona'].queryset = Persona.objects.filter(rol='TUT').exclude(ci__in=ids_existentes)
    class Meta:
        model = Tutor
        fields = '__all__'
        
class TutoriaForm(forms.ModelForm):
    class Meta:
        model = Tutoria
        fields = ['tutor', 'estudiante', 'materia', 'fecha', 'estado']

