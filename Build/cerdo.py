from animal import Animal

class cerdo(Animal):
    def __init__(self, id_animal, edad, peso, grasa_corporal):
        super().__init__(id_animal, edad, peso)
        self.grasa_corporal: float = grasa_corporal

    def control_peso(self):
        print("control del peso realizado")
