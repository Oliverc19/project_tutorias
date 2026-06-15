"""
URL configuration for proyecto_tutorias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from tutorias.views import( EstudianteListCreate,
    TutorListCreate,
    TutoriaListCreate,
    EstudianteDetail,
    TutorDetail,
    TutoriaDetail
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("estudiantes/", EstudianteListCreate.as_view()),
    path("estudiantes/<int:pk>/", EstudianteDetail.as_view()),

    path("tutores/", TutorListCreate.as_view()),
    path("tutores/<int:pk>/", TutorDetail.as_view()),

    path("tutorias/", TutoriaListCreate.as_view()),
    path("tutorias/<int:pk>/", TutoriaDetail.as_view()),
    
]
