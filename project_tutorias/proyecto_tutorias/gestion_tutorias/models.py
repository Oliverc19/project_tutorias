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
    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

from django.db import models

class Tutoria(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
        ('finalizada', 'Finalizada'),
    ]
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE)
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    materia = models.ForeignKey('Materia', on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    estado = models.CharField(
        max_length=20, 
        choices=ESTADOS, 
        default='pendiente'
    )

    class Meta:
        verbose_name = "Tutoría"
        verbose_name_plural = "Tutorías"

    def __str__(self):
        return f"{self.materia} - {self.estado}"