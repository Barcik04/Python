||||||||||||||||||||||||||||||||||||||||||||||......NWD......|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
a= int(input('wprowadz liczbe a '))
b = int(input('wprowadz liczbe b '))

while b != 0:
    a, b = b, a % b
print(f'NWD to {a}')
