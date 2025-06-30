from django.db import models
from Aplicaciones.Docentes.models import Docente

# Create your models here.
class Asignatura(models.Model):
    ESTADO_CHOICES = [('Activo', 'Activo'),('Inactivo', 'Inactivo'),]
    idAignatura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    nivel = models.CharField(max_length=200)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    docentes = models.ManyToManyField(Docente)

    def __str__(self):
        return f"Asignatura: {self.nombre} ({self.carrera})"
