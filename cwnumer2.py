wejscie=input("Wprowadz wartosc: ")
print(wejscie)

# liczba =10
# if liczba < 10 and liczba > 0:
#     print()

# else:
#     print("Poza zakresem")

liczba =10
if 10 > liczba > 0:
    print()

else:
    print("Poza zakresem")


# rozne od liczba != 0
# rowne liczba ==0
# liczba is  not True
# liczba is True

if liczba in [1, 2, 3, 10]:        #sprawdza czy liczba jest w liscie
    print("jest w liscie")
else:
    print("Nie ma na liscie")


for liczba in [1, 2, 3, 10]:
    print(liczba)

imie = "Malgorzata"
for litera in imie:
    print(litera)

for liczba in range(5): #start, stop, step
    print(liczba)

print(list(range(5)))
# [0, 1, 2, 3, 4]
print(list(range(10, 0, -2)))
#x
imie = "Malgorzata"
print(imie[0:6:2])

#tak testowo aby nie bylo ze dziala
#czarnobyl