from listaalumnos import ListaAlumnos
from fichero import Fichero
import pytest
import os

FILENAME = 'lista.dat'
DATA    = 'Juan' + ListaAlumnos.LIMITCHAR + 'Pedro'

@pytest.fixture
def fichero():
    return Fichero(FILENAME)

def test_ficheroLeer(fichero):
    os.remove(FILENAME)
    assert fichero.leer() == ''

def test_ficheroEscribir(fichero):
    assert fichero.escribir(DATA) == True

def test_ficheroLeer2(fichero):
    assert fichero.leer() == DATA