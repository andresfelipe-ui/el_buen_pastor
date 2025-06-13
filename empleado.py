# Clase Empleado
class Empleado:
    def _init_(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.tareas_realizadas = []
        self.asistencias = 0
        self.incidencias = []

    def realizar_tarea(self, tarea):
        self.tareas_realizadas.append(tarea)
        print(f"{self.nombre} realizó la tarea: {tarea}.")

    def registrar_asistencia(self):
        self.asistencias += 1
        print(f"Asistencia registrada para {self.nombre}. Total asistencias: {self.asistencias}")

    def reportar_incidencias(self, descripcion):
        self.incidencias.append(descripcion)
        print(f"{self.nombre} reportó una incidencia: {descripcion}")