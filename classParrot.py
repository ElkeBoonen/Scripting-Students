class Parrot:
    # attributen
    species = "Parrot"

    #def __init__(self):
    #    print("Parrot is created!")

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def sing(self):
        print("sing sing")

    def talk(self, text):
        print(self.name,"says '",text,"'")
