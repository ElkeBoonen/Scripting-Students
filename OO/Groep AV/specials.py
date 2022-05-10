from mammals import Mammal
from birds import Bird

class Platypus(Mammal, Bird):

    def info(self):
        super().info()