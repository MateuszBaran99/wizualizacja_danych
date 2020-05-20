import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx)
print(df)

wykres1 = df.groupby(["Plec"])["Liczba"].sum().reset_index()
wykres2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
wykres2M = wykres2[wykres2["Plec"]== "M"].reset_index()
wykres2K = wykres2[wykres2["Plec"]== "K"].reset_index()
wykres3 = df.groupby(["Rok"])["Liczba"].sum().reset_index()

plt.subplot(1,3,1)
plt.bar(wykres1["Plec"], wykres1["Liczba"], color=["red", "blue"])
plt.xlabel("Plec")
plt.ylabel("Liczba urodzonych")

plt.subplot(1,3,2)
plt.plot(wykres2K["Rok"], wykres2K["Liczba"], color="purple")
plt.plot(wykres2M["Rok"], wykres2M["Liczba"], color="yellow")
plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")

plt.subplot(1,3,3)
plt.bar(wykres3["Rok"], wykres3["Liczba"], color="orange")
plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")


plt.show()