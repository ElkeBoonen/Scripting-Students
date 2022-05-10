from animals import Animal

class Mammal(Animal):
    species = "zoogdier"

    def info(self):
        print(self.species)