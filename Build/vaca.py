from animal import Animal

class Vaca(Animal):
    def __init__(self, id_animal, edad, peso, produccion_leche):
        super().__init__(id_animal, edad, peso)
        self.produccion_leche: float = produccion_leche

    def ordenar(self):
        print("Vaca ordeñada.")
