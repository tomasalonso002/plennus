from django.urls import path

from . import views

urlpatterns = [
    path("crear_alumno/", views.crear_usuario, name="crear_alumno"),
    path("mostrar_alumnos/", views.get_alumnos, name="mostrar_alumnos"),
    path("editar/<int:id>", views.editar_alumno, name="editar_alumno"),
]

