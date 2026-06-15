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
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = ['persona', 'carrera', 'codigo_estudiante']
        widgets = {
            'persona': forms.Select(attrs={'class': 'form-select'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Carrera'}),
            'codigo_estudiante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código'}),
        }
>>>>>>> b3342f674c46a8e4878c607de002bd0256026d41

class TutorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ids_existentes = Tutor.objects.values_list('persona__ci', flat=True)
        self.fields['persona'].queryset = Persona.objects.filter(rol='TUT').exclude(ci__in=ids_existentes)
    class Meta:
        model = Tutor
<<<<<<< HEAD
        fields = '__all__'
        
=======
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

>>>>>>> b3342f674c46a8e4878c607de002bd0256026d41
class TutoriaForm(forms.ModelForm):
    class Meta:
        model = Tutoria
        fields = ['tutor', 'estudiante', 'materia', 'fecha', 'estado']
<<<<<<< HEAD

=======
        widgets = {
            'tutor': forms.Select(attrs={'class': 'form-select'}),
            'estudiante': forms.Select(attrs={'class': 'form-select'}),
            'materia': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
>>>>>>> b3342f674c46a8e4878c607de002bd0256026d41
