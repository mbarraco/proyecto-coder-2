"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from multiprocessing import context
from re import template
from django.urls import path

from AppCoder24.views import (
    CursoDelete,
    CursoDetalle,
    CursoUpdateView,
    CursoList,
    CursoCreacion,
    busqueda_de_curso,
    listar_cursos,
    buscar_curso,
    # clase 23
    MyLogin,
    # MyLogout,
    login_request,
    mostrar_inicio,
    register,
    # clase 24
    editar_perfil,
    agregar_avatar,
)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # CLASE 22
    path("busqueda-de-curso/", busqueda_de_curso, name="busqueda"),
    path("buscar-curso/", buscar_curso),
    path("cursos-lista/", listar_cursos),
    path("curso/list", CursoList.as_view(), name="CursoList"),
    # path("r'(?P<pk>\d+)^$'", CursoDetalle.as_view(), name="CursoDetail"),
    path("curso-nuevo/", CursoCreacion.as_view(), name="CursoNew"),
    path("editar/<pk>", CursoUpdateView.as_view(), name="CursoUpdate"),
    path("borrar/<pk>", CursoDelete.as_view(), name="CursoDelete"),
    # CLASE 23
    path("inicio/", mostrar_inicio, name="Inicio"),
    path("login/", MyLogin.as_view(), name="Login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="AppCoder24/logout.html"),
        name="Logout",
    ),
    path("register/", register, name="Register"),
    # Clase 24
    path("curso/<pk>'", CursoDetalle.as_view(), name="CursoDetail"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
    # Clase 25
    path("", mostrar_inicio),
]
