import numpy as np
import matplotlib.pyplot as plt
import random

def kostka(n):
    
    wynik = []
    for i in range(6):
        A = [random.randint(1, 6) for i in range(2)]
        wynik.append(sum(A))

    plt.hist(wynik, bins=12, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Suma rzutów')
    plt.ylabel('Prawdopodobieństwo')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()


print(kostka(100))