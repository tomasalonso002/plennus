from django.shortcuts import render, redirect, get_object_or_404

from django.db import transaction

# Create your views here.
from .forms import UserForm,AlumnoForm,PersonaForm
from .models import Alumno, Persona
from django.contrib.auth.models import User

def get_alumnos(request):
    alumnos = Alumno.objects.all()
    contexto = {"alumnos":alumnos}
    return render(request, "alumnos/alumnos.html", contexto)


@transaction.atomic
def crear_usuario(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        persona_form = PersonaForm(request.POST, request.FILES)
        alumno_form = AlumnoForm(request.POST)
        if user_form.is_valid() and persona_form.is_valid() and alumno_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            persona = persona_form.save(commit=False)
            persona.user = user
            persona.save()
            alumno = alumno_form.save(commit=False)
            alumno.persona=persona
            alumno.save()
            return redirect("mostrar_alumnos")
    else:
        user_form = UserForm()
        persona_form = PersonaForm()
        alumno_form = AlumnoForm()
    return render(request, 'alumnos/añadir_alumno.html', {'user_form': user_form, 'persona_form': persona_form,'alumno_form': alumno_form})



def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    persona = get_object_or_404(Persona,  = alumno)

    if request.method == "POST":



