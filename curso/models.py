# models.py
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()  # Duración en horas

    def __str__(self):
        return self.nombre
