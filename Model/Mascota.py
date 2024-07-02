class Mascota:
    def __init__(self,codigo,nombre,raza,duenio,peso,edad,estado):
        self.codigo=codigo
        self.nombre=nombre
        self.raza=raza
        self.duenio=duenio
        self.peso=peso
        self.edad=edad
        self.estado=estado

    def __str__(self):
        return f"Nombre: {self.nombre} - Raza: {self.raza.nombre} - Duenio: {self.duenio.apellido}, {self.duenio.nombre}"

    def __repr__(self):
        return f"Nombre: {self.nombre} - Raza: {self.raza.nombre} - Duenio: {self.duenio.apellido}, {self.duenio.nombre}"