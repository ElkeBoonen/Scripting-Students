from .rectangle import rectangle

class square(rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def area(self):
        return super().area()

    def circumference(self):
        return super().circumference()

    def draw(self):
        return super().draw()