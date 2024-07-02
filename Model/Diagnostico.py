class Diagnostico:
    def __init__(self,codigo,fecha,nombre,resultado,gravedad,tratamiento,mascota):
        self.codigo=codigo
        self.fecha=fecha
        self.nombre=nombre
        self.resultado=resultado
        self.gravedad=gravedad
        self.tratamiento=tratamiento
        self.mascota=mascota

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre