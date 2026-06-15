from rest_framework import viewsets
from .serializers import MateriaSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Persona, Estudiante, Tutor, Materia, Tutoria
from .forms import PersonaForm, EstudianteForm, TutorForm, MateriaForm, TutoriaForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def cerrar_sesion(request):
    logout(request)
    return redirect('login')
# ============================================
# DASHBOARD
# ============================================

@login_required
def dashboard(request):
    total_personas = Persona.objects.count()
    total_estudiantes = Estudiante.objects.count()
    total_tutores = Tutor.objects.count()
    total_materias = Materia.objects.count()
    total_tutorias = Tutoria.objects.count()
    
    tutorias_pendientes = Tutoria.objects.filter(estado='pendiente').count()
    tutorias_aceptadas = Tutoria.objects.filter(estado='aceptada').count()
    tutorias_finalizadas = Tutoria.objects.filter(estado='finalizada').count()
    
    context = {
        'total_personas': total_personas,
        'total_estudiantes': total_estudiantes,
        'total_tutores': total_tutores,
        'total_materias': total_materias,
        'total_tutorias': total_tutorias,
        'tutorias_pendientes': tutorias_pendientes,
        'tutorias_aceptadas': tutorias_aceptadas,
        'tutorias_finalizadas': tutorias_finalizadas,
    }
    return render(request, 'gestion_tutorias/dashboard.html', context)

# ============================================
# PERSONA
# ============================================

@login_required
def persona_list(request):
    personas = Persona.objects.all()
    return render(request, 'gestion_tutorias/persona_list.html', {'personas': personas})

@login_required
def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
    else:
        form = PersonaForm()
    return render(request, 'gestion_tutorias/persona_form.html', {'form': form, 'titulo': 'Nueva Persona'})

@login_required
def persona_edit(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'gestion_tutorias/persona_form.html', {'form': form, 'titulo': 'Editar Persona'})

@login_required
def persona_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona_list')
    return render(request, 'gestion_tutorias/confirm_delete.html', {'object': persona, 'tipo': 'Persona'})

# ============================================
# ESTUDIANTE
# ============================================

@login_required
def estudiante_list(request):
    estudiantes = Estudiante.objects.select_related('persona').all()
    return render(request, 'gestion_tutorias/estudiante_list.html', {'estudiantes': estudiantes})

@login_required
def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    return render(request, 'gestion_tutorias/form.html', {'form': form, 'titulo': 'Nuevo Estudiante'})

@login_required
def estudiante_edit(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'gestion_tutorias/form.html', {'form': form, 'titulo': 'Editar Estudiante'})

@login_required
def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('estudiante_list')
    return render(request, 'gestion_tutorias/confirm_delete.html', {'object': estudiante, 'tipo': 'Estudiante'})

# ============================================
# TUTOR
# ============================================

@login_required
def tutor_list(request):
    tutores = Tutor.objects.select_related('persona').all()
    return render(request, 'gestion_tutorias/tutor_list.html', {'tutores': tutores})

@login_required
def tutor_create(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')
    else:
        form = TutorForm()
    return render(request, 'gestion_tutorias/form.html', {'form': form, 'titulo': 'Nuevo Tutor'})

@login_required
def tutor_edit(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')
    else:
        form = TutorForm(instance=tutor)
    return render(request, 'gestion_tutorias/form.html', {'form': form, 'titulo': 'Editar Tutor'})

@login_required
def tutor_delete(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        tutor.delete()
        return redirect('tutor_list')
    return render(request, 'gestion_tutorias/confirm_delete.html', {'object': tutor, 'tipo': 'Tutor'})

# ============================================
# MATERIA
# ============================================
@login_required
def materia_list(request):
    return render(
        request,
        'gestion_tutorias/materia_list.html'
    )
@login_required
def materia_create(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm()
    return render(request, 'gestion_tutorias/form.html', {'form': form, 'titulo': 'Nueva Materia'})

@login_required
def materia_edit(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'gestion_tutorias/form.html', {'form': form, 'titulo': 'Editar Materia'})

@login_required
def materia_delete(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('materia_list')
    return render(request, 'gestion_tutorias/confirm_delete.html', {'object': materia, 'tipo': 'Materia'})

# ============================================
# TUTORÍA
# ============================================

@login_required
def tutoria_list(request):
    tutorias = Tutoria.objects.select_related('tutor__persona', 'estudiante__persona', 'materia').all()
    return render(request, 'gestion_tutorias/tutoria_list.html', {'tutorias': tutorias})

@login_required
def tutoria_create(request):
    if request.method == 'POST':
        form = TutoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutoria_list')
    else:
        form = TutoriaForm()
    return render(request, 'gestion_tutorias/form.html', {'form': form, 'titulo': 'Nueva Tutoría'})

@login_required
def tutoria_edit(request, pk):
    tutoria = get_object_or_404(Tutoria, pk=pk)
    if request.method == 'POST':
        form = TutoriaForm(request.POST, instance=tutoria)
        if form.is_valid():
            form.save()
            return redirect('tutoria_list')
    else:
        form = TutoriaForm(instance=tutoria)
    return render(request, 'gestion_tutorias/form.html', {'form': form, 'titulo': 'Editar Tutoría'})

@login_required
def tutoria_delete(request, pk):
    tutoria = get_object_or_404(Tutoria, pk=pk)
    if request.method == 'POST':
        tutoria.delete()
        return redirect('tutoria_list')
    return render(request, 'gestion_tutorias/confirm_delete.html', {'object': tutoria, 'tipo': 'Tutoría'})


from django.db.models import Count

@login_required
def reporte_tutorias_estado(request):

    pendientes = Tutoria.objects.filter(
        estado='pendiente'
    ).count()

    aceptadas = Tutoria.objects.filter(
        estado='aceptada'
    ).count()

    finalizadas = Tutoria.objects.filter(
        estado='finalizada'
    ).count()

    rechazadas = Tutoria.objects.filter(
        estado='rechazada'
    ).count()

    total = Tutoria.objects.count()

    context = {
        'pendientes': pendientes,
        'aceptadas': aceptadas,
        'finalizadas': finalizadas,
        'rechazadas': rechazadas,
        'total': total,
    }

    return render(
        request,
        'gestion_tutorias/reporte_estado.html',
        context
    )
class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    
    
from .serializers import (
    PersonaSerializer,
    EstudianteSerializer,
    TutorSerializer,
    TutoriaSerializer
)
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TutoriaViewSet(viewsets.ModelViewSet):
    queryset = Tutoria.objects.all()
    serializer_class = TutoriaSerializer