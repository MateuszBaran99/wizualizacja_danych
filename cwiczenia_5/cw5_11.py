def fibonaci(dane):
    a0 = 0
    a1 = 1
    i = 0
    while i < dane:
        a2 = a0 + a1 
        a0 = a1
        a1 = a2
        yield a2


f = fibonaci(1)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
