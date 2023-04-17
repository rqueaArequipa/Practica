from django.shortcuts import render
from .models import Pregunta, Opcion, Nota, Alumno

def Index(request):
    list_pregunta = Pregunta.objects.all()
    context = {
        'pregunta' : list_pregunta
    }

    return render(request, 'examen/pregunta.html', context)

def Resultado(request):
    list_pregunta = Pregunta.objects.all()
    puntaje = 0
    for i in list_pregunta:
        puntaje += int(request.POST['opcion_' + str(i.id)])
    
    context = {
        'nota' : puntaje
    }
    return render(request, 'examen/resultado.html', context)

def Alumnos(request):
    nombre = request.POST['nombre']
    email = request.POST['email']
    alumno = Alumno(nombre = nombre, email = email)
    alumno.save()
    nota = int(request.POST['nota'])
    puntaje = Nota(nota = nota, alumno = alumno)
    puntaje.save()
    list_alumno = Alumno.objects.all()
    context = {
        'alumno': list_alumno
    }

    return render(request, 'examen/lista.html', context)