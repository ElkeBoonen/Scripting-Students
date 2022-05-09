from birds import Parrot
import datetime as dt

henkie = Parrot("Henkie", dt.datetime(2020, 6, 9, 9, 0, 0), "wit")
print(henkie.Name,"is",henkie.Age(),"jaar oud")

frankie = Parrot("Frankie",dt.datetime(2000, 12, 9, 9, 0, 0), "rood")
print(frankie.Name,"is",frankie.Age(),"jaar oud")

henkie.Talk("blabla")
# frankie.Sing()

# print(henkie.__calculateAge()) --> geeft foutmelding omdat methode __
