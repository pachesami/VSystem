
from django.shortcuts import render

def get_curso(request):
    return render (request, 'curso.html')
