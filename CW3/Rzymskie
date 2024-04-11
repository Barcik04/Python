

def zmiana(liczba):
    rzymskie = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    suma = 0
    poprzednia = 0
    for symbol in reversed(liczba):
        wartosc = rzymskie[symbol]
        if wartosc < poprzednia:
            suma -= wartosc
        else:
            suma += wartosc
        poprzednia = wartosc
    return suma


print(zmiana('MXV'))

