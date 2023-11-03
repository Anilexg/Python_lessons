import matplotlib.pyplot as plt
import pandas as pd

# data = pd.Series([1,2,3,4,5,2,5])
#grazina pirmus skaicius
#print(data.head(3))
#grazina paskutinius skaicius
#print(data.tail(2))
#grazina statistine info
#print(data.describe())
#grazina vidurki
#print(data.mean())
#print(data.mediana())
#grazina unikalias reiksmes
#print(data.unique())
#grazina veiksmu pasikartojimu skaiciu
#print(data.value_counts())

#grazina didziausios reiksmas indeksa
#print(data.idxmax())

#grazina maziausios reiksmes indeksa
#print(data.idxmin())
#
# knygos = ['Haris Poteris', 'Alchemikas', 'Mazasis princas', 'Mobis dikas', 'Don Kichotas']
# vertinimas = [4.9, 5.2, 2.3, 3.8, 2.5]
#
# data = pd.Series(data=vertinimas, index=knygos)
#print(data)
# vidurkis =data.mean().round(2)
#
# print(f"Vidutinis knygu vertinimas: {vidurkis}")
#
# std_nuokrypis = data.std().round(2)
# print(f"Vidutinis standartinis nuokrypis: {std_nuokrypis}")
#
# auksciausias_ivertinimas = data.idxmax()
#
# print(f"Auksciausia ivertinima turinti knyga": {auksciausias_ivertinimas}")

# plt.figure(figsize=(10,6))
# data.plot(kind='bar',color='green')
# plt.title('Knygu ivertinimas')
# plt.xlabel('Knygos')
# plt.ylabel('Ivertinimas')
# plt.xticks(rotation=45, ha='right')
# plt.show()

# labels = 'A', 'C', 'B', 'D'
# sizes = [15,20,35,10]
#
# colors = ['gold', 'yellowgreen', 'lightcoral', 'blue']
# plt.pie(sizes,labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title('Skrituline diagrama')
# plt.show()

#
# x = [5, 3, 5, 10, 20, 34]
# y = [15, 20, 35, 10, 21, 45]
#
# plt.scatter(x, y, label='taskai', color='red')
# plt.title('Sklaidos diagrama')
# plt.ylabel('X asis')
# plt.xlabel('Y asis')
# plt.legend()
# plt.show()
data = pd.read_csv('soft_drink_sales.csv')
print(data)

#rasti bendra pardavimu suma pagal data

# pardavimai_pagal_data = data.groupby('Purchase Date')['Revenue'].sum().reset_index()
# print(pardavimai_pagal_data)


# pardavimai_pagal_data = data.groupby('Purchase Date').sum(['Revenue'])
# print(pardavimai_pagal_data)

#surasti vidurki pardavimu sumos pagal kompanija

# pardavimu_vidurkis = data.groupby('Company') ['Revenue'].mean().round(2).reset_index()
# print(pardavimu_vidurkis)

#nustatyti kurios 5 prekes atnesa max pelno ir min pelno

surusiavimas = data.sort_values(by='Profit', ascending=True).head(5)

print(surusiavimas)
