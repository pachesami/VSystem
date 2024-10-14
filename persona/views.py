# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

def lista_estudiantes(request):
    if request.method == 'POST':
        
        nombre = request.POST.get('txtnombre')
        apellido = request.POST.get('txtapellido')
        dni = request.POST.get('numdni')
        telefono = request.POST.get('numtelefono')
        email = request.POST.get('correo')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        rol = request.POST.get('txtrol')

        if nombre and apellido and dni and telefono and email and fecha_nacimiento and rol:
            persona = Persona(
                nombre=nombre,
                apellido=apellido,
                dni=dni,
                telefono=telefono,
                email=email,
                fecha_nacimiento=fecha_nacimiento,
                rol=rol
            )
            try:

                persona.save()

            except Exception as e:
                print(f"Error al guardar la persona: {e}")
                return HttpResponse(f"Error al guardar: {e}")
        else:
            return HttpResponse("Error: Todos los campos son obligatorios.")


    estudiantes = Persona.objects.filter(rol='Estudiante')
    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de estudiantes',
        'estudiantes': estudiantes
    })
