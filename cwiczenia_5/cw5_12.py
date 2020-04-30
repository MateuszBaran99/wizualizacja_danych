def miesiac():
    for i in ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]:
        yield i

m = miesiac()
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())

