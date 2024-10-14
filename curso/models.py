from django.db import models
from django.core.exceptions import ValidationError  
from persona.models import Persona

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()  
    capacidadMaxima = models.IntegerField()
    profesor = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.profesor and self.profesor.rol != 'Docente':
            raise ValidationError('El rol de profesor debe ser docente.') 
        super().save(*args, **kwargs)  

    def clean(self):
        # Verifica si capacidadMaxima tiene un valor
        if self.capacidadMaxima is not None and self.capacidadMaxima <= 0:
            raise ValidationError('La capacidad máxima no puede ser negativa o cero.')

class EstudianteYCurso(models.Model):  
    dni = models.CharField(max_length=20, primary_key=True, default='SIN_DNI')
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)  
    fechadeinicio = models.DateField()  
    fechefinal = models.DateField()     
    estado = models.CharField(max_length=100)
    nota_final = models.FloatField()

    def __str__(self):
        return self.nombre  
