from django.shortcuts import render

from AppCoder.models import Estudiante


def inicio(request):
    estudiante = Estudiante(
        nombre="Exequiel", apellido="Velazquez", email="eze@hotmail.com"
    )
    estudiante.save()
    contexto = {"estudiante_1": estudiante}
    return render(request, "AppCoder/inicio.html", contexto)


def cursos(request):
    return render(request, "AppCoder/cursos.html")


def profesores(request):
    return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder/entregables.html")
