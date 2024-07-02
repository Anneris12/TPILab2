class Consulta:
    def __init__(self,codigo,fecha,diagnostico,veterinario,mascota,vacuna):
        self.codigo=codigo
        self.fecha=fecha
        self.diagnostico=diagnostico
        self.veterinario=veterinario
        self.mascota=mascota
        self.vacuna=vacuna

    def __str__(self):
        return self.diagnostico

    def __repr__(self):
        return self.diagnostico