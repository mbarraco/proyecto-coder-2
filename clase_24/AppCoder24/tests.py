from datetime import datetime
from django.test import TestCase
from AppCoder24.models import Curso


class ViewTestCase(TestCase):

    def test_crear_curso(self):
        Curso.objects.create(nombre="test 1234", camada="9091")
        todos_los_cursos = Curso.objects.all()
        assert len(todos_los_cursos) == 1
        assert todos_los_cursos[0].nombre == "test 1234"


    def test_crear_curso_sin_fecha(self):
        Curso.objects.create(nombre="test 1234", camada="9091")
        todos_los_cursos = Curso.objects.all()
        assert todos_los_cursos[0].fecha_de_inicio is None


    def test_crear_4_cursos(self):
        Curso.objects.create(nombre="curso 01", camada=1)
        Curso.objects.create(nombre="curso 02", camada=2)
        Curso.objects.create(nombre="curso 03", camada=3)
        Curso.objects.create(nombre="curso 04", camada=4)
        Curso.objects.create(nombre="curso 05", camada=5)
        todos_los_cursos = Curso.objects.all()
        assert len(todos_los_cursos) == 4

















