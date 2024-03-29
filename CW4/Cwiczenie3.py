# def iloczyn_arg(*args):
#     wynik = 1
#     for i in args:
#         wynik *= i
#     return wynik
#
#
# print(iloczyn_arg(1, 2, 3, 4, 5))


#######



# def sum_potegi(n, *args):
#     wynik = sum(x ** n for x in args)
#     return wynik
#
# print(sum_potegi(3, 1, 2, 3))


#######


# def mean(*args):
#     return (sum(args)) / len(args)
#
#
# mean = mean(1, 2, 3, 4)
# print(mean)
#
# from math import prod
# def gmean(*args):
#     n = len(args)
#     srednia_geo = (prod(x for x in args)) ** (1/n)
#     return srednia_geo
#
# gmean = gmean(1, 2, 5)
# print(gmean)


#######


# def sum_string(*args):
#     return sum(len(x.replace(" ", "")) for x in args)
#
# stringi = sum_string("Kuba Dzwolak", "Wiktor Lata", "Wiktor Grurze")
# print(stringi)




########



# def naj_i_naj(*args):
#     najwieksza = max(args)
#     najmniejsza = min(args)
#     return najwieksza, najmniejsza
#
#
#
# wartosci = naj_i_naj(1, 2, 23, 4, 5, 6, -3, -2, -3.012)
# print(wartosci)