from View.ViewConsulta import ViewConsulta
from Model.Consulta import Consulta
class ControllerConsulta:
    def __init__(self,controllerDiagnostico,controllerVeterinario,controllerMascota,controllerVacuna):
        self.vista=ViewConsulta()
        self.listaConsultas=[]
        self.controllerDiagnostico=controllerDiagnostico
        self.controllerVeterinario=controllerVeterinario
        self.controllerMascota=controllerMascota
        self.controllerVacuna=controllerVacuna

    def cargarConsultas(self):
        pass
