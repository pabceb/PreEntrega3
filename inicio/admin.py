from django.contrib import admin
from inicio.models import Alumno

# Register your models here.
# v1
admin.site.register(Alumno)

# v2
# admin.site.register([Alumno, otro_model])