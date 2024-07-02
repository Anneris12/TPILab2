class Raza:
    def __init__(self,codigo,nombre,origen,especie,estado):
        self.codigo=codigo
        self.nombre=nombre
        self.origen=origen
        self.especie=especie
        self.estado=estado

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre