from listaalumnos import ListaAlumnos
import pytest

# Test de la clase ListaAlumnos
def test_listaalumnos():
    lista = ListaAlumnos()
    assert len(lista) == 0

    lista.agregar('Juan')
    assert len(lista) == 1

    lista.agregar('Pedro')
    assert len(lista) == 2

    assert lista[0] == 'Juan'
    assert lista[1] == 'Pedro'

    lista[0] = 'Luis'
    assert lista[0] == 'Luis'

    del lista[0]
    assert len(lista) == 1

    assert 'Pedro' in lista
    assert 'Luis' not in lista

    assert lista == ['Pedro']

    lista.agregar('Juan')
    assert lista == ['Pedro', 'Juan']

    lista.delete('Juan')
    assert lista == ['Pedro']

    lista.delete('Juan')
    assert lista == ['Pedro']

    lista.delete('Pedro')
    assert lista == []

    lista.delete('Pedro')
    assert lista == []

    lista.agregar('Juan')
    lista.agregar('Pedro')
    lista.agregar('Luis')
    lista.agregar('Ana')
    lista.agregar('Maria')
    lista.agregar('Carlos')
    lista.agregar('Pedro')
    lista.agregar('Luis')
    lista.agregar('Ana')
    lista.agregar('Maria')
    lista.agregar('Carlos')
    lista.agregar('Pedro')
    lista.agregar('Luis')
    lista.agregar('Ana')
    lista.agregar('Maria')
    lista.agregar('Carlos')
    lista.agregar('Pedro')
    lista.agregar('Luis')
    lista.agregar('Ana')
    lista.agregar('Maria')
    lista.agregar('Carlos')
    lista.agregar('Pedro')
    lista.agregar('Luis')
    lista.agregar('Ana')
    lista.agregar('Maria')
    lista.agregar('Carlos')
    lista.agregar('Pedro')
    lista.agregar('Luis')
    lista.agregar('Ana')
    lista.agregar('Maria')
    lista.agregar('Carlos')
    lista.agregar('Pedro')
    lista.agregar('Luis')
    lista.agregar('Ana')
    lista.agregar('Maria')
    lista.agregar('Carlos')
    lista.agregar('Pedro')
    lista.agregar('Luis')
    lista.agregar('Ana')
