
from Persona import *

class Alumno(Persona):

    def __init__(self,nombre,matricula):

        self.nombre=nombre
        self.matricula=matricula

    def comer(self):
        super().comer()

    def caminando(self):
        super().caminando()

    def promedio(self):
        return f"Soy {self.nombre} y No tengo promedio aun"





