from classParrot import Parrot

blu = Parrot("Blu", 20, "blue")
print(blu)
print(blu.name,"is", blu.age," years old")

parrot = Parrot("Parrot", 10, "yellow")
print(parrot.name,"is", parrot.age," years old")

parrot.sing()
parrot.talk("hello")