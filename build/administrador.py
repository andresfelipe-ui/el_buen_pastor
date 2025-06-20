from empleado import Empleado

class Administrador(Empleado):
    def realizar_tarea(self):
        self.generar_reportes()

    def supervisar_corrales(self):
        print("Supervisando corrales...")

    def registrar_asistencias(self):
        print("Asistencias registradas.")

    def generar_reportes(self):
        print("Reportes generados.")



