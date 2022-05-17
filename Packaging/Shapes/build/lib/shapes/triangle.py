from .shape import shape

class triangle(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return (self.width*self.height)/2

    def circumference(self):
        return super().circumference()

    def draw(self):
        return super().draw()

