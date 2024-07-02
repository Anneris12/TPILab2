from View.ViewDuenio import ViewDuenio
from Model.Persona import Duenio
class ControllerDuenio:
    def __init__(self):
        self.vista=ViewDuenio()
        self.listaDuenios=[]

    def cargarDuenio(self):
        with open("Archivos/duenios.txt") as file:
            renglones = file.readlines()
            for i in renglones:
                apellido, nombre, dni, correo, telefono, direccion, estado, codigoDuenio =i.strip().split(",")
                self.listaDuenios.append(Duenio(apellido,nombre,dni,correo,telefono,direccion,estado,codigoDuenio))

    def buscarObjeto(self,obj):
        for i in self.listaDuenios:
            if i.codigoDuenio == obj:
                return i