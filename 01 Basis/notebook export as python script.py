# %% [markdown]
# # Les 2 - de basis
# 
# ## Herhaling
# Oefening: Harshad‑getal (Niven‑getal)
# Schrijf een functie som_cijfers(n) die de som van de cijfers van een positief geheel getal n teruggeeft.
# Schrijf daarna een functie is_harshad(n) die True teruggeeft als n deelbaar is door de som van zijn cijfers, anders False.
# 
# - 18 → 1+8 = 9 en 18 % 9 == 0 ⇒ Harshad
# - 21 → 2+1 = 3 en 21 % 3 == 0 ⇒ Harshad
# - 19 → 1+9 = 10 en 19 % 10 ≠ 0 ⇒ niet Harshad
# 
# Eisen
# - Werk met twee aparte functies (som_cijfers en is_harshad).
# - Geen lijsten nodig; je mag werken met delen door 10 en modulo 10.
# - Ga ervan uit dat n > 0 (je mag optioneel invoer‑validatie toevoegen).

# %%
def som_cijfers(getal):
    # som van de cijfers van een positief geheel getal n teruggeeft
    som = 0
    for cijfer in getal: # dit werkt alleen als getal een string, indien een 'echt' getal --> str(getal)
        som += int(cijfer)
    return som

def is_harshad(getal):
    # die True teruggeeft als n deelbaar is door de som van zijn cijfers
    som = som_cijfers(getal)
    if int(getal) % som == 0:
        return True
    return False


getal = input("Geef een getal")
is_harshad(getal)

# %% [markdown]
# ## Collections
# 
# ### Lists [ ]
# --> gesorteerd en veranderbaar

# %%
fruit = ['appel', 'kiwi', 'peer']

print(fruit)
for element in fruit:
    print(element)

print(fruit[0])

print(fruit[-1])
print(fruit[len(fruit)-1])
print(fruit[-3])

fruit.append("kers")
print(fruit)

fruit.pop()
print(fruit)

fruit[1] = "kers"
print(fruit)

fruit.append(1) # DOE DIT NIET!!
print(fruit)

fruit[1] = True # DOE DIT NIET!!
print(fruit)

getallen = range(0,5) # 0 1 2 3 4
for getal in getallen:
    print(getal, end=" iets anders ")
machten_van_3 = [x**3 for x in getallen] # 0^3 1^3 2^3 3^3 4^3
print(machten_van_3)

print(27 in machten_van_3)
print("kers" in fruit)


# %%
matrix = [[1,2,3], [4,5,6], [7,8,9]]
for rij in matrix:
    for element in rij:
        print(element, end ="\t")
    print()

# %% [markdown]
# ### Tuple ( ) 
# --> gesorteerd maar niet veranderbaar

# %%
seizoenen = ("winter", "lente", "zomer", "herfst")
print(seizoenen)
print(seizoenen[0])
# seizoenen[0] = "iets anders"

# %% [markdown]
# ### Set { }
# --> veranderbaar maar geen duplicaten

# %%
bezoekers = {"jan", "piet", "joris", "korneel"}
print(bezoekers)

bezoekers.add("milan")
print(bezoekers)

bezoekers.add("jan")
print(bezoekers)

bezoekers.add("romeo")
print(bezoekers)


# %% [markdown]
# ### Dictionary { : }
# --> key/value-pairs, geen duplicaten

# %%
menu = {"pizza":10, "biefstuk met friet":50, "frietjes": 4, "tiramisu": 10}
print(menu)

menu["kapsalon"] = 9
print(menu)

menu["pizza"] = 12
print(menu) 

for key in menu.keys():
    print(key, menu[key])

for key, value in menu.items():
    print(key, value)

print(menu.keys())
print(menu.values())
print(menu.items())

# %% [markdown]
# ### Oefeningen
# 
# Oefening 2: Gastenlijst Opschonen - Hoe verwijder je automatisch duplicaten?
# - Start met aanmeldingen: Jan, An, Jan, Bert, An
# - Print aantal aanmeldingen
# - Verwijder duplicaten
# - Print unieke gasten + aantal
# - Output: 5 aanmeldingen → 3 unieke gasten

