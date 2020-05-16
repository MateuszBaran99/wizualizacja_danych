import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("zamowienia.csv", sep=";")

print(df)

group = df.groupby(["Sprzedawca"]).agg({"idZamowienia": ["count"]})
print(group)
wykres = group.plot.bar()
wykres.set_xlabel("Sprzedawca")
wykres.set_ylabel("Ilosc zamowien")
wykres.legend()
plt.show()