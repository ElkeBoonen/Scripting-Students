from .shape import shape

class rectangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def circumference(self):
        return 2*self.base + 2*self.height

    def draw(self):
        super.draw()
