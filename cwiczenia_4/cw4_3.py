with open("cw4_3_plik.txt", "w") as plik:
    plik.writelines("jakis tekst")

with open("cw4_3_plik.txt", "r") as plik1:
    for linia in plik1:
        print(linia, end="")