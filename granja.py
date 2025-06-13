# Clase Granja
class Granja:
    def _init_(self, nombre):
        self.nombre = nombre
        self.corrales = []
        self.empleados = []

    def agregar_corral(self, corral):
        self.corrales.append(corral)
        print(f"Corral {corral.id_corral} agregado a la granja {self.nombre}.")

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} contratado en la granja {self.nombre}.")

    def cerrar_granja(self):
        print(f"La granja {self.nombre} ha cerrado. Todos los empleados han sido desvinculados.")
        self.empleados.clear()