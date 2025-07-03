class Administrador:
    def nombre_rol(self):
        return "Administrador"

    # Registrar animal
    def registrar_animal(self):
        print("Registrando animal...")
        self.generar_reporte_poblacion()
        self.actualizar_informacion_animal()

    def generar_reporte_poblacion(self):
        print("Generando reporte de población...")

    def actualizar_informacion_animal(self):
        print("Actualizando información del animal...")

    # Supervisar corrales
    def supervisar_corrales(self):
        print("Supervisando corrales...")
        self.alertar_limpieza_corral()
        self.asignar_animal_a_corral()

    def alertar_limpieza_corral(self):
        print("Alerta: limpieza necesaria en corral.")

    def asignar_animal_a_corral(self):
        print("Asignando animal a corral...")

    # Registrar asistencia
    def registrar_asistencia(self):
        print("Registrando asistencia de empleados...")
        self.generar_reporte_asistencia()
        self.alertar_ausencias()

    def generar_reporte_asistencia(self):
        print("Generando reporte de asistencia...")

    def alertar_ausencias(self):
        print("Alerta: hay empleados ausentes.")

