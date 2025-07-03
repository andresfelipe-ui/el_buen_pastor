class EmpleadoSanitario:
    def nombre_rol(self):
        return "Empleado Sanitario"

    def registrar_control_sanitario(self):
        self.registrar_vacunas()
        self.generar_reporte_salud()
        self.alertar_vacunas_pendientes()

    def registrar_vacunas(self):
        print("Registrando vacunas...")
        self.generar_reporte_vacunacion()

    def generar_reporte_vacunacion(self):
        print("Generando reporte de vacunación...")

    def generar_reporte_salud(self):
        print("Generando reporte de salud...")

    def alertar_vacunas_pendientes(self):
        print("Alerta: hay vacunas pendientes.")
