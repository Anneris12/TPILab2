from View.ViewMascota import ViewMascota
from Model.Mascota import Mascota
class ControllerMascota:
    def __init__(self,controllerRaza,controllerDuenio):
        self.vista=ViewMascota()
        self.listaMascotas=[]
        self.controllerRaza=controllerRaza
        self.controllerDuenio=controllerDuenio

    def cargarMascotas(self):
        with open("Archivos/mascotas.txt") as file:
            renglones = file.readlines()
            for i in renglones:
                codigo,nombre,codRaza,codDuenio,peso,edad,estado =i.strip().split(",")
                objRaza=self.controllerRaza.buscarObjeto(codRaza)
                objDuenio=self.controllerDuenio.buscarObjeto(codDuenio)
                self.listaMascotas.append(Mascota(codigo,nombre,objRaza,objDuenio,peso,edad,estado))

    def listaMascotasActivas(self):
        listaMascotasActivas=[]
        for i in self.listaMascotas:
            if (i.estado == "1"):
                listaMascotasActivas.append(i)
        self.vista.listar(listaMascotasActivas)

