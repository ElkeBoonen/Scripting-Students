from birds import Parrot

henkie = Parrot("Henkie", 10, "wit")
print(henkie.Name,"is",henkie.Age,"jaar oud")

frankie = Parrot("Frankie",15, "rood")
print(frankie.Name,"is",frankie.Age,"jaar oud")

henkie.Talk("blabla")
frankie.Sing()
