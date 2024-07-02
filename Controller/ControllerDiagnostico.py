from View.ViewDiagnostico import ViewDiagnostico
from Model.Diagnostico import Diagnostico
class ControllerDiagnostico:
    def __init__(self, controllerTratamiento,controllerMascota):
        self.vista=ViewDiagnostico()
        self.listaDiagnosticos=[]
        self.controllerTratamiento=controllerTratamiento
        self.controllerMascota=controllerMascota

    def cargarDiagnostico(self):
        pass
