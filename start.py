liczba = 0
liczba = "0"
liczba = 0.0
print(liczba+liczba)
print("Ala")
print(liczba)

# def funkcja():

print("Ala ma " + "5 lat")
print(0 - 1)
print(2 / 1)
print(2 * 1)
print(2 // 1) # dzielenie bez reszty
print(2 ** 1) # potegowanie
print(2 % 1) # dzielenie modulo 
print(5)
print("Ala ma 5 lat")
# print("Ala ma " + 5 + "lat") # bład
print("Ala ma " + str(5) + " lat")

# formatowanie wyjścia

print("Ala ma {} lat".format(5))
print("Ala ma {1} lat  a Marta {0}".format(5, 10))

#f-string(od Python 3.6)

wiek = 18
print(f"Ala ma {wiek} lat")

imie ="Małgorzata"
print(imie[4])
# imie[4]= "a" # błąd
imie="Adam"
# print(imie.lower()) # tak tez mozna
imie = imie.lower()
print(imie)
"Wojtek".lower().lstrip().rsplit()


#listy
lista = []
print(type(lista))
print(type("ala"))
print(type(5))

lista.append(5)
lista.insert(0, 6)

lista2=[1, 2, 3, 4, 5]
lista2[3]
lista3=lista+lista2
print(lista3)
lista4 = [1, "Ala", imie, 3.4, [1, 3]]
print(lista4[4][1])

macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
macierz[1][1]


#slownik

slownik = {}
print(type(slownik))

slownik["imie"] = "Marek"
print(slownik)
slownik2 = {
    'imie': "Marek",
    'wiek': 25,
    'wzrost': 175
    }
print(slownik2)
print(slownik2.keys())
print(slownik2.items())
print(slownik2['imie'])

#import

# from math import *
# from math import pow

# pow (2, 2)

import math as m

m.pow(2, 2)