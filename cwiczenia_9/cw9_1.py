import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

dane = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(dane)
print(df)

group = df.groupby(['Rok']).agg({"Liczba":["sum"]})
print(group)
wykres = group.plot()
wykres.legend()
plt.show()