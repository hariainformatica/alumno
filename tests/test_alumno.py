import pytest

from alumno import Alumno

def test_alumno():
    alumno = Alumno('Juan')
    assert alumno.read() == 'Juan'

def test_read():
    alumno = Alumno('Juan')
    assert alumno.read() == 'Juan'

def test_update():
    alumno = Alumno('Juan')
    alumno.update('Pedro')
    assert alumno.read() == 'Pedro'

def test_delete():
    alumno = Alumno('Juan')
    alumno.delete()
    assert alumno.read() == None