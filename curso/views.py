from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Curso, EstudianteYCurso
from django.shortcuts import render
from .models import EstudianteYCurso

def get_curso(request):
    
    Cursos = Curso.objects.values()
    
    
    return render (request, 'estudianteCurso.html',{'title': 'Lista de estudiantes',
        'curso': Cursos})
    

def lista_estudiantes_cursos(request):
    estudiantes_cursos = EstudianteYCurso.objects.all()
    print(estudiantes_cursos)
    return render(request, 'estudianteCurso.html', {'estudiantes_cursos': estudiantes_cursos})
