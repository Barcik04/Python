names = ["michal", "nela", "ola", "przemek"]

duze = [x[0].upper() + x[1:].lower() for x in names]
print(duze)

tylko_i = [x for x in duze if 'i' in x]
print(tylko_i)

tupla = ("Ola", "Marta", "Gosia", "Magda", "Baba")
dlugosc_all = sum(len(x) for x in tupla)

print(dlugosc_all)
