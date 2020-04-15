class Robaczek:
    x = 0
    y = 0
    k = 0

    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k
    
    def idz_w_gore(self):
        self.k_ile = input("podaj ile krokow w gore: ")
        self.k_ile = int(self.k_ile)
        self.y = self.y + (self.k * self.k_ile)
        print(f"x= {self.x} , y= {self.y}")
    
    def idz_w_dol(self):
        self.k_ile = input("podaj ile krokow w dol: ")
        self.k_ile = int(self.k_ile)
        self.y = self.y - (self.k * self.k_ile)
        print(f"x= {self.x} , y= {self.y}")

    def idz_w_prawo(self):
        self.k_ile = input("podaj ile krokow w prawo: ")
        self.k_ile = int(self.k_ile)
        self.x = self.x + (self.k * self.k_ile)
        print(f"x= {self.x} , y= {self.y}")

    def idz_w_lewo(self):
        self.k_ile = input("podaj ile krokow w lewo: ")
        self.k_ile = int(self.k_ile)
        self.x = self.x - (self.k * self.k_ile)
        print(f"x= {self.x} , y= {self.y}")
        
    
    def pokaz_gdzie_jestes(self):
        print(f"x= {self.x} , y= {self.y}")
    
    def __del__(self):
        print("usunieto")
    
    


robak = Robaczek(0, 0, 2)
robak.idz_w_gore()
robak.idz_w_dol()
robak.idz_w_prawo()
robak.idz_w_lewo()
robak.pokaz_gdzie_jestes()
robak.idz_w_lewo()