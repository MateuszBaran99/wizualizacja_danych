class Parzyste:

    def __init__(self, dane):
        self.dane = dane
        self.index = -2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index = self.index + 2
        if self.index < len(self.dane):
            return self.dane[self.index]
        else:
            raise StopIteration


        
tab = [0, 1, 2, 3, 4, 5]

par = Parzyste(tab)

print(par.__next__())
print(par.__next__())
print(par.__next__())
print(par.__next__())
