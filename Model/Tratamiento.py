class Tratamiento:
    def __init__(self,codigo,nombre,medicacion,duracion,instruccion,riesgos,estado):
        self.codigo=codigo
        self.nombre=nombre
        self.medicacion=medicacion
        self.duracion=duracion
        self.instruccion=instruccion
        self.riesgos=riesgos
        self.estado=estado

    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.nombre