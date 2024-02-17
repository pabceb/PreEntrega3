from django.urls import path
from inicio.views import inicio, mostrar_horario, saludo, crear_alumno, mostrar_alumnos, crear_nuevo_alumno

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('mostrar-horario/', mostrar_horario, name = 'mostrar_horario'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name = 'saludo'),
    path('alumnos/nuevo/<str:nombre>/<str:apellido>/<int:edad>/', crear_alumno, name = 'crear_alumno'),
    path('alumnos/nuevo/', crear_nuevo_alumno, name = 'nuevo_alumno'),
    path('mostrar_alumnos/', mostrar_alumnos, name = 'mostrar_alumnos'),
]