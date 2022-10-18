from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse

from AppCoder24.models import Avatar, Curso

# Clase 23 ####
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Clase 24 ####
from AppCoder24.forms import AvatarForm, UserEditionForm


###############################################################################
# Clase 22
###############################################################################


class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppCoder24/cursos_list.html"


@login_required
def listar_cursos(request):
    todos_los_cursos = Curso.objects.all()
    avatar = Avatar.objects.filter(user=request.user).first()
    contexto = {
        "cursos_encontrados": todos_los_cursos,
        "avatar": avatar.imagen.url
    }

    return render(request, "AppCoder24/listar-cursos.html", contexto)


class CursoDetalle(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "AppCoder24/curso_detalle.html"


class CursoCreacion(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ["nombre", "camada"]
    success_url = "/appcoder24/curso/list"


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = "/appcoder24/curso/list"
    fields = ["nombre", "camada"]


class CursoDelete(LoginRequiredMixin, DeleteView):

    model = Curso
    success_url = "/appcoder24/curso/list"


@login_required
def busqueda_de_curso(request):
    return render(request, "AppCoder24/busqueda_de_curso.html")


@login_required
def buscar_curso(request):
    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "cursos_encontrados": cursos}

        return render(request, "AppCoder24/resultado_busqueda_nombre.html", contexto)


###############################################################################
# Clase 23
###############################################################################

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required


class MyLogin(LoginView):
    template_name = "AppCoder24/login.html"


@login_required
def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "AppCoder24/inicio.html", contexto)


# Eto es lo que muestra la slide de CODER
# Yo prefiero usar MyLogin
def login_request(request):

    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "AppCoder24/login.html", {"form": form})

    form = AuthenticationForm(request, data=request.POST)

    if not form.is_valid():
        return render(
            request,
            "AppCoder24/inicio.html",
            {"mensaje": "Error: los datos ingresados no son correctos"},
        )
    else:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            return render(
                request, "AppCoder24/inicio.html", {"mensaje": f"Bienvenido {username}"}
            )
        else:
            return render(
                request,
                "AppCoder24/inicio.html",
                {"mensaje": "El usuario no existe en nuestra appliación"},
            )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "AppCoder24/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "AppCoder24/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "AppCoder24/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {
        "user": user,
        "form": form,
        "avatar": avatar.imagen.url
    }
    return render(request, "AppCoder24/editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "AppCoder24/inicio.html")

    contexto = {"form": form}
    return render(request, "AppCoder24/avatar_form.html", contexto)
