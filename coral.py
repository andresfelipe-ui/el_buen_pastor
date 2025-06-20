class Corral:
    def __init__(self, id_corral, capacidad, estado):
        self.id_corral: str = id_corral
        self.capacidad: int = capacidad
        self.estado: str = estado

    def limpiar(self):
        print("Corral limpiado.")

    def asignar_animal(self):
        print("Animal asignado al corral.")

    def verificar_estado(self):
        print("Estado del corral verificado.")

