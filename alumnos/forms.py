from django import forms
from django.contrib.auth.models import User
from .models import Persona, Alumno, Consultas

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name","email"]

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields =["telefono", "direccion","imagen"]
    
class AlumnoForm(forms.ModelForm):
    class Meta:
        model=Alumno
        fields = ["nro_alumno"]

class Editar_user_form(forms.ModelForm):
    class Meta:
        model= User
        fields= ['username', 'last_name', 'email', 'first_name']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model= Consultas
        fields= ['nombre', 'email', 'telefono', 'consulta']