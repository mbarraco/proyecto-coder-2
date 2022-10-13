from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso, Estudiante


def ayuda(request):
    return render(request, "AppCoder23/ayuda.html")


def inicio(request):
    estudiante = Estudiante(
        nombre="Rodrigo", apellido="Pacheco", email="eze@hotmail.com"
    )
    estudiante.save()
    contexto = {"estudiante_1": estudiante}
    return render(request, "AppCoder23/inicio.html", contexto)


def cursos(request):
    return render(request, "AppCoder23/cursos.html")


def profesores(request):
    return render(request, "AppCoder23/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder23/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder23/entregables.html")


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "AppCoder23/formulario.html")

    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
    curso.save()
    return render(request, "AppCoder23/inicio.html")


def procesar_formulario_2(request):
    if request.method != "POST":
        mi_formulario = CursoFormulario()
    else:
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder23/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppCoder23/formulario_2.html", contexto)


def busqueda(request):
    return render(request, "AppCoder23/busqueda.html")


def busqueda_2(request):
    return render(request, "AppCoder23/busqueda_2.html")


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

        return render(request, "AppCoder23/resultado_busqueda.html", contexto)


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class CursoList(ListView):
    model = Curso
    template_name = "AppCoder23/cursos_list.html"


def listar_cursos(request):
    todos_los_cursos = Curso.objects.all()
    contexto = {"cursos_encontrados": todos_los_cursos}
    return render(request, "AppCoder23/listar-cursos.html", contexto)


class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder23/curso_detalle.html"


from django.urls import reverse


class CursoCreacion(CreateView):
    model = Curso
    fields = ["nombre", "camada"]

    def get_success_url(self):
        return reverse("CursoList")


class CursoUpdateView(UpdateView):
    model = Curso
    success_url = "/AppCoder23/curso/list"
    fields = ["nombre", "camada"]


class CursoDelete(DeleteView):

    model = Curso
    success_url = "/AppCoder23/curso/list"


def busqueda_de_curso(request):
    return render(request, "AppCoder23/busqueda_de_curso.html")


def buscar_curso(request):
    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "cursos_encontrados": cursos}

        return render(request, "AppCoder23/resultado_busqueda_nombre.html", contexto)
