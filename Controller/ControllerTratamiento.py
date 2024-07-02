from View.ViewTratamiento import ViewTratamiento
from Model.Tratamiento import Tratamiento
class ControllerTratamiento:
    def __init__(self):
        self.vista=ViewTratamiento()
        self.listaTratamientos=[]

    def cargarTratamientos(self):
        pass