import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# numpy skirtas atlikti tam tikrus skaiciavimus, skaiciavimu atlikimui

#masyvas = np.array([1,2,3,4,5])
# masyvas2 = np.array([6,7,8,9,10])
# sujungtas_masyvas = np.concatenate((masyvas, masyvas2))

# suma = np.sum(masyvas)
# print(sujungtas_masyvas)
# randint - sveiki skaiciai
# atsitiktiniai_sk = np.random.random((3,2))

# atsitiktiniai_sk = np.random.randint(0,10, size=5)
# print(atsitiktiniai_sk)

# masyvas = np.array([10,20,30,40,50])
# atsitiktiniai_ele = np.random.choice(masyvas, size=2)
# print(atsitiktiniai_ele)
# masyvas = np.arange(0,10,2)
# print(masyvas)
#
# masyvas = np.array([1,3,5])
# masyvas2 = np.array([2,3,4])
# lyginimas = masyvas > masyvas2
# print(masyvas)

# masyvas = np.array([1,2,3,4,5,6,7,8,9,10])
#
# filtered_array = masyvas [masyvas < 5]
# print(filtered_array)
# masyvas = np.array([1,2,3,4,5,6])
#
# split_array = np.split(masyvas,2)
# print(split_array)

# array = np.array(np.arange(1,21)).reshape(5,4)
# # print(array)
# df = pd.DataFrame(array, columns=['A','B','C','D'])
# second_column = df['B']
# print(second_column)

# suma = df.groupby('A')['B']
# # second_column = array[:, 0] + array[:, 1]         #sudeda tarp A ir B
# second_column = np.sum(array[:, 1])                 # sudeda tik B stulpeli
# print(second_column)

trimate_matrica = np.array([[1,2,3], [4,5,6], [7,8,9]])
# eiluciu suma ir stulpeliu suma

# eiluciu_suma =np.sum(trimate_matrica, axis=1)
# print(eiluciu_suma)
# stulpeliu_suma =np.sum(trimate_matrica, axis=0)
# stulpeliu_suma =np.sum(trimate_matrica [1])         # sudeda tik viena pasirinkta eilute
# print(stulpeliu_suma)
masyvas = np.array([0,1,2,3,4,5,6,7,8,9])
# parodyti sk. nuo 2 iki 5
# filtered_array = masyvas[2:6]
# print(filtered_array)

# filtered_array = masyvas[(masyvas < 5) & (masyvas > 2)]
# print(filtered_array)

#sugeneruoti Dataframe is atsitiktiniu 100 eiluciu

# df = pd.DataFrame(np.random.randn(100, 3), columns=['1', '2', '3'])
# print(df)
# isfiltruoti skaicius didesnius uz 0

# filterred_array = df[df['1'] > 0]      # filtruoja be neigiamu reiksmiu, negali buti nun

# print(filterred_array)

# df = pd.DataFrame({
#     'x': np.arange(1, 6),
#     "y": np.arange(1, 6)
# })
# df['x_y_suma'] = df['x'] + df['y']
# print(df)
# df = pd.DataFrame({
#     'A': [1,np.nan,3],
#     'B': [4,5,np.nan]                         # su nan reiksme, kuri negali buti, turi rasyti 0
# })
# df.fillna(0,inplace=True)      # vietoje nan rasome 0
# df.replace(np.nan,0, inplace=True)                # Rosvaldo
# df1 = df.replace(np.nan,0)
# print(df1)

# su Pandas sukurti vienmati masyva su atitiktiniais sk iki 10,
# ir tuos skaitmenis ideti i DataFrame?

# df = pd.DataFrame(columns=['0','1', '2', '3', '4', '5', '6', '7'])
# eilute = np.random.rand(8)         #rand ima skaicius tarp 0 ir 1
# df.loc[len(df)] = eilute            # len nusako kiek yra stulpeliu #loc reiksme prie kiekvieno stulpelio
# print(df)

# df.loc['nauja eilute'] = ['reiksmes']        # DataFrame galima susikurti nauja eilute

# data = {
#     'Amzius':[25,44],
#     'Miestas':['Kaunas','Vilnius']
# }
# df = pd.DataFrame(data, index=['Ona', 'Zose'])
# df.loc['Tomas'] = [31, 'Varena']
# # print(df)
# df.loc[df['Amzius'] > 30, 'Miestas'] = 'Klaipeda'  # kai nori pakeisti miesta
# print(df)
# df ['Miestas'][df['Amzius'] > 30] = 'Klaipeda'    # su loc geriau
# print(df)

# Vienetuku_matrica = np.ones((3,3)) ##### idomi lentele
# Krastu_matrica = np.pad(Vienetuku_matrica, pad_width=1, mode='constant',constant_values=0)
# print(Krastu_matrica)

#matricu kalkuliatorius

# matrica1 = np.array([[1,2], [3,4]])
# matrica2 = np.array([[4,5], [6,7]])
# c = np.add(matrica1,matrica2)             # sudetis
# print(c)
# daugyba = np.matmul(matrica1, matrica2)     #daugyba
# print(daugyba)

# kainos = np.random.normal(100,10,100)
# print(kainos)
# def slankusis_vidurkis(data, langas):
#     sv_filtrai = np.cumsum(data, dtype=float)   #kumuliacine suma
#     sv_filtrai[langas:] = sv_filtrai[langas:] - sv_filtrai[:-langas]
#     return sv_filtrai[langas-1:]/langas
#
# langas = 5
# sv_kainos = slankusis_vidurkis(kainos, langas)
# plt.plot(kainos,label= 'originalios kainos')
# plt.plot(np.arange(langas-1, len(kainos)), sv_kainos, label='slankusis vidurkis', color='red')
# plt.legend()
# plt.title('Finansiniu duomenu isgryninimas slankiojo vidurkio filtru')
# plt.show()
akciju_kainos = pd.read_csv('all_stocks_5yr.csv')
# print(df)
kainos = np.array(akciju_kainos['close'])
# print(kainos)

#apskaiciuoti vidurki,mediana, standarntini nuokrypis, dirbti su all stock scv

# akciju_kainos=pd.read_csv("all_stocks_5yr.csv")
# kainos=np.array(akciju_kainos['close'])
# vidurkis=np.average(kainos)
# mediana=np.median(kainos)
# standartinis_nuokrypis=np.std(kainos)
# print(vidurkis)
# print(mediana)
# print(standartinis_nuokrypis)
#
# plt.figure(figsize=(14,5))
# plt.subplot(1, 4, 1)
# plt.plot(kainos,label='Akciju kainos'))
# plt.legend()
# plt.title('Akciju kainos)')
#
# plt.subplot(1, 4, 2)
# plt.plot(kainos,label='vidurkis')
# plt.legend()
# plt.title(''vidurkis')
#
# plt.subplot(1, 4, 3)
# plt.plot(kainos,label='standartinis_nuokrypis')
# plt.legend()
# plt.title('standartinis_nuokrypis')
#
# plt.subplot(1, 4, 4)
# plt.plot(kainos,label='vidurkis')
# plt.legend()
# plt.title(''vidurkis')
#
# plt.show()

# akciju_kainos = pd.read_csv("all_stocks_5yr.csv")
# kainos = np.array(akciju_kainos["close"])
# kainos_vidurkis = np.mean(akciju_kainos["close"])
# kainos_mediana = np.median((akciju_kainos["close"]))
# kainos_stand = np.std((akciju_kainos["close"]))
# print(kainos_vidurkis)
# print(kainos_mediana)
# print(kainos_stand)
#
#
# plt.figure(figsize=(14,5))
# plt.subplot(1, 4, 1)
# plt.plot(kainos, label="Akciju kainos")
# plt.legend()
# plt.title("Akciju kainos")
#
#
# plt.subplot(1, 4, 2)
# plt.plot([kainos_vidurkis]*len(kainos), label="Kainos vidurkis")
# plt.legend()
# plt.title("Kainos vidurkis")
#
#
# plt.subplot(1, 4, 3)
# plt.plot([kainos_mediana]*len(kainos), label="Kainos mediana")
# plt.legend()
# plt.title("Kainos mediana")
#
#
# plt.subplot(1, 4, 4)
# plt.plot([kainos_stand]*len(kainos), label="Kainos stand. nuokrypis")
# plt.legend()
# plt.title("Kainos stand. nuokrypis")
#
#
# plt.show()#
# trajektoriju simuliavima
# zingsniu_skaicius = 1000
# x_zingsniai = np.random.choice([-1, 1], size=zingsniu_skaicius)
# y_zingsniai = np.random.choice([-1, 1], size=zingsniu_skaicius)
# z_zingsniai = np.random.choice([-1, 1], size=zingsniu_skaicius)
#
# x_trajektorija = np.cumsum(x_zingsniai)
# y_trajektorija = np.cumsum(y_zingsniai)
# z_trajektorija = np.cumsum(z_zingsniai)
#
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x_trajektorija, y_trajektorija, z_trajektorija)
# ax.view_init(elev=20, azim=45)
# plt.show()
