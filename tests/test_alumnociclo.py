import pytest
from alumno.alumnociclo import AlumnoCiclo

#------------------------
@pytest.fixture
def alumnociclo():
    return AlumnoCiclo('Juan', 'DAW', 1)

def test_alumnociclo(alumnociclo):
    assert alumnociclo.read() == 'Juan|##|DAW|##|1'
#---------------------------
def test_2alumnociclo():
    al = AlumnoCiclo('Juan', 'DAW', 1)
    assert al.read() == 'Juan|##|DAW|##|1'