from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone  # Asegúrate de importar desde django.utils

class matriculas(models.Model):  # Cambié el nombre a Matriculas para seguir la convención de nombres
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=100)
    cursos = models.CharField(max_length=100)
    fecha_de_inicio = models.DateField(default=timezone.now)  # Establecer valor por defecto
    estado = models.CharField(max_length=100)
    costo = models.FloatField()

    def clean(self):
        # Verifica si costo tiene un valor
        if self.costo is not None and self.costo < 0:
            raise ValidationError('El costo no puede ser negativo.')

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'
