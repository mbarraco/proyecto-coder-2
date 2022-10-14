from datetime import datetime
from django.test import TestCase
from AppCoder24.models import Curso


class ViewTestCase(TestCase):

    def test_crear_curso(self):
        ahora = datetime.now()
        curso = Curso.objects.create(nombre="test 1234", camada="9091")
        todos_los_cursos = Curso.objects.all()
        assert len(todos_los_cursos) == 1
        assert curso == todos_los_cursos[0]

        assert curso.fecha_de_inicio.year == ahora.year
        assert curso.fecha_de_inicio.month == ahora.month
        assert curso.fecha_de_inicio.day == ahora.day
        assert curso.fecha_de_inicio.hour == ahora.hour
        assert curso.fecha_de_inicio.minute == ahora.minute
