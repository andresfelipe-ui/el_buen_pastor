class Empleado:
    def __init__(self, id_empleado: str, nombre: str, cargo: str):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.cargo = cargo

    def realizar_tarea(self):
        print(f"{self.nombre} está realizando una tarea.")

    def registrar_asistencia(self):
        print(f"{self.nombre} registró asistencia.")

    def reportar_incidencia(self):
        print(f"{self.nombre} reportó una incidencia.")

