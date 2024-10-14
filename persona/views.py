from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_estudiantes(request):
    
    estudiantes = Persona.objects.filter(rol='Estudiante')
    
    return render(request, 'lista-estudiantes.html',{
        'title': 'Lista de estudiantes',
        'estudiantes': estudiantes
    })

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Persona

def registrar_persona(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtnombre')
        apellidos = request.POST.get('txtapellido')
        dni = request.POST.get('numdni')
        telefono = request.POST.get('numtelefono')
        email = request.POST.get('correo')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        rol = request.POST.get('txtrol')

        # Asegúrate de que todos los campos tengan valores
        if nombre and apellidos and dni and telefono and email and fecha_nacimiento and rol:
            persona = Persona(
                nombre=nombre,
                apellidos=apellidos,
                dni=dni,
                telefono=telefono,
                email=email,
                fecha_nacimiento=fecha_nacimiento,
                rol=rol
            )
            # Guardar en la base de datos
            persona.save()
            print(f'Persona guardada: {persona}')  # Debug: ver si se guarda correctamente

            # Redirigir a la lista de estudiantes
            return redirect('lista-estudiantes')
        else:
            return HttpResponse("Error: Todos los campos son obligatorios.")

    return render(request, 'lista-estudiantes.html')
