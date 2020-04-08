slownik = {'jajko' : "sztuki", 'chleb' : "sztuki", 'ziemniaki' : "kg"}

produkty = [i for i in slownik if slownik[i] == "sztuki"]
print(produkty)