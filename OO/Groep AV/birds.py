# import playsound
import datetime as dt
from animals import Animal

class Bird(Animal):
    species = "vogel"

    def info(self):
        print("dit is een", self.species)
        super().info()

class Parrot(Bird):
    species = "papegaai"

    def __age(self, birthdate): # __ --> private methode om de leeftijd te berekenen
        return dt.datetime.now().year - birthdate.year

    def __init__(self, name, birthdate, color):
        self.name = name
        self.age = self.__age(birthdate)
        self.color = color

    def sing(self):
        pass
        # playsound.playsound("sound.wav")

    def talk(self,text):
        print(self.name,"zegt",text)
    
    def info(self):
        print(self.name,"is een", self.species)