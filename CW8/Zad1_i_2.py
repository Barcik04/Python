
import numpy as np


print(f'Czwiczenie 1\n')

aria = np.array([i for i in range(10,40,2)])
print(np.shape(aria)[0])
print(np.resize(aria,(2,6)))
print((aria + 3)*2)
aria[aria % 6 == 0] = 0
print(aria)

x = 99
def change(A, x):
    nowa = A.copy()
    nowa[nowa == 0] = x
    return nowa
print(f'{change(aria, x)}\n\n\n')

print(f'\n\n\n\nCzwiczenie 2\n')

A = np.array([[1,1,2],[2,1,0],[4,1,2]])
B = np.array([[2,5,7],[2,8,0],[4,3,1]])

print(A+B)
print(f'\n')
print(np.dot(A,B)) #mnozenie macierzy
print(f'\n')
print(np.multiply(A,B)) #mnozenie skalarne
print(f'\n')
print(np.transpose(A)) #transpozycja
print(f'\n')
print(np.invert(A)) #odwrocona
print(f'\n')
print(A**5) #kazdy element do ^5
print(f'\n')
print(np.linalg.matrix_power(A,5)) #macierz do ^5
print(f'\n')
print(np.linalg.det(B)) #wyznacznik
print(f'\n')
print(np.linalg.matrix_power(B, -3)) #do potegi -3
print(f'\n\n\n')


C = np.array([[1],[2],[4]])
D = np.array([[2,5,7]])

print(C * D)
print(f'\n')
print(D * C)
print(f'\n')
print(np.multiply(C,D))
print(f'\n\n\n')


E = np.array([[1,5],[2,1]])
F = np.array([[2,1],[2,8]])

print(E/F)
print(f'\n')
print(E//F)
print(f'\n')
print(E%F)

