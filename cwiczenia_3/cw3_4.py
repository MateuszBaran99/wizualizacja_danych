def monotonicznosc(a):
    if(a > 0):
        print("funkcja rosnaca")
        return 0
    elif(a < 0):
        print("funkcja malejaca")
        return 0
    else:
        print("funckja stala")
        return 0



a=input("Podaj wartosc a funkcji y=ax+b ")
a=int(a)
print(monotonicznosc(a))
    