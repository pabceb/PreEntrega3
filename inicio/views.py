from datetime import datetime
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader

# para modificar la DB
from inicio.models import Alumno
from inicio.forms import FormularioCreacionAlumno
# Create your views here.

def inicio(request):
    # return HttpResponse('Primera web')
    # return HttpResponse('<h1>Primera web</h1><br><p>Subtitulo</p>')
# para representar HTML --> usar templates
    
    # FORMA 1 - INICIAL
    
    # archivo_abierto = open(r'C:\Users\pablo\Desktop\0 - Pablo\CODE\CoderHouse\PreEntrega3\templates\inicio.html', 'r')

    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    # # se necesita crear un contexto
    
    # #contexto = Context({}) # Es la información que se le va a pasar al template
    # dic_contexto = {'nombre': 'Jade',
    #                 'apellido': 'Melon'}
    # contexto = Context(dic_contexto)
    # template_renderizado = template.render(contexto)
    
    # return HttpResponse(template_renderizado)
    
    # FORMA 2 - CARGADORES
    # template = loader.get_template('inicio.html')
    # # se puede acortar la direccion cambiando en Settings.py DIRS[BASE_DIR / 'templates'] 
    # # ahora no se requiere contexto --> se pasa directamente el diccionario
       
    # dic_contexto = {'nombre': 'Jade',
    #                 'apellido': 'Melon'}

    # template_renderizado = template.render(dic_contexto)
    
    # return HttpResponse(template_renderizado)
    
    # FORMA 3 - RENDER - ok
    # dic_contexto = {'nombre': 'Jade', 'apellido': 'Melon'}
    # return render(request, 'inicio.html', dic_contexto)
    
    # modificar para ver listados de alumnos
    
    dic_contexto = {'nombre': 'Jade', 'apellido': 'Melon'}
    return render(request, 'inicio.html', dic_contexto)

def mostrar_horario(request):
    fecha = datetime.now()
    return HttpResponse(f'Fecha: {fecha}')

def saludo(request, nombre, apellido):
    # nombre = ''
    # apellido = ''
    return HttpResponse(f' Bienvenid@ {nombre} {apellido}')

def crear_alumno(request, nombre, apellido, edad):
    alumno = Alumno(nombre = nombre, apellido = apellido, edad = edad, nota = random.randint(1,10))
    # devuelve None porque todavía no se guardó en la DB
    alumno.save() # método que viene por herencia de models
    # ojo que se cargan varias veces cada vez que se ejecuta esa web
    # no usar de esta manera en carga de url
    
    return render(request, 'crear_alumno.html', {'alumno': alumno}) 

def crear_nuevo_alumno(request):
    # version1 - con HTML
    #if request.method == 'POST':
        # nombre = request.POST.get('nombre')
        # apellido = request.POST.get('apellido')
        # edad = request.POST.get('edad')
        # alumno = Alumno(nombre = nombre, apellido = apellido, edad = edad, nota = random.randint(1,10))
        # alumno.save()
        
    # VERSION 2 - Formularios de Django
    
    formulario_crea = FormularioCreacionAlumno()
    
    if request.method == 'POST':
        formulario_crea = FormularioCreacionAlumno(request.POST)
        if formulario_crea.is_valid():
            nombre = formulario_crea.cleaned_data.get('nombre')
            apellido = formulario_crea.cleaned_data.get('apellido')
            edad = formulario_crea.cleaned_data.get('edad')
            nota = random.randint(1,10)
            alumno = Alumno(nombre = nombre, apellido = apellido, edad = edad, nota = nota)
            alumno.save()
            return redirect('mostrar_alumnos')
        
    
    return render(request, 'crear_nuevo_alumno.html',{'formulario_crea': formulario_crea})
    
    


def mostrar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'mostrar_alumnos.html', {'alumnos': alumnos})

