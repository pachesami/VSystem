from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone  

class matriculas(models.Model):  
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=100)
    cursos = models.CharField(max_length=100)
    fecha_de_inicio = models.DateField(default=timezone.now)  
    estado = models.CharField(max_length=100)
    costo = models.FloatField()

    def clean(self):
        
        if self.costo is not None and self.costo < 0:
            raise ValidationError('El costo no puede ser negativo.')

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'
