import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")
print(df)

df1 = df["Sprzedawca"].unique()
print(df1)

print("|||||||||||||||||||||||||||")

df2 = df["Utarg"].nlargest(5)
print(df2)
print("|||||||||||||||||")

df3 = df.groupby(by= ["Sprzedawca"])["idZamowienia"].count()
print(df3)
print("|||||||||||||||||")

df4 = df.groupby(by= ["Kraj"])["idZamowienia"].count()
print(df4)
print("|||||||||||||||||")

df5 = df[(df["Kraj"] == "Polska") & (df["Data zamowienia"].str.contains("2005"))]["idZamowienia"].count()
print(df5)
print("|||||||||||||||||")

df6 = df[df["Data zamowienia"].str.contains("2004")]["Utarg"].mean()
print(df6)

df[df["Data zamowienia"].str.contains("2004")].to_csv("zamowienia_2004.csv", index=False, sep=";")
df[df["Data zamowienia"].str.contains("2005")].to_csv("zamowienia_2005.csv", index=False, sep=";")
