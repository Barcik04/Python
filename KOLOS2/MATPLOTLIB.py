import matplotlib.pyplot as plt

# Przykładowe dane
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Tworzenie wykresu liniowego
plt.plot(x, y, label='Prime numbers')

# Dodawanie tytułu i etykiet osi
plt.title('Example Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Dodawanie legendy
plt.legend()

# Zapisanie wykresu do pliku
plt.savefig('example_plot.png')

# Wyświetlanie wykresu
plt.show()
