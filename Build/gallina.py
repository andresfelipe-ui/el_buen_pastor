from animal import Animal

class gallina(Animal):
    def __init__(self, id_animal, edad, peso, produccion_huevos):
        super().__init__(id_animal, edad, peso)
        self.produccion_huevos: float = produccion_huevos

    def recolectar_huevos(self):
        print("huevos recolectados")
