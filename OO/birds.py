import subprocess

class Parrot:
    species = "bird"

    def __init__(self, name, age, color):
        self.Name = name
        self.Age = age
        self.Color = color

    def Talk(self, text):
        print(self.Name,"zegt",text)
    
    def Sing(self):
        subprocess.Popen(['start','sound.wav'], shell=True)