# %%
aanmeldingen = []
gastenlijst = set() # { } --> dictionary  dus let op aanmaken set
naam = input("Geef een naam")
while naam != "stop":
    aanmeldingen.append(naam)
    gastenlijst.add(naam)
    naam = input("Geef een naam")

print(len(aanmeldingen))
print(gastenlijst)

# %% [markdown]
# Digitale Kassa - Welke structuur gebruik je voor prijzen opzoeken? En voor items bewaren?
# - Bewaar prijzen: appel (€0.5), peer (€0.8), banaan (€0.6)
# - Bewaar winkelmandje: appel, peer, appel
# - Bereken totaalbedrag
# - Output: Totaal: € 1.8

# %%
prijzen = {"appel":0.5, "peer":0.8, "banaan":0.6 }

winkelmandje = []
item = input("Geef een item voor je winkelmand")
while item != "stop":
    winkelmandje.append(item)
    item = input("Geef een item voor je winkelmand")

som = 0
for item in winkelmandje:
    som += prijzen[item]

print("€",som)


# %% [markdown]
# Oefening 3: Wachtwoordcheck - Welke structuur voor snel checken of iets voorkomt?
# - Bewaar veelgebruikte wachtwoorden: "123456", "password", "qwerty", "admin"
# - Check of gebruikersinput erin voorkomt
# - Test met: "admin" en "MijnVeiligWW2024"
# - Output: "admin" → Onveilig!, "MijnVeiligWW2024" → Veilig

# %%
wachtwoorden = ("123456", "password", "qwerty", "admin")

user = input("Geef een wachtwoord")
if user in wachtwoorden:
    print("Onveilig!")
else:
    print("Veilig")

# %% [markdown]
# ## Packages
# 
# https://pypi.org/

# %%
! py -m pip install pywhatkit # https://pypi.org/project/pywhatkit/

! py -m pip install numpy # https://numpy.org/

# %%
import pywhatkit

pywhatkit.playonyt("PyWhatKit")

# %%
import numpy as np

array = np.array(machten_van_3)

print(array)
print(machten_van_3)

print(array*2)
print(machten_van_3*2)

array = np.arange((10))
print(array)

array = np.zeros(10)
print(array)

array = np.ones((10,5))
print(array)

array = np.full((10,),4)
print(array)

array = np.random.random(10)
print(array)

array = np.random.random_integers(-5,5,(10,1))
print(array)

print(type(array))
print(array.dtype)

# %%
a = np.arange(0,10)
b = np.arange(9,-1,-1) # start - stop - step
c = np.arange(9,-10,-3) # start - stop - step

print(a)
print(b)
print(c)

d = a-b
print(d)

print(d < 0)

print(d % 3)

b = np.reshape(b, (2,5))
print(b)

print(b.sum(axis=0))
print(b.sum(axis=1))

# %% [markdown]
# Vraag de gebruiker om een getal x 
# Maak een x×x matrix gevuld met willekeurige gehele getallen tussen 0 en x
# Print de matrix en controleer de shape en ndim
# Vind de indices (locaties) van alle elementen die niet nul zijn.
# Zoek alle locaties waar de waarde exact gelijk is aan 
# x
# x.
# Transformeer de matrix zodat elk even getal verandert in een oneven getal (bijv. door er 
# +
# 1
# +1 bij te tellen).Tip: Gebruik np.where(matrix % 2 == 0, matrix + 1, matrix).
# Draai de matrix om: de kolommen worden rijen en de rijen worden kolommen.
# Maak een tweede matrix met dezelfde afmetingen en willekeurige waarden.
# Vind de waarden die in beide matrices voorkomen (gemeenschappelijke items).
# Verwijder of vervang deze gemeenschappelijke items in de tweede matrix door 
# 0
# 0.

# %%
import numpy 

x = int(input("Geef een getal"))

matrix = numpy.random.random_integers(0,x,(x,x))
print(matrix)


