from empleado import Empleado

class EmpleadoAlimentacion(Empleado):
    def __init__(self, id_empleado, nombre, cargo, tipo_alimento):
        super().__init__(id_empleado, nombre, cargo)
        self.tipo_alimento: str = tipo_alimento

    def realizar_tarea(self):
        print("Alimentación registrada.")

    def registrar_alimentacion(self):
        print(f"Alimento tipo {self.tipo_alimento} suministrado.")


