from mammals import Mammal
from birds import Bird

class Platypus(Bird, Mammal):

    def info(self):
        super().info()