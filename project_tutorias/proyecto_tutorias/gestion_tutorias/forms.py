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
    class Meta:
        model = Estudiante
        fields = ['persona', 'carrera', 'codigo_estudiante']
        widgets = {
            'persona': forms.Select(attrs={'class': 'form-select'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Carrera'}),
            'codigo_estudiante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código'}),
        }

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['persona', 'especialidad']
        widgets = {
            'persona': forms.Select(attrs={'class': 'form-select'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especialidad'}),
        }

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'codigo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Materia'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código'}),
        }

class TutoriaForm(forms.ModelForm):
    class Meta:
        model = Tutoria
        fields = ['tutor', 'estudiante', 'materia', 'fecha', 'estado']
        widgets = {
            'tutor': forms.Select(attrs={'class': 'form-select'}),
            'estudiante': forms.Select(attrs={'class': 'form-select'}),
            'materia': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }