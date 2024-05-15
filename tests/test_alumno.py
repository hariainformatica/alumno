import pytest

from alumno import Alumno

def test_alumno():
    alumno = Alumno('Juan')
    assert alumno.nombre == 'Juan'