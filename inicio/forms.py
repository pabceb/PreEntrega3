from django import forms

# se crean formularios de manera parecida a clases
class FormularioCreacionAlumno(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()