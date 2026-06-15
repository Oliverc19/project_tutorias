from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Tutor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Tutoria(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )

    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()
    tema = models.CharField(max_length=200)
    estado = models.CharField(max_length=30)

    def __str__(self):
        return self.tema
# Create your models here.
