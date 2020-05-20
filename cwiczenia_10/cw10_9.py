import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

df = pd.read_csv("zamowienia.csv", sep=";")

dane = df.groupby("Sprzedawca")["Utarg"].sum().reset_index()


wedges, texts, autotexts = plt.pie(dane["Utarg"], labels=dane["Sprzedawca"], autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color="black"), shadow=True)
plt.setp(autotexts, size=10, weight="bold")
plt.title("Procent udziałów sprzedawców")
plt.legend(title="Sprzedawcy", bbox_to_anchor=(1.2, 1))
plt.show()