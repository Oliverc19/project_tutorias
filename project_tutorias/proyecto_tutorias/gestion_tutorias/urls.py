from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/materias', views.MateriaViewSet)
router.register(r'api/personas', views.PersonaViewSet)

router.register(r'api/estudiantes', views.EstudianteViewSet)

router.register(r'api/tutores', views.TutorViewSet)

router.register(r'api/tutorias', views.TutoriaViewSet)


urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Persona
    path('personas/', views.persona_list, name='persona_list'),
    path('personas/nueva/', views.persona_create, name='persona_create'),
    path('personas/<str:pk>/editar/', views.persona_edit, name='persona_edit'),
    path('personas/<str:pk>/eliminar/', views.persona_delete, name='persona_delete'),

    # Estudiante
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('estudiantes/nuevo/', views.estudiante_create, name='estudiante_create'),
    path('estudiantes/<str:pk>/editar/', views.estudiante_edit, name='estudiante_edit'),
    path('estudiantes/<str:pk>/eliminar/', views.estudiante_delete, name='estudiante_delete'),

    # Tutor
    path('tutores/', views.tutor_list, name='tutor_list'),
    path('tutores/nuevo/', views.tutor_create, name='tutor_create'),
    path('tutores/<str:pk>/editar/', views.tutor_edit, name='tutor_edit'),
    path('tutores/<str:pk>/eliminar/', views.tutor_delete, name='tutor_delete'),

    # Materia
    path('materias/', views.materia_list, name='materia_list'),
    path('materias/nueva/', views.materia_create, name='materia_create'),
    path('materias/<int:pk>/editar/', views.materia_edit, name='materia_edit'),
    path('materias/<int:pk>/eliminar/', views.materia_delete, name='materia_delete'),

    # Tutoría
    path('tutorias/', views.tutoria_list, name='tutoria_list'),
    path('tutorias/nueva/', views.tutoria_create, name='tutoria_create'),
    path('tutorias/<int:pk>/editar/', views.tutoria_edit, name='tutoria_edit'),
    path('tutorias/<int:pk>/eliminar/', views.tutoria_delete, name='tutoria_delete'),

    # Reporte
    path(
        'reportes/estado/',
        views.reporte_tutorias_estado,
        name='reporte_estado'
    ),
    path('logout/', views.cerrar_sesion, name='logout'),
]

urlpatterns += router.urls