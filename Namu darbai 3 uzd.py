# Sukurkite žodyną su kliento informacija,
# ir patikrinkite ar jo sąskaitoje yra pakankamai lėšų tam tikram pirkiniui.

Klientas = {
    "Vardas": "Jonas",
    "Amzius": 40,
    "Miestas": "Vilnius",
    "Telefonas": "+37063025252",
    "Sask.likutis": 10000
}
# print(Klientas)

Pirkinys = 500
# 10000 < 500 = False
if Klientas["Sask.likutis"] < Pirkinys:
    print("lesu nepakanka")
else:
    print("galima pirkti")
