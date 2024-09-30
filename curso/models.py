# models.py
from django.db import models

from persona.models import Persona

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()  # Duración en horas
    
    estudiantes = models.ManyToManyField(Persona, related_name='curso', blank=True)
    
    def __str__(self):
        return self.nombre
