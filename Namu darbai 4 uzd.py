# Pagal nurodytą pajamų sumą, paskaičiuokite mokesčius, taikant šias taisykles:
# pajamoms iki 1000 - 10%, nuo 1001 iki 5000 - 15%, virš 5000 - 20%.

Pajamos = 1000
if Pajamos <= 1000:
    mokestis = Pajamos * 0.1
if Pajamos <= 5000 and Pajamos > 1000:
    mokestis = Pajamos * 0.15
if Pajamos > 5000:
    mokestis = Pajamos * 0.20

print(mokestis)