from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Curso
from django.shortcuts import render

def get_curso(request):
    
    Cursos = Curso.objects.values()
    print(Cursos.estudiantes.values())
    
    return render (request, 'curso.html',{'title': 'Lista de estudiantes',
        'curso': Cursos})

