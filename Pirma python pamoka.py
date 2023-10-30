
# # vaisiai = ["Obuolys","Arbuzas","Bananas","Kriause"]
# # ilgis = len(vaisiai)
# # print (vaisiai [:1])
# # pridedame_vaisiu = vaisiai.append ("Melionas")
# # pridet_i_pradzia =
# # vaisiai.insert(0,"Melionas")
# # keiciam_reiksme = vaisiai[1] = "Kivis"
# # indeksas = vaisiai.index("Arbuzas")
# # vaisiai.remove("Bananas")
# # vaisiai.pop(2)
# # print(vaisiai)

# # dictionary -structure = my_dict = {key1:value1, key2:value2}
#
# # zodynas = [
# #     "Vardas": "Jonas",
# #     "Amzius": 30,
# #     "Miestas": "Vilnius" # zodynas["ar_studentas"] = True
# # ---
# # del zodynas["Miestas"]
# # print(zodynas) #### miesto pasalinimas
# # print(zodynas["Miestas"])
#
# #  ### kuriame studentu sarasa
# # studentai = [
#
#  # {
# #     "Vardas": "Jonas",
# #         "Amzius": 32,
# #          "Miestas": "Kaunas",
# #          "Profesija": "Inzinierius"
# # },
# # {
# #          "Vardas": "Ona",
# #         "Amzius": 25,
# #         "Miestas": "Klaipeda",
# #         "Profesija": "Gydytoja"
# # },
# # {
# #        "Vardas": "Antanas",
# #         "Amzius": 46,
# #          "Miestas": "Vilnius",
# #          "Profesija": "Mokytojas"
# # }
# # ] print(studentai[0]) # kai nori Jono
#
# # naujas_studentas = { #kai nori prideti nauja studenta
# #         "Vardas": "Petras",
# #         "Amzius": 36,
# #          "Miestas": "Kaunas",
# #          "Profesija": "Siuvejas"
# # }
# #
# # studentai.append(naujas_studentas)##kai nori prideti nauja studenta
# # print(studentai)
#
#  # if salyga: jusu veiksmai; (priklauso nuo tam tikros salygos)
# #
# # amzius = 40
# # if amzius >= 18:
# #    print ("Asmuo yra pilnametis")
# #
# # elif amzius > 13:
# #    print("Asmuo yra paauglys")
# # else:
# #     print("Asmuo nera pilnametis")
#
# # vaisiai = []
# #
# # if not vaisiai: #true
# #     print("Vaisiu sarasas tuscias")
# # elif "Kivis" in vaisiai:
# #     print("Vaisius nerastas")
# # else:
# #     print("Vaisiu sarasas tuscias, taciau sarasas turi elementu")
#
#
# # age = 18
# # has_id = False
# #
# # if age >= 18:
# #     if has_id:
# #         print("Gali balsuoti")
# #     else:
# #         print("Jums reikia as korteles")
# # else:
# #     print("Jums dar negalima balsuoti")
#
# #
# # prekiu_kategorijos = ['Vaisiai', 'Mesa', "Darzoves"]
# # prekes = {
# #     'Vaisiai': ['Obouliai', 'Bananai'],
# #     'Mesa': ['Kialiena', 'Vistiena'],
# #     'Darzoves': ['Bulves', 'Pomidorai']
# # }
# # # norime rasti prekes kategorija "Mesa" ir prekes "Vistiena";
# # norima_kategorija = 'Mesa'
# # norima_preke = 'Vistiena'
#
# # if norima_kategorija in prekiu_kategorijos:
# #     if norima_preke in prekes[norima_kategorija]:
# #         print(f"Parduotuveje yra {norima_preke}")
# #     else:
# #         print(f"Parduotuveje nera {norima_preke}")
# # else:
# #         print(f"Parduotuveje nera prekiu kategorijos: {norima_kategorija}")
#
# # 1 dalis. Sukurkite sąrašą su žmonių vardais ir amžiumi:
# # 2 dalis. Jūsų užduotis - parašyti kodą, kuris išvestų kiekvieno žmogaus vardą su amžiumi:
# # "nepilnametis", "suaugęs" arba "vaikas" (jei amžius yra 18).
#
# # sarasas = [
# #     {
# #     "Vardas": "Lina",
# #     "Amzius": 45
# #     },
# #     {
# #     "Vardas": "Eva",
# #     "Amzius": 25
# #     },
# #     {
# #     "Vardas": "Mo",
# #     "Amzius": 8
# #     }
# # ]
# # # print(sarasas)
# #
# # zmogus = sarasas [0]
# #
# # if zmogus['Amzius'] > 18:
# #     print(f'Sis zmogus {zmogus["Vardas"]} yra suauges')
# #     if zmogus['Amzius'] == 18:
# #         print(f'Sis zmogus {zmogus["Vardas"]} yra paauglys')
# #         if zmogus['Amzius'] < 18:
# #             print(f'Sis zmogus {zmogus["Vardas"]} yra nepilnametis')
# #
# # # 2 užduotis:
# # # 1 dalis: Sukurkite žodyną su darbuotojo informacija(Vardas, atlyginimas,pareigos);
# # # 2.dalis: Pagal darbuotojo pareigas (jei jis yra "inžinierius"),
# # # padidinkite jo atlyginimą 10%. Jei jis nėra "inžinierius", palikite atlyginimą nepakeistą.
# #
# # Darbuotojas = {
# #     "Vardas": "Tomas",
# #     "Atlyginimas": 2200,
# #     "Pareigos": "Siuvejas"
# # }
# # # print(Darbuotojas)
# #
# # if Darbuotojas["Pareigos"] == "Inzinierius":
# #     # padidinti 10% atlyginima
# #     #ilgesnis uzrasymas
# #     # Darbuotojas["Atlyginimas"] = Darbuotojas["Atlyginimas"] * 1.10
# #     #trumpesnis uzrasymas
# #     Darbuotojas["Atlyginimas"] *= 1.10 # galima prideti +ir atimti -
#
# #
# # print(Darbuotojas)
# # # 3 užduotis:
# # # 1 dalis: Sukurkite sąrašą su knygų informacija(Pavadinimas, išleidimo metai);
# # # 2 dalis: Suraskite norimos knygos metus pagal vartotojo įvesti;
# #
# # knygos = [
# #     {"pavadinimas": "Haris Poteris", "isleidimo_metai": 1997},
# #     {"pavadinimas": "Moby Dikas", "isleidimo_metai": 1851},
# #     {"pavadinimas": "Metai", "isleidimo_metai": 2002},
# # ]
# # # knyga_pagal_ieskomus_metus = int(input("iveskite knygos isleidimo metus kuriu ieskote_>"))
# # # knyga = knygos[0]
# # #
# # # if knygos[0]["isleidimo metai"] == knyga_pagal_ieskomus_metus:
# # #     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0] ['pavadinimas']}")
# # #
# # # if knyga["isleidimo metai"] != knyga_pagal_ieskomus_metus:
# # #     print("Tokia knyga nerasta")
# # try:
# #     knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))
# #
# #     if knygos[0]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
# #         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
# #     elif knygos[1]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
# #         print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[1]['pavadinimas']}.")
# #     elif knygos[2]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
# #         print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[2]['pavadinimas']}.")
# #     else:
# #         print(f"Deja, knygų išleistų {knyga_pagal_ieskomus_metus} metais nėra.")
# # except ValueError:
# #     print("Blogas ivesties formatas")
# # # importuojamos bibliotekos VISUOMET rasomos pirmose eilutese
# # # Patarimas - nedirbti ant to paties failo
# # import os
# #
# # dabartinis_katalogas = os.getcwd()
# # # print(dabartinis_katalogas)
# # norimas_aplankas = input("Iveskite aplanko pavadinima, kurio turini norite matyti_>")
# # # naujas_katalogas = input("Prasome nurodyti katalogo lokacija_>")
# # # keiciam_kataloga = os.chdir(naujas_katalogas)
#
#
# # # Renatos
# # try:
# #     #bandome gauti aplanko turiny
# #     turinys = os.listdir(norimas_aplankas)
# #     print(",".join(turinys))
# # except FileNotFoundError:
# #     print(f"Deja aplankas '{norimas_aplankas}' nerastas")
# #
# #     naujas_katalogas = input("Prasome nurodyt katalogo lokacija->")
# #     # keiciam_kataloga=os.chdir(naujas_katalogas)
# #     try:
# #         keiciam_kataloga = os.chdir(naujas_katalogas)
# #         if os.getcwd() == naujas_katalogas:
# #             print(f"Darbinis katalogas sekmingai pakeistas i {naujas_katalogas}")
# #         # bandome gautiaplanko turini;
# #         turinys = os.listdir(naujas_katalogas)
# #         print(",".join(turinys))
# #     except FileNotFoundError:
# #         print(f"Deja aplankas' {naujas_katalogas}'nerastas") im
# import os
import shutil

# EXTENSION_MAP = {
#     '.jpg': "Images",
#     '.jpeg': "Images",
#     '.png': "Images",
#     '.gif': "Images",
#     '.pdf': "Documents",
#     '.txt': "Documents"
#
# }
# filename = input("Please the name of the file you want to organize_>")
#
# file_extension = os.path.splitext(filename)[1]

# try:
#     if os.path.exists(filename) and file_extension in EXTENSION_MAP:
#         directory_name = EXTENSION_MAP[file_extension]
#
#         #create the directory if it doesn't exist
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
#             #move the file
#             shutil.move(filename, os.path.join(directory_name, filename))
#             print(f"{filename} has been moved to {directory_name}")
#     else:
#         print("The file doesn't exist or its extension is on recognized")
# except FileNotFoundError:
#     print(f'Error: {filename} was not found')
# except PermissionError:
#     print(f'Error: you dont have permissions to move {filename}')



