def Parzyste(dane):
    for i in range(0, len(dane), 2):
        yield dane[i]

tab = [0, 1, 2, 3, 4, 5]

par = Parzyste(tab)

print(par.__next__())
print(par.__next__())
print(par.__next__())
print(par.__next__())