from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    # no se le da un valor, se le da el tipo de dato
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    nota = models.IntegerField()
    # para que lo reconozca la DB (y se creen las tablas) --> manage.py makemigrations
    # se creó la migración
    # se tiene que migrar a la DB --> manage.py migrate 
    # ! actualizar DB
    
    # para que muestre con formato en el html
    def __str__(self):
        return f'{self.nombre} {self.apellido} - Nota: {self.nota}'
    
    
    