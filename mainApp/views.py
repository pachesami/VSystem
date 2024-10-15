from django.shortcuts import render
from matriculas.models import matriculas
 
def inicio(request):
    return render(request, 'index.html')

def get_prueba(request):
    return render(request, 'prueba.html')

def get_curso(request):
    return render(request, '../curso/templates/curso.html')


def lista_matriculas(request):
    matricula = matriculas.objects.all()
    return render(request, 'prueba.html', {'matriculas': matricula})
