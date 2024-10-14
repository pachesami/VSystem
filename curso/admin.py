from django.contrib import admin
from .models import Curso 
from .models import EstudianteYCurso


admin.site.register(Curso)

# Register your models here.

admin.site.register(EstudianteYCurso)
