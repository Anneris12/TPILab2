class Persona:
    def __init__(self,apellido,nombre,dni,correo,telefono,direccion,estado):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado

    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.nombre

class Duenio(Persona):
    def __init__(self,apellido,nombre,dni,correo,telefono,direccion,estado,codigoDuenio):
        super().__init__(apellido,nombre,dni,correo,telefono,direccion,estado)
        self.codigoDuenio=codigoDuenio
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.nombre

class Veterinario(Persona):
    def __init__(self,apellido,nombre,dni,correo,telefono,direccion,estado,matricula,antiguedad):
        super().__init__(apellido,nombre,dni,correo,telefono,direccion,estado)
        self.matricula=matricula
        self.antiguedad=antiguedad
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.nombre
