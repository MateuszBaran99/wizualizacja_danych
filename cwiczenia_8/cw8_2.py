import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx)
print(df)

print("||||||||||||||||||||||||||||||||||||")
df1 = df[df["Liczba"] > 1000]
print(df1)
print("||||||||||||||||||||||||||||||||||||")
df2 = df[df["Imie"] == "MATEUSZ"]
print(df2)
print("||||||||||||||||||||||||||||||||||||")
df3 = df["Liczba"].sum()
print(df3)
print("||||||||||||||||||||||||||||||||||||")
df4 = df[(df["Rok"] >= 2000) & (df["Rok"] <= 2005)]
df41 = df4["Rok"].sum()
print(df41)
print("||||||||||||||||||||||||||||||||||||")
df5M = df[df["Plec"] == "M"] 
print(df5M)
print("||||||||||||||||||||||||||||||||||||")
df5K = df[df["Plec"] == "K"] 
print(df5K)
print("||||||||||||||||||||||||||||||||||||")
df6 = df.copy()
df6["Popular"] = df.groupby(by=["Rok", "Plec"])["Liczba"].transform(max)
df6_imie = df6[df6["Liczba"] == df6["Popular"]]
print(df6_imie)
print("||||||||||||||||||||||||||||||||||||")
df7 = df.copy()
df7["Popular"] = df.groupby(by= "Rok")["Liczba"].transform(max)
df7_imie = df7[df7["Liczba"] == df7["Popular"]]
print(df7_imie)