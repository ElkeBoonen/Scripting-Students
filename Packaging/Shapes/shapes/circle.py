from .shape import shape # . is nodig in package om relatief te importeren --> . staat voor huidige folder
import math

class circle(shape): # circle inherits all methods from shape!!
    def __init__(self, radius): # alles properties geef je mee aan de constructor!!!
        self.r = radius

    def circumference(self): #omtrek
        return 2 * math.pi * self.r
    
    def area(self): #opp
        return math.pi * math.pow(self.r,2)

# mag je overschrijven, maar moet niet
#    def draw(self):
#        return super().draw()