import subprocess
import datetime

class Parrot:
    species = "bird"

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

