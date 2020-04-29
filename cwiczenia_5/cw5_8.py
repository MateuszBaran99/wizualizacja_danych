class Samogloski:
    def __init__(self, dane):
        if not isinstance(dane, str):
            raise BaseException("Mial byc str!!!!!! d>_<b")
    
        self.dane = dane
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index = self.index + 1
        if self.index < len(self.dane):
            for n in "AaEeIiOoUuYy":
                if n == self.dane[self.index]:
                    return self.dane[self.index]
            return self.__next__()


        else:
            raise StopIteration


A = "Urashiki"

sam = Samogloski(A)

print(sam.__next__())
print(sam.__next__())
print(sam.__next__())
print(sam.__next__())
print(sam.__next__())
