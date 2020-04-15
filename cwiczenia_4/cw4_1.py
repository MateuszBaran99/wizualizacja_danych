import random

A = [random.randint(0, 50) for i in range(20) ]
B = [x for x in A if x % 4 == 0]

plik = open("cw4_1_plik.txt", "w")

plik.writelines(str(B))

plik.close()
