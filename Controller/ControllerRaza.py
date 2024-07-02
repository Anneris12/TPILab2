from View.ViewRaza import ViewRaza
from Model.Raza import Raza
class ControllerRaza:
    def __init__(self):
        self.vista=ViewRaza()
        self.listaRazas=[]

    def cargarRazas(self):
        with open("Archivos/razas.txt") as file:
            renglones = file.readlines()
            for i in renglones:
                codigo,nombre,origen,especie,estado = i.strip().split(",")
                self.listaRazas.append(Raza(codigo,nombre,origen,especie,estado))

    def buscarObjeto(self,obj):
        for i in self.listaRazas:
            if i.codigo == obj:
                return i
