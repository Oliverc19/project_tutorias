from rest_framework import generics
from .models import Estudiante, Tutor, Tutoria
from .serializers import (
EstudianteSerializer,
    TutorSerializer,
    TutoriaSerializer
)


class EstudianteListCreate(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    
class TutorListCreate(generics.ListCreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TutoriaListCreate(generics.ListCreateAPIView):
    queryset = Tutoria.objects.all()
    serializer_class = TutoriaSerializer
    
class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TutoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutoria.objects.all()
    serializer_class = TutoriaSerializer    
    
# Create your views here.
