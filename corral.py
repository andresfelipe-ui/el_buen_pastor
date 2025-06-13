# Clase Corral
class Corral:
    def _init_(self, id_corral):
        self.id_corral = id_corral
        self.animales = []

    def asignar_animal(self, animal):
        self.animales.append(animal)
        print(f"{animal.nombre} asignado al corral {self.id_corral}.")

    def limpiar(self):
        print(f"El corral {self.id_corral} ha sido limpiado.")

    def listar_animales(self):
        print(f"Animales en el corral {self.id_corral}:")
        for animal in self.animales:
            print(f" - {animal.nombre} ({animal.tipo})")