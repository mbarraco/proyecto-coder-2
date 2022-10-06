from django.contrib import admin
from django.urls import path, include

from blog.views import (
    buscar,
    mostrar_inicio,
    procesar_formulario_autor,
    procesar_formulario_articulo,
    procesar_formulario_seccion,
)


urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario-autor/", procesar_formulario_autor),
    path("formulario-articulo/", procesar_formulario_articulo),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("buscar-articulo/", buscar),
]
