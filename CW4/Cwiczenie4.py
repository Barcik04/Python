# def dane_osob(**kwargs):
#     wynik = []
#     for key, value in kwargs.items():
#         wynik.append(f'({key}) na numer ({value})')
#     return " ".join(wynik)
#
#
# numery = dane_osob(Jakub = "1234384")
# print(numery)


###########



# def srednia_zarobkow(**kwargs):
#     suma = 0
#     for value in kwargs.values():
#         suma += int(value)
#     suma = suma / len(kwargs)
#     return suma
#
# srednia = srednia_zarobkow(Styczen = "5000", Luty = "4300", Marzec = "9100")
# print(srednia)