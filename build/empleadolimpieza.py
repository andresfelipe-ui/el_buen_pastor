from empleado import Empleado

class EmpleadoLimpieza(Empleado):
    def __init__(self, id_empleado, nombre, cargo, area_asignada):
        super().__init__(id_empleado, nombre, cargo)
        self.area_asignada: str  = area_asignada

    def realizar_tarea(self):
        print(f"Limpieza del área {self.area_asignada} realizada.")

    def realizar_limpieza(self):
        print("Área limpia.")


