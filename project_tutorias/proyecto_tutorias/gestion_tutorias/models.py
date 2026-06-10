from django.db import models

class Persona(models.Model):
    ci = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=3, choices=(('EST', 'Estudiante'), ('TUT', 'Tutor')))
    def __str__(self):
        return f"{self.ci} - {self.nombre} {self.paterno} {self.materno} ({self.email})"

class Estudiante(models.Model):
    persona = models.OneToOneField(
        Persona, 
        on_delete=models.CASCADE, 
        primary_key=True
    )
    carrera = models.CharField(max_length=100)
    codigo_estudiante = models.CharField(max_length=20, unique=True)

class Tutor(models.Model):
    persona = models.OneToOneField(
        Persona, 
        on_delete=models.CASCADE, 
        primary_key=True
    )
    especialidad = models.CharField(max_length=100)
    cubiculo = models.CharField(max_length=10)

class Materia(models.Model):
    # Aquí Django creará automáticamente un campo 'id' autoincremental
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Tutoria(models.Model):
    # Relacionamos la tutoría usando las llaves primarias de Tutor y Estudiante
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"Tutoría de {self.materia.nombre} - {self.fecha_hora}"