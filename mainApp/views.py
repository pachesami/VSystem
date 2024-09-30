from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def get_prueba(request):
    return render(request, 'prueba.html')

def get_curso(request):
    return render(request, 'curso.html')
