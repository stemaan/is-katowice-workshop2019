monety = [5, 2, 1, 0.5, 0.2, 0.1]
monety_reszta = [0, 0, 0, 0, 0, 0]

banknot = 20
zakup = 8.40

reszta = banknot - zakup
indeks = 0

for moneta in monety:
    print(reszta)
    if reszta >= moneta:
        ilosc = reszta // moneta
        wartosc = ilosc * moneta
        reszta -= wartosc
        monety_reszta[indeks] = ilosc
    indeks += 1

print(monety_reszta)
