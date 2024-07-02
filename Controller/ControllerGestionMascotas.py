from View.ViewGestionMascotas import ViewGestionMascotas
class ControllerGestionMascotas:
    def __init__(self):
        vista=ViewGestionMascotas()

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