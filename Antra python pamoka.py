# for - raktas , in - seka
# print (raktas)


# for i in range(5):
#     print("Skaicius", i)

# skaiciai = [1,2,3,4,5]
# for skaicius in skaiciai:
#     print("Mano saraso skaicius", skaicius)
# #
# tekstas = "python data science"
# for raide in tekstas:
#     print(raide)
# #
# zodynas = {"a":1,"b":2,"c":3}
# for abecele in zodynas:
#     print(abecele, zodynas[abecele])
# # #
# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         # break # lieka 1 2 ir nutruksta
#         continue #-- ciklas nutruksta ir lieka 1245
#     print(skaicius)
# #
# skaiciai = [10,20,30,40,50]
#
# suma = sum(skaiciai)
#
# vidurkis = suma /len(skaiciai)
# print("Gautas vidurkis", vidurkis)

# # for skaicius in skaiciai:
# #     if skaicius > vidurkis:
#         print(skaicius)

# Kai nori kad grupuotu stulpeliu
# sarasas = ["jonas", "antanas", "ona", "marija"]
# for vardas in sarasas:
#     print(vardas)
#
# sarasas = ["jonas", "antanas", "ona", "marija"] # rusiuoja kitaip
# for vardas in sarasas:
#     print(vardas+'\n')

# tekstas_1 = "python"
# tekstas_2 = ""
# for raide in tekstas_1:
#     tekstas_2 = raide+ tekstas_2
# print(tekstas_2)
#
# daugybos_lentele = 10
# for i in range(1,daugybos_lentele +1):
#     for j in range(1,daugybos_lentele +1):
#         print(i*j, end="\t")                           # t reiskia tarpa
#     print()
#
# # sarasas kuriame butu tekstas su tarpais
# #
# sarasas = ["Labas", "rytas", "mieli", "mokiniai"]
# # print(sarasas)
# sarasas_2 = ""
# for zodis in sarasas:
#     sarasas_2 += zodis+" "
# # sujungtas_sakinys = sarasas_2.strip()
# print(sarasas_2)
#
#  # Rosvaldo pavyzdys
#
# sarasas = ["labas", "rytas", "suraitytas", "skanios", "kavytes"]
# for i in sarasas:
#     print(i, end=" ")
#
# # while  - vykdoma kol salyga  tenkinama
#
# # spausdina skaicius is eiles
# skaicius = 1
# while skaicius <= 20:
#     print(skaicius)
#     skaicius += 1
#
# # ivestis = int(input("Iveskite teigiama skaiciu_>"))
# #
# # while ivestis < 0:
# #     print("Jusu skaicius neigiamas")
# #     ivestis = int(input("Bandykite dar karta_>"))
# # print("Ivedete teigiama skaici
# # atsakymas = 5
# # spejimas = int(input("Spekite skaiciu nuo 1 iki 10_>"))
# #
# # while spejimas != atsakymas:
# #     spejimas = int(input("Neteisingas atsakymas! Bandykite dar karta_>"))
# #
# # print("Sveikiname, atspejote!")
#
# # ar_veikia = True
# # while ar_veikia:                                 # gali buti while = True
# #
# #     print("----Meniu----")
# #     print("1. Atspausdinti pasveikinima")
# #     print("2. Iveskite nauja varda")
# #     print("3. Iseiti")
# #
# #     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3/_>")
# #     if pasirinkimas == "1":
# #         print(f"Labas!")
# #     elif pasirinkimas == "2":
# #         vardas = input("Iveskite nauja varda_>")
# #
# #         print("Sekmingai ivedete nauja varda!")
# #         print(f"Jusus vardas pakeistas i {vardas}")
# #     elif pasirinkimas == "3":
# #         print("Aciu, kad naudojates programa. IKI")
# #         ar_veikia = False                                   # gali buti ir break
# #     else:
# #         print("Neteisingas pasirinkimas! Bandykite dar karta")
#
#
# # parasyti programa kurioje nurodytas zodis, jei neatspes tures speti kol atspes
#
# paslaptingas_zodis = "sniegas"
# spejimas = input("Spekite paslaptingaji zodi:")
#
# while spejimas != paslaptingas_zodis:
#     spejimas = input("Spekite paslaptingaji zodi DAR KARTA: ")
# print("Norime pasveikinti, laimejote!")

# #parasyti programa, irasau skaiciu ir turi ismesti to skaiciaus daugybos lentele. pvz 5*1 = ir tt
#
# # pasirinkimas = int(input("Pasirinkite skaiciu nuo 1 iki 10: "))
# # max_skaicius = 1
# # while max_skaicius <= 10:
# #     rezultatas = max_skaicius*pasirinkimas
# #     print(f'{pasirinkimas} * {max_skaicius} = {rezultatas}')
# #     max_skaicius += 1
# # Ęsintakse funkcijose: def funkcijosPavadinimas(argumentai) :
# #     # Jusu kodas
#
# # def pasisveikinti ():
# #     print ("Hello Python")
#
# # if __name__ == '__main__':  -------------antras budas
# #     pasisveikinti()
#
# # def pasisveikinti (vardas):
# #     print (f"Hello {vardas}")
# # pasisveikinti("Renata")
#
# # def suma(a,b):
# #     return a + b
# # atsakymas = suma(5,3)
# # print(atsakymas)
# # kusime knygu valdymo sistema
#
# def rodyti_meniu():
#     print("-----Meniu-----")
#     print("1. Prideti knyga")
#     print("2. Perziureti visas knygas")
#     print("3. Ieskoti knygos pagal pavadinima")
#     print("4. Iseiti")
#
# def prideti_knyga(knygu_sarasas) :
#     pavadinimas = input("Iveskite knygos pavadinima_>")
#     autorius = input("Iveskite knygos autoroiu_>")
#     knygu_sarasas.append({"pavadinimas": pavadinimas, "autorius":autorius})
#     print(f"Knyga '{pavadinimas} prideta!")
#
# def perziureti_knygas(knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#
# def ieskoti_knygos(knygos_sarasas):
#     ieskomas_pavadinimas = input("Iveskite knygos pavadinima kurios eskote_>")
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga['pavadinimas'].lower()]
#
#     if rasti_knygas:
#         for knyga in rasti_knygas:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga ['autorius']}")
#         else:
#             print(f"Knyga su pavadinimu:'{ieskomas_pavadinimas}' b=nerasta")
#
# def mai ():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma(1-4)_>")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "3":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "4":
#             prideti_knyga(knygu_sarasas)
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome nuo 1 iki 4")
# main()
# mini banko sistema

#bankine sistema. mes galime atidaryti sas, inesti pin, nusiimti pin, perziureti likuti, uzdaryti sas, iseiti is sistemos:

banko_saskaitos = {

}
def rodyti_meniu():
    print("\n=== Mini Banko sistema ===")
    print("1. Atidaryti naują saskaitą")
    print("2. Įnešti pinigus")
    print("3. Nusiimti pinigus")
    print("4. Peržiūrėti sąskaitos likutį")
    print("5. Uždaryti sąskaitą")
    print("6. Išeiti")

def prideti_saskaita(paslaugos):
    saskaitos_turetojas = input("Iveskite vardą: ")
    pradinis_likutis = int(input("Įveskite pradinį pinigų likutį: "))
    saskaitos_nr = len(banko_saskaitos) + 1
    banko_saskaitos[saskaitos_nr] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
    print(f"Nauja sąskaita '{saskaitos_nr}' sekmingai prideta!")

def inesti_pinigus(paslaugos):
    saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
    suma = int(input("Įveskite įnešamų pinigų sumą: "))
    banko_saskaitos[saskaitos_nr]["pradinis_likutis"] += suma
    print(f"Į sąskaitą nr.: '{saskaitos_nr}' sėkmingai įnešta '{suma}' eurai")

def nusiimti_pinigus(paslaugos):
    saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
    suma = int(input("Įveskite nusiimamų pinigų sumą: "))
    if suma <= banko_saskaitos[saskaitos_nr]["pradinis_likutis"]:
        banko_saskaitos[saskaitos_nr]["pradinis_likutis"] -= suma
        print(f"Iš sąskaitos nr.: '{saskaitos_nr}' sėkmingai nusiimta '{suma}' eurai")
    else:
        print(f"Jūsų pradinis likutis yra per mazas. Jis yra: '{banko_saskaitos[saskaitos_nr]['pradinis_likutis']}' eurai")

def perziureti_likuti(paslaugos):
    saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
    likutis = banko_saskaitos[saskaitos_nr]["pradinis_likutis"]
    print(f"Sąskaitos nr.: '{saskaitos_nr}' likutis yra '{likutis}' eurai")

def istrinti_saskaita(paslaugos):
    saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
    del banko_saskaitos[saskaitos_nr]
    print(f"Banko sąskaita nr.: '{saskaitos_nr}' buvo ištrinta")


def main():
    paslaugos = []

    while True:
        rodyti_meniu()
        pasirinkimas = input("Pasirinkite veiksmą(1-6): ")
        if pasirinkimas == "1":
            prideti_saskaita(banko_saskaitos)
        elif pasirinkimas == "2":
            inesti_pinigus(banko_saskaitos)
        elif pasirinkimas == "3":
            nusiimti_pinigus(banko_saskaitos)
        elif pasirinkimas == "4":
            perziureti_likuti(banko_saskaitos)
        elif pasirinkimas == "5":
            istrinti_saskaita(banko_saskaitos)
        elif pasirinkimas == "6":
            print("Iki greito!")
            break
        else:
            print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 6")

main()

# Sukurkite funkciją pvm_skaiciuokle(), kuri priimtų kainą be PVM ir grąžintų kainą su 21% PVM.

# Sukurkite funkciją pvm_skaiciuokle(), kuri priimtų kainą be PVM ir grąžintų kainą su 21% PVM.

# def PVM_skaiciuokle (kaina):
#     PVM_tarifas = 0.21
#     kaina_su_PVM = kaina + kaina * PVM_tarifas
#     print(kaina_su_PVM, 'kaina su PVM.')
    # return kaina_su_PVM ---- galima dar ir be return

# kaina_be_PVM = int(input("kaina be PVM:"))
# PVM_skaiciuokle(kaina_be_PVM)
