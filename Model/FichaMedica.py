class FichaMedica:
    def __init__(self,codigo,fecha,mascota,duenio,consulta):
        self.codigo=codigo
        self.fecha=fecha
        self.mascota=mascota
        self.duenio=duenio
        self.consulta=consulta

    def __str__(self):
        return self.codigo

    def __repr__(self):
        return self.codigo