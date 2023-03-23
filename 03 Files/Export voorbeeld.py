# %% [markdown]
# # Les 3 - Python basics - 27/02
# 
# - Numpy: arrays
# - Pythonic
# 
# Hoe installeer je nieuwe packages: pip install package_naam in terminal
# 
# In de notebooks zet je gewoon een ! voor de pip install package_naam
# 
# Een een package erin zit, gebruik je hem door import package_naam bovenaan je script te zetten!
# 
# Let erop dat als je verschillende versies van Python naast mekaar hebt staan, dat er soms onduidelijkheden zijn in welke versie packages geinstalleerd werden! Typische Python-fout waar je lang kan achter zoeken. Oplossingen:
# - oude versies verwijderen en pacakges opnieuw installeren
# - of packages handmatig kopieren van de ene naar de andere versie (C:\Users\<>\AppData\Local\Programs\Python)

# %%
# zet installaties altijd in apart codeblokje
! pip install numpy

# %%
# verschillende import mogelijkheden
import numpy
import numpy as np
from numpy import arange

# %% [markdown]
# ## Aanmaken arrays

# %%
import numpy as np

list = [1,2,3,4,5]
print(list)

array = np.array(list) # fixed size op het moment dat ze werden aangemaakt!
print(array)

list += [1,2,3]
print(list)

# array += [1,2,3] KAN NIET!!

print(list*2)   # list * 2 van grootte
print(array*2)  # array elementen * 2

print(np.arange(10))
print(np.arange(0,10,2))

print(np.zeros(5))
print(np.ones((5,3)))   # als je 2D array maakt op plek van size moet nu (rij,kolom)

print(np.full((5,3,2),4))
print(np.full(5,4))

print(np.eye(4))    # is altijd vierkante matrix (eenheidsmatrix) dus vandaar slechts 1 waarde meegeven als grootte

print(np.random.random((4,2)))
print(np.random.random(5))

print(np.random.random_integers(-10,10, 8)) # niet meer gebruiken, function is deprecated, call randint(-10, 10 + 1) instead
print(np.random.randint(-10,10, 8))

# %% [markdown]
# ### Pythonic vs. Algoritmische manier van lijsten/arrays aanmaken

# %%
array = np.arange(-9,10,3)  # Pythonic
print(array)

list = [x for x in range(-9,10,3)] # Pythonic
print(list)

list = []
for x in range(-9,10,3):
    list.append(x)
print(list)

# %% [markdown]
# ## Arrays omvormen naar ander type

# %%
array = np.random.randint(-10,10, 8)
print(array, "array is van type =",type(array)) # procedurele functie
print(array, "array is van type =",array.dtype) # OO-property

array = array.astype('f') # omvormen van type, naar een float
# array = array.astype(float) --> zelfde maar op andere manier
print(array)
print(array, "array is van type =",array.dtype) # OO-property

# %% [markdown]
# ## Arrays omvormen naar andere dimensies
# 
# Als ja van 1D naar 2D gaat moeten dimensies kloppen
# - 1D 8 --> 2D 2 x 4
# - 1D 9 --> 2D 3 x 3

# %%
import random

array = np.random.randint(-10,10, 8) 

matrix = np.reshape(array, (2,4))
print(matrix)


# %%
# maak een matrix van een array van een random aantal elementen 
# met grootste deler moet aantal rijen zijn
# voorbeeld: 100 elementen, grootste deler is 50, dus 50 rijen en 2 kolommen
# voorbeeld: 27 elementen, grootste deler is 9, dus 9 rijen en 3 kolommen
# voorbeeld: speciaal geval met priemgetal bv, 13 elementen, grootste deler is 13, dus 13 rijen en 1 kolom

array = np.random.randint(-10,10, random.randint(10,50)) 
print(array)

delers = []
for x in range(2,array.shape[0]):
    if array.shape[0] % x == 0:
        delers.append(x)

if delers == []:
    print(np.reshape(array, (array.shape[0],1)))
else:
    print(np.reshape(array, (max(delers), array.shape[0]//max(delers))))


# %% [markdown]
# ## Arrays slicen
# 
# [start:end:step]
# - als start leeg is --> 0 als start
# - als end leeg is --> laatste index als end
# - als step leeg is --> step = 1

# %%
array = np.random.randint(-10,10, 10) 

print(array)

print(array[1:5])
print(array[1:5:2])
print(array[::-1]) # reverse
print(array[9::-1])
print(array[1::2]) # oneven indexen
print(array[::-2])

# %% [markdown]
# ## Arrays extra methoden

# %%
a = np.random.randint(-10,10, 10) 
b = np.random.randint(-10,10, 10) 

print("a =",a,"b =",b)

c = a + b
print("c = ", c)

print(a.max(axis=0))
print(max(a))

print(a > 0)
print(np.where(a > 0)) # geeft indexen terug, niet de waarden!

print(a.sum(axis=0))

# %% [markdown]
# ## Oefening: It's magic time!
# 
# Read a 1D array and a number of rows! Convert this 1D array to a 2D array! Calculate the sum of each column and if all sums are equal... you are dealing with a magic table!
# 
# 
# <b>input</b><br>
# 2 7 0 8 4 1 1 0 10<br>
# 3<br>
# <b>output</b><br>True
# 
# 2 7 0<br>
# 8 4 1<br>
# 1 0 10<br>
# 
# 11 11 11 --> MAGIC TABLE

# %%
import numpy as np

list = input("Geef array in").split()
array = np.array(list).astype(int)
print(array)

rows = int(input("Geef een aantal rijen in"))

array = np.reshape(array,(rows,rows))
sums = array.sum(axis=0)

check = True
for value in sums:
    if value != sums[0]:
        check = False
        print("Not magic")
        break

if check==True:
    print("Magic")

# %% [markdown]
# ## Pythonic code
# 
# import this voor zen van Python

# %%
import this

# %% [markdown]
# ## Interessant!
# Exporteer je notebook naar een script door:
# - Open Command Palet Ctrl+Shift+P
# - Zoek commando 'Jupyter: Export to Python script'
# ## Oefening packages
# Your task is to create a Python program that uses the pyjokes package to generate random jokes. The program should prompt the user to select a category of jokes and then display a random joke from that category.
# 
# Instructions
# - Install the pyjokes package using pip.
# - Create a new Python script named joke_generator.py.
# - Import the pyjokes package.
# - Display a menu of joke categories to the user. The menu should include at least three categories, such as "programming", "general", and "knock-knock".
# - Prompt the user to select a category by entering the corresponding number.
# - Use the pyjokes package to generate a random joke from the selected category.
# - Display the joke to the user.
# - Ask the user if they want to hear another joke from the same category. If they say yes, generate and display another joke from the same category. If they say no, return to the main menu.
# - Allow the user to quit the program by entering a special command (such as "quit" or "exit").


