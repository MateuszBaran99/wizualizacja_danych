class Material:

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    
    def wyswietl_nazwe(self):
        print(f"{self.rodzaj}, {self.dlugosc}, {self.szerokosc}")

class Ubrania(Material):

    def __init__(self, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    
    def wyświetl_dane(self):
        print(f"{self.rozmiar}, {self.kolor}, {self.dla_kogo}")

class Sweter(Ubrania):

    def __init__(self, rodzaj_swetra, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        self.rodzaj_swetra = rodzaj_swetra
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    
    def wyswietl_dane_swetra(self):
        print(f"{self.rodzaj_swetra}, {self.rozmiar}, {self.kolor}, {self.dla_kogo}, {self.rodzaj}, {self.dlugosc}, {self.szerokosc}")


material = Material("Poliester", 60, 40)
material.wyswietl_nazwe()

ubranie = Ubrania("M", "czarny", "uniwersalny", "Poliester", 71,62 )
ubranie.wyświetl_dane()
ubranie.wyswietl_nazwe()

sweter = Sweter("rozpinany", "M", "czarny", "uniwesalny", "Bawelna", 76, 64)
sweter.wyswietl_dane_swetra()
sweter.wyswietl_nazwe()
