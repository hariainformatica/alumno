class Fichero:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer(self):
        with open(self.nombre, 'r') as f:
            return f.read()

    def escribir(self, contenido):
        with open(self.nombre, 'w') as f:
            f.write(contenido)