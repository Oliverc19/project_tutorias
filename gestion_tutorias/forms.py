from django import forms
from .models import Persona, Estudiante, Tutor, Materia, Tutoria

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['ci', 'nombre', 'paterno', 'materno', 'email', 'rol']
        widgets = {
            'ci': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'C.I.'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'paterno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Paterno'}),
            'materno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Materno'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
        }

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
class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'codigo'] 
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
        }

