from empleado import Empleado

class EmpleadoSanidad(Empleado):
    def __init__(self, id_empleado, nombre, cargo, especialidad):
        super().__init__(id_empleado, nombre, cargo)
        self.especialidad: str = especialidad

    def realizar_tarea(self):
        print("Realizando chequeo sanitario...")

    def aplicar_vacuna(self):
        print("Vacuna aplicada.")

    def realizar_chequeo(self):
        print("Chequeo realizado.")

