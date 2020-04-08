import math

def proste(a1, a2):
    if(a1 == a2):
        print("proste sa rownolegle")
    elif(a1*a2 == -1):
        print("proste sa prostopadle")
    else:
        print("proste nie sa rownolegle ani prostopadle")

a1=input("podaj a1 jakie stoi w rownaniu prostej y=a1x+b1 ")
a1=int(a1)
a2=input("podaj a2 jakie stoi w rownaniu prostej y=a2x+b2 ")
a2=int(a2)

print(proste(a1, a2))