class Vacuna:
    def __init__(self,codigo,nombre,funcion,duracion,dosis,fecha_vencimiento,costo,stock):
        self.codigo=codigo
        self.nombre=nombre
        self.funcion=funcion
        self.duracion=duracion
        self.dosis=dosis
        self.fecha_vencimiento=fecha_vencimiento
        self.costo=costo
        self.stock=stock

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre
