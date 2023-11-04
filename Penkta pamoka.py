import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import psycopg2



# data = {
#     "Vardas": ["Jonas", "Arturas", "Ignas", "Migle"],
#     "Amzius": [25, 28, 29, 19],
#     "Miestas": ["Vilnius", "Klaipeda","Anykciai", "Vilnius"]
# }

# df = pd.DataFrame(data)

#pagal amziu reikia dar ir print, kaip zemiau

# vyresni_nei_25 = df[df['Amzius'] > 25]

#pagal miesta grupavimas + print

# grupavimas_pagal_miesta = df.groupby('Miestas').size()
# print(grupavimas_pagal_miesta)

#suriusiavimas

# df = df.sort_values(by='Amzius'), ascending=False)

#naujo stulpelio kurimas 1 , pasalinimas 2
# df["darbo_stazas"] = [2,1,5,9]
# df.drop(columns=['darbo_stazas'], inplace=True)
#
# eiluciu_sk = df.shape[0]
# stulpeliu_sk = df.shape[1]
# print(f"Eiluciu skaicius {eiluciu_sk}, stulpeliu skaiciu {stulpeliu_sk}")

# df = pd.read_csv("Sales_Records.csv")
#
# df["Profit"] = df["Total Revenue"] - df["Total Cost"]
#
# df["Profit"] = df["Profit"].round(2)  #suapvalina
#
# # df.to_csv("sales_with_profit.csv", index=False) #sukurti nauja ir perkelia i nauja faila
#
# # print('Bendras pelnas', df['Profit'].sum(), df['Total Revenue'].sum(), df['Total Cost'].sum())
#
# df["Order Date"] = pd.to_datetime(df["Order Date"])     # formatavimas i data
# df["Ship Date"] = pd.to_datetime(df["Ship Date"])           #
# # df["Units Sold"] = df["Units Sold"].astype(int)                  #formatavimas is teksto i skaicius
# #
# #
# df["Dienu skirtumas"] = (df["Order Date"] - df["Ship Date"]).dt.days

# print(df.isnull().sum()) #tikrinti tuscius langelius

# sort_profit = df.sort_values(by="Profit", ascending=False)

# df['margin_on_revenue'] = (df["Profit"]/df["Total Revenue"])*100
# df['margin_on_revenue'] = df["margin_on_revenue"].round(2).astype(str)+'%'
#print(df)

#Histogramos kurimas

# plt.figure(figsize=(10,7))
# plt.hist(df['Profit'],bins=10,edgecolor="black")
# plt.title('Pelno histograma')
# plt.xlabel('Pelnas')
# plt.ylabel("Daznis")
# plt.savefig("Histograma.png")
# plt.show()

# plt.bar(["Unit Price", "Units Sold"], [df["Unit Price"].mean(),df["Units Sold"].mean()])
# plt.title("Vidutine kaina")
# plt.ylabel("Kaina")
# plt.show()

# plt.figure(figsize=(6,8))
# plt.hist(df["Dienu skirtumas"], bins=15, edgecolor="black")
# plt.title("Dienu skirtumas")
# plt.xlabel("Dienu skirtumas")
# plt.ylabel("Uzsakymu kiekis")
# plt.show()

#isrinkti temperaturas ir atvaizduoti grafike
# Uzdavinys su temperaturomis:

# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
#
#
# weekdays = soup.find_all('span', class_= "date")
# temperatures = soup.find_all('span', class_= "big up-from-zero")[1::2]
#
# filter_weekdays = [weekday.get_text().split(",")[0] for weekday in weekdays]
# day_temperatures = []
# for temperature in temperatures:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
# # interval = min(len(filter_weekdays), len(day_temperatures))
#
# data = {"weekday": filter_weekdays,
#         "temperatures": day_temperatures
# }
#
# df = pd.DataFrame(data)
#
# plt.figure(figsize=(10,7))
# plt.bar(df["weekday"], df["temperatures"])
# plt.title("Temperaturos kaita per savaite")
# plt.ylabel("Temperatura C")
# plt.show()

######## Bitcoins
#
# data = []
# for i in range(6):
#
#     headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
#     }
#     url = "https://www.coinbase.com/explore?page={1}"
#     res = requests.get(url, headers=headers)
#     soup = BeautifulSoup(res.content, "html.parser")
#
#
#
#     table = soup.find('table', class_="cds-table-top40r1")
#
#     if table:
#         rows = table.find_all('tr')
#         for row in rows:
#             columns = row.find_all("td")
#             if len(columns) >= 8:
#                 player_data = [column.text.strip() for column in columns]
#                 data.append(player_data)
#
#     columns = ['Name', 'Price', 'Charts', 'Change', 'Market cap', 'Trade', 'Volume (24h)', 'Supply']
#
#
# df = pd.DataFrame(data, columns = columns)
#
# df.to_csv("Coinbase.csv",index=False)
#
# print(df)
#isvalo simbolius

# df = pd.DataFrame({
#     'Stulpelis':["vienas#", 'Du@'],
#     'Stulpelis2': ['Keturi#','penki@']
# })
#
# special_chars = '[#@]'
# df_cleaned = df.replace(special_chars,'', regex=True)
# print(df_cleaned)