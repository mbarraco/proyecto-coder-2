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
from django.urls import path

from AppCoder.views import (
    CursoDelete,
    CursoDetalle,
    CursoUpdateView,
    CursoList,
    CursoCreacion,
    ayuda,
    buscar,
    buscar_2,
    busqueda,
    busqueda_2,
    busqueda_de_curso,
    entregables,
    estudiantes,
    inicio,
    cursos,
    profesores,
    procesar_formulario,
    procesar_formulario_2,
    listar_cursos,
    buscar_curso,
)

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("entregables/", entregables, name="entregables"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("cursos/", cursos, name="mis_cursos"),
    path("profesores/", profesores, name="profesores"),
    path("ayuda/", ayuda),
    path("formulario/", procesar_formulario, name="formulario"),
    path("formulario-2/", procesar_formulario_2, name="formulario_2"),
    path("busqueda/", busqueda, name="busqueda"),
    path("busqueda-2/", busqueda_2, name="busqueda-2"),
    path("buscar/", buscar),
    path("buscar-2/", buscar_2),
    # CLASE 22: repaso de busqueda
    path("busqueda-de-curso/", busqueda_de_curso, name="busqueda"),
    path("buscar-curso/", buscar_curso),
    # URLS CLASE 22
    path("cursos-lista/", listar_cursos),
    path("curso/list", CursoList.as_view(), name="CursoList"),
    path("curso/<pk>'", CursoDetalle.as_view(), name="CursoDetail"),
    path("curso-nuevo/", CursoCreacion.as_view(), name="CursoNew"),
    path("editar/<pk>", CursoUpdateView.as_view(), name="CursoUpdate"),
    path("borrar/<pk>", CursoDelete.as_view(), name="CursoDelete"),
]
