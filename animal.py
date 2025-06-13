# Clase Animal sin arreglos
class Animal:
    def _init_(self, tipo, peso=0):
        self.tipo = tipo  
        self.peso = peso
        self.vacunado = False

    def alimentar(self, cantidad):
        self.peso += cantidad * 0.1  # Aumenta un 10% del alimento dado como peso
        print(f"{self.nombre} ha sido alimentado con {cantidad}kg. Nuevo peso: {self.peso:.2f}kg")

    def vacunar(self):
        self.vacunado = True
        print(f"{self.nombre} ha sido vacunado.")

    def registrar_peso(self):
        print(f"Peso actual de {self.nombre}: {self.peso:.2f}kg registrado.")