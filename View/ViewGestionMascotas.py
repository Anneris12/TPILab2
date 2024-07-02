class ViewGestionMascotas:
    def eleccionMenuPrincipal(self):
        print("Menu Principal:"
              "\n1-Lista de Mascotas Activas"
              "\n2-Registrar Mascota"
              "\n3-Modificar Mascota"
              "\n4-"
              "\n5-"
              "\n6-"
              "\n7-"
              "\n8-")
        op = int(input("Ingrese una opcion: "))
        return op
    def opcionInvalida(self):
        print("La opcion ingresada no es correcta.")