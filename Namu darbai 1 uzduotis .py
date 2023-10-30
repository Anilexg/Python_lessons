
# 1. Sukurkite prekių sąrašą su kainomis ir raskite brangiausią prekę.

prekes = [
    { "Preke": "Batai", "Kaina": 60},
    {"Preke": "Suknele","Kaina": 45},
    {"Preke": "Dzinsai","Kaina": 75}
]
# print(prekes)
brangiausia_kaina = 0
preke = ""

if prekes[0]["Kaina"] > brangiausia_kaina:
    brangiausia_kaina = prekes[0]["Kaina"]
    preke = prekes[0]["Preke"]
if prekes[1]["Kaina"] > brangiausia_kaina:
    brangiausia_kaina = prekes[1]["Kaina"]
    preke = prekes[1]["Preke"]
if prekes[2]["Kaina"] > brangiausia_kaina:
    brangiausia_kaina = prekes[2]["Kaina"]
    preke = prekes[2]["Preke"]

print("Brangiausia preke yra:", preke, " jos  kaina: ", brangiausia_kaina)


prekiu_sarasas = [
    {"preke": "Arbuzas", "kaina": 5.25},
    {"preke": "Limonadas", "kaina": 6.99},
    {"preke": "Sokoladas", "kaina": 10.29}
]

a = prekiu_sarasas[0]
b = prekiu_sarasas[1]
c = prekiu_sarasas[2]

verte = max(a["kaina"],b["kaina"],c["kaina"])

if a["kaina"] == verte:
    print(f' Brangiausia preke sarase yra {a["preke"]}')
if b["kaina"] == verte:
    print(f' Brangiausia preke sarase yra {b["preke"]}')
if c["kaina"] == verte:
    print(f' Brangiausia preke sarase yra {c["preke"]}')
