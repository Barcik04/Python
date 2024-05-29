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





Tworzenie wykresu liniowego
        plt.plot(x, y)
        plt.show()
        plt.plot(x, y): Tworzy wykres liniowy punktów danych x i y.
        plt.show(): Wyświetla wykres w oknie graficznym.

Tytuły i etykiety osi
        plt.plot(x, y)
        plt.title('Title of the plot')
        plt.xlabel('X-axis label')
        plt.ylabel('Y-axis label')
        plt.show()
        plt.title('Title of the plot'): Ustawia tytuł wykresu.
        plt.xlabel('X-axis label'): Ustawia etykietę osi X.
        plt.ylabel('Y-axis label'): Ustawia etykietę osi Y.


Dodawanie legendy
        plt.plot(x, y, label='Label for line')
        plt.legend()
        plt.show()
        plt.plot(x, y, label='Label for line'): Dodaje etykietę do linii wykresu.
        plt.legend(): Wyświetla legendę na wykresie.


Tworzenie wykresu słupkowego
        plt.bar(x, height)
        plt.show()
        plt.bar(x, height): Tworzy wykres słupkowy z punktami x i wysokościami słupków height.


Tworzenie wykresu kołowego
        plt.pie(sizes, labels=labels)
        plt.show()
        plt.pie(sizes, labels=labels): Tworzy wykres kołowy z wartościami sizes i etykietami labels.


Tworzenie histogramu
        plt.hist(data, bins=10)
        plt.show()
        plt.hist(data, bins=10): Tworzy histogram danych data podzielony na 10 przedziałów (bins).


Tworzenie wykresu rozrzutu
        plt.scatter(x, y)
        plt.show()
        plt.scatter(x, y): Tworzy wykres punktowy (rozrzutu) z punktami x i y.
  

Zapisywanie wykresu do pliku
        plt.plot(x, y)
        plt.savefig('plot.png')
