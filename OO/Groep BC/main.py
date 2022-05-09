
from birds import Bird, Parrot, Mammel, Platypus, Fish
# import birds voor alles

import datetime as dt

bert = Bird()
bert.WhoIsThis()

henkie = Parrot("Henkie", dt.datetime(2020, 6, 9, 9, 0, 0), "wit")
# print(henkie.Name,"is",henkie.Age(),"jaar oud")
frankie = Parrot("Frankie",dt.datetime(2000, 12, 9, 9, 0, 0), "rood")
# print(frankie.Name,"is",frankie.Age(),"jaar oud")

henkie.WhoIsThis()
frankie.WhoIsThis()

# henkie.Talk("blabla")
# frankie.Sing()

# print(henkie.__calculateAge()) --> geeft foutmelding omdat methode __

animals = [bert, frankie, henkie, Mammel(), Platypus(), Fish()]
for a in animals:
    a.WhoIsThis()