plt.stackplot(days, olsztyn, torun, gdansk, labels=['Olsztyn', 'Toruń', 'Gdańsk'], colors=['blue', 'orange', 'green'])




fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))




df['Year'] = df['Year'].astype(str)
df['Value'] = df['Value'].str.replace(' ', '').astype(int)




############################### TWORZENIE KOLUMN ####################################
df = pd.read_csv('handel07.csv', delimiter=';', header=None)
!!!!!!!!!!header=None!!!!!!!!!!
# Reset the index to ensure proper DataFrame format
df.reset_index(drop=True, inplace=True)



############################### PRZEKSZTALCANIE KOLUMN #############################
df.columns = df.iloc[0]
df = df[1:]
df.reset_index(inplace=True)
df.rename(columns={'index': 'Nazwa'}, inplace=True)









################### INNY PIVOT ################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('praca09.xlsx')
print(df)

utworzone = df[df['Miejsca pracy'].str.startswith('liczba nowo')]
wartosc = utworzone['Wartosc'].to_numpy()
print(wartosc)

zlikwidowane = df[df['Miejsca pracy'].str.startswith('liczba zli')]
wartosc_z = zlikwidowane['Wartosc'].to_numpy()
print(wartosc_z)

X = np.arange(len(wartosc))

plt.bar(X + 0, wartosc, color='b', width=0.25, label='utworzone')
plt.bar(X + 0.25, wartosc_z, color='magenta', width=0.25, label='zlikwidowane')
labelsbar = np.arange(2013, 2013 + len(wartosc))
plt.xticks(X + 0.25, labelsbar)
plt.legend()
plt.show()
