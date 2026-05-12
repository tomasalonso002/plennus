from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction

# Create your views here.
from .forms import UserForm,AlumnoForm,PersonaForm, Editar_user_form
from .models import Alumno, Persona
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView
from django.contrib import messages


        

@login_required
def get_alumnos(request):
    alumnos = Alumno.objects.filter(activo = True).order_by("-id")
    contexto = {"alumnos":alumnos}
    return render(request, "alumnos/alumnos.html", contexto)

@login_required
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

@login_required
def borrar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id = id)
    if request.method == "POST":
        if alumno.activo:
            alumno.activo=False
            alumno.save()
            usuario = alumno.persona.user
            usuario.is_active = False
            usuario.save()
        return redirect("alumnos")
    return render(request,"alumnos/alumnos.html",{"alumnos":alumno})

@login_required
def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id = id)
    persona = alumno.persona
    usuario= alumno.persona.user
    if request.method == "POST":
        form_alumno = AlumnoForm(request.POST, request.FILES, instance=alumno)
        form_persona = PersonaForm(request.POST,request.FILES, instance=persona)
        form_usuario = Editar_user_form(request.POST, request.FILES, instance=usuario)
        if form_persona.is_valid() and form_usuario.is_valid() and form_usuario.is_valid():
            form_alumno.save()
            form_persona.save()
            form_usuario.save()
            return redirect("alumnos")
    else:
        form_alumno = AlumnoForm(instance=alumno)
        form_persona = PersonaForm(instance=persona)
        form_usuario = Editar_user_form(instance=usuario)
    return render(request, "alumnos/editar_alumno.html", {"form_alumno":form_alumno,"form_persona": form_persona, "form_usuario":form_usuario})

    


