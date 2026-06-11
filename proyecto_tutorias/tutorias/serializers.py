from rest_framework import serializers
from .models import Estudiante, Tutor, Tutoria


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class TutoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoria
        fields = '__all__'
