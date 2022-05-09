import subprocess
import datetime

class Animal:
    species = "animal"

    def WhoIsThis(self):
        print(self.species)

# superclass
class Mammel(Animal):
    species = "mammel"

# superclass
class Bird(Animal):
    species = "bird"

class Platypus(Bird, Mammel):
    species = "platypus"

class Fish(Animal):
    species = "fish"

# subclass
class Parrot(Bird):
    species = "parrot"

    def __calculateAge(self):
        return datetime.datetime.now().year - self.Birthdate.year

    def __init__(self, name, birthdate, color):
        self.Name = name
        self.Birthdate = birthdate
        self.Color = color

    def Talk(self, text):
        print(self.Name,"zegt",text)
    
    def Sing(self):
        subprocess.Popen(['start','sound.wav'], shell=True)

    def Age(self):
        return self.__calculateAge()

    def WhoIsThis(self):
        super().WhoIsThis()
        print("My name is",self.Name)

