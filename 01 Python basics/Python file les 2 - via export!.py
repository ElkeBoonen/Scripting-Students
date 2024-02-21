# %% [markdown]
# # Les 2 - 21/2 - Python basics
# 
# ## De echte basis
# - loops (while)
# - functies
# - lijsten
# 
# ## Loops - While

# %%
answer = input("Geef iets in, X om te stoppen!")

while answer.upper() != "X":
    print(answer)
    answer = input("Geef iets in, X om te stoppen!")

while answer != "X" and answer!="x":
    print(answer)
    answer = input("Geef iets in, X om te stoppen!")

# %% [markdown]
# Genereer de Lucas-reeks. De Lucas-reeks is vergelijkbaar met de Fibonacci-reeks, waarbij elk getal de som is van de twee voorgaande getallen. Echter, in tegenstelling tot de Fibonacci-reeks, die begint met 0 en 1, begint de Lucas-reeks met 2 en 1.
# 
# FIBONACCI 0 1 1 2 3 5 8 13 21 34 ...
# LUCAS 2 1 3 4 7 11 18 29 ...

# %%
count = int(input("Geef het aantal te berekenen LUCAS cijfers"))

a = 2
b = 1

print(a,b, end = " ")

for i in range(count):
    result = a + b
    print(result, end = " ")
    a = b
    b = result


# %%
count = int(input("Geef het aantal te berekenen LUCAS cijfers"))

a = 2
b = 1

print(a,b, end = " ")

i = 0
while i < count:
    result = a + b
    print(result, end = " ")
    a = b
    b = result
    i+=1 # i = i + 1

# %% [markdown]
# ## Functies
# 
# Lucas-reeks in een functie!

# %%
def Lucas(count):
    a = 2
    b = 1
    return_result = str(a) + " " + str(b) + " "

    for i in range(count):
        result = a + b
        return_result += str(result) + " "
        a = b
        b = result
    return return_result

print(Lucas(20))
print(Lucas(10))
print(Lucas(1))

aantal = int(input("Geef een aantal in"))
print(Lucas(aantal))

for i in range(1,20):
    print(Lucas(i))

# %% [markdown]
# Schrijf een functie die controleert of een getal een priemgetal is. Een priemgetal is een getal dat alleen deelbaar is door 1 en zichzelf!
# 
# voorbeeld priemgetallen: 1 2 3 5 7 11 13 17 ... 
# 
# 

# %%
def PrimeNumber(number):
    count = 0
    for i in range(2,number//2):
        if number % i == 0:
            count += 1
    
    if count == 0:
        return True
    else:
        return False

print("5 is een priemgetal:", PrimeNumber(5))

for i in range(0,100):
    print(i, "is een priemgetal", PrimeNumber(i))

x = int(input("geef een getal"))
print(x,"is een priemgetal", PrimeNumber(x))


# %%
# Gebruik daarna deze funcie in je zoektocht naar het volgende priemgetal na een ingegeven getal!

number = int(input("Geef een getal"))

number += 1
while(not PrimeNumber(number)):
      number += 1

print(number, "is het volgende priemgetal")



