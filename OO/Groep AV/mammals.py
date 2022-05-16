from animals import Animal

class Mammal(Animal):
    species = "zoogdier"

    def info(self):
        print("dit is een", self.species)
        super().info()