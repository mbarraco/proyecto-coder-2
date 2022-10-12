from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso, Estudiante


def ayuda(request):
    return render(request, "AppCoder/ayuda.html")


def inicio(request):
    estudiante = Estudiante(
        nombre="Rodrigo", apellido="Pacheco", email="eze@hotmail.com"
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
        return render(request, "AppCoder/formulario.html")

    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
    curso.save()
    return render(request, "AppCoder/inicio.html")


def procesar_formulario_2(request):
    if request.method != "POST":
        mi_formulario = CursoFormulario()
    else:
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppCoder/formulario_2.html", contexto)


def busqueda(request):
    return render(request, "AppCoder/busqueda.html")


def busqueda_2(request):
    return render(request, "AppCoder/busqueda_2.html")


def buscar(request):
    respuesta = f"Buscando la camada nro: {request.GET['camada']}"
    return HttpResponse(respuesta)  # TODO: podríamos mostrarla, no?


def buscar_2(request):

    if not request.GET["camada"]:
        return HttpResponse("No enviaste datos")
    else:
        camada_a_buscar = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada_a_buscar)

        contexto = {"camada": camada_a_buscar, "cursos_encontrados": cursos}

        return render(request, "AppCoder/resultado_busqueda.html", contexto)
