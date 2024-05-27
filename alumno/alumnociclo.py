from alumno.alumno import Alumno

class AlumnoCiclo(Alumno):
    def __init__(self, nombre, edad, ciclo, curso):
        super().__init__(nombre)
        self.ciclo = ciclo
        self.curso = curso

    def read(self):
        return f"{super().read()}|##|{self.ciclo}|##|{self.curso}"