from django.shortcuts import render

from AppCoder.models import Estudiante
from clase_21.AppCoder.models import Curso


def ayuda(request):
    return render(request, "AppCoder/ayuda.html")


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


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "AppCoder/inicio.html")

    curso = Curso(curso=request.POST["curso"], camada=request.POST["camada"])
    curso.save()
    return render(request, "AppCoder/inicio.html")


def procesar_formulario_2(request):
    if request.method != "POST":
        return render(request, "AppCoder/inicio.html")

    curso = Curso(curso=request.POST["curso"], camada=request.POST["camada"])
    curso.save()
    return render(request, "AppCoder/inicio.html")
