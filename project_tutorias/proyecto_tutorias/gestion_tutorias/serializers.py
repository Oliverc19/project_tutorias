from rest_framework import serializers
from .models import Materia, Tutoria, Tutor, Estudiante, Persona

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__' 

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()  # Anidamos el serializer de Persona
    class Meta:
        model = Estudiante
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()  # Anidamos el serializer de Persona
    class Meta:
        model = Tutor
        fields = '__all__'

class TutoriaSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer()  # Anidamos el serializer de Tutor
    estudiante = EstudianteSerializer()  # Anidamos el serializer de Estudiante
    materia = MateriaSerializer()  # Anidamos el serializer de Materia
    class Meta:
        model = Tutoria
        fields = '__all__'
        