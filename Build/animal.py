
class Animal:
    def __init__(self, id_animal, edad, peso):
        self.id_animal: str = id_animal
        self.edad: int = edad
        self.peso: float = peso

    def alimentar(self):
        print("Animal alimentado.")

    def vacunar(self):
        print("Animal vacunado.")

    def registrar_peso(self):
        print("Peso registrado.")
