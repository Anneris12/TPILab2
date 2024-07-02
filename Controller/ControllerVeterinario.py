from View.ViewVeterinario import ViewVeterinario
from Model.Persona import Veterinario
class ControllerVeterinario:
    def __init__(self):
        self.vista=ViewVeterinario()
        self.listaVeterinarios=[]

    def cargarVeterinarios(self):
        pass