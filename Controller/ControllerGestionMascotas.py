from View.ViewGestionMascotas import ViewGestionMascotas
from Controller.ControllerConsulta import ControllerConsulta
from Controller.ControllerDiagnostico import ControllerDiagnostico
from Controller.ControllerMascota import ControllerMascota
from Controller.ControllerDuenio import ControllerDuenio
from Controller.ControllerVeterinario import ControllerVeterinario
from Controller.ControllerFichaMedica import ControllerFichaMedica
from Controller.ControllerRaza import ControllerRaza
from Controller.ControllerTratamiento import ControllerTratamiento
from Controller.ControllerVacuna import ControllerVacuna

class ControllerGestionMascotas:
    def __init__(self):
        self.vista=ViewGestionMascotas()
        self.controllerRaza = ControllerRaza()
        self.controllerDuenio = ControllerDuenio()
        self.controllerVeterinario = ControllerVeterinario()
        self.controllerTratamiento = ControllerTratamiento()
        self.controllerVacunas = ControllerVacuna()
        self.controllerMascota = ControllerMascota(self.controllerRaza, self.controllerDuenio)
        self.controllerDiagnostico = ControllerDiagnostico(self.controllerTratamiento, self.controllerMascota)
        self.controllerConsulta = ControllerConsulta(self.controllerDiagnostico, self.controllerVeterinario,self.controllerMascota, self.controllerVacunas)
        self.controllerFichaMedica = ControllerFichaMedica(self.controllerMascota, self.controllerDuenio,self.controllerConsulta)

    def iniciar(self):
        
        op=self.vista.eleccionMenuPrincipal()
        while (op!=0):
            if (op==1):
                self.controllerMascota.listaMascotasActivas()
            elif (op==2):
                pass
            elif (op==3):
                pass
            elif (op==4):
                pass
            elif (op==5):
                pass
            elif (op==6):
                pass
            elif (op==7):
                pass
            else:
                self.vista.opcionInvalida()
            op=self.vista.eleccionMenuPrincipal()