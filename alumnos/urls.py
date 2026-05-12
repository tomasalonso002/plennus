from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_alumnos, name="alumnos"),
    path("crear_alumno/", views.crear_usuario, name="crear_alumno"),
    path("mostrar_alumnos/", views.get_alumnos, name="mostrar_alumnos"),
    path("borrar_alumno/<int:id>", views.borrar_alumno, name="borrar_alumno"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
]

