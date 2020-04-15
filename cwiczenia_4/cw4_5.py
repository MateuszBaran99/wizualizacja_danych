class ciagi:
    a1 = 0
    n = 0
    r = 0
    

    def wyswietl_dane(self):
        print(f"{self.a1} {self.n} {self.r}")
    
    def pobierz_elementy(self):
        self.a1 = input("podaj a1: ")
        self.a1 = int(self.a1)
        self.a2 = input("podaj a2: ")
        self.a2 = int(self.a2)
        
    def pobierz_parametry(self):
        self.a1 = input("podaj a1: ")
        self.a1 = int(self.a1)
        self.r = input("podaj roznice ciagu: ")
        self.r = int(self.r)
        self.n = input("podaj ilosc elementow do wygenerowania: ")
        self.n = int(self.n)
    
    def policz_sume(self):
        self.an = self.a1 + (self.n -1)*self.r
        self.sn = ((self.a1 + self.an)/2)*self.n
        return self.sn
    
    def policz_elementy(self):
        if (self.a1 & self.r):
            return self.a1 + (6 -1)*self.r
    

ciag = ciagi()

ciag.pobierz_parametry()
ciag.wyswietl_dane()
print(ciag.policz_sume())
print(ciag.policz_elementy())



