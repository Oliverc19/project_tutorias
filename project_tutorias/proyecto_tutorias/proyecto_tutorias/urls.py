from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.shortcuts import redirect
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from gestion_tutorias import views

# Configuración del Router para la API
router = DefaultRouter()
router.register(r'materias', views.MateriaViewSet)
router.register(r'personas', views.PersonaViewSet)
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'tutores', views.TutorViewSet)
router.register(r'tutorias', views.TutoriaViewSet)
=======
from django.contrib.auth import views as auth_views
>>>>>>> b3342f674c46a8e4878c607de002bd0256026d41

urlpatterns = [
    # Administración
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    
    
    path('api/', include(router.urls)),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Dashboard y Web
    path('', RedirectView.as_view(url='/login/'), name='index'),
    path('login/', views.login_view, name='login_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.cerrar_sesion, name='logout'),

    # Rutas Web (Personas)
    path('personas/', views.persona_list, name='persona_list'),
    path('personas/nueva/', views.persona_create, name='persona_create'),
    path('personas/<str:pk>/editar/', views.persona_edit, name='persona_edit'),
    path('personas/<str:pk>/eliminar/', views.persona_delete, name='persona_delete'),

    # Rutas Web (Estudiantes)
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('estudiantes/nuevo/', views.estudiante_create, name='estudiante_create'),
    path('estudiantes/<str:pk>/editar/', views.estudiante_edit, name='estudiante_edit'),
    path('estudiantes/<str:pk>/eliminar/', views.estudiante_delete, name='estudiante_delete'),

    # Rutas Web (Tutores)
    path('tutores/', views.tutor_list, name='tutor_list'),
    path('tutores/nuevo/', views.tutor_create, name='tutor_create'),
    path('tutores/<str:pk>/editar/', views.tutor_edit, name='tutor_edit'),
    path('tutores/<str:pk>/eliminar/', views.tutor_delete, name='tutor_delete'),

    # Rutas Web (Materias)
    path('materias/', views.materia_list, name='materia_list'),
    path('materias/nueva/', views.materia_create, name='materia_create'),
    path('materias/<int:pk>/editar/', views.materia_edit, name='materia_edit'),
    path('materias/<int:pk>/eliminar/', views.materia_delete, name='materia_delete'),

    # Rutas Web (Tutorías)
    path('tutorias/', views.tutoria_list, name='tutoria_list'),
    path('tutorias/nueva/', views.tutoria_create, name='tutoria_create'),
    path('tutorias/<int:pk>/editar/', views.tutoria_edit, name='tutoria_edit'),
    path('tutorias/<int:pk>/eliminar/', views.tutoria_delete, name='tutoria_delete'),

    # Reportes
    path('reportes/estado/', views.reporte_tutorias_estado, name='reporte_estado'),
]
STATIC_URL = 'static/'
=======
    path('', include('gestion_tutorias.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
   path(
    'logout/',
    auth_views.LogoutView.as_view(next_page='/login/'),
    name='logout'
    ),
    

]
>>>>>>> b3342f674c46a8e4878c607de002bd0256026d41
