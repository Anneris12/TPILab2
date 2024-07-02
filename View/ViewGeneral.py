class ViewGeneral:
    def eleccionMenuPrincipal(self):
        print("Menu Principal:"
              "\n1-Gestion Mascotas"
              "\n2-Gestion Clientes"
              "\n3-Gestion Tratamientos"
              "\n4-Gestion Fichas Medicas"
              "\n5-"
              "\n6-"
              "\n7-"
              "\n8-")
        op=int(input("Ingrese una opcion: "))
        return op

    def opcionInvalida(self):
        print("La opcion ingresada no es correcta.")