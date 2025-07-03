class Empleado:
    def nombre_rol(self):
        return "Empleado"

    def registrar_asistencia(self):
        print("Registrando asistencia...")
        self.generar_reporte_asistencia()
        self.alertar_ausencias()

    def generar_reporte_asistencia(self):
        print("Generando reporte de asistencia...")

    def alertar_ausencias(self):
        print("Alerta: hay ausencias.")

