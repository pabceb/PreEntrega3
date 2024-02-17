from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

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
    
    
    
    # FORMA 3 - RENDER
    dic_contexto = {'nombre': 'Jade', 'apellido': 'Melon'}
    return render(request, 'inicio.html', dic_contexto)
    
    
    
    
    
    
    

def mostrar_horario(request):
    fecha = datetime.now()
    return HttpResponse(f'Fecha: {fecha}')

def saludo(request, nombre, apellido):
    # nombre = ''
    # apellido = ''
    return HttpResponse(f' Bienvenid@ {nombre} {apellido}')