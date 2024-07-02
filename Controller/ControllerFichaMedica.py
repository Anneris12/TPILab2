from View.ViewFichaMedica import ViewFichaMedica
from Model.FichaMedica import FichaMedica


class ControllerFichaMedica:
    def __init__(self,controllerMascota,controllerDuenio,controllerConsulta):
        self.vista=ViewFichaMedica
        self.listaFichasMedicas=[]
        self.controllerMascota=controllerMascota
        self.controllerDuenio=controllerDuenio
        self.controllerConsulta=controllerConsulta

    def cargarFichasMedicas(self):
        pass